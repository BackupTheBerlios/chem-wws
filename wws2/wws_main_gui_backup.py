#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# generated by wxGlade 0.4.1cvs on Sat Aug 19 08:11:06 2006

import wx
# Eigene Importe
import Benutzer
import mail_gui
import help_gui
import about_gui
import wws_dialogs

class wwsLoginDialog(wx.Dialog):
    def __init__(self, *args, **kwds):
        # begin wxGlade: wwsLoginDialog.__init__
        kwds["style"] = wx.DEFAULT_DIALOG_STYLE
        wx.Dialog.__init__(self, *args, **kwds)
        self.label_1 = wx.StaticText(self, -1, "Bitte geben Sie Ihren Namen und Ihr Passwort ein.", style=wx.ALIGN_CENTRE)
        self.label_2 = wx.StaticText(self, -1, "Benutzername:", style=wx.ALIGN_CENTRE)
        self.text_ctrl_1 = wx.TextCtrl(self, -1, "")
        self.label_3 = wx.StaticText(self, -1, "Passwort:", style=wx.ALIGN_CENTRE)
        self.text_ctrl_2 = wx.TextCtrl(self, -1, "", style=wx.TE_PROCESS_ENTER|wx.TE_PASSWORD)
        self.button_1 = wx.Button(self, -1, "Abbruch")
        self.bitmap_button_1 = wx.BitmapButton(self, -1, wx.Bitmap("icon/commit.png", wx.BITMAP_TYPE_ANY))

        self.__set_properties()
        self.__do_layout()

        self.Bind(wx.EVT_TEXT_ENTER, self.tryLogin, self.text_ctrl_2)
        self.Bind(wx.EVT_BUTTON, self.tryCancel, self.button_1)
        self.Bind(wx.EVT_BUTTON, self.tryLogin, self.bitmap_button_1)
        # end wxGlade
        self.parent = args[0]
        self.user = ''
        self.pw = ''

    def __set_properties(self):
        # begin wxGlade: wwsLoginDialog.__set_properties
        self.SetTitle("Authentifizierung")
        self.SetSize((372, 182))
        self.label_1.SetMinSize((400, 40))
        self.label_1.SetFont(wx.Font(12, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, ""))
        self.label_1.SetToolTipString("Maximal 3 Versuche, danach wird die Anwendung beendet.")
        self.label_2.SetMinSize((100, 30))
        self.label_2.SetFont(wx.Font(12, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, ""))
        self.text_ctrl_1.SetMinSize((200, 22))
        self.label_3.SetMinSize((100, 30))
        self.label_3.SetFont(wx.Font(12, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, ""))
        self.text_ctrl_2.SetMinSize((200, 22))
        self.bitmap_button_1.SetMinSize((88, 30))
        self.bitmap_button_1.SetToolTipString("Weiter")
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: wwsLoginDialog.__do_layout
        sizer_3 = wx.BoxSizer(wx.VERTICAL)
        sizer_6 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_5 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_4 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_3.Add(self.label_1, 0, wx.ALL|wx.EXPAND, 5)
        sizer_4.Add(self.label_2, 0, wx.ALL|wx.EXPAND, 5)
        sizer_4.Add(self.text_ctrl_1, 0, wx.ALL|wx.ADJUST_MINSIZE, 5)
        sizer_3.Add(sizer_4, 0, wx.EXPAND, 0)
        sizer_5.Add(self.label_3, 0, wx.ALL|wx.EXPAND, 5)
        sizer_5.Add(self.text_ctrl_2, 0, wx.ALL|wx.ADJUST_MINSIZE, 5)
        sizer_3.Add(sizer_5, 0, wx.EXPAND, 0)
        sizer_6.Add(self.button_1, 0, wx.ALL|wx.ADJUST_MINSIZE, 5)
        sizer_6.Add((170, 40), 0, wx.ADJUST_MINSIZE, 0)
        sizer_6.Add(self.bitmap_button_1, 0, wx.ALL|wx.ADJUST_MINSIZE, 5)
        sizer_3.Add(sizer_6, 0, wx.EXPAND, 0)
        self.SetAutoLayout(True)
        self.SetSizer(sizer_3)
        self.Layout()
        self.Centre()
        # end wxGlade

    def tryCancel(self, event): # wxGlade: wwsLoginDialog.<event_handler>
        self.parent.cancel = True
        self.Destroy()

    def tryLogin(self, event): # wxGlade: wwsLoginDialog.<event_handler>
        self.user = self.text_ctrl_1.GetValue()
        self.pw = self.text_ctrl_2.GetValue()
        self.Show(False)

# end of class wwsLoginDialog


class wwsMainNb(wx.Notebook):
    def __init__(self, *args, **kwds):
        # begin wxGlade: wwsMainNb.__init__
        kwds["style"] = 0
        wx.Notebook.__init__(self, *args, **kwds)
        self.wws_nb_pane_4 = wx.ScrolledWindow(self, -1, style=wx.TAB_TRAVERSAL)
        self.wws_nb_pane_3 = wx.ScrolledWindow(self, -1, style=wx.TAB_TRAVERSAL)
        self.wws_nb_pane_2 = wx.ScrolledWindow(self, -1, style=wx.TAB_TRAVERSAL)
        self.wws_nb_pane_1 = wx.ScrolledWindow(self, 151, style=wx.TAB_TRAVERSAL)

        self.__set_properties()
        self.__do_layout()
        # end wxGlade
        self.parent = args[0]

    def __set_properties(self):
        # begin wxGlade: wwsMainNb.__set_properties
        self.AddPage(self.wws_nb_pane_1, "Recherche")
        self.AddPage(self.wws_nb_pane_2, "A-Z Recherche")
        self.AddPage(self.wws_nb_pane_3, "Bestellen")
        self.AddPage(self.wws_nb_pane_4, "Lager")
        self.wws_nb_pane_1.SetScrollRate(10, 10)
        self.wws_nb_pane_2.SetScrollRate(10, 10)
        self.wws_nb_pane_3.SetScrollRate(10, 10)
        self.wws_nb_pane_4.SetScrollRate(10, 10)
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: wwsMainNb.__do_layout
        sizer_10 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_9 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_8 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_7 = wx.BoxSizer(wx.HORIZONTAL)
        self.wws_nb_pane_1.SetAutoLayout(True)
        self.wws_nb_pane_1.SetSizer(sizer_7)
        sizer_7.Fit(self.wws_nb_pane_1)
        sizer_7.SetSizeHints(self.wws_nb_pane_1)
        self.wws_nb_pane_2.SetAutoLayout(True)
        self.wws_nb_pane_2.SetSizer(sizer_8)
        sizer_8.Fit(self.wws_nb_pane_2)
        sizer_8.SetSizeHints(self.wws_nb_pane_2)
        self.wws_nb_pane_3.SetAutoLayout(True)
        self.wws_nb_pane_3.SetSizer(sizer_9)
        sizer_9.Fit(self.wws_nb_pane_3)
        sizer_9.SetSizeHints(self.wws_nb_pane_3)
        self.wws_nb_pane_4.SetAutoLayout(True)
        self.wws_nb_pane_4.SetSizer(sizer_10)
        sizer_10.Fit(self.wws_nb_pane_4)
        sizer_10.SetSizeHints(self.wws_nb_pane_4)
        # end wxGlade
        #self.mypanel_1 = nb_panels.MyPanel(self.wws_nb_pane_1, -1)
        #sizer_7.Add(self.mypanel_1, 1, wx.EXPAND, 0)
        
# end of class wwsMainNb


class wwsMainFrame(wx.Frame, wws_main.wws_main):
    def __init__(self, *args, **kwds):
        # begin wxGlade: wwsMainFrame.__init__
        kwds["style"] = wx.DEFAULT_FRAME_STYLE
        wx.Frame.__init__(self, *args, **kwds)
        
        # Menu Bar
        self.wws_main_frame_menubar = wx.MenuBar()
        self.SetMenuBar(self.wws_main_frame_menubar)
        self.file = wx.Menu()
        self.file_close = wx.MenuItem(self.file, 101, u"Schließen", "Programm beenden", wx.ITEM_NORMAL)
        self.file.AppendItem(self.file_close)
        self.wws_main_frame_menubar.Append(self.file, "Datei")
        self.edit = wx.Menu()
        self.edit_conf = wx.MenuItem(self.edit, 201, "Einstellungen", "Anwendung einrichten", wx.ITEM_NORMAL)
        self.edit.AppendItem(self.edit_conf)
        self.wws_main_frame_menubar.Append(self.edit, "Bearbeiten")
        self.extra = wx.Menu()
        self.extra_mail = wx.MenuItem(self.extra, 301, "Mail", u"Öffnet das integrierte Mailprogramm", wx.ITEM_NORMAL)
        self.extra.AppendItem(self.extra_mail)
        self.wws_main_frame_menubar.Append(self.extra, "Extras")
        self.help = wx.Menu()
        self.help_show = wx.MenuItem(self.help, 401, "Onlinehilfe", u"Öffnet die Onlinehilfe", wx.ITEM_NORMAL)
        self.help.AppendItem(self.help_show)
        self.help.AppendSeparator()
        self.help_about = wx.MenuItem(self.help, 402, u"Über wws ...", "Informationen zu wws", wx.ITEM_NORMAL)
        self.help.AppendItem(self.help_about)
        self.wws_main_frame_menubar.Append(self.help, "Hilfe")
        # Menu Bar end
        self.wws_main_frame_statusbar = self.CreateStatusBar(3, 0)
        
        # Tool Bar
        self.wws_main_frame_toolbar = wx.ToolBar(self, -1, style=wx.TB_HORIZONTAL|wx.TB_3DBUTTONS)
        self.SetToolBar(self.wws_main_frame_toolbar)
        self.wws_main_frame_toolbar.AddLabelTool(50, u"Schließen", wx.Bitmap("/home/tweimann/workspace/wws/icon/exit.png", wx.BITMAP_TYPE_ANY), wx.NullBitmap, wx.ITEM_NORMAL, "Programm beenden", u"Schließt die Anwendung")
        self.wws_main_frame_toolbar.AddSeparator()
        self.wws_main_frame_toolbar.AddLabelTool(51, "Mail", wx.Bitmap("/home/tweimann/workspace/wws/icon/mail.png", wx.BITMAP_TYPE_ANY), wx.NullBitmap, wx.ITEM_NORMAL, u"Mailprogramm öffnen", u"Öffnet das integrierte Mailprogramm")
        self.wws_main_frame_toolbar.AddSeparator()
        self.wws_main_frame_toolbar.AddLabelTool(53, "Einstellungen", wx.Bitmap("/home/tweimann/workspace/wws/icon/config.png", wx.BITMAP_TYPE_ANY), wx.NullBitmap, wx.ITEM_NORMAL, "Anwendung einrichten", "Einstellungen anpassen")
        self.wws_main_frame_toolbar.AddSeparator()
        self.wws_main_frame_toolbar.AddLabelTool(52, "Hilfe", wx.Bitmap("/home/tweimann/workspace/wws/icon/help.png", wx.BITMAP_TYPE_ANY), wx.NullBitmap, wx.ITEM_NORMAL, "Onlinehilfe", u"Öffnet die Onlinehilfe")
        # Tool Bar end
        self.wws_nb = wwsMainNb(self, 150)

        self.__set_properties()
        self.__do_layout()

        self.Bind(wx.EVT_MENU, self.wwsClose, self.file_close)
        self.Bind(wx.EVT_MENU, self.wwsEditConf, self.edit_conf)
        self.Bind(wx.EVT_MENU, self.wwsMail, self.extra_mail)
        self.Bind(wx.EVT_MENU, self.wwsHelp, self.help_show)
        self.Bind(wx.EVT_MENU, self.wwsAbout, self.help_about)
        self.Bind(wx.EVT_TOOL, self.wwsClose, id=50)
        self.Bind(wx.EVT_TOOL, self.wwsMail, id=51)
        self.Bind(wx.EVT_TOOL, self.wwsEditConf, id=53)
        self.Bind(wx.EVT_TOOL, self.wwsHelp, id=52)
        # end wxGlade
        self.wwsLogin()
        try:
            self.rights = self.user.rights
            wichtig, normal = self.mail.countMessages()
            text = u'Neue Nachrichten: %s davon %s als wichtig gekennzeichnet.' % (wichtig + normal, wichtig)
            self.setStatus(text)
            self.SetTitle('Warenwirtschaftssystem V %s' % self.wws.set['VERSION'])
        except:
            pass

    def __set_properties(self):
        # begin wxGlade: wwsMainFrame.__set_properties
        self.SetTitle("Warenwirtschaftssystem")
        self.SetSize((750, 550))
        self.wws_main_frame_statusbar.SetStatusWidths([-1, 160, 210])
        # statusbar fields
        wws_main_frame_statusbar_fields = ["Bereit", "---", "Copyright 2006 by Thorsten Weimann"]
        for i in range(len(wws_main_frame_statusbar_fields)):
            self.wws_main_frame_statusbar.SetStatusText(wws_main_frame_statusbar_fields[i], i)
        self.wws_main_frame_toolbar.Realize()
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: wwsMainFrame.__do_layout
        sizer_1 = wx.BoxSizer(wx.VERTICAL)
        sizer_2 = wx.BoxSizer(wx.VERTICAL)
        sizer_2.Add(self.wws_nb, 1, wx.EXPAND, 0)
        sizer_1.Add(sizer_2, 1, wx.EXPAND, 2)
        self.SetAutoLayout(True)
        self.SetSizer(sizer_1)
        self.Layout()
        # end wxGlade

    def wwsClose(self, event): # wxGlade: wwsMainFrame.<event_handler>
        '''
        Schließt das Hauptprogramm
        '''
        self.Destroy()

    def wwsMail(self, event): # wxGlade: wwsMainFrame.<event_handler>
        '''
        Ruft das Mailprogramm auf.
        '''
        mail_edit = mail_gui.MailFrame(self, -1, "")
        mail_edit.Show()
        event.Skip()

    def wwsHelp(self, event): # wxGlade: wwsMainFrame.<event_handler>
        '''
        Ruft die Onlinehilfe auf.
        '''
        help = help_gui.helpFrame(None, -1, '', page = 'index.html')
        help.Show()
        event.Skip()

    def wwsAbout(self, event): # wxGlade: wwsMainFrame.<event_handler>
        title = u'Warenwirtschaftssystem - V ' + str(self.set['VERSION'])
        text  = u''
        text += u''
        text += u''
        text += u''
        text += u'\n\n'
        text += u'Copyright 2006 by Thorsten Weimann'
        about = about_gui.AboutDialog(self, -1, "", about_title = title,
                                      about_text = text)
        about.ShowModal()
        event.Skip()

    def wwsLogin(self):
        '''
        Benutzerauthentifizierung
        '''
        self.cancel = False
        versuche = 1
        user = {}
        while versuche <= 3:
            pw_dlg = wwsLoginDialog(self)
            pw_dlg.ShowModal()
            if self.cancel:
                self.Destroy()
            user['name'] = pw_dlg.user
            user['pass'] = pw_dlg.pw
            wws_main.wws_main.__init__(self, user)
            if self.logged_in:
                pw_dlg.Destroy()
                self.setStatus(self.user.name_lang, 'middle')
                return
            versuche += 1
        msg  = u'Leider konnten Ihre Daten nicht im System gefunden werden.\n'
        msg += u'Wenden Sie sich an den Administrator.'
        exit_dlg = wx.MessageDialog(self, msg, u'Authentifizierung gescheitert', style = wx.OK)
        exit_dlg.ShowModal()
        self.Destroy()
    
    def setStatus(self, text, direction = 'left'):
        '''
        Text in die Statusbar setzen
        :param text String Text für die Statuszeile
        :param direction String left für linke Statuszeile, right für rechte Statuszeile
        '''
        if direction == 'left':
            pos = 0
        elif direction == 'middle':
            pos = 1
        elif direction == 'right':
            pos = 2
        self.wws_main_frame_statusbar.SetStatusText(text, pos)
                
    def wwsEditConf(self, event): # wxGlade: wwsMainFrame.<event_handler>
        conf = wws_dialogs.ConfDialog(self, -1, "")
        conf.ShowModal()
        event.Skip()

# end of class wwsMainFrame


class wwsMainApp(wx.App):
    def OnInit(self):
        wx.InitAllImageHandlers()
        wws_main_frame = wwsMainFrame(None, -1, "")
        self.SetTopWindow(wws_main_frame)
        wws_main_frame.Show()
        return 1

# end of class wwsMainApp

if __name__ == "__main__":
    wws_app = wwsMainApp(0)
    wws_app.MainLoop()
