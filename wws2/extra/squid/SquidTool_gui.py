#!/usr/bin/env python
#-*- coding: utf-8 -*-
# generated by wxGlade 0.4.1 on Fri Sep 01 13:22:01 2006

import wx
import Pyro.core
import Pyro.naming
import time

class SquidTool_gui(wx.Frame):
    def __init__(self, *args, **kwds):
        self.ips = [('EDV-Client01', '10.0.1.11'),
                    ('EDV-Client02', '10.0.1.12'),
                    ('EDV-Client03', '10.0.1.13'),
                    ('EDV-Client04', '10.0.1.14'),
                    ('EDV-Client05', '10.0.1.15'),
                    ('EDV-Client06', '10.0.1.16'),
                    ('EDV-Client07', '10.0.1.17'),
                    ('EDV-Client08', '10.0.1.18'),
                    ('EDV-Client09', '10.0.1.19'),
                    ('EDV-Client10', '10.0.1.20'),
                    ('EDV-Client11', '10.0.1.21'),
                    ('EDV-Client12', '10.0.1.22'),
                    ('EDV-Laptop01', '10.0.1.31'),
                    ('EDV-Laptop02', '10.0.1.32'),
                    ('EDV-Laptop03', '10.0.1.33'),
                    ('EDV-Laptop04', '10.0.1.34'),
                    ('EDV-Laptop05', '10.0.1.35'),
                    ('Mediothek', '10.0.1.40')]
        Pyro.core.initClient()
        locator = Pyro.naming.NameServerLocator()
        ns = locator.getNS(host = '10.0.1.1', port = 9091)
        uri = ns.resolve(':edv.squid')
        self.obj = Pyro.core.getProxyForURI(uri)
        # begin wxGlade: SquidTool_gui.__init__
        kwds["style"] = wx.DEFAULT_FRAME_STYLE
        wx.Frame.__init__(self, *args, **kwds)
        self.window_1 = wx.SplitterWindow(self, -1, style=wx.SP_3D|wx.SP_BORDER)
        self.window_1_pane_2 = wx.Panel(self.window_1, -1)
        self.window_1_pane_1 = wx.Panel(self.window_1, -1)
        self.frame_1_statusbar = self.CreateStatusBar(1, 0)
        self.checkbox = []
        for ip in self.ips:
            self.checkbox.append(wx.CheckBox(self.window_1_pane_1, -1, ip[0]))
        self.button_1 = wx.Button(self.window_1_pane_2, -1, "Neu Laden")
        self.button_2 = wx.Button(self.window_1_pane_2, -1, "Anwenden")
        self.button_3 = wx.Button(self.window_1_pane_2, -1, "Beenden")

        self.__set_properties()
        self.__do_layout()

        self.Bind(wx.EVT_BUTTON, self.refresh, self.button_1)
        self.Bind(wx.EVT_BUTTON, self.write, self.button_2)
        self.Bind(wx.EVT_BUTTON, self.appExit, self.button_3)
        # end wxGlade
        self.setState()

    def __set_properties(self):
        # begin wxGlade: SquidTool_gui.__set_properties
        self.SetTitle("Internetzugriff EDV-Raum")
        self.SetSize((250, 530))
        self.frame_1_statusbar.SetStatusWidths([-1])
        # statusbar fields
        frame_1_statusbar_fields = ["Copyright 2006 by Thorsten Weimann"]
        for i in range(len(frame_1_statusbar_fields)):
            self.frame_1_statusbar.SetStatusText(frame_1_statusbar_fields[i], i)
        for box in self.checkbox:
            box.SetFont(wx.Font(10, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, ""))
        self.window_1_pane_1.SetMinSize((111, 444))
        self.button_1.SetMinSize((100, 20))
        self.button_1.SetFont(wx.Font(10, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, ""))
        self.button_2.SetMinSize((100, 20))
        self.button_2.SetFont(wx.Font(10, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, ""))
        self.button_3.SetMinSize((100, 20))
        self.button_3.SetFont(wx.Font(10, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, ""))
        self.window_1_pane_2.SetMinSize((120, 444))
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: SquidTool_gui.__do_layout
        sizer_1 = wx.BoxSizer(wx.VERTICAL)
        sizer_3 = wx.BoxSizer(wx.VERTICAL)
        sizer_2 = wx.BoxSizer(wx.VERTICAL)
        for box in self.checkbox:
            sizer_2.Add(box, 0, wx.ALL|wx.EXPAND, 5)
        self.window_1_pane_1.SetAutoLayout(True)
        self.window_1_pane_1.SetSizer(sizer_2)
        sizer_3.Add(self.button_1, 0, wx.ALL|wx.ADJUST_MINSIZE, 10)
        sizer_3.Add(self.button_2, 0, wx.ALL|wx.ADJUST_MINSIZE, 10)
        sizer_3.Add(self.button_3, 0, wx.ALL|wx.ADJUST_MINSIZE, 10)
        self.window_1_pane_2.SetAutoLayout(True)
        self.window_1_pane_2.SetSizer(sizer_3)
        self.window_1.SplitVertically(self.window_1_pane_1, self.window_1_pane_2)
        sizer_1.Add(self.window_1, 1, wx.EXPAND, 0)
        self.SetAutoLayout(True)
        self.SetSizer(sizer_1)
        self.Layout()
        # end wxGlade

    def refresh(self, event): # wxGlade: SquidTool_gui.<event_handler>
        print u'Lese IP-Liste vom Server neu ein.'
        self.setState()
        print u'Übermittlung abgeschlossen.'
        print u'Warte ...'

    def write(self, event): # wxGlade: SquidTool_gui.<event_handler>
        activated = []
        i = 0
        for box in self.checkbox:
            if box.GetValue():
                activated.append(self.ips[i][1])
            i += 1
        if self.obj.writeIPs(activated):
            tmp = self.obj.restartSquid()
            msg = u'\n'.join(tmp)
            self.setState()
        else:
            msg  = u'Fehler beim Schreiben in die Squid-Datei.\n'
            msg += u'Bitte versuchen Sie es erneut oder wenden\n'
            msg += u'Sie sich an den Administrator.'
        dlg = wx.MessageDialog(self, msg, u'Information', style = wx.OK|wx.ICON_INFORMATION)
        dlg.ShowModal()
        print u'Zu aktivierende IP\'s:'
        print u'\n'.join(activated)
        print u'Übermittlung abgeschlossen.'
        print u'Warte ...'

    def appExit(self, event): # wxGlade: SquidTool_gui.<event_handler>
        print u'Anwendung wird beendet.'
        print u'SquidTool_gui V 1.0'
        print u'Copyright 2006 by Thorsten Weimann <thorsten.weimann@gmx.net>'
        print u'Auf Wiedersehen ...'
        self.Destroy()

    def setState(self):
        self.obj.loadIPs()
        activated = self.obj.getIPs()
        print u'Aktivierte IP\'s:'
        print u'\n'.join(activated)
        i = 0
        for ip in self.ips:
            if ip[1] in activated:
                self.checkbox[i].SetValue(True)
            else:
                self.checkbox[i].SetValue(False)
            i += 1
        print u'Einlesen der Daten abgeschlossen.'
        print u'Warte ...'
    
# end of class SquidTool_gui


class MyApp(wx.App):
    def OnInit(self):
        wx.InitAllImageHandlers()
        frame_1 = SquidTool_gui(None, -1, "")
        self.SetTopWindow(frame_1)
        frame_1.Show()
        return 1

# end of class MyApp

if __name__ == "__main__":
    app = MyApp(0)
    app.MainLoop()
