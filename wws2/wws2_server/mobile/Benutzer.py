#!/usr/bin/python
# -*- coding: UTF-8 -*-

class Benutzer:
    '''
    Klasse für Benutzer.
    '''
    def __init__(self, rows, zones):
        '''
        Initialisieren eines neuen Benutzers.
        Identität (Benutzername + Passwort) muss vorher geprüft werden.
        :param db_row 2-Tupel (Tupel der Spaltennamen, Tupel Zeile aus der DB oder neuer Datensatz)
        :param zones List Liste mit 2-Tupeln der Zuständigkeitsbereiche
        '''
        self.vals = {}
        self._keys = []
        keys, vals = rows
        for i in xrange(len(keys)):
            self._setitem(keys[i], vals[i])
        # Einige Werte werden zum Schnellzugriff direkt gespeichert
        self.uid = int(vals[0])
        self.name_lang = vals[4] + ' ' + vals[3] + ' ' + vals[2]
        self.last_login = int(vals[10]) # Aus Kompatibilitätsgründen
        self.zones = zones
        self._setitem(u'Bereiche', zones)
        
    def __str__(self):
        return self.name_lang
    
    def _setitem(self, key, val):
        if type(val) == long:
            self.vals[key] = int(val)
        else:
            self.vals[key] = val
        if not key in self._keys:
            self._keys.append(key)
    
    def __iter__(self):
        for key in self._keys:
            yield self.vals[key]

    def keys(self):
        return self._keys
    
    def values(self):
        return [self.vals[key] for key in self._keys]
    
    def items(self):
        return [(key, self.vals[key]) for key in self._keys]
    
    
    