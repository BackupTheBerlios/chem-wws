#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
Hauptklasse der Anwendung.
Hier wird die grundlegende Datenbankfunktionalität implementiert.
Alle anderen Klassen sind von dieser hier abgeleitet.
'''
__version__ = 1.0
__author__ = 'Thorsten Weimann <thorsten.weimann@gmx.net'
__date__ = '02.09.2006'

# Falls libmysql nicht in $PATH liegt
import sys
sys.path.append('/opt/lampp/lib/mysql')
import time
import base64
import MySQLdb
# Eigene Importe
import Config
import mobile.Benutzer

class SimpleDB:
    '''
    Klasse für Datenbankfunktionen.
    '''
    def __init__(self, host = Config.DB_Host, user = Config.DB_User,
                 passwd = Config.DB_Pass, db = Config.DB,
                 use_unicode = Config.DB_Unicode, enc = Config.DB_Encoding):
        '''
        Speichert die Verbindungsdaten in Instanzvariablen.
        :param host String DB-Host
        :param user String DB-User
        :param passwd String DB-Passwort
        :param db String Zu benutzende Datenbank
        :param use_unicode Boolean Unicode benutzen (Standard: True)
        '''
        self.host = host
        self.user = user
        self.passwd = base64.b64decode(passwd)
        self.db = db
        self.use_unicode = use_unicode
        self.row = 0
        self.enc = enc
        
    def _connect(self, test = False):
        '''
        Stellt die Verbindung zur Datenbank her.
        '''
        try:
            self.con = MySQLdb.connect(host = self.host, user = self.user,
                                       passwd = self.passwd, db = self.db,
                                       use_unicode = self.use_unicode)
            if test:
                self.closeDB()
            return True
        except Exception, e:
            print 'Fehler beim Verbindungsaufbau zum MySQL-Server.'
            print 'Fehler: ', e
            return False

    def test(self):
        '''
        Testet die Datenbankverbindung.
        :return Boolean True, wenn DB-Verbindung besteht
        '''
        return self._connect(True)

    def login(self, user, passwd):
        '''
        Überprüft Benutzer und Passwort und setzt den Benutzer online.
        :param user String Benutzername
        :param passwd String base64 kodiertes Passwort
        :return Object Instanz der Klasse Benutzer oder False
        '''
        args = (user, base64.b64decode(passwd))
        sql = "SELECT * FROM benutzer WHERE Benutzername=%s AND Passwort=MD5(%s) \
               AND aktiviert='ja' LIMIT 1"
        cols, daten = self.fetch(sql, args, mode = 'one', type = 'assoc', table = 'benutzer')
        print cols
        print daten
        try:
            user_zones = self._zones(daten[14])
            new_user = mobile.Benutzer.Benutzer((cols, daten), user_zones)
            session = base64.b64encode(new_user.name_lang)
            self.writeLog(new_user.uid, u'Log', u'Anmeldung: %s, Session: %s' % (new_user.name_lang, session))
            sql = "UPDATE benutzer SET Session_ID=%s WHERE UID=%s"
            self.query(sql, (session, new_user.uid))
            return new_user
        except Exception, e:
            print 'Fehler: ', e
            self.writeLog(0, u'Fehler', u'Anmeldung von %s fehlgeschlagen' % user)
            return False
    
    def logout(self, user):
        '''
        Setzt den Benutzer mit der übergebenen UID offline.
        :param user Object Instanz der Klasse Benutzer
        '''
        zeit = int(time.time())
        sql = "UPDATE benutzer SET Session_ID=NULL,Last_Login=%s,Logins=Logins+1 \
               WHERE UID=%s LIMIT 1"
        self.query(sql, (zeit, user.uid))
        self.writeLog(user.uid, u'Log', u'Abmeldung: %s' % user.name_lang)
        return True
    
    def getENC(self):
        '''
        Liefert das Encoding der DB zurück.
        :return String Encoding
        '''
        return self.enc
    
    def fetch(self, sql, args = tuple(), mode = 'all', type = 'std', table = ''):
        '''
        Führt eine Datenbankabfrage aus.
        Speichert die Anzahl der betroffenen Datensätze in self.row.
        :param sql String SQL-Abfrage
        :param args Tuple Argumente für die Abfrage
        :param mode String Modus für fetch (all = fetchall(), one = fetchone())
        :param type String std = Standard, assoc = Liefert Spaltennamen mit
        :param table String Tabellenname für type = assoc
        :return Tuple one = Tupel mit einer Zeile, all = Tupel aus one-Tupeln
                oder Liste mit [0]Tupel der Spaltennamen und [1]one oder all
        '''
        self._connect()
        cursor = self.con.cursor()
        if args:
            cursor.execute(sql, args)
        else:
            cursor.execute(sql)
        self.row = int(cursor.rowcount)
        if mode == 'all':
            daten = cursor.fetchall()
        elif mode == 'one':
            daten = cursor.fetchone()
        cursor.close()
        self.closeDB()
        if type == 'assoc':
            cols = self._getCols(table)
            tmp = (cols, daten)
            return tmp
        else:
            return daten

    def query(self, sql, args = tuple()):
        '''
        Führt eine SQL-Abfrage aus, ohne die Ergebnisse abzuholen.
        Für INSERT, UPDATE und DELETE.
        :param sql String SQL-Abfrage
        :param args Tuple Argumente für die Abfrage
        '''
        self._connect()
        cursor = self.con.cursor()
        if args:
            cursor.execute(sql, args)
        else:
            cursor.execute(sql)
        self.row = int(cursor.rowcount)
        cursor.close()
        self.closeDB()

    def getUser(self, uid = 0):
        '''
        Liest alle Benutzer aus der DB aus.
        :return Tuple Tupel aus 3-Tupeln (UID, Nachname, Anrede)
        '''
        if uid:
            sql = "SELECT Name,Vorname,Anrede FROM benutzer WHERE UID=%s"
            daten = self.fetch(sql, (uid,), 'one')
        else:
            sql = "SELECT UID,Name,Anrede FROM benutzer WHERE aktiviert='ja'"
            daten = self.fetch(sql)
        return daten
    
    def getUserOnline(self):
        '''
        Gibt alle Benutzer, die online sind, zurück.
        :return Tuple Tupel aus 3-Tupeln ((User1-UID, User1-Nachname, User1-Anrede), (User2-UID,...))
        '''
        sql = "SELECT UID,Name,Anrede FROM benutzer WHERE Session_ID IS NOT NULL"
        daten = self.fetch(sql)
        return daten
    
    def _getCols(self, table):
        '''
        :param table String Tabellenname
        :return Tuple Spaltennamen
        '''
        sql = "SHOW COLUMNS FROM %s" % table
        self._connect()
        cursor = self.con.cursor()
        cursor.execute(sql)
        daten = cursor.fetchall()
        cursor.close()
        self.closeDB()
        cols = []
        for zeile in daten:
            cols.append(zeile[0])
        return tuple(cols)

    def writeLog(self, userid, type, entry):
        '''
        Eintrag in das Journal (DB) schreiben.
        Journal wird geschrieben, damit root zentral die Log's
        lesen kann und eine zentrale Auswertung möglich ist.
        :param userid Integer Benutzer-ID des aktuell angemeldeten Benutzers
        :param type Unicode-String Typ des Eintrags (Log, Fehler, Warnung)
        :param entry Unicode-String Eintrag für das Journal
        :return Boolean True, wenn Eintrag in DB geschrieben wurde
        '''
        zeit = int(time.time())
        sql = "INSERT INTO journal SET Lfd_Nr=NULL,Zeit=%s,UID=%s,\
               Typ=%s,Eintrag=%s,ausblenden=%s"
        try:
            self._connect()
            cursor = self.con.cursor()
            enc = self.enc
            cursor.execute(sql, (zeit, userid, type.encode(enc), entry.encode(enc),
                                 u'nein'.encode(enc)))
            cursor.close()
            self.closeDB()
            return True
        except Exception, e:
            print 'Fehler: ', e
            return False

    def _zones(self, zones):
        '''
        Auslesen der Zonen aus der Bereiche-Tabelle
        :param zones String Zonen als HEX-Zahl
        :param db_con Object Gültiger Cursor der Klasse MySQLdb
        :return Liste Liste aus 2-Tupeln der gesetzten Bereiche des Benutzers [(Bereich_ID, Kürzel)]
        '''
        zones = self._formBinary(zones)
        sql = "SELECT Bereich_ID,Kuerzel FROM bereiche"
        daten = self.fetch(sql)
        tmp = []
        i = 0
        for zeile in daten:
            if int(zones[i]) == 1:
                tmp.append((int(zeile[0]), zeile[1].lower()))
            i += 1
        return tmp

    def _formBinary(self, hex_string):
        '''
        Umwandeln der HEX-Zahl in eine Binärzahl und umkehren
        der Reihenfolge.
        :param hex_string String HEX-Zahl
        :return String Binärzahl (umgedreht)
        '''
        bin = ('0000', '0001', '0010', '0011', '0100', '0101',
               '0110', '0111', '1000', '1001', '1010', '1011',
               '1100', '1101', '1110', '1111')
        hex = {'A' : 10, 'B' : 11, 'C' : 12, 'D' : 13, 'E' : 14, 'F' : 15}
        hex_str = hex_string.upper()
        tmp = []
        for char in hex_str:
            if char in hex.keys():
                c = hex[char]
            else:
                c = int(char)
            tmp.append(bin[c])
        tmp.reverse()
        return ''.join(tmp)

    def closeDB(self):
        self.con.close()
