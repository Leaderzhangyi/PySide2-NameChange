from UI_dist.Des_UI import Ui_MainWindow
from UI_dist.customize import Ui_Dialog
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from PySide2.QtCore import QSettings
import pandas as pd
import os, re, math
import webbrowser
from threading import Thread


class MainWindow(Ui_MainWindow, QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        # 使用ui文件导入定义界面类
        # 初始化界面
        self.setupUi(self)
        self.setWindowIcon(QIcon("./icon/work.ico"))

        self.app_data = QSettings('config.ini', QSettings.IniFormat)
        self.app_data.setIniCodec('utf-8')  # 设置ini文件编码为 UTF-8
        self.cwd = self.app_data.value("SETUP/PATH")
        self.progressBar.setMaximum(100)
        self.progressBar.setValue(0)
        self.student_table = {}
        self.Var_Init()
        self.Button_Init()  # 信号初始化

        # 设置表格参数
        self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)  # 自适应列宽
        self.tableWidget.horizontalHeader().setSectionResizeMode(0, QHeaderView.Interactive)  # 仅首列可手动调整
        # self.tableWidget.verticalHeader().setVisible(False)  # 隐藏行表头

    def Var_Init(self):
        self.format_list = ["学号-姓名-文件名称(默认)", "姓名-学号-文件名称", "文件名称-学号-姓名", "文件名称-姓名-学号", "班级-学号-姓名-文件名称",
                            "自定义(班上有同名者，慎用)"]
        dir_set = set() if self.app_data.value("SETUP/DIR_PATH") is None else self.app_data.value("SETUP/DIR_PATH")
        # print("初始化set---",dir_set,type(dir_set))
        data_path = self.app_data.value("SETUP/DATA_PATH")
        number = self.app_data.value("SETUP/FOUR_ID")
        FileNames = self.app_data.value("SETUP/CHANGE_FIlENAME")
        ClassName = self.app_data.value("SETUP/CLASSNAME")
        Char_format = self.app_data.value("SETUP/SIGNAL")
        Format_list = [] if self.app_data.value("SETUP/FORMAT_LIST") is None else [self.app_data.value(
            "SETUP/FORMAT_LIST")]
        if len(Format_list) > len(self.format_list):
            self.format_list = Format_list
        self.dir_set = dir_set
        self.lineEdit_2.setText(data_path)
        self.number.setText(number)
        self.charsplit.setText(Char_format)
        self.ClassName.setText(ClassName)
        self.FileNames.setText(FileNames)
        self.data_path = self.lineEdit_2.text()
        self.comboBox.addItems(self.dir_set)
        self.comboBox_2.addItems(self.format_list)
        self.btn_delete.setEnabled(False)
        self.Download.setEnabled(False)
        if len(self.dir_set) != 0:
            self.comboBox.addItem(QIcon("./icon/clear.png"), "清除所有历史记录")

    def Button_Init(self):
        # self.radioButton.toggled.connect(lambda: self.Radio_Download(self.radioButton))
        self.Change.clicked.connect(self.Change_Name)  # begin change
        self.select1.clicked.connect(self.Get_DataFilename)
        self.select2.clicked.connect(self.Get_Filename)
        self.GetData.clicked.connect(self.Read_Data)
        self.Download.clicked.connect(self.Download_Incompete)
        self.btn_delete.clicked.connect(self.Delete_options)
        self.menu.triggered[QAction].connect(self.Other_menu)
        self.menu_2.triggered[QAction].connect(self.About)
        self.comboBox.activated[str].connect(self.clear_all)
        self.comboBox_2.activated[str].connect(self.Customize)
        self.comboBox_2.highlighted[str].connect(self.Set_Delete_btn)
        self.Download.setToolTip("导出未交人员名单")
        self.btn_delete.setToolTip("删除自定义选项")

    def get_name_list(self, path):
        data = pd.read_excel(path)
        data['学号'] = data['学号'].astype('int64')
        name_list = data[['姓名', '学号']]
        name_list = dict(name_list.values.tolist())
        name_list = dict([str(value), key] for key, value in name_list.items())
        return name_list

    def Get_DataFilename(self):
        file_choose, filetype = QFileDialog.getOpenFileName(self, "选择学号姓名文件", self.cwd,
                                                            "Excel files (*.csv *.xlsx *.xls)")
        self.data_path = file_choose
        self.app_data.setValue("SETUP/PATH", file_choose)
        self.cwd = file_choose
        self.lineEdit_2.setText(file_choose)

    def Get_Filename(self):
        dir_choose = QFileDialog.getExistingDirectory(self, "选择修改文件夹", self.cwd)
        self.app_data.value("SETUP/PATH", dir_choose)
        self.comboBox.clear()
        self.dir_set.add(dir_choose)
        print(type(self.dir_set))
        self.comboBox.addItems(self.dir_set)
        self.comboBox.setCurrentText(dir_choose)
        if len(self.dir_set) != 0:
            self.comboBox.addItem(QIcon("./icon/clear.png"), "清除所有历史记录")

    # def Radio_Download(self, btn):
    #     self.Download.setEnabled(btn.isChecked())

    def Read_Data(self):
        self.tableWidget.clear()
        self.label.setText("仅展示前50条数据")
        if self.data_path == "":
            QMessageBox.critical(self, "错误", "请选择信息文件！", QMessageBox.Yes)
        else:
            self.student_table = self.get_name_list(self.data_path)
            self.tableWidget.setRowCount(50)
            self.tableWidget.setHorizontalHeaderLabels(['学号', '姓名'])
            self.Download.setEnabled(False)
            try:
                for row, (id, name) in enumerate(self.student_table.items()):
                    self.tableWidget.setItem(row, 0, QTableWidgetItem(str(id)))
                    self.tableWidget.setItem(row, 1, QTableWidgetItem(str(name)))
            except:
                QMessageBox.information(self, "说明", "仅展示前50条数据")

    def Change_Name(self):
        # print(self.dir_set)
        # print(type(self.dir_set))
        # print(set(self.dir_set))
        self.app_data.setValue("SETUP/DIR_PATH", self.dir_set)
        self.app_data.setValue("SETUP/DATA_PATH", self.data_path)
        self.app_data.setValue("SETUP/FOUR_ID", self.number.text())
        self.app_data.setValue("SETUP/CHANGE_FIlENAME", self.FileNames.text())
        self.app_data.setValue("SETUP/CLASSNAME", self.ClassName.text())
        self.app_data.setValue("SETUP/FORMAT_LIST", self.format_list)
        self.app_data.setValue("SETUP/SIGNAL", self.charsplit.text())
        if self.number.text() == "":
            QMessageBox.critical(self, "错误", "请填写学号前4位！")
        elif self.student_table == {}:
            QMessageBox.critical(self, "错误", "未读取数据！")
        elif self.comboBox.currentText() == "":
            QMessageBox.critical(self, "错误", "未选择修改文件路径！")
        else:
            self.to_rename(self.comboBox.currentText(), self.student_table, self.number.text(), self.FileNames.text(),
                           self.ClassName.text(), self.charsplit.text())

    def to_rename(self, work_path, name_list, four_num, File_Name, ClassName, format_signal):
        work_list = os.listdir(work_path)
        res_error = "此文件学号格式错误或花名册中无此学号(可能此人存在多份文件)！"
        self.textBrowser.setText("未出现异常错误....")
        offer = []
        for item in work_list:
            res_name = os.path.splitext(item)
            filename = res_name[0]
            filetype = res_name[1]
            try:
                st_number = re.findall('(' + four_num + '\d+)', item)[0]
                # print("找到的学号---",st_number)
                right_name = self.setName(format_signal, st_number, name_list, ClassName, File_Name)
                offer.append(st_number)
                if item != right_name:
                    os.rename(os.path.join(work_path, item), os.path.join(work_path, right_name + filetype))
            except:
                print("大大大大")
                res_error += "\n" + filename

        if res_error != "此文件学号格式错误或花名册中无此学号(可能此人存在多份文件)！":
            self.textBrowser.setText(res_error)

        if self.radioButton.isChecked():
            self.to_check(offer, name_list)

        else:
            self.progressBar.setValue(100)
            # self.textBrowser.setText("未出现异常错误....")
            QMessageBox.information(self, "完成", "修改完成，请到文件夹中查看")

    def setName(self, format_signal, st_number, name_list, ClassName, File_Name):
        right_format = self.comboBox_2.currentText().split("-")
        format_dict = dict(zip(['学号', '姓名', '文件名称', '文件名称(默认)', '班级'],
                               [st_number, name_list[st_number], File_Name, File_Name, ClassName]))
        ans = [format_dict[item] for item in right_format]
        ans = list(filter(None, ans))
        if format_signal == "":
            return "-".join(ans)
        else:
            return format_signal.join(ans)

    def to_check(self, offer_list, name_list):
        self.tableWidget.clear()
        olist = [int(i) for i in offer_list]
        olist.sort()
        id_list = [int(i) for i in name_list.keys()]
        total = len(self.student_table)
        self.no_offer = [i for i in id_list if i not in olist]
        result = "有" + str(len(self.no_offer)) + "人未交！\n收齐作业进度为 %%%.2f" % (
                (total - len(self.no_offer)) / float(total)) + "\n点击表格右上角的↓按钮可以导出未交名单"
        self.tableWidget.setHorizontalHeaderLabels(['学号', '姓名'])
        self.tableWidget.clear()
        for i, item in enumerate(self.no_offer):
            if i == 49:
                break
            self.tableWidget.setItem(i, 0, QTableWidgetItem(str(item)))
            self.tableWidget.setItem(i, 1, QTableWidgetItem(name_list[str(item)]))
        self.label.setText("有" + str(len(self.no_offer)) + "人未交！")
        self.Download.setEnabled(True)
        pv = (len(name_list) - len(self.no_offer)) / float(len(name_list))
        self.progressBar.setValue(math.ceil(pv))
        QMessageBox.information(self, "结果", result)

    def Download_Incompete(self):

        df = pd.DataFrame(columns=['学号', '姓名'])
        df["学号"] = self.no_offer
        df["姓名"] = [self.student_table[str(item)] for item in self.no_offer]
        file_choose, filetype = QFileDialog.getSaveFileName(self, "未交人员名单", self.cwd, "Excel files (*.xlsx);;CSV files("
                                                                                      "*.csv)")
        if filetype == "Excel files (*.xlsx)":
            df.to_excel(file_choose, index=False)
        elif filetype == "CSV files(*.csv)":
            df.to_csv(file_choose, index=False)

    def Other_menu(self, ans):
        if ans.text() == "交作业倒计时" or "催作业轰炸器":
            QMessageBox.information(self, "其他工具", "敬请期待")

    def About(self, ans):
        if ans.text() == "Github" or "使用说明":
            webbrowser.open("https://github.com/Leaderzhangyi/Pyqt5-Change")

    def clear_all(self, text):
        if text == "清除所有历史记录":
            self.comboBox.clear()
            self.dir_set.clear()

    def Customize(self, text):
        if text == "自定义(班上有同名者，慎用)":
            custdia = Customize_Dialog()
            r = custdia.exec_()
            if r > 0:
                format_item = custdia.get_customize_format()
                now_format = {'学号', '姓名', '文件名称', '班级'}
                if format_item == "":
                    return None
                elif not set(format_item.split("-")).issubset(now_format):
                    QMessageBox.critical(self, "错误", "请按要求填写自定义格式！")
                else:
                    self.format_list.insert(0, format_item)
                    self.comboBox_2.clear()
                    self.comboBox_2.addItems(self.format_list)
                    self.comboBox_2.setCurrentText(self.format_list[0])

    def Set_Delete_btn(self, text):
        if text in self.format_list[-6:]:
            self.btn_delete.setEnabled(False)

        elif text not in self.format_list[-6:]:
            self.btn_delete.setEnabled(True)

    def Delete_options(self):
        index = self.comboBox_2.currentIndex()
        self.comboBox_2.removeItem(index)
        self.format_list.remove(self.comboBox_2.currentText())


class Customize_Dialog(Ui_Dialog, QDialog):
    def __init__(self):
        super(Customize_Dialog, self).__init__()
        self.setupUi(self)
        self.buttonBox.accepted.connect(self.accept)

    def get_customize_format(self):
        return self.lineEdit.text()


if __name__ == '__main__':
    app = QApplication([])
    mainw = MainWindow()
    mainw.show()
    app.exec_()
