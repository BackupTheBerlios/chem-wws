#!/usr/bin/python
# -*- coding: UTF-8 -*-

# Import von eigenen Modulen
import SimpleDB
import re

class wwsMain(SimpleDB.SimpleDB):
    '''
    Klasse für die gesamte Anwendung im Warenwirtschaftssystem.
    Erbt von SimpleDB.SimpleDB().
    '''
    def __init__(self):
        '''
        Konstruktor
        '''
        SimpleDB.SimpleDB.__init__(self)
        if not self.test():
            print 'Keine Verbindung zur Datenbank.'
            print 'Programm kann nicht korrekt ausgeführt werden.'

    def getChem(self, id):
        '''
        Holt den Rohstoff mit der übergebenen ID aus der DB.
        :param id Integer ID des Rohstoffs
        :return Tuple Datenbankzeile
        '''
        sql = "SELECT * FROM rohstoffe WHERE ID=%s LIMIT 1"
        daten = self.fetch(sql, (id,), 'one')
        if self.row:
            return daten
        else:
            return False

    def search(self, table, field, search_string, andor = 'oder'):
        '''
        Formt einen Suchstring und führt die gewünschte Suche in der
        Datenbank aus.
        :param table String DB-Tabelle, die durchsucht werden soll
        :param field String DB-Spalte, die den Suchbegriff enthalten soll
        :param search_string String Suchbegriff(e)
        :param andor String Verknüpfung der Suchbegriffe (und/oder)
        :return Tuple Tupel aus Datenbankzeilen
        '''
        # Suchstring verarbeiten
        s = search_string.strip()
        # 1. Mehr als ein Leerzeichen durch genau eins erstzen
        s = re.sub(r'\s+', ' ', s)
        # Unterstriche und Prozentzeichen escapen (Sonderbedeutung in SQL)
        s = s.replace(r'_', r'\_')
        s = s.replace(r'%', r'\%')
        # Wildcards ersetzen
        s = s.replace(r'*', r'%')
        if 'oder' == andor:
            tmp = s.split()
        else:
            tmp = []
            tmp.append(s)
        sql = "SELECT * FROM %s WHERE" % table
        if 'rohstoffe' == table:
            if 'name' == field.lower():
                counter = 1
                for search in tmp:
                    sql += " (Name LIKE '%s' OR Synonym_1 LIKE '%s' OR Synonym_2 LIKE '%s' \
                           OR Synonym_3 LIKE '%s')" % (search, search, search, search)
                    if counter < len(tmp):
                        sql += " OR"
                    counter += 1
            elif 'chem_formel' == field.lower():
                counter = 0
                for search in tmp:
                    sql += " %s LIKE '%s'" % (field, search)
                    if counter < len(tmp):
                        sql += " OR"
                    counter += 1
            elif 'ean' == field.lower():
                sql += " %s LIKE '%s'" % (field, tmp[0])
        elif 'inventar' == table:
            counter = 1
            for search in tmp:
                sql += " %s LIKE '%s'" % (field, search)
                if counter < len(tmp):
                    sql += " OR"
                counter += 1
        elif 'literatur' == table:
            # Weiter ...