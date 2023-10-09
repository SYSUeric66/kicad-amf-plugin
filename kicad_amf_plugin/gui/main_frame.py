
from kicad_amf_plugin.kicad.board_manager import BoardManager
from kicad_amf_plugin.pcb_fabrication.base.base_info_view import BaseInfoView
from kicad_amf_plugin.pcb_fabrication.process.process_info_view import ProcessInfoView
from kicad_amf_plugin.pcb_fabrication.special_process.special_process_view import SpecialProcessView
from kicad_amf_plugin.pcb_fabrication.personalized.personalized_info_view import PersonalizedInfoView
from kicad_amf_plugin.pcb_fabrication.order.order_info_view import OrderInfoView
from kicad_amf_plugin.gui.event.pcb_fabrication_evt_list import EVT_LAYER_COUNT_CHANGE , LayerCountChange

import wx
import wx.xrc
import wx.dataview


class MainFrame (wx.Frame):

    def __init__(self, board_manager : BoardManager ,  parent = None):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=_(u"HQ NextPCB Active Manufacturing"),
                           pos=wx.DefaultPosition, size=wx.Size(900, 600), style=wx.DEFAULT_DIALOG_STYLE | wx.RESIZE_BORDER)
        wx.SizerFlags.DisableConsistencyChecks()
        self.board_manager = board_manager
        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)
        main_sizer = wx.BoxSizer(wx.HORIZONTAL)

        pcb_fab_panel = wx.ScrolledWindow(
            self, wx.ID_ANY, wx.DefaultPosition, wx.Size(-1, -1), wx.HSCROLL | wx.VSCROLL)
        pcb_fab_panel.SetScrollRate(10, 10)
        lay_pcb_fab_panel = wx.BoxSizer(wx.VERTICAL)

        base_info_panel = BaseInfoView(pcb_fab_panel , self.board_manager)
        lay_pcb_fab_panel.Add(base_info_panel, 0, wx.ALL | wx.EXPAND, 5)
        

        process_info_panel = ProcessInfoView(pcb_fab_panel , self.board_manager)
        lay_pcb_fab_panel.Add(process_info_panel, 0, wx.ALL | wx.EXPAND, 5)

        special_process_panel = SpecialProcessView(pcb_fab_panel, self.board_manager)
        lay_pcb_fab_panel.Add(special_process_panel, 0, wx.ALL | wx.EXPAND, 5)

        service_panel = PersonalizedInfoView(
            pcb_fab_panel)
        lay_pcb_fab_panel.Add(service_panel, 0, wx.ALL | wx.EXPAND, 5)

        pcb_fab_panel.SetSizer(lay_pcb_fab_panel)
        pcb_fab_panel.Layout()
        
        order_info_view = OrderInfoView(self)

        main_sizer.Add(pcb_fab_panel, 1, wx.EXPAND, 8)
        main_sizer.Add(order_info_view, 0, wx.EXPAND, 8)

        self.Bind(EVT_LAYER_COUNT_CHANGE , process_info_panel.on_layer_count_changed )


        for i in base_info_panel , process_info_panel : 
            i.init()

        self.SetSizer(main_sizer)
        self.Layout()
        self.Centre(wx.BOTH)


    def __del__(self):
        pass


    # Virtual event handlers, override them in your derived class
    def OnTemplateChanged(self, event):
        event.Skip()

    def OnPcbPackagingChanged(self, event):
        event.Skip()

    def OnPanelizeXChanged(self, event):
        event.Skip()

    def OnPanelizeYChanged(self, event):
        event.Skip()

    def OnPcbQuantityChanged(self, event):
        event.Skip()

    def OnMarginModeChanged(self, event):
        event.Skip()

    def OnSurfaceProcessChanged(self, event):
        event.Skip()

    def OnHDIChanged(self, event):
        event.Skip()

    def OnReportChanged(self, event):
        event.Skip()

    def OnUpdatePrice(self, event):
        event.Skip()

    def OnPlaceOrder(self, event):
        event.Skip()

    def OnMaskColorChange(self, event):
        event.Skip()

    def OnThicknessChangebyLayer(self, event):
        event.Skip()
