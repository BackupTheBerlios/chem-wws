#!/usr/bin/python
# -*- coding: UTF-8 -*-

import time
import SimpleDB

class myMail(SimpleDB.SimpleDB):
    '''
    Klasse für das Mailsystem. Die Mails verbleiben immer auf dem DB-Server.
    Erweitert SimpleDB.SimpleDB().
    '''
    def __init__(self):
        '''
        Konstruktor
        '''
        SimpleDB.SimpleDB.__init__(self)
        # self.connect_ok ist True, wenn auf die DB zugegriffen werden kann
        self.connect_ok = self.test()
        # Nur zum Testen
        #self.connect_ok = False

    def getMail(self, user, which):
        '''
        Gibt die Listen der Nachrichten zurück.
        :param user Object Instanz der Klasse Benutzer
        :param which String Ordner, der geliefert werden soll.
        :return List Angefordertes Postfach
        '''
        if which == 'post':
            return self._getMessages(user.uid, user.last_login, True) + \
                   self._getMessages(user.uid, user.last_login, False)
        elif which == 'ges':
            return self._getOwnMail(user.uid)
        elif which == 'arch':
            return self._getArchiv(user.uid)
        elif which == 'neu':
            return self._getMessages(user.uid, user.last_login, True)
        elif which == 'alt':
            return self._getMessages(user.uid, user.last_login, False)
        else:
            return False
        
    def countMessages(self, user):
        '''
        Zählt die Nachrichten, die evtl. seit dem letzten Login
        dazugekommen sind, trennt nach wichtig und normal.
        :param user Object Instanz der Klasse Benutzer
        :return Tuple Anzahl neuer Nachrichten (wichtig, normal)
        '''
        sql = "SELECT Lfd_Nr FROM nachrichten WHERE \
        UID_Empf=%s AND wichtig='ja' AND Datum>%s"
        self.fetch(sql, (user.uid, user.last_login))
        wichtig = self.row
        sql = "SELECT Lfd_Nr FROM nachrichten WHERE \
        UID_Empf=%s AND wichtig='nein' AND Datum>%s"
        self.fetch(sql, (user.uid, user.last_login))
        normal = self.row
        return (wichtig, normal)

    def _getMessages(self, uid, last_login, new = False):
        '''
        Liest alle neuen oder nicht neuen Nachrichten aus der DB aus.
        :param new Boolean Nur neue Nachrichten auslesen (Standard: False)
        :return List Zeilen aus der DB als Tupel
        '''
        if new:
            where = " AND Datum>=%s" % last_login
        else:
            where = " AND Datum<%s" % last_login
        sql_1 = "SELECT * FROM nachrichten WHERE UID_Empf=%s AND archiviert='nein'"
        sql = sql_1 + where + ' ORDER BY Datum DESC'
        daten = self.fetch(sql, (uid,))
        return list(daten)

    def _getArchiv(self, uid):
        '''
        Liest alle archivierten Nachrichten aus.
        :return List Zeilen aus der DB
        '''
        sql = "SELECT * FROM nachrichten WHERE UID_Empf=%s AND archiviert='ja' \
               ORDER BY Datum DESC"
        daten = self.fetch(sql, (uid,))
        return list(daten)

    def _getOwnMail(self, uid):
        '''
        Holt alle geschriebenen Mails aus der DB.
        :return List Zeilen aus der DB
        '''
        sql = "SELECT * FROM eigene_nachrichten WHERE UID_Abs=%s ORDER BY Datum DESC"
        daten = self.db.fetch(sql, (uid,))
        return list(daten)

    def writeMail(self, user, empf, betreff, text, wichtig = False):
        '''
        Schreibt eine neue Mail in die Datenbank.
        :param user Object Instanz der Klasse Benutzer (Absender)
        :param empf Integer UID des Empfängers
        :param betreff Unicode-String Betreffzeile
        :param text Unicode-String Nachrichtentext
        :param wichtig Boolean
        '''
        zeit = int(time.time())
        enc = self.db.getENC()
        if wichtig:
            imp = u'ja'
        else:
            imp = u'nein'
        sql = "INSERT INTO nachrichten VALUES(NULL,%s,%s,%s,%s,%s,%s,%s)"
        self.query(sql, (user.uid, empf, betreff.encode(enc), text.encode(enc),
                         imp.encode(enc), zeit, u'nein'.encode(enc)))
        sql = "INSERT INTO eigene_nachrichten VALUES(NULL,%s,%s,%s,%s,%s,%s)"
        self.query(sql, (user.uid, empf, betreff.encode(enc), text.encode(enc),
                         imp.encode(enc), zeit))

    def archMail(self, id):
        '''
        Verschiebt Mail in das Archiv.
        :param id Integer Lfd_nr der zu verschiebenden Mail
        '''
        sql = "UPDATE nachrichten SET archiviert='ja' WHERE Lfd_Nr=%s"
        self.query(sql, (id,))
        return True

    def delMail(self, id, own = False):
        '''
        Löscht Mails aus der DB.
        :param id List Liste der ID's zum Löschen
        :param own Boolean True = Löschen aus eigene_nachrichten,
                False = Löschen aus nachrichten
        '''
        if own:
            table = "eigene_nachrichten"
        else:
            table = "nachrichten"
        sql = "DELETE FROM " + table + " WHERE Lfd_Nr=%s AND LIMIT 1"
        self.query(sql, (id,))
        return True

# End of Class myMail
