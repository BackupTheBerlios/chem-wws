#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# generated by wxGlade 0.4.1cvs on Tue Aug  8 08:17:18 2006

import wx
from wx.html import HtmlWindow
import time, os
# Eigene Klassen
import help_gui
import about_gui

class MailFrame(wx.Frame):
    def __init__(self, *args, **kwds):
        self.parent = args[0]
        self.mail = self.parent.mail
        self.user = self.parent.user
        # begin wxGlade: MailFrame.__init__
        kwds["style"] = wx.DEFAULT_FRAME_STYLE
        wx.Frame.__init__(self, *args, **kwds)
        self.window_1 = wx.SplitterWindow(self, -1, style=wx.SP_3D|wx.SP_BORDER)
        self.window_1_pane_2 = wx.Panel(self.window_1, -1)
        self.window_2 = wx.SplitterWindow(self.window_1_pane_2, -1, style=wx.SP_3D|wx.SP_BORDER)
        self.window_2_pane_2 = wx.Panel(self.window_2, -1)
        self.window_2_pane_1 = wx.Panel(self.window_2, -1)
        self.window_1_pane_1 = wx.Panel(self.window_1, -1)

        # Menu Bar
        self.frame_1_menubar = wx.MenuBar()
        self.SetMenuBar(self.frame_1_menubar)
        self.file = wx.Menu()
        self.close = wx.MenuItem(self.file, 101, u"Schließen", u"Schließt das Mailfenster", wx.ITEM_NORMAL)
        self.file.AppendItem(self.close)
        self.frame_1_menubar.Append(self.file, "Datei")
        self.mail = wx.Menu()
        self.mail_new = wx.MenuItem(self.mail, 201, "Neu", "Neue Nachricht schreiben", wx.ITEM_NORMAL)
        self.mail.AppendItem(self.mail_new)
        self.mail_get = wx.MenuItem(self.mail, 202, "Abholen", "Neue Mails vom Server abholen", wx.ITEM_NORMAL)
        self.mail.AppendItem(self.mail_get)
        self.mail_ans = wx.MenuItem(self.mail, 203, "Antworten", "Markierte Nachricht beantworten", wx.ITEM_NORMAL)
        self.mail.AppendItem(self.mail_ans)
        self.mail_arch = wx.MenuItem(self.mail, 204, "Archivieren", "Markierte Nachricht in das Archiv verschieben", wx.ITEM_NORMAL)
        self.mail.AppendItem(self.mail_arch)
        self.mail_print = wx.MenuItem(self.mail, 207, "Drucken", "Markierte Nachricht drucken", wx.ITEM_NORMAL)
        self.mail.AppendItem(self.mail_print)
        self.mail_save = wx.MenuItem(self.mail, 206, "Speichern", "Markierte Nachricht als Datei speichern", wx.ITEM_NORMAL)
        self.mail.AppendItem(self.mail_save)
        self.mail.AppendSeparator()
        self.mail_del = wx.MenuItem(self.mail, 205, u"Löschen", u"Markierte Nachricht löschen", wx.ITEM_NORMAL)
        self.mail.AppendItem(self.mail_del)
        self.frame_1_menubar.Append(self.mail, "Nachrichten")
        self.help = wx.Menu()
        self.help_show = wx.MenuItem(self.help, 301, "Hilfe anzeigen", "Zeigt die Hilfe zu den Mailfunktionen an", wx.ITEM_NORMAL)
        self.help.AppendItem(self.help_show)
        self.help_about = wx.MenuItem(self.help, 302, u"Über ...", u"Über den Mailclient", wx.ITEM_NORMAL)
        self.help.AppendItem(self.help_about)
        self.frame_1_menubar.Append(self.help, "Hilfe")
        # Menu Bar end
        self.frame_1_statusbar = self.CreateStatusBar(2, 0)

        # Tool Bar
        self.frame_1_toolbar = wx.ToolBar(self, -1, style=wx.TB_HORIZONTAL|wx.TB_3DBUTTONS)
        self.SetToolBar(self.frame_1_toolbar)
        self.frame_1_toolbar.AddLabelTool(150, u"Schließen", wx.Bitmap("/home/tweimann/workspace/wws/icon/exit.png", wx.BITMAP_TYPE_ANY), wx.NullBitmap, wx.ITEM_NORMAL, u"Schließt das Mailfenster", "")
        self.frame_1_toolbar.AddSeparator()
        self.frame_1_toolbar.AddLabelTool(250, "Mail neu", wx.Bitmap("/home/tweimann/workspace/wws/icon/mail_new.png", wx.BITMAP_TYPE_ANY), wx.NullBitmap, wx.ITEM_NORMAL, "Neue Nachricht schreiben", "")
        self.frame_1_toolbar.AddLabelTool(251, "Mails holen", wx.Bitmap("/home/tweimann/workspace/wws/icon/mail_get.png", wx.BITMAP_TYPE_ANY), wx.NullBitmap, wx.ITEM_NORMAL, "Neue Nachrichten vom Server holen", "")
        self.frame_1_toolbar.AddLabelTool(252, "Mail antworten", wx.Bitmap("/home/tweimann/workspace/wws/icon/mail_ans.png", wx.BITMAP_TYPE_ANY), wx.NullBitmap, wx.ITEM_NORMAL, "Markierte Nachricht beantworten", "")
        self.frame_1_toolbar.AddLabelTool(253, "Mail archivieren", wx.Bitmap("/home/tweimann/workspace/wws/icon/mail_arch.png", wx.BITMAP_TYPE_ANY), wx.NullBitmap, wx.ITEM_NORMAL, "Markierte Nachricht in das Archiv verschieben", "")
        self.frame_1_toolbar.AddLabelTool(256, "Mail drucken", wx.Bitmap("icon/print.png", wx.BITMAP_TYPE_ANY), wx.NullBitmap, wx.ITEM_NORMAL, "Markierte Nachricht drucken", "")
        self.frame_1_toolbar.AddLabelTool(255, "Mail speichern", wx.Bitmap("/home/tweimann/workspace/wws/icon/filesave.png", wx.BITMAP_TYPE_ANY), wx.NullBitmap, wx.ITEM_NORMAL, "Als Datei speichern", "Markierte Nachricht als Datei speichern")
        self.frame_1_toolbar.AddSeparator()
        self.frame_1_toolbar.AddLabelTool(254, u"Mail löschen", wx.Bitmap("/home/tweimann/workspace/wws/icon/remove.png", wx.BITMAP_TYPE_ANY), wx.NullBitmap, wx.ITEM_NORMAL, u"Markierte Nachricht löschen", "")
        self.frame_1_toolbar.AddSeparator()
        self.frame_1_toolbar.AddLabelTool(350, "Hilfe", wx.Bitmap("/home/tweimann/workspace/wws/icon/help.png", wx.BITMAP_TYPE_ANY), wx.NullBitmap, wx.ITEM_NORMAL, "Zeigt die Hilfe an", "")
        # Tool Bar end
        self.tree_ctrl_1 = wx.TreeCtrl(self.window_1_pane_1, -1, style=wx.TR_HAS_BUTTONS|wx.TR_NO_LINES|wx.TR_DEFAULT_STYLE|wx.SUNKEN_BORDER)
        self.label_1 = wx.StaticText(self.window_2_pane_1, -1, "Posteingang")
        self.list_box_1 = wx.ListBox(self.window_2_pane_1, -1, choices=[], style=wx.LB_SINGLE)
        self.window_3 = HtmlWindow(self.window_2_pane_2, -1)

        self.__set_properties()
        self.__do_layout()

        self.Bind(wx.EVT_MENU, self.mailClose, self.close)
        self.Bind(wx.EVT_MENU, self.mailNew, self.mail_new)
        self.Bind(wx.EVT_MENU, self.mailGet, self.mail_get)
        self.Bind(wx.EVT_MENU, self.mailAns, self.mail_ans)
        self.Bind(wx.EVT_MENU, self.mailArch, self.mail_arch)
        self.Bind(wx.EVT_MENU, self.mailPrint, self.mail_print)
        self.Bind(wx.EVT_MENU, self.mailSave, self.mail_save)
        self.Bind(wx.EVT_MENU, self.mailDel, self.mail_del)
        self.Bind(wx.EVT_MENU, self.helpGet, self.help_show)
        self.Bind(wx.EVT_MENU, self.helpAbout, self.help_about)
        self.Bind(wx.EVT_TOOL, self.mailClose, id=150)
        self.Bind(wx.EVT_TOOL, self.mailNew, id=250)
        self.Bind(wx.EVT_TOOL, self.mailGet, id=251)
        self.Bind(wx.EVT_TOOL, self.mailAns, id=252)
        self.Bind(wx.EVT_TOOL, self.mailArch, id=253)
        self.Bind(wx.EVT_TOOL, self.mailPrint, id=256)
        self.Bind(wx.EVT_TOOL, self.mailSave, id=255)
        self.Bind(wx.EVT_TOOL, self.mailDel, id=254)
        self.Bind(wx.EVT_TOOL, self.helpGet, id=350)
        self.Bind(wx.EVT_TREE_ITEM_ACTIVATED, self.selectFolder, self.tree_ctrl_1)
        self.Bind(wx.EVT_LISTBOX_DCLICK, self.mailShowNewWindow, self.list_box_1)
        self.Bind(wx.EVT_LISTBOX, self.mailShow, self.list_box_1)
        # end wxGlade
        if not self.mail.test():
            msg  = u'Zur Zeit besteht keine Verbindung zur Datenbank.\n'
            msg += u'Die Anwendung kann nur online arbeiten und wird\n'
            msg += u'deshalb geschlossen.'
            dlg = wx.MessageDialog(None, msg, u'Datenbankfehler', wx.OK|wx.ICON_ERROR|wx.CENTRE)
            dlg.ShowModal()
            self.Destroy()
        self.Bind(wx.EVT_CLOSE, self.mailClose)
        self.tree_select = 'ein'
        self.mailInit()

    def __set_properties(self):
        # begin wxGlade: MailFrame.__set_properties
        self.SetTitle("OMC - OnlineMailClient")
        self.SetSize((640, 500))
        self.frame_1_statusbar.SetStatusWidths([-1, 250])
        # statusbar fields
        frame_1_statusbar_fields = ["Copyright 2006 by Thorsten Weimann", ""]
        for i in range(len(frame_1_statusbar_fields)):
            self.frame_1_statusbar.SetStatusText(frame_1_statusbar_fields[i], i)
        self.frame_1_toolbar.SetToolBitmapSize((16, 16))
        self.frame_1_toolbar.Realize()
        self.tree_ctrl_1.SetToolTipString(u"Eintrag auswählen durch Doppelklick")
        self.label_1.SetFont(wx.Font(14, wx.DEFAULT, wx.NORMAL, wx.BOLD, 0, ""))
        self.window_1.SetMinSize((640, 417))
        # end wxGlade
        # Namen des Benutzers in die rechte Statuszeile schreiben
        self.frame_1_statusbar.SetStatusText(self.mailobj.user.name_lang, 1)
        # TreeControl initialisieren
        self.tree_root = self.tree_ctrl_1.AddRoot('Verzeichnis')
        data = [('Posteingang', 'ein'), ('Gesendete', 'ges'), ('Archiv', 'arch')]
        self.tree_items = []
        for row in data:
            dat = wx.TreeItemData()
            dat.SetData(row[1])
            item = self.tree_ctrl_1.AppendItem(self.tree_root, row[0], data = dat)
            self.tree_items.append(item)
            del(dat, item)

    def __do_layout(self):
        # begin wxGlade: MailFrame.__do_layout
        sizer_1 = wx.BoxSizer(wx.VERTICAL)
        sizer_3 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_5 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_4 = wx.BoxSizer(wx.VERTICAL)
        sizer_2 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_2.Add(self.tree_ctrl_1, 1, wx.EXPAND, 0)
        self.window_1_pane_1.SetAutoLayout(True)
        self.window_1_pane_1.SetSizer(sizer_2)
        sizer_2.Fit(self.window_1_pane_1)
        sizer_2.SetSizeHints(self.window_1_pane_1)
        sizer_4.Add(self.label_1, 0, wx.ALL|wx.ADJUST_MINSIZE, 2)
        sizer_4.Add(self.list_box_1, 1, wx.RIGHT|wx.EXPAND|wx.ADJUST_MINSIZE, 5)
        self.window_2_pane_1.SetAutoLayout(True)
        self.window_2_pane_1.SetSizer(sizer_4)
        sizer_4.Fit(self.window_2_pane_1)
        sizer_4.SetSizeHints(self.window_2_pane_1)
        sizer_5.Add(self.window_3, 1, wx.RIGHT|wx.EXPAND, 5)
        self.window_2_pane_2.SetAutoLayout(True)
        self.window_2_pane_2.SetSizer(sizer_5)
        sizer_5.Fit(self.window_2_pane_2)
        sizer_5.SetSizeHints(self.window_2_pane_2)
        self.window_2.SplitHorizontally(self.window_2_pane_1, self.window_2_pane_2)
        sizer_3.Add(self.window_2, 1, wx.EXPAND, 0)
        self.window_1_pane_2.SetAutoLayout(True)
        self.window_1_pane_2.SetSizer(sizer_3)
        sizer_3.Fit(self.window_1_pane_2)
        sizer_3.SetSizeHints(self.window_1_pane_2)
        self.window_1.SplitVertically(self.window_1_pane_1, self.window_1_pane_2, 165)
        sizer_1.Add(self.window_1, 1, wx.EXPAND, 0)
        self.SetAutoLayout(True)
        self.SetSizer(sizer_1)
        self.Layout()
        # end wxGlade
        self.tree_ctrl_1.Expand(self.tree_root)
        self.tree_ctrl_1.SelectItem(self.tree_items[0])

    def mailClose(self, event): # wxGlade: MyFrame.<event_handler>
        self.Destroy()

    def selectFolder(self, event): # wxGlade: MyFrame.<event_handler>
        self.tree_select = self.tree_ctrl_1.GetPyData(self.tree_ctrl_1.GetSelection())
        self.mailInit()
        event.Skip()

    def mailPrint(self, event):
        event.Skip()

    def mailNew(self, event): # wxGlade: MyFrame.<event_handler>
        self.answer = False
        editor = MailEditor(self, -1, "")
        editor.Show()

    def mailAns(self, event): # wxGlade: MyFrame.<event_handler>
        self.answer = True
        editor = MailEditor(self, -1, "")
        editor.Show()

    def mailGet(self, event): # wxGlade: MyFrame.<event_handler>
        self.tree_ctrl_1.SelectItem(self.tree_items[0])
        self.tree_select = 'ein'
        self.mailInit()
        event.Skip()

    def mailArch(self, event): # wxGlade: MyFrame.<event_handler>
        if self.tree_select == 'ges':
            self.setStatus(u'Aktion nicht möglich.')
            return
        id = self.list_box_1.GetSelection()
        self.mail.archMail(self.list_data[id][0])
        self.mailInit()
        event.Skip()

    def mailDel(self, event): # wxGlade: MyFrame.<event_handler>
        if self.tree_select == 'ges':
            own = True
        else:
            own = False
        id = self.list_box_1.GetSelection()
        self.mail.delMail(self.list_data[id][0], own)
        self.mailInit()
        event.Skip()

    def helpGet(self, event): # wxGlade: MyFrame.<event_handler>
        help = help_gui.helpFrame(None, -1, "", page = 'index.html')
        help.Show()

    def helpAbout(self, event): # wxGlade: MyFrame.<event_handler>
        title = u'OMC - OnlineMailClient - V ' + str(set['VERSION'])
        text  = u'Der OMC dient dazu, auf die Datenbanktabelle mit '
        text += u'den Nachrichten (Mails) zuzugreifen. Alle '
        text += u'Aktionen im OMC werden online ausgeführt. '
        text += u'Dadurch sind die Nachrichten '
        text += u'auf jedem Rechner im Netz verfügbar.\n\n'
        text += u'Copyright 2006 by Thorsten Weimann'
        about = about_gui.AboutDialog(self, -1, "", about_title = title,
                                      about_text = text)
        about.ShowModal()

    def mailShow(self, event): # wxGlade: MyFrame.<event_handler>
        id = self.list_box_1.GetSelection()
        try:
            self.window_3.SetPage(self.setHTML(self.list_data[id][4],
                                               self.list_data[id][3]))
            self.mailtext = (self.list_data[id][4], int(self.list_data[id][6]),
                             self.list_data[id][3])
        except IndexError:
            self.setStatus('Falsche Auswahl, bitte korrigieren.')
        event.Skip()

    def mailShowNewWindow(self, event): # wxGlade: MailFrame.<event_handler>
        mail = ShowMail(self, -1, "")
        id = self.list_box_1.GetSelection()
        try:
            mail.SetTitle('Nachricht anzeigen: ' + self.list_data[id][3])
            mail.window_1.SetPage(self.setHTML(self.list_data[id][4],
                                               self.list_data[id][3]))
        except IndexError:
            pass
        mail.Show()
        event.Skip()

    def mailSave(self, event): # wxGlade: MailFrame.<event_handler>
        id = self.list_box_1.GetSelection()
        data = self.list_data[id]
        dataline = self.list_box_1.GetString(id)
        text  = u'<h3>' + dataline + u'</h3>\n' + (len(dataline) + 2) * u'-' + u'\n\n'
        text += u'<h3>Betreff:</h3>\n' + data[3] + u'\n\n'
        text += u'<h3>Nachricht:</h3>\n' + data[4] + u'\n\n'
        text += time.strftime('<i>Gespeichert am %x um %X.</i>')
        text  = self.setHTML(text, data[3])
        fmsg  = u'Bitte wählen Sie (Endung wird automatisch erzeugt)'
        fdlg  = wx.FileDialog(self, fmsg, wildcard = '*.html', style = wx.SAVE)
        clicked = fdlg.ShowModal()
        if clicked == wx.ID_CANCEL:
            return
        datei = fdlg.GetPath()
        date = str(int(time.time()))
        if not datei:
            return
        else:
            tmp = datei + '.html'
            if os.path.isfile(tmp):
                for_save = datei + '_' + date + '.html'
            else:
                for_save = tmp
        try:
            f = file(for_save, 'w')
            f.write(text.encode('utf-8'))
            f.close()
            self.setStatus('Die Datei wurde gespeichert.')
        except Exception, e:
            msg  = u'Beim Speichern ist ein Fehler aufgetreten.'
            msg += u'Bitte überprüfen Sie, ob Sie Schreibrechte im angegebenen '
            msg += u'Verzeichnis haben und versuchen Sie es erneut.\n'
            msg += u'Fehler: %s' % e
            self.setStatus('Fehler beim Speichern.')
            dlg = wx.MessageDialog(self, msg, 'Fehler', wx.OK|wx.ICON_ERROR)
            dlg.ShowModal()

    def setStatus(self, text):
        self.frame_1_statusbar.SetStatusText(text, 0)

    def setHTML(self, text, betreff):
        html  = u'<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 '
        html += u'Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">'
        html += u'<html>\n<head>'
        html += u'<meta content="text/html; charset=UTF-8" '
        html += u'http-equiv="content-type" />\n'
        html += u'<title>' + betreff + u'</title>\n'
        html += u'</head>\n<body>\n<div align="left">\n' + text.replace('\n', '<br />')
        html += u'\n</div>\n</body>\n</html>\n'
        return html

    def mailInit(self):
        '''
        Widgets mit Inhalt füllen.
        '''
        if self.tree_select == 'ein':
            self.label_1.SetLabel('Posteingang')
            self.list_data = self.mail.getMail(self.user, 'post')
            wichtig, normal = self.mailobj.countMessages()
            if wichtig or normal:
                new_msg = 'Neue Nachrichten: %s wichtig / %s normal' % (wichtig, normal)
                self.setStatus(new_msg)
        elif self.tree_select == 'ges':
            self.label_1.SetLabel('Gesendete Nachrichten')
            self.list_data = self.mail.getMail(self.user, 'ges')
        elif self.tree_select == 'arch':
            self.label_1.SetLabel('Archiv')
            self.list_data = self.mail.getMail(self.user, 'arch')
        self.list_box_1.Clear()
        if not self.list_data:
            self.list_box_1.Append('Keine Nachrichten vorhanden')
            self.window_3.SetPage('<html><body></body></html>')
            return
        self.list_uid = []
        for row in self.list_data:
            tmp = u''
            abs = self.mail.getUser(row[1])
            absender = abs[2] + ' ' + abs[0]
            empf = self.mail.getUser(row[2])
            empfaenger = empf[2] + ' ' + empf[0]
            date = int(row[6])
            if date > self.user.last_login:
                tmp += u'neu: '
            if row[5] == u'ja':
                tmp += u'*'
            tmp += row[3]
            if self.tree_select == 'ges':
                tmp += u'(An: ' + empfaenger
            else:
                tmp += u'(Abs: ' + absender
            tmp += u') %s' % time.strftime('%x %X', time.gmtime(date))
            list_id = self.list_box_1.Append(tmp)
            # Liste erstellen, um den Zusammenhang von ID in der Liste
            # zu UID des Benutzers herstellen zu können.
            self.list_uid.append((list_id, int(row[1])))
        self.list_box_1.SetSelection(0)
        self.window_3.SetPage(self.setHTML(self.list_data[0][4],
                                           self.list_data[0][3]))
        # Tupel bauen zum Zugriff aus Editor bei Antworten
        self.mailtext = (self.list_data[0][4], date, self.list_data[0][3])

# end of class MailFrame


class MailEditor(wx.Frame):
    def __init__(self, *args, **kwds):
        self.parent = args[0]
        users = self.parent.mail.getUser()
        choices = []
        self.uids = []
        for user in users:
            tmp = user[2] + u' ' + user[1]
            choices.append(tmp)
            # Für jeden Benutzer einen Tupel in Liste schreiben.
            # self.uids = [(UID1, combobox1), (UID2, combobox2), ...]
            self.uids.append((int(user[0]), tmp))
        # begin wxGlade: MailEditor.__init__
        kwds["style"] = wx.DEFAULT_FRAME_STYLE
        wx.Frame.__init__(self, *args, **kwds)

        # Menu Bar
        self.frame_1_menubar = wx.MenuBar()
        self.SetMenuBar(self.frame_1_menubar)
        self.file = wx.Menu()
        self.ed_close = wx.MenuItem(self.file, 101, u"Schließen", u"Schließt das Editorfenster", wx.ITEM_NORMAL)
        self.file.AppendItem(self.ed_close)
        self.frame_1_menubar.Append(self.file, "Datei")
        self.ed_mail = wx.Menu()
        self.ed_send = wx.MenuItem(self.ed_mail, 301, "Senden", "Nachricht verschicken", wx.ITEM_NORMAL)
        self.ed_mail.AppendItem(self.ed_send)
        self.frame_1_menubar.Append(self.ed_mail, "Nachricht")
        self.ed_help = wx.Menu()
        self.ed_help_show = wx.MenuItem(self.ed_help, 201, "Hilfe", "Hilfedatei anzeigen", wx.ITEM_NORMAL)
        self.ed_help.AppendItem(self.ed_help_show)
        self.frame_1_menubar.Append(self.ed_help, "Hilfe")
        # Menu Bar end
        self.frame_1_statusbar = self.CreateStatusBar(1, 0)

        # Tool Bar
        self.frame_1_toolbar = wx.ToolBar(self, -1)
        self.SetToolBar(self.frame_1_toolbar)
        self.frame_1_toolbar.AddLabelTool(50, u"Schließen", wx.Bitmap("/home/tweimann/workspace/wws/icon/exit.png", wx.BITMAP_TYPE_ANY), wx.NullBitmap, wx.ITEM_NORMAL, u"Fenster schließen", u"Schließt das Editorfenster")
        self.frame_1_toolbar.AddSeparator()
        self.frame_1_toolbar.AddLabelTool(51, "Senden", wx.Bitmap("/home/tweimann/workspace/wws/icon/mail_send.png", wx.BITMAP_TYPE_ANY), wx.NullBitmap, wx.ITEM_NORMAL, "Nachricht versenden", "Nachricht versenden")
        self.frame_1_toolbar.AddSeparator()
        self.frame_1_toolbar.AddLabelTool(52, u"Linksbündig", wx.Bitmap("/home/tweimann/workspace/wws/icon/ed_left.png", wx.BITMAP_TYPE_ANY), wx.NullBitmap, wx.ITEM_NORMAL, u"Linksbündig", u"Richtet den markierten Text linksbündig aus")
        self.frame_1_toolbar.AddLabelTool(53, "Zentrieren", wx.Bitmap("/home/tweimann/workspace/wws/icon/ed_center.png", wx.BITMAP_TYPE_ANY), wx.NullBitmap, wx.ITEM_NORMAL, "Zentrieren", "Zentriert den markierten Text")
        self.frame_1_toolbar.AddLabelTool(54, "Fett", wx.Bitmap("/home/tweimann/workspace/wws/icon/ed_bold.png", wx.BITMAP_TYPE_ANY), wx.NullBitmap, wx.ITEM_NORMAL, "Fett", "Markierter Text wird fett dargestellt")
        self.frame_1_toolbar.AddLabelTool(55, "Kursiv", wx.Bitmap("/home/tweimann/workspace/wws/icon/ed_italic.png", wx.BITMAP_TYPE_ANY), wx.NullBitmap, wx.ITEM_NORMAL, "Kursiv", "Markierter Text wird kursiv dargestellt")
        self.frame_1_toolbar.AddLabelTool(56, "Unterstrichen", wx.Bitmap("/home/tweimann/workspace/wws/icon/ed_under.png", wx.BITMAP_TYPE_ANY), wx.NullBitmap, wx.ITEM_NORMAL, "Unterstrichen", "Markierter Text wird unterstrichen")
        self.frame_1_toolbar.AddSeparator()
        self.frame_1_toolbar.AddLabelTool(58, "Hilfe", wx.Bitmap("/home/tweimann/workspace/wws/icon/help.png", wx.BITMAP_TYPE_ANY), wx.NullBitmap, wx.ITEM_NORMAL, "Hilfe anzeigen", "Zeigt die Hilfedatei an")
        # Tool Bar end
        self.label_1 = wx.StaticText(self, -1, "Senden an:")
        self.combo_box_1 = wx.ComboBox(self, -1, choices=choices, style=wx.CB_DROPDOWN|wx.CB_READONLY)
        self.label_2 = wx.StaticText(self, -1, "Wichtig:")
        self.checkbox_1 = wx.CheckBox(self, -1, "")
        self.label_3 = wx.StaticText(self, -1, "Betreff:")
        self.text_ctrl_2 = wx.TextCtrl(self, -1, "")
        self.text_ctrl_1 = wx.TextCtrl(self, -1, "", style=wx.TE_MULTILINE)
        self.button_1 = wx.Button(self, -1, "Vorschau")
        self.button_2 = wx.Button(self, -1, "Senden")
        self.window_1 = HtmlWindow(self, -1)

        self.__set_properties()
        self.__do_layout()

        self.Bind(wx.EVT_MENU, self.edClose, self.ed_close)
        self.Bind(wx.EVT_MENU, self.edSend, self.ed_send)
        self.Bind(wx.EVT_MENU, self.edHelp, self.ed_help_show)
        self.Bind(wx.EVT_TOOL, self.edClose, id=50)
        self.Bind(wx.EVT_TOOL, self.edSend, id=51)
        self.Bind(wx.EVT_TOOL, self.textLeft, id=52)
        self.Bind(wx.EVT_TOOL, self.textCenter, id=53)
        self.Bind(wx.EVT_TOOL, self.textBold, id=54)
        self.Bind(wx.EVT_TOOL, self.textItalic, id=55)
        self.Bind(wx.EVT_TOOL, self.textUnderline, id=56)
        self.Bind(wx.EVT_TOOL, self.edHelp, id=58)
        self.Bind(wx.EVT_CHECKBOX, self.edImportant, self.checkbox_1)
        self.Bind(wx.EVT_BUTTON, self.butPreview, self.button_1)
        self.Bind(wx.EVT_BUTTON, self.edSend, self.button_2)
        # end wxGl
        self.Bind(wx.EVT_CLOSE, self.edClose)
        self.edInit()

    def __set_properties(self):
        # begin wxGl
        self.SetTitle("Mail - Editor")
        self.SetSize((450, 565))
        self.frame_1_statusbar.SetStatusWidths([-1])
        # statusbar fields
        frame_1_statusbar_fields = ["Copyright 2006 by Thorsten Weimann"]
        for i in range(len(frame_1_statusbar_fields)):
            self.frame_1_statusbar.SetStatusText(frame_1_statusbar_fields[i], i)
        self.frame_1_toolbar.Realize()
        self.label_1.SetFont(wx.Font(12, wx.DEFAULT, wx.NORMAL, wx.BOLD, 0, ""))
        self.combo_box_1.SetMinSize((200, 23))
        self.combo_box_1.SetFont(wx.Font(10, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, ""))
        self.label_2.SetFont(wx.Font(12, wx.DEFAULT, wx.NORMAL, wx.BOLD, 0, ""))
        self.checkbox_1.SetToolTipString("Nachricht als wichtig kennzeichnen")
        self.label_3.SetFont(wx.Font(12, wx.DEFAULT, wx.NORMAL, wx.BOLD, 0, ""))
        self.text_ctrl_2.SetFont(wx.Font(10, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, ""))
        self.text_ctrl_1.SetFont(wx.Font(10, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, ""))
        # end wxGl

    def __do_layout(self):
        # begin wxGl
        sizer_1 = wx.BoxSizer(wx.VERTICAL)
        sizer_2 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_4 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_3 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_3.Add(self.label_1, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ADJUST_MINSIZE, 5)
        sizer_3.Add(self.combo_box_1, 0, wx.ALL|wx.ADJUST_MINSIZE, 5)
        sizer_3.Add(self.label_2, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ADJUST_MINSIZE, 5)
        sizer_3.Add(self.checkbox_1, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ADJUST_MINSIZE, 5)
        sizer_1.Add(sizer_3, 0, wx.EXPAND, 0)
        sizer_4.Add(self.label_3, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ADJUST_MINSIZE, 5)
        sizer_4.Add(self.text_ctrl_2, 1, wx.ALL|wx.EXPAND|wx.ALIGN_CENTER_VERTICAL, 5)
        sizer_1.Add(sizer_4, 0, wx.EXPAND, 1)
        sizer_1.Add(self.text_ctrl_1, 3, wx.ALL|wx.EXPAND, 5)
        sizer_2.Add(self.button_1, 0, wx.ALL|wx.ADJUST_MINSIZE, 5)
        sizer_2.Add((20, 5), 1, wx.EXPAND, 0)
        sizer_2.Add(self.button_2, 0, wx.ALL|wx.ADJUST_MINSIZE, 5)
        sizer_1.Add(sizer_2, 0, wx.EXPAND, 0)
        sizer_1.Add(self.window_1, 3, wx.ALL|wx.EXPAND, 5)
        self.SetAutoLayout(True)
        self.SetSizer(sizer_1)
        self.Layout()
        # end wxGl

    def edClose(self, event): # wxGlade: MailEditor.<event_handler>
        # Nachfrage, wenn Nachricht nicht versendet
        self.Destroy()

    def edSend(self, event): # wxGlade: MailEditor.<event_handler>
        for user in self.uids:
            if user[1] == self.combo_box_1.GetValue():
                empf = user[0]
                empf_lang = user[1]
        betreff = self.text_ctrl_2.GetValue()
        text = self.text_ctrl_1.GetValue()
        wichtig = self.mail_imp
        self.parent.mail.writeMail(self.parent.user, empf, betreff, text, wichtig)
        msg = u'Nachricht wurde an ' + empf_lang + u' verschickt.'
        if self.mail_imp == u'ja':
            msg += u'\nDie Nachricht wurde als wichtig gekennzeichnet !'
        dlg = wx.MessageDialog(self, msg, 'Information', wx.OK)
        dlg.ShowModal()
        self.Destroy()

    def edHelp(self, event): # wxGlade: MailEditor.<event_handler>
        help = help_gui.helpFrame(None, -1, "", page = 'index.html')
        help.Show()

    def textLeft(self, event): # wxGlade: MailEditor.<event_handler>
        self.textEdit(u'div align="left"')

    def textCenter(self, event): # wxGlade: MailEditor.<event_handler>
        self.textEdit(u'div align="center"')

    def textBold(self, event): # wxGlade: MailEditor.<event_handler>
        self.textEdit(u'b')

    def textItalic(self, event): # wxGlade: MailEditor.<event_handler>
        self.textEdit(u'i')

    def textUnderline(self, event): # wxGlade: MailEditor.<event_handler>
        self.textEdit(u'u')

    def textEdit(self, markup):
        begin, end = self.text_ctrl_1.GetSelection()
        text = self.text_ctrl_1.GetStringSelection()
        new_text = u'<' + markup + u'>' + text + u'</' + markup + u'>'
        self.text_ctrl_1.Replace(begin, end, new_text)

    def butPreview(self, event): # wxGlade: MailEditor.<event_handler>
        text = self.text_ctrl_1.GetValue()
        betreff = self.text_ctrl_2.GetValue()
        self.window_1.SetPage(self.parent.setHTML(text, betreff))

    def edImportant(self, event): # wxGlade: MailEditor.<event_handler>
        if self.mail_imp == u'nein':
            self.mail_imp = u'ja'
        else:
            self.mail_imp = u'nein'

    def edInit(self):
        self.mail_imp = u'nein'
        if not self.parent.answer:
            return
        # ID des Listbox-Eintrags holen, auf den geantwortet werden soll
        listbox_id = self.parent.list_box_1.GetSelection()
        # UID aus Liste mit Tupeln ermittel. [(listbox_id1, UID1), (lis..2, UID2)]
        for t in self.parent.list_uid:
            if t[0] == listbox_id:
                self.to = t[1]
        # Combobox-Eintrag aus Liste mit Tupeln holen. [(UID1, combo_str1), (..2, ..2)]
        for t in self.uids:
            if t[0] == self.to:
                self.combo_box_1.SetValue(t[1])
                quote = t[1]
        # self.parent.mailtext = tuple(Mailtext, Datum, Betreff)
        self.old_text = self.parent.mailtext
        quote += u' schrieb am ' + time.strftime('%x %X', time.gmtime(self.old_text[1]))
        quote += u':\n' + 70 * u'-' + '\n'
        self.text_ctrl_1.AppendText('\n\n' + quote + self.old_text[0])
        self.window_1.SetPage(self.parent.setHTML(self.old_text[0],
                                                  self.old_text[2]))
        self.text_ctrl_2.AppendText('Antwort: ' + self.old_text[2])

# end of class MailEditor

class ShowMail(wx.Frame):
    def __init__(self, *args, **kwds):
        self.parent = args[0]
        # begin wxGlade: ShowMail.__init__
        kwds["style"] = wx.DEFAULT_FRAME_STYLE
        wx.Frame.__init__(self, *args, **kwds)
        
        # Menu Bar
        self.frame_1_menubar = wx.MenuBar()
        self.SetMenuBar(self.frame_1_menubar)
        self.file = wx.Menu()
        self.file_print = wx.MenuItem(self.file, 102, "Drucken", "Nachricht drucken", wx.ITEM_NORMAL)
        self.file.AppendItem(self.file_print)
        self.file_close = wx.MenuItem(self.file, 101, u"Schließen", u"Fenster schließen", wx.ITEM_NORMAL)
        self.file.AppendItem(self.file_close)
        self.frame_1_menubar.Append(self.file, "Datei")
        # Menu Bar end
        self.frame_1_statusbar = self.CreateStatusBar(1, 0)
        
        # Tool Bar
        self.frame_1_toolbar = wx.ToolBar(self, -1)
        self.SetToolBar(self.frame_1_toolbar)
        self.frame_1_toolbar.AddLabelTool(50, u"Schließen", wx.Bitmap("/home/tweimann/workspace/wws/icon/exit.png", wx.BITMAP_TYPE_ANY), wx.NullBitmap, wx.ITEM_NORMAL, u"Fenster schließen", u"Schließt das Mailfenster")
        self.frame_1_toolbar.AddSeparator()
        self.frame_1_toolbar.AddLabelTool(51, "Drucken", wx.Bitmap("/home/tweimann/workspace/wws/icon/print.png", wx.BITMAP_TYPE_ANY), wx.NullBitmap, wx.ITEM_NORMAL, "Nachricht drucken", "Druckt die angezeigte Nachricht")
        # Tool Bar end
        self.window_1 = HtmlWindow(self, -1)

        self.__set_properties()
        self.__do_layout()

        self.Bind(wx.EVT_MENU, self.mClose, self.file_close)
        self.Bind(wx.EVT_MENU, self.parent.mailPrint, self.file_print)
        self.Bind(wx.EVT_TOOL, self.mClose, id=50)
        self.Bind(wx.EVT_TOOL, self.parent.mailPrint, id=51)
        # end wxGlade

    def __set_properties(self):
        # begin wxGlade: ShowMail.__set_properties
        self.SetTitle("")
        self.SetSize((480, 500))
        self.frame_1_statusbar.SetStatusWidths([-1])
        # statusbar fields
        frame_1_statusbar_fields = ["Copyright 2006 by Thorsten Weimann"]
        for i in range(len(frame_1_statusbar_fields)):
            self.frame_1_statusbar.SetStatusText(frame_1_statusbar_fields[i], i)
        self.frame_1_toolbar.Realize()
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: ShowMail.__do_layout
        sizer_1 = wx.BoxSizer(wx.VERTICAL)
        sizer_1.Add(self.window_1, 1, wx.EXPAND, 0)
        self.SetAutoLayout(True)
        self.SetSizer(sizer_1)
        self.Layout()
        # end wxGlade

    def mClose(self, event): # wxGlade: ShowMail.<event_handler>
        self.Destroy()

# end of class ShowMail
