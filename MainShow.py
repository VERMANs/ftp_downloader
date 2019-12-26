# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QHeaderView, QComboBox, QInputDialog, QHBoxLayout, QCheckBox, QMessageBox, QFileDialog, \
    QDirModel, \
    QFileSystemModel, QTreeView, QLineEdit
from PyQt5.QtCore import Qt
import os
from MyFTPClient import FTPClient
import threading
from config import GlobalData


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1150, 722)
        self.FTP = None
        self.back = None
        self.file_length = 0
        self.baseSavePath = GlobalData.baseSavePath
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.columnView = QtWidgets.QColumnView(self.centralwidget)
        self.columnView.setGeometry(QtCore.QRect(0, 0, 1131, 51))
        self.columnView.setObjectName("columnView")
        self.LinkBtn = QtWidgets.QPushButton(self.centralwidget)
        self.LinkBtn.setGeometry(QtCore.QRect(1040, 10, 75, 31))
        self.LinkBtn.setStyleSheet("font: 75 12pt \"Agency FB\";")
        self.LinkBtn.setObjectName("LinkBtn")
        self.LinkBtn.clicked.connect(self.LinkServer)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(23, 11, 81, 31))
        self.label.setStyleSheet("font: 12pt \"黑体\";")
        self.label.setObjectName("label")
        self.HostText = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.HostText.setGeometry(QtCore.QRect(100, 10, 121, 31))
        self.HostText.setObjectName("HostText")
        self.UserNameText = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.UserNameText.setGeometry(QtCore.QRect(340, 10, 121, 31))
        self.UserNameText.setObjectName("UserNameText")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(250, 10, 81, 31))
        self.label_2.setStyleSheet("font: 12pt \"黑体\";")
        self.label_2.setObjectName("label_2")
        self.PswText = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.PswText.setGeometry(QtCore.QRect(570, 10, 121, 31))
        self.PswText.setObjectName("PswText")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(490, 10, 71, 31))
        self.label_3.setStyleSheet("font: 12pt \"黑体\";")
        self.label_3.setObjectName("label_3")
        self.PortText = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.PortText.setGeometry(QtCore.QRect(797, 9, 71, 31))
        self.PortText.setObjectName("PortText")
        self.HostText.setPlainText(GlobalData.host)
        self.PortText.setPlainText(GlobalData.port)
        self.UserNameText.setPlainText(GlobalData.username)
        self.PswText.setPlainText(GlobalData.password)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(720, 10, 71, 31))
        self.label_4.setStyleSheet("font: 12pt \"黑体\";")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(890, 10, 71, 31))
        self.label_5.setStyleSheet("font: 12pt \"黑体\";")
        self.label_5.setObjectName("label_5")
        self.StutasLabel = QtWidgets.QLabel(self.centralwidget)
        self.StutasLabel.setGeometry(QtCore.QRect(970, 10, 25, 25))
        self.StutasLabel.setText("")
        self.StutasLabel.setPixmap(QtGui.QPixmap("F:/Allimages/network/wait.png"))
        self.StutasLabel.setScaledContents(True)
        self.StutasLabel.setObjectName("StutasLabel")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(10, 60, 81, 31))
        self.label_8.setStyleSheet("font: 12pt \"黑体\";")
        self.label_8.setObjectName("label_8")
        self.ServerFilePath = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.ServerFilePath.setGeometry(QtCore.QRect(100, 60, 361, 31))
        self.ServerFilePath.setObjectName("ServerFilePath")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.tableWidget.setGeometry(QtCore.QRect(10, 100, 1131, 261))
        self.tableWidget.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.tableWidget.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setRowCount(25)
        # self.tableWidget.setItem()
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(15)
        item.setFont(font)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(15)
        item.setFont(font)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        self.tableWidget.cellDoubleClicked.connect(self.ChooseFunction)
        # item = QtWidgets.QTableWidgetItem()
        # self.tableWidget.setItem(0, 0, item)
        # item = QtWidgets.QTableWidgetItem()
        # self.tableWidget.setItem(1, 4, item)
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(0, 360, 1151, 21))
        self.line.setLineWidth(0)
        self.line.setMidLineWidth(10)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(550, 370, 20, 351))
        self.line_2.setLineWidth(4)
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(490, 60, 71, 31))
        self.label_6.setStyleSheet("font: 12pt \"黑体\";")
        self.label_6.setObjectName("label_6")

        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(580, 60, 71, 31))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(16)
        self.comboBox.setFont(font)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.DownloadBtn = QtWidgets.QPushButton(self.centralwidget)
        self.DownloadBtn.setGeometry(QtCore.QRect(680, 60, 71, 31))
        self.DownloadBtn.setObjectName("DownloadBtn")
        self.DownloadBtn.clicked.connect(self.downloadFile)
        self.RefreshBtn = QtWidgets.QPushButton(self.centralwidget)
        self.RefreshBtn.setGeometry(QtCore.QRect(780, 60, 71, 31))
        self.RefreshBtn.setObjectName("RefreshBtn")
        self.RefreshBtn.clicked.connect(self.refreshList)
        self.DeleteBtn = QtWidgets.QPushButton(self.centralwidget)
        self.DeleteBtn.setGeometry(QtCore.QRect(880, 60, 71, 31))
        self.DeleteBtn.setObjectName("DeleteBtn")
        self.DeleteBtn.clicked.connect(self.deleteFile)
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(20, 380, 521, 31))
        self.label_7.setStyleSheet("font: 12pt \"黑体\";")
        self.label_7.setObjectName("label_7")
        self.MessageList = QtWidgets.QListWidget(self.centralwidget)
        self.MessageList.setGeometry(QtCore.QRect(10, 410, 531, 261))
        self.MessageList.setObjectName("MessageList")
        self.UploadFileText = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.UploadFileText.setGeometry(QtCore.QRect(700, 380, 351, 31))
        self.UploadFileText.setObjectName("UploadFileText")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(590, 380, 111, 31))
        self.label_9.setStyleSheet("font: 12pt \"黑体\";")
        self.label_9.setObjectName("label_9")
        self.treeView = QtWidgets.QTreeView(self.centralwidget)
        self.model = QDirModel()
        self.treeView.setModel(self.model)
        self.treeView.setRootIndex(self.model.index(r''))
        # self.treeView.setModel(self.model)
        self.treeView.setGeometry(QtCore.QRect(595, 421, 531, 241))
        self.treeView.setObjectName("treeView")
        self.treeView.setSortingEnabled(True)
        self.treeView.setAlternatingRowColors(True)
        self.treeView.doubleClicked.connect(self.UploadFile)
        MainWindow.setCentralWidget(self.centralwidget)
        # self.label_9.setLayout(tree)
        self.MakeSureBtn = QtWidgets.QPushButton(self.centralwidget)
        self.MakeSureBtn.setGeometry(QtCore.QRect(1060, 380, 75, 31))
        self.MakeSureBtn.setStyleSheet("font: 75 12pt \"Agency FB\";")
        self.MakeSureBtn.setObjectName("MakeSureBtn")
        self.MakeSureBtn.clicked.connect(self.searchLoaclFile)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1150, 23))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        self.menu_2 = QtWidgets.QMenu(self.menubar)
        self.menu_2.setObjectName("menu_2")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actioninitiative = QtWidgets.QAction(MainWindow)
        self.actioninitiative.setObjectName("actioninitiative")
        self.action_passive = QtWidgets.QAction(MainWindow)
        self.action_passive.setObjectName("action_passive")
        self.actionDesigner_By_VERMAN = QtWidgets.QAction(MainWindow)
        self.actionDesigner_By_VERMAN.setObjectName("actionDesigner_By_VERMAN")
        self.action2019_12_24 = QtWidgets.QAction(MainWindow)
        self.action2019_12_24.setObjectName("action2019_12_24")
        self.menu_2.addAction(self.actionDesigner_By_VERMAN)
        self.menu_2.addAction(self.action2019_12_24)
        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.LinkBtn.setText(_translate("MainWindow", "快速连接"))
        self.label.setText(_translate("MainWindow", "主机（H）"))
        self.label_2.setText(_translate("MainWindow", "用户名（U）"))
        self.label_3.setText(_translate("MainWindow", "密码（W）"))
        self.label_4.setText(_translate("MainWindow", "端口（P）"))
        self.label_5.setText(_translate("MainWindow", "状态（S）"))
        self.label_8.setText(_translate("MainWindow", "本地站点:"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "选择"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "名称"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "状态"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "进度"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "大小(byte)"))
        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        self.tableWidget.setSortingEnabled(__sortingEnabled)
        self.label_6.setText(_translate("MainWindow", "模式（M）"))
        self.comboBox.setItemText(0, _translate("MainWindow", "默认"))
        self.comboBox.setItemText(1, _translate("MainWindow", "主动"))
        self.comboBox.setItemText(2, _translate("MainWindow", "被动"))
        self.label_7.setText(_translate("MainWindow", "消息记录(M):"))
        __sortingEnabled = self.MessageList.isSortingEnabled()
        self.MessageList.setSortingEnabled(False)

        # item = self.MessageList.item(0)
        # item.setText(_translate("MainWindow", "12312"))
        # item = self.MessageList.item(1)
        # item.setText(_translate("MainWindow", "131"))
        self.MessageList.setSortingEnabled(__sortingEnabled)
        self.label_9.setText(_translate("MainWindow", "选择上传路径:"))
        self.MakeSureBtn.setText(_translate("MainWindow", "上传"))
        self.DownloadBtn.setText(_translate("MainWindow", "下载"))
        self.RefreshBtn.setText(_translate("MainWindow", "刷新"))
        self.DeleteBtn.setText(_translate("MainWindow", "删除"))
        self.menu.setTitle(_translate("MainWindow", "选项"))
        self.menu_2.setTitle(_translate("MainWindow", "关于"))
        self.actioninitiative.setText(_translate("MainWindow", "initiative"))
        self.action_passive.setText(_translate("MainWindow", "\n"
                                                             "passive"))
        self.actionDesigner_By_VERMAN.setText(_translate("MainWindow", "Designer By VERMAN"))
        self.action2019_12_24.setText(_translate("MainWindow", "2019.12.24"))

    def searchLoaclFile(self):
        fileName = self.UploadFileText.toPlainText()
        info = "确定上传文件 {} 吗？".format(fileName)
        msg = QMessageBox()
        msg.setWindowTitle("Warning")
        msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        msg.setText(info)
        btn = msg.exec()
        if btn == QMessageBox.Ok:
            self.MessageList.addItem("正在上传文件...")
            t = threading.Thread(target=self.uploadFile_, args=(fileName,))
            t.start()
            self.MessageList.addItem("上传完成...")
        else:
            pass

    def downloadFile(self):
        info = "确定下载选择的文件吗？"
        msg = QMessageBox()
        msg.setWindowTitle("Warning")
        msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        msg.setText(info)
        btn = msg.exec()
        if btn == QMessageBox.Ok:
            try:
                self.FTP.ftp.cwd("../")
                for i in range(self.file_length):
                    if self.tableWidget.cellWidget(i, 0).isChecked():
                        filename = self.tableWidget.cellWidget(i, 1).text()
                        if filename.find("/") == -1:
                            self.MessageList.addItem("正在下载...")
                            print(os.path.join(self.baseSavePath, filename))
                            t = threading.Thread(target=self.FTP.download,
                                                 args=(filename, os.path.join(self.baseSavePath, filename),))
                            t.start()
                            self.MessageList.addItem("下载完成...")
                        else:
                            self.MessageList.addItem("正在下载...")
                            s = filename.split('/')
                            print("save path:", os.path.join(self.baseSavePath, filename))
                            self.FTP.ftp.cwd(s[0])
                            # self.FTP.download(s[-1], os.path.join(self.baseSavePath, s[-1]))
                            if not os.path.exists(os.path.join(self.baseSavePath, s[0])):
                                os.mkdir(os.path.join(self.baseSavePath, s[0]))
                            t = threading.Thread(target=self.FTP.download,
                                                 args=(s[1], os.path.join(self.baseSavePath, filename),))
                            t.start()
                            self.MessageList.addItem("下载完成...")

            except Exception as e:
                print(e)

    def refreshList(self):
        self.tableWidget.clearContents()
        self.getRemoteList()

    def getRemoteList(self):
        try:
            self.FTP.ftp.cwd("../")
            if self.FTP:
                files = self.FTP.sort_files()
                i = 0
                self.file_length = len(files)
                for f in files:
                    ck = QCheckBox()
                    # self.ck.stateChanged.connect(self.changeCk)
                    h = QHBoxLayout()
                    h.setAlignment(Qt.AlignCenter)
                    h.addWidget(ck)
                    textbox = QLineEdit()
                    textbox.setText(f[0])
                    try:
                        filename = f[0].split()[-1]
                    except:
                        filename = f[0]
                    self.tableWidget.setCellWidget(i, 0, ck)
                    self.tableWidget.setCellWidget(i, 1, textbox)
                    textbox1 = QLineEdit()
                    if os.path.exists(os.path.join(self.baseSavePath, filename)):
                        if os.path.getsize(os.path.join(self.baseSavePath, filename)) >= f[1]:
                            textbox1.setText("已下载")
                        else:
                            print(os.path.join(self.baseSavePath, filename))
                            textbox1.setText("下载中，可断点重传")
                    else:
                        textbox1.setText("未下载")
                    textbox2 = QLineEdit()
                    textbox2.setText("zero")
                    textbox3 = QLineEdit()
                    textbox3.setText(str(f[1]))
                    self.tableWidget.setCellWidget(i, 2, textbox1)
                    self.tableWidget.setCellWidget(i, 3, textbox2)
                    self.tableWidget.setCellWidget(i, 4, textbox3)
                    i += 1
                    item = QtWidgets.QTableWidgetItem()
                    # self.tableWidget.setHorizontalHeaderItem(i - 1, item)
                self.MessageList.addItem("已成功获取到List...")
            else:
                msg = QMessageBox()
                msg.setWindowTitle("Warning")
                msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
                msg.setText("请先连接...")
                self.MessageList.addItem("请先连接...")
                btn = msg.exec()
        except Exception as e:
            print(e)

    def showToast(self):
        while self.back is None:
            pass
        if self.back:
            msg = QMessageBox()
            msg.setWindowTitle("Warning")
            msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
            msg.setText("上传完成!")
            btn = msg.exec()
            if btn == QMessageBox.Ok:
                pass
        else:
            msg = QMessageBox()
            msg.setWindowTitle("Warning")
            msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
            msg.setText("上传失败!")
            btn = msg.exec()
            if btn == QMessageBox.Ok:
                pass

    def uploadFile_(self, fileName):
        back = self.FTP.upload(fileName)
        self.back = back
        if back:
            msg = QMessageBox()
            msg.setWindowTitle("Warning")
            msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
            msg.setText("上传完成!")
            self.MessageList.addItem("上传完成...")
            btn = msg.exec()
            if btn == QMessageBox.Ok:
                pass
        else:
            self.MessageList.addItem("上传失败...")
            msg = QMessageBox()
            msg.setWindowTitle("Warning")
            msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
            msg.setText("上传失败!")
            btn = msg.exec()
            if btn == QMessageBox.Ok:
                pass

    def LinkServer(self):
        host = self.HostText.toPlainText()
        name = self.UserNameText.toPlainText()
        psw = self.PswText.toPlainText()
        port = self.PortText.toPlainText()
        try:
            self.FTP = FTPClient(host=host)
            self.StutasLabel.setPixmap(QtGui.QPixmap("F:/Allimages/network/ok.png"))
            self.ServerFilePath.setPlainText("FTP:{}".format(host))
        except Exception as e:
            self.StutasLabel.setPixmap(QtGui.QPixmap("F:/Allimages/network/wrong.png"))
            print(e)
            self.FTP = None
        self.getRemoteList()

    def UploadFile(self, Qmodelidx):
        fileWholeName = self.model.filePath(Qmodelidx)
        fileName = self.model.fileName(Qmodelidx)
        # print(self.model.fileInfo(Qmodelidx))
        info = "确定上传文件 {} 吗？".format(fileName)
        detail = "详情路径为:{}".format(fileWholeName)
        msg = QMessageBox()
        msg.setWindowTitle("Warning")
        msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        msg.setText(info)
        msg.setDetailedText(detail)
        btn = msg.exec()
        if btn == QMessageBox.Ok:
            t = threading.Thread(target=self.FTP.upload, args=(fileWholeName,))
            t.start()
        else:
            pass

    def ChooseFunction(self):
        col = self.tableWidget.currentColumn()
        row = self.tableWidget.currentRow()
        dirName = "../"
        fileName = ""
        for i in range(self.file_length):
            if i == row:
                filename = self.tableWidget.cellWidget(i, 1).text()
                if filename.find("/") == -1:
                    fileName = filename
                else:
                    fs = filename.split("/")
                    dirName = fs[0]
                    fileName = fs[1]
                break
        try:
            value, ok = QInputDialog().getText(self.centralwidget, "文件名修改",
                                               "请将文件名：{}\n修改如下:(放弃修改点cancel)".format(fileName))
            self.FTP.ftp.cwd("../")
            if ok:
                self.FTP.ftp.cwd(dirName)
                self.FTP.rename(fileName, str(value))
                self.MessageList.addItem("文件 {} 修改成功!".format(fileName))
            else:
                self.MessageList.addItem("用户取消修改...")

        except Exception as e:
            print(e)
            self.MessageList.addItem("文件 {} 修改失败!".format(fileName))

    def deleteFile(self):
        row = self.tableWidget.currentRow()
        if row == -1:
            info = "请选择文件列表的指定行"
            msg = QMessageBox()
            msg.setWindowTitle("Warning")
            msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
            msg.setText(info)
            btn = msg.exec()
            return
        dirName = "../"
        fileName = ""
        for i in range(self.file_length):
            if i == row:
                filename = self.tableWidget.cellWidget(i, 1).text()
                if filename.find("/") == -1:
                    fileName = filename
                else:
                    fs = filename.split("/")
                    dirName = fs[0]
                    fileName = fs[1]
                break
        info = "确定删除文件{}?".format(fileName)
        msg = QMessageBox()
        msg.setWindowTitle("Warning")
        msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        msg.setText(info)
        btn = msg.exec()
        if btn == QMessageBox.Ok:
            self.FTP.ftp.cwd("../")
            try:
                self.FTP.ftp.cwd(dirName)
                self.FTP.delete_file(fileName)
                self.MessageList.addItem("文件 {} 删除成功!".format(fileName))

            except Exception as e:
                print(e)
        else:
            self.MessageList.addItem("用户取消文件删除...")


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
