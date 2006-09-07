#!/usr/bin/env python
#-*- coding: utf-8 -*-

import Pyro.core
import Pyro.naming
from Pyro.errors import NamingError
import sys
from threading import Thread
# Eigene Importe
import wwsMain
import SimpleDB
import myMail
import Config

Pyro.config.PYRO_MOBILE_CODE = 1

# Klassen die für Gruppen :test und :wws registriert werden sollen.
# Abgeleitet von Pyro.core.ObjBase und der eigentlichen importierten Klasse.

# :test
class testclass(Pyro.core.ObjBase):
    def __init__(self):
        Pyro.core.ObjBase.__init__(self)
    
    def test(self, str):
        return str.upper()

# :wws
class wwsMain_wrapper(Pyro.core.ObjBase, wwsMain.wwsMain):
    def __init__(self):
        Pyro.core.ObjBase.__init__(self)
        wwsMain.wwsMain.__init__(self)

class SimpleDB_wrapper(Pyro.core.ObjBase, SimpleDB.SimpleDB):
    def __init__(self):
        Pyro.core.ObjBase.__init__(self)
        SimpleDB.SimpleDB.__init__(self)

class myMail_wrapper(Pyro.core.ObjBase, myMail.myMail):
    def __init__(self):
        Pyro.core.ObjBase.__init__(self)
        myMail.myMail.__init__(self)

# Zweiter Dämon, falls an beide Nameserver gekoppelt werden soll

class wwsDaemon(Thread):
    def __init__(self, host, port, ns, groups):
        Thread.__init__(self)
        Pyro.core.initServer()
        self.daemon = Pyro.core.Daemon(host = host, port = port)
        self.daemon.useNameServer(ns)
        try:
            for group in groups:
                ns.createGroup(group)
                print 'Gruppe %s erstellt' % group
        except NamingError:
            pass
        self.ns = ns
        self.uri = []
        
    def register(self, obj, name):
        uri = self.daemon.connect(obj, name)
        self.uri.append(uri)
    
    def run(self):
        print 'Daemon 2 wurde gestartet...'
        self.daemon.requestloop()


# Hauptprogramm

def main():
    # Gruppen die am Name Server registriert werden sollen
    groups = [':test', ':wws']
    
    # Zweiten Dämon als Thread starten falls erforderlich
    if Config.Daemon_2_Start:
        locator2 = Pyro.naming.NameServerLocator()
        ns2 = locator.getNS(host = Config.NS_2_Host, port = Config.NS_2_Port)
        print 'NameServer 2 gefunden: %s' % ns2
        daemon2 = wwsDaemon(Config.Daemon_2_Host, Config.Daemon_2_Port, ns2, groups)
        daemon2.register(testclass(), ':test.simple')
        # Hier alle Objekte nacheinander registrieren
        daemon2.start()
        
    # Pyro initialisieren
    Pyro.core.initServer()
    
    # Name Server lokalisieren
    locator = Pyro.naming.NameServerLocator()
    ns = locator.getNS(host = Config.NS_1_Host, port = Config.NS_1_Port)
    print 'NameServer 1 gefunden: %s' % ns
    
    # Pyro Dämon initialisieren
    daemon = Pyro.core.Daemon()
    # Name Server für Pyro Dämon setzen
    daemon.useNameServer(ns)

    # Gruppen am Name Server registrieren
    try:
        for group in groups:
            ns.createGroup(group)
            print 'Gruppe %s erstellt' % group
    except NamingError:
        pass
    
    # Objekte in Gruppen veröffentlichen
    # Gruppe :test
    uri1 = daemon.connect(testclass(),":test.simple")
    # Gruppe :wws
    uri2 = daemon.connect(wwsMain_wrapper(), ':wws.main')
    uri3 = daemon.connect(SimpleDB_wrapper(), ':wws.db')
    uri4 = daemon.connect(myMail_wrapper(), ':wws.mail')
    print 'Daemon 1 wurde gestartet ...'
    # Server in der Hauptschleife laufen lassen
    daemon.requestLoop()
    
# Nur zum Testen
sys.argv.append('start')
if 'start' in sys.argv:
    main()