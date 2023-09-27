# -*- coding: utf-8 -*-

###########################################################################
# Python code generated with wxFormBuilder (version 3.10.1-0-g8feb16b3)
# http://www.wxformbuilder.org/
##
# PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
# Class UiBaseInfo
###########################################################################


class UiBaseInfo (wx.Panel):

    def __init__(self, parent, id=wx.ID_ANY, pos=wx.DefaultPosition, size=wx.Size(421, 301), style=wx.TAB_TRAVERSAL, name=wx.EmptyString):
        wx.Panel.__init__(self, parent, id=id, pos=pos,
                          size=size, style=style, name=name)

        sbSizer2 = wx.StaticBoxSizer(wx.StaticBox(
            self, wx.ID_ANY, u"Base Info"), wx.VERTICAL)

        fgSizer2 = wx.FlexGridSizer(0, 2, 0, 0)
        fgSizer2.AddGrowableCol(1)
        fgSizer2.SetFlexibleDirection(wx.BOTH)
        fgSizer2.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        self.m_staticText3 = wx.StaticText(sbSizer2.GetStaticBox(
        ), wx.ID_ANY, u"Material Type", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText3.Wrap(-1)

        self.m_staticText3.SetToolTip(u"Non-conductive base material")

        fgSizer2.Add(self.m_staticText3, 0, wx.ALL, 5)

        combo_material_typeChoices = []
        self.combo_material_type = wx.Choice(sbSizer2.GetStaticBox(
        ), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, combo_material_typeChoices, 0)
        self.combo_material_type.SetSelection(0)
        self.combo_material_type.SetToolTip(u"Non-conductive base material")

        fgSizer2.Add(self.combo_material_type, 0, wx.ALL | wx.EXPAND, 5)

        self.m_staticText4 = wx.StaticText(sbSizer2.GetStaticBox(
        ), wx.ID_ANY, u"Layer Count", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText4.Wrap(-1)

        fgSizer2.Add(self.m_staticText4, 0, wx.ALL, 5)

        combo_layer_countChoices = []
        self.combo_layer_count = wx.Choice(sbSizer2.GetStaticBox(
        ), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, combo_layer_countChoices, 0)
        self.combo_layer_count.SetSelection(0)
        fgSizer2.Add(self.combo_layer_count, 0, wx.ALL | wx.EXPAND, 5)

        sbSizer2.Add(fgSizer2, 0, wx.EXPAND, 5)

        fgSizer3 = wx.FlexGridSizer(0, 2, 0, 0)
        fgSizer3.AddGrowableCol(1)
        fgSizer3.SetFlexibleDirection(wx.HORIZONTAL)
        fgSizer3.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        self.m_staticText5 = wx.StaticText(sbSizer2.GetStaticBox(
        ), wx.ID_ANY, u"Board Type", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText5.Wrap(-1)

        self.m_staticText5.SetToolTip(
            u"The finished PCB are by single or by panel")

        fgSizer3.Add(self.m_staticText5, 0, wx.ALL, 5)

        pcb_package_kindChoices = []
        self.pcb_package_kind = wx.Choice(sbSizer2.GetStaticBox(
        ), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, pcb_package_kindChoices, 0)
        self.pcb_package_kind.SetSelection(0)
        self.pcb_package_kind.SetToolTip(
            u"The finished PCB are by single or by panel")

        fgSizer3.Add(self.pcb_package_kind, 0, wx.ALL | wx.EXPAND, 5)

        self.m_staticText51 = wx.StaticText(sbSizer2.GetStaticBox(
        ), wx.ID_ANY, u"Qty(single)", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText51.Wrap(-1)

        fgSizer3.Add(self.m_staticText51, 0, wx.ALL, 5)

        fgSizer21 = wx.FlexGridSizer(0, 2, 0, 0)
        fgSizer21.AddGrowableCol(0)
        fgSizer21.SetFlexibleDirection(wx.BOTH)
        fgSizer21.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        combo_quantityChoices = []
        self.combo_quantity = wx.Choice(sbSizer2.GetStaticBox(
        ), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, combo_quantityChoices, 0)
        self.combo_quantity.SetSelection(0)
        fgSizer21.Add(self.combo_quantity, 0, wx.ALL | wx.EXPAND, 5)

        self.m_staticText71 = wx.StaticText(sbSizer2.GetStaticBox(
        ), wx.ID_ANY, u"Pcs", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText71.Wrap(-1)

        fgSizer21.Add(self.m_staticText71, 0, wx.ALL, 5)

        fgSizer3.Add(fgSizer21, 1, wx.EXPAND, 5)

        sbSizer2.Add(fgSizer3, 0, wx.EXPAND, 5)

        bSizer2 = wx.BoxSizer(wx.HORIZONTAL)

        sbSizer21 = wx.StaticBoxSizer(wx.StaticBox(
            sbSizer2.GetStaticBox(), wx.ID_ANY, u"Panel Type"), wx.VERTICAL)

        fgSizer4 = wx.FlexGridSizer(0, 2, 0, 0)
        fgSizer4.AddGrowableCol(1)
        fgSizer4.SetFlexibleDirection(wx.BOTH)
        fgSizer4.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        self.m_staticText8 = wx.StaticText(sbSizer21.GetStaticBox(
        ), wx.ID_ANY, u"X:", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText8.Wrap(-1)

        fgSizer4.Add(self.m_staticText8, 0, wx.ALL, 5)

        fgSizer6 = wx.FlexGridSizer(0, 2, 0, 0)
        fgSizer6.AddGrowableCol(0)
        fgSizer6.SetFlexibleDirection(wx.BOTH)
        fgSizer6.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        self.edit_panel_x = wx.TextCtrl(sbSizer21.GetStaticBox(
        ), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        fgSizer6.Add(self.edit_panel_x, 0, wx.ALL | wx.EXPAND, 5)

        self.m_staticText10 = wx.StaticText(sbSizer21.GetStaticBox(
        ), wx.ID_ANY, u"pcs", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText10.Wrap(-1)

        fgSizer6.Add(self.m_staticText10, 0, wx.ALL, 5)

        fgSizer4.Add(fgSizer6, 1, wx.EXPAND, 5)

        self.m_staticText81 = wx.StaticText(sbSizer21.GetStaticBox(
        ), wx.ID_ANY, u"Y:", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText81.Wrap(-1)

        fgSizer4.Add(self.m_staticText81, 0, wx.ALL, 5)

        fgSizer61 = wx.FlexGridSizer(0, 2, 0, 0)
        fgSizer61.AddGrowableCol(0)
        fgSizer61.SetFlexibleDirection(wx.BOTH)
        fgSizer61.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        self.edit_panel_y = wx.TextCtrl(sbSizer21.GetStaticBox(
        ), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        fgSizer61.Add(self.edit_panel_y, 0, wx.ALL | wx.EXPAND, 5)

        self.m_staticText101 = wx.StaticText(sbSizer21.GetStaticBox(
        ), wx.ID_ANY, u"pcs", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText101.Wrap(-1)

        fgSizer61.Add(self.m_staticText101, 0, wx.ALL, 5)

        fgSizer4.Add(fgSizer61, 1, wx.EXPAND, 5)

        sbSizer21.Add(fgSizer4, 1, wx.EXPAND, 5)

        bSizer2.Add(sbSizer21, 1, wx.EXPAND, 5)

        sbSizer211 = wx.StaticBoxSizer(wx.StaticBox(
            sbSizer2.GetStaticBox(), wx.ID_ANY, u"Size (single)"), wx.VERTICAL)

        fgSizer41 = wx.FlexGridSizer(0, 2, 0, 0)
        fgSizer41.AddGrowableCol(1)
        fgSizer41.SetFlexibleDirection(wx.BOTH)
        fgSizer41.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        self.m_staticText82 = wx.StaticText(sbSizer211.GetStaticBox(
        ), wx.ID_ANY, u"X:", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText82.Wrap(-1)

        fgSizer41.Add(self.m_staticText82, 0, wx.ALL, 5)

        fgSizer62 = wx.FlexGridSizer(0, 2, 0, 0)
        fgSizer62.AddGrowableCol(0)
        fgSizer62.SetFlexibleDirection(wx.BOTH)
        fgSizer62.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        self.edit_size_x = wx.TextCtrl(sbSizer211.GetStaticBox(
        ), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        fgSizer62.Add(self.edit_size_x, 0, wx.ALL | wx.EXPAND, 5)

        self.m_staticText102 = wx.StaticText(sbSizer211.GetStaticBox(
        ), wx.ID_ANY, u"pcs", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText102.Wrap(-1)

        fgSizer62.Add(self.m_staticText102, 0, wx.ALL, 5)

        fgSizer41.Add(fgSizer62, 1, wx.EXPAND, 5)

        self.m_staticText811 = wx.StaticText(sbSizer211.GetStaticBox(
        ), wx.ID_ANY, u"Y:", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText811.Wrap(-1)

        fgSizer41.Add(self.m_staticText811, 0, wx.ALL, 5)

        fgSizer611 = wx.FlexGridSizer(0, 2, 0, 0)
        fgSizer611.AddGrowableCol(0)
        fgSizer611.SetFlexibleDirection(wx.BOTH)
        fgSizer611.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        self.edit_size_y = wx.TextCtrl(sbSizer211.GetStaticBox(
        ), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        fgSizer611.Add(self.edit_size_y, 0, wx.ALL | wx.EXPAND, 5)

        self.m_staticText1011 = wx.StaticText(sbSizer211.GetStaticBox(
        ), wx.ID_ANY, u"pcs", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText1011.Wrap(-1)

        fgSizer611.Add(self.m_staticText1011, 0, wx.ALL, 5)

        fgSizer41.Add(fgSizer611, 1, wx.EXPAND, 5)

        sbSizer211.Add(fgSizer41, 1, wx.EXPAND, 5)

        bSizer2.Add(sbSizer211, 1, wx.EXPAND, 5)

        sbSizer2.Add(bSizer2, 0, wx.EXPAND, 5)

        sbSizer12 = wx.StaticBoxSizer(wx.StaticBox(
            sbSizer2.GetStaticBox(), wx.ID_ANY, u"Break-away Rail"), wx.VERTICAL)

        fgSizer24 = wx.FlexGridSizer(0, 3, 0, 0)
        fgSizer24.AddGrowableCol(1)
        fgSizer24.SetFlexibleDirection(wx.BOTH)
        fgSizer24.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        comb_margin_modeChoices = []
        self.comb_margin_mode = wx.Choice(sbSizer12.GetStaticBox(
        ), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, comb_margin_modeChoices, 0)
        self.comb_margin_mode.SetSelection(0)
        fgSizer24.Add(self.comb_margin_mode, 0, wx.ALL, 5)

        self.edit_margin_size = wx.TextCtrl(sbSizer12.GetStaticBox(
        ), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        fgSizer24.Add(self.edit_margin_size, 0, wx.ALL | wx.EXPAND, 5)

        self.m_staticText39 = wx.StaticText(sbSizer12.GetStaticBox(
        ), wx.ID_ANY, u"mm", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText39.Wrap(-1)

        fgSizer24.Add(self.m_staticText39, 0, wx.ALL, 5)

        sbSizer12.Add(fgSizer24, 1, wx.EXPAND, 5)

        sbSizer2.Add(sbSizer12, 0, wx.EXPAND, 5)

        self.SetSizer(sbSizer2)
        self.Layout()

    def __del__(self):
        pass
