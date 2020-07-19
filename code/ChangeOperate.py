from UI.noname import *
from socket import *
from client_config import *
import pandas as pd
import wx, os, re
import webbrowser


# self.icon = wx.Icon('work.ico', wx.BITMAP_TYPE_ICO)
# self.SetIcon(self.icon)
client_socket = socket(AF_INET, SOCK_STREAM)

class Myframe(MyFrame4):
    def __init__(self, parent):


        # wx.MessageDialog(None, u"网络连接", u'请求服务器失败,请检查网络连接!', wx.OK)

        #client_socket.connect((host, port))
        MyFrame4.__init__(self, parent)




    def m_button99OnButtonClick(self, event):  # 选择文件
        # wildcard = "Text Files (*.txt)|*.txt"
        # file_wildcard = "Paint files(*.paint)|*.paint|All files(*.*)|*.*"
        dlg = wx.FileDialog(self, "Open xls/xlsx file",
                            wildcard="Excel files(*.xls/*.xlsx)|*.xls;*.xlsx",
                            style=wx.FD_OPEN | wx.FD_FILE_MUST_EXIST)
        if dlg.ShowModal() == wx.ID_OK:
            self.m_textCtrl4.Value = dlg.GetPath()
        dlg.Destroy()

    def get_name_list(self, path):
        data = pd.read_excel(path)
        data['学号'] = data['学号'].astype('int64')
        name_list = data[['姓名', '学号']]
        name_list = dict(name_list.values.tolist())
        name_list = dict([str(value), key] for key, value in name_list.items())
        return name_list

    def to_check(self, offer_list, name_list):
        self.m_grid12.ClearGrid()
        olist = [int(i) for i in offer_list]
        olist.sort()
        id_list = [int(i) for i in name_list.keys()]
        no_offer = [i for i in id_list if i not in olist]
        self.m_staticText2.SetLabelText("有" + str(len(no_offer)) + "人未交！")
        self.m_staticText2.SetForegroundColour((255, 0, 0))
        for i, item in enumerate(no_offer):
            self.m_grid12.SetCellValue(i, 0, str(item))
            self.m_grid12.SetCellValue(i, 1, name_list[str(item)])

    def setName(self, format_signal, st_number, name_list, File_Name):

        symbol = self.m_choice2.GetStringSelection()
        if format_signal == 0:
            right_name = st_number + symbol + name_list[st_number] + symbol + File_Name
        elif format_signal == 1:
            right_name = name_list[st_number] + symbol + st_number + symbol + File_Name
        elif format_signal == 2:
            right_name = File_Name + symbol + name_list[st_number] + symbol + st_number
        else:
            right_name = File_Name + symbol + st_number + symbol + name_list[st_number]
        return right_name

    def to_rename(self, work_path, name_list, four_num, File_Name, format_signal):
        work_list = os.listdir(work_path)
        res_error = "此文件学号格式错误或花名册中无此学号(可能此人存在多份文件)！"

        offer = []
        for item in work_list:
            res_name = os.path.splitext(item)
            filename = res_name[0]
            filetype = res_name[1]
            try:

                st_number = re.findall('(' + four_num + '\d+)', item)[0]
                right_name = self.setName(format_signal, st_number, name_list, File_Name)
                offer.append(st_number)
                if item != right_name:
                    os.rename(os.path.join(work_path, item), os.path.join(work_path, right_name + filetype))
            except:
                res_error += "\n" + filename
                # print("此文件学号格式错误或花名册中无此学号(可能此人存在多份文件)！--->\033[0;31m%s\033[0m" % filename)
        # print(res_error)
        if res_error != "此文件学号格式错误或花名册中无此学号(可能此人存在多份文件)！":
            self.m_textCtrl6.Value = res_error

        if self.m_checkBox2.IsChecked():
            self.to_check(offer, name_list)

    def m_button100OnButtonClick(self, event):
        self.m_staticText2.SetLabelText("数据显示(仅前100条)")
        self.m_staticText2.SetForegroundColour((0, 0, 0))
        self.m_grid12.ClearGrid()
        if self.m_textCtrl4.Value == "":
            dlg = wx.MessageDialog(None, u"请选择学号姓名文件！", u"警告", wx.OK | wx.ICON_HAND)
            if dlg.ShowModal() == wx.ID_YES:
                self.Close(True)
            dlg.Destroy()
        else:
            path = self.m_textCtrl4.Value
            try:
                self.name_list = self.get_name_list(path)
                self.m_grid12.SetColLabelValue(0, "学号")
                self.m_grid12.SetColLabelValue(1, "姓名")
                try:
                    for i, item in enumerate(self.name_list.items()):
                        self.m_grid12.SetCellValue(i, 0, item[0])
                        self.m_grid12.SetCellValue(i, 1, item[1])
                finally:
                    self.m_staticText4.SetLabelText("读取成功！")
            except:
                self.m_staticText4.SetLabelText("读取失败！请检查Excel列名是否在第一行！")

    def m_button115OnButtonClick(self, event):
        dlg = wx.DirDialog(self, u"选择文件夹", style=wx.DD_DEFAULT_STYLE)
        if dlg.ShowModal() == wx.ID_OK:
            self.m_textCtrl5.Value = dlg.GetPath()
        dlg.Destroy()

    def m_button116OnButtonClick(self, event):
        if self.m_textCtrl4.Value == "":
            dlg = wx.MessageDialog(None, u"先选择相应文件！", u"错误", wx.OK | wx.ICON_HAND)
            if dlg.ShowModal() == wx.ID_YES:
                self.Close(True)
            dlg.Destroy()

        elif self.m_textCtrl3.Value == "":
            dlg = wx.MessageDialog(None, u"请填写学号！", u"错误", wx.OK | wx.ICON_HAND)
            if dlg.ShowModal() == wx.ID_YES:
                self.Close(True)
            dlg.Destroy()

        else:
            num = self.m_textCtrl3.Value
            fileName = self.m_textCtrl41.Value
            format_status = self.m_choice1.GetCurrentSelection()

            self.to_rename(self.m_textCtrl5.Value, self.name_list, num, fileName, format_status)
            self.m_gauge2.SetValue(100)

    def m_menuItem1OnMenuSelection(self, event):
        webbrowser.open("https://zyink.top/homework_change.html")

    def m_menuItem2OnMenuSelection(self, event):
        frame2 = Second(None)
        frame2.Show()


class Second(classification):
    def __init__(self, parent):
        classification.__init__(self, parent)
