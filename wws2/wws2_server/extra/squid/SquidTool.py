#!/usr/bin/python
#-*- coding: utf-8 -*-

# Programm zum Schreiben und Anzeigen der freigegebenen IP's
# aus der Text-Datei des Squid-Servers.
# Der Squid-Server wird nach Änderungen neu gestartet.

import sys
from subprocess import Popen, PIPE, STDOUT

# Globale Variablen (evtl. anpassen)
SQUID_IP_FILE = '/etc/squid/edv-raum.txt'
SQUID_START_SCRIPT = '/etc/init.d/squid'
SQUID_START_PARAM = 'reload'

class SquidTool:

    def __init__(self):
        '''
        Konstruktor
        '''
        self.ip_file = SQUID_IP_FILE
        self.reload_command = (SQUID_START_SCRIPT, SQUID_START_PARAM)
        self.errors = []
        self.loadIPs()

    def loadIPs(self):
        '''
        Liest die IP-Adressen aus self.ip_file in eine Liste.
        '''
        self.ips = []
        try:
            ip_file = file(self.ip_file, 'r')
            for line in ip_file:
                if line.strip() and not line.startswith('#'):
                    self.ips.append(line.strip())
            ip_file.close()
        except IOError, e:
            print 'Fehler beim Öffnen der IP-Datei: ', self.ip_file
            print 'Fehler: ', e
            self.errors.append(e)

    def getIPs(self):
        '''
        Gibt die Liste der aktiven IP's zurück.
        :return List IP-Liste
        '''
        return self.ips

    def writeIPs(self, ips = []):
        '''
        Schreibt die bergebenen IP's in die Datei.
        Updatet self.ips.
        :param ips List Liste der IP's zum schreiben
        :return Boolean True, wenn Datei geschrieben wurde
        '''
        try:
            ip_file = file(self.ip_file, 'w')
            for ip in ips:
                ip_file.write(ip + '\n')
            ip_file.close()
            self.ips = ips
            return True
        except IOError, e:
            print 'Fehler beim Schreiben der Datei: ', self.ip_file
            print 'Fehler: ', e
            self.errors.append(e)
            return False

    def restartSquid(self):
        '''
        Squid neu starten und Ausgabe des Befehls zurückgeben.
        :return List Ausgabe von Squid-Befehl oder Fehlermeldung
        '''
        output = []
        process = Popen(self.reload_command, stdout = PIPE, stderr = STDOUT)
        for line in process.stdout:
            output.append(line)
        return output
