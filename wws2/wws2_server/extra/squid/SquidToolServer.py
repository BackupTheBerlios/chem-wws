#! /usr/bin/env python
#-*- coding: utf-8 -*-

import Pyro.core
import Pyro.naming
from Pyro.errors import NamingError
import sys
from threading import Thread
# Eigene Importe
import SquidTool

# Klassen die für Gruppe :wws registriert werden sollen.
# Abgeleitet von Pyro.core.ObjBase und der eigentlichen importierten Klasse.

class SquidTool_wrapper(Pyro.core.ObjBase, SquidTool.SquidTool):
    def __init__(self):
        Pyro.core.ObjBase.__init__(self)
        SquidTool.SquidTool.__init__(self)


# Klasse für den Dämon, da für jede Netzwerkkarte einer gestartet werden muss

class SquidToolDaemon(Thread):
    def __init__(self, host, port, ns, groups = []):
      Thread.__init__(self)
      Pyro.core.initServer()
      self.daemon = Pyro.core.Daemon(host = host, port = port)
      self.daemon.useNameServer(ns)
      try:
        for group in groups:
          ns.createGroup(group)
          print 'Gruppe %s an erstem NS erzeugt.' % group
      except NamingError:
        pass
    
    def register(self, obj, name):
      self.uri = self.daemon.connect(obj, name)
    
    def run(self):
      print 'Dämon wird gestartet...'
      self.daemon.requestLoop()

# Hauptprogramm

def main():
    # Gruppen die an den Nameservern registriert werden sollen
    groups = [':edv']

    # Name Server lokalisieren
    loc1 = Pyro.naming.NameServerLocator()
    ns1 = loc1.getNS(host = '10.0.1.1', port = 9091)
    
    # Pyro Dämon initialisieren
    daemon1 = SquidToolDaemon('10.0.1.1', 21000, ns1, groups)
    
    # Gruppen am Name Server registrieren
    # Gruppe :edv
    daemon1.register(SquidTool_wrapper(),":edv.squid")

    daemon1.start()
    
    # Zweiten Dämon starten
    Pyro.core.initServer()
    loc2 = Pyro.naming.NameServerLocator()
    ns2 = loc2.getNS(host = '10.0.0.4', port = 9090)
    
    daemon2 = Pyro.core.Daemon(host = '10.0.0.4', port = 21001)
    daemon2.useNameServer(ns2)
    
    # Gruppen registrieren
    try:
      for group in groups:
        ns2.createGroup(group)
        print 'Gruppe %s an zweitem NS erzeugt.' % group
    except NamingError:
      pass
    
    # Objekte verbinden
    uri = daemon2.connect(SquidTool_wrapper(), ':edv.squid')
    
    # Dämon 2 in Endlosschleife laufen lassen
    daemon2.requestLoop()
    
# Nur zum Testen
#sys.argv.append('start')
if 'start' in sys.argv:
    main()
    