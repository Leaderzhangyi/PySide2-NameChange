# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Oct 26 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.grid

###########################################################################
## Class MyFrame4
###########################################################################

class MyFrame4 ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"作业名称修改器 张大帅制作https://zyink.top", pos = wx.DefaultPosition, size = wx.Size( 885,806 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		fgSizer6 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer6.SetFlexibleDirection( wx.BOTH )
		fgSizer6.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_staticText2 = wx.StaticText( self, wx.ID_ANY, u"数据显示(仅前100条)", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTER_HORIZONTAL )
		self.m_staticText2.Wrap( -1 )

		self.m_staticText2.SetFont( wx.Font( 16, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "腾讯体" ) )
		self.m_staticText2.SetForegroundColour( wx.Colour( 0, 0, 0 ) )
		self.m_staticText2.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_APPWORKSPACE ) )

		fgSizer6.Add( self.m_staticText2, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_staticText13 = wx.StaticText( self, wx.ID_ANY, u"进行此操作前最好先备份！！", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTER_HORIZONTAL )
		self.m_staticText13.Wrap( -1 )

		self.m_staticText13.SetFont( wx.Font( 12, wx.FONTFAMILY_MODERN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "楷体" ) )
		self.m_staticText13.SetBackgroundColour( wx.Colour( 255, 255, 0 ) )

		fgSizer6.Add( self.m_staticText13, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_grid12 = wx.grid.Grid( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )

		# Grid
		self.m_grid12.CreateGrid( 50, 2 )
		self.m_grid12.EnableEditing( True )
		self.m_grid12.EnableGridLines( True )
		self.m_grid12.SetGridLineColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INACTIVECAPTION ) )
		self.m_grid12.EnableDragGridSize( False )
		self.m_grid12.SetMargins( 0, 0 )

		# Columns
		self.m_grid12.EnableDragColMove( False )
		self.m_grid12.EnableDragColSize( True )
		self.m_grid12.SetColLabelSize( 30 )
		self.m_grid12.SetColLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Rows
		self.m_grid12.EnableDragRowSize( True )
		self.m_grid12.SetRowLabelSize( 80 )
		self.m_grid12.SetRowLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Label Appearance

		# Cell Defaults
		self.m_grid12.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
		fgSizer6.Add( self.m_grid12, 0, wx.ALL|wx.EXPAND, 5 )

		bSizer8 = wx.BoxSizer( wx.VERTICAL )

		self.m_textCtrl4 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 900,30 ), 0 )
		bSizer8.Add( self.m_textCtrl4, 0, wx.ALL, 5 )

		self.m_button99 = wx.Button( self, wx.ID_ANY, u"选择学号姓名文件", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer8.Add( self.m_button99, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_button100 = wx.Button( self, wx.ID_ANY, u"读取数据", wx.DefaultPosition, wx.Size( 200,50 ), 0 )
		self.m_button100.SetFont( wx.Font( 12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "宋体" ) )
		self.m_button100.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INACTIVECAPTION ) )

		bSizer8.Add( self.m_button100, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		wSizer6 = wx.WrapSizer( wx.HORIZONTAL, wx.WRAPSIZER_DEFAULT_FLAGS )

		self.m_checkBox2 = wx.CheckBox( self, wx.ID_ANY, u"是否检测未交", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_checkBox2.SetValue(True)
		self.m_checkBox2.SetFont( wx.Font( 9, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "宋体" ) )

		wSizer6.Add( self.m_checkBox2, 0, wx.ALL, 5 )

		self.m_textCtrl5 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 450,-1 ), 0 )
		wSizer6.Add( self.m_textCtrl5, 0, wx.ALL|wx.EXPAND, 5 )

		bSizer9 = wx.BoxSizer( wx.VERTICAL )

		bSizer9.SetMinSize( wx.Size( 600,-1 ) )
		self.m_staticText4 = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.Point( -1,-1 ), wx.DefaultSize, 0 )
		self.m_staticText4.Wrap( -1 )

		self.m_staticText4.SetFont( wx.Font( 14, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "阿里巴巴普惠体 H" ) )
		self.m_staticText4.SetForegroundColour( wx.Colour( 162, 36, 36 ) )

		bSizer9.Add( self.m_staticText4, 0, wx.ALL, 5 )

		self.m_button115 = wx.Button( self, wx.ID_ANY, u"选择修改文件夹路径", wx.DefaultPosition, wx.Size( -1,40 ), 0 )
		bSizer9.Add( self.m_button115, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		wSizer2 = wx.WrapSizer( wx.HORIZONTAL, wx.WRAPSIZER_DEFAULT_FLAGS )

		self.m_staticText5 = wx.StaticText( self, wx.ID_ANY, u"输入学号前4位：", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText5.Wrap( -1 )

		wSizer2.Add( self.m_staticText5, 0, wx.ALL, 5 )

		self.m_textCtrl3 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		wSizer2.Add( self.m_textCtrl3, 0, wx.ALL, 5 )

		self.m_staticText6 = wx.StaticText( self, wx.ID_ANY, u"输入文件名名称：", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText6.Wrap( -1 )

		wSizer2.Add( self.m_staticText6, 0, wx.ALL, 5 )

		self.m_textCtrl41 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 210,-1 ), 0 )
		wSizer2.Add( self.m_textCtrl41, 0, wx.ALL, 5 )

		self.m_staticText7 = wx.StaticText( self, wx.ID_ANY, u"请选择相应格式：", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText7.Wrap( -1 )

		wSizer2.Add( self.m_staticText7, 0, wx.ALL, 5 )

		m_choice1Choices = [ u"学号-姓名-文件名称", u"姓名-学号-文件名称", u"文件名称-姓名-学号", u"文件名称-学号-姓名" ]
		self.m_choice1 = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 220,-1 ), m_choice1Choices, 0 )
		self.m_choice1.SetSelection( 0 )
		wSizer2.Add( self.m_choice1, 0, wx.ALL, 5 )

		self.m_staticText8 = wx.StaticText( self, wx.ID_ANY, u"请选择连接符：", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText8.Wrap( -1 )

		wSizer2.Add( self.m_staticText8, 0, wx.ALL, 5 )

		m_choice2Choices = [ u"-", u"--", u"+", u"_", u"——" ]
		self.m_choice2 = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 110,-1 ), m_choice2Choices, 0 )
		self.m_choice2.SetSelection( 2 )
		self.m_choice2.SetFont( wx.Font( 12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "宋体" ) )

		wSizer2.Add( self.m_choice2, 0, wx.ALL, 5 )


		bSizer9.Add( wSizer2, 1, wx.EXPAND, 5 )

		self.m_button116 = wx.Button( self, wx.ID_ANY, u"开始修改 ", wx.DefaultPosition, wx.Size( 200,60 ), 0 )
		self.m_button116.SetFont( wx.Font( 14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "腾讯体" ) )
		self.m_button116.SetBackgroundColour( wx.Colour( 255, 0, 0 ) )

		bSizer9.Add( self.m_button116, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_gauge2 = wx.Gauge( self, wx.ID_ANY, 100, wx.DefaultPosition, wx.Size( -1,30 ), wx.GA_HORIZONTAL )
		self.m_gauge2.SetValue( 0 )
		bSizer9.Add( self.m_gauge2, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.EXPAND, 5 )

		self.m_staticText14 = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText14.Wrap( -1 )

		bSizer9.Add( self.m_staticText14, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


		wSizer6.Add( bSizer9, 1, wx.EXPAND|wx.ALIGN_CENTER_VERTICAL, 5 )


		bSizer8.Add( wSizer6, 1, wx.EXPAND, 5 )

		bSizer3 = wx.BoxSizer( wx.VERTICAL )

		self.m_textCtrl6 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE )
		self.m_textCtrl6.SetForegroundColour( wx.Colour( 255, 0, 0 ) )
		self.m_textCtrl6.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )

		bSizer3.Add( self.m_textCtrl6, 1, wx.ALL|wx.EXPAND, 5 )


		bSizer8.Add( bSizer3, 1, wx.EXPAND, 5 )


		fgSizer6.Add( bSizer8, 1, wx.EXPAND, 5 )


		self.SetSizer( fgSizer6 )
		self.Layout()
		self.m_menubar1 = wx.MenuBar( 0 )
		self.m_menu3 = wx.Menu()
		self.m_menuItem1 = wx.MenuItem( self.m_menu3, wx.ID_ANY, u"使用说明", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu3.Append( self.m_menuItem1 )

		self.m_menubar1.Append( self.m_menu3, u"帮助" )

		self.m_menu2 = wx.Menu()
		self.m_menuItem2 = wx.MenuItem( self.m_menu2, wx.ID_ANY, u"图片分类器", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu2.Append( self.m_menuItem2 )

		self.m_menubar1.Append( self.m_menu2, u"其他工具" )

		self.SetMenuBar( self.m_menubar1 )


		self.Centre( wx.BOTH )

		# Connect Events
		self.m_button99.Bind( wx.EVT_BUTTON, self.m_button99OnButtonClick )
		self.m_button100.Bind( wx.EVT_BUTTON, self.m_button100OnButtonClick )
		self.m_checkBox2.Bind( wx.EVT_CHECKBOX, self.m_checkBox2OnCheckBox )
		self.m_button115.Bind( wx.EVT_BUTTON, self.m_button115OnButtonClick )
		self.m_choice1.Bind( wx.EVT_CHOICE, self.m_choice1OnChoice )
		self.m_button116.Bind( wx.EVT_BUTTON, self.m_button116OnButtonClick )
		self.Bind( wx.EVT_MENU, self.m_menuItem1OnMenuSelection, id = self.m_menuItem1.GetId() )
		self.Bind( wx.EVT_MENU, self.m_menuItem2OnMenuSelection, id = self.m_menuItem2.GetId() )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def m_button99OnButtonClick( self, event ):
		event.Skip()

	def m_button100OnButtonClick( self, event ):
		event.Skip()

	def m_checkBox2OnCheckBox( self, event ):
		event.Skip()

	def m_button115OnButtonClick( self, event ):
		event.Skip()

	def m_choice1OnChoice( self, event ):
		event.Skip()

	def m_button116OnButtonClick( self, event ):
		event.Skip()

	def m_menuItem1OnMenuSelection( self, event ):
		event.Skip()

	def m_menuItem2OnMenuSelection( self, event ):
		event.Skip()


###########################################################################
## Class classification
###########################################################################

class classification ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 756,528 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		fgSizer2 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer2.SetFlexibleDirection( wx.BOTH )
		fgSizer2.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_slider1 = wx.Slider( self, wx.ID_ANY, 50, 0, 100, wx.DefaultPosition, wx.DefaultSize, wx.SL_HORIZONTAL )
		fgSizer2.Add( self.m_slider1, 0, wx.ALL, 5 )

		self.m_gauge2 = wx.Gauge( self, wx.ID_ANY, 100, wx.DefaultPosition, wx.DefaultSize, wx.GA_HORIZONTAL )
		self.m_gauge2.SetValue( 0 )
		fgSizer2.Add( self.m_gauge2, 0, wx.ALL, 5 )

		self.m_staticline1 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		fgSizer2.Add( self.m_staticline1, 0, wx.EXPAND |wx.ALL, 5 )


		self.SetSizer( fgSizer2 )
		self.Layout()

		self.Centre( wx.BOTH )

	def __del__( self ):
		pass


