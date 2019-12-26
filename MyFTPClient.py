"""
    Create by VERMAN on 2019/12/13 
"""
__author__ = 'VERMAN'
"""
ftp相关命令操作
ftp.cwd(pathname)                 #设置FTP当前操作的路径
ftp.dir()                         #显示目录下所有目录信息
ftp.nlst()                        #获取目录下的文件
ftp.mkd(pathname)                 #新建远程目录
ftp.pwd()                         #返回当前所在位置
ftp.rmd(dirname)                  #删除远程目录
ftp.delete(filename)              #删除远程文件
ftp.rename(fromname, toname)#将fromname修改名称为toname。
ftp.storbinaly("STOR filename.txt",file_handel,bufsize)  #上传目标文件
ftp.retrbinary("RETR filename.txt",file_handel,bufsize)  #下载FTP文件
"""
# -*- encoding:utf-8 -*-
from ftplib import FTP
from PyQt5.QtWidgets import QHeaderView, QComboBox, QMessageBox, QProgressBar
import os
from threading import Thread


class MyThread(Thread):
    pass


class FTPClient:
    def __init__(self, host, user='IUSR', passwd='123'):
        self.ftp = FTP()
        self.ftp.connect(host, port=21)
        self.ftp.login()
        self.ftp.encoding = 'gbk'

    def sendCmd(self, cmd):
        return self.ftp.sendcmd(cmd)

    def MessageBox(self):
        msg = QMessageBox()
        msg.setWindowTitle("Warning")
        msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        msg.setText("下载完成!")
        btn = msg.exec_()
        if btn == QMessageBox.Ok:
            pass

    def size(self, filename):
        resp = self.ftp.sendcmd('SIZE ' + filename)
        s = -1
        if resp[:3] == '213':
            s = resp[3:].strip()
        return int(s)

    def getDir(self):
        return self.ftp.dir()

    def getList(self):
        return self.ftp.nlst()  # retrlines('LIST')

    def download(self, name, path, messageList=None, tableWidgets=None):
        downFlag = False
        fsize = self.size(name)
        progress = QProgressBar()
        progress.setGeometry(0,0,300, 25)
        progress.setMaximum(100)
        if os.path.exists(path):
            lsize = os.path.getsize(path)
            if lsize >= fsize:
                return
            blocksize = 1024 * 1024
            cmpsize = lsize
            try:
                print(name)
                conn = self.ftp.transfercmd('RETR ' + name, lsize)
                lwrite = open(path, 'ab')
                currentSize = 0.0
                while True:
                    data = conn.recv(blocksize)
                    if not data:
                        break
                    lwrite.write(data)
                    cmpsize += len(data)
                    # print '\b'*30,'download process:%.2f%%'%(float(cmpsize)/fsize*100),
                    if (float(cmpsize) / fsize * 100) > (currentSize + 1.0):
                        currentSize = float(cmpsize) / fsize * 100
                        info = 'download process:%.2f%%' % (float(cmpsize) / fsize * 100)
                        # progress.setValue(int(float(cmpsize) / fsize * 100))
                        messageList.addItem(info)
                        # tableWidgets.setCellWidget(2, 3, progress)
                lwrite.close()
                self.ftp.voidcmd('NOOP')
                self.ftp.voidresp()
                conn.close()
                downFlag = True
            except Exception as e:
                print(e)
                downFlag = False
        else:
            try:
                cmpsize = 0
                blocksize = 1024 * 1024
                conn = self.ftp.transfercmd('RETR ' + name, 0)
                lwrite = open(path, 'wb')
                currentSize = 0.0
                while True:
                    data = conn.recv(blocksize)
                    if not data:
                        break
                    lwrite.write(data)
                    cmpsize += len(data)
                    # print '\b'*30,'download process:%.2f%%'%(float(cmpsize)/fsize*100),
                    if (float(cmpsize) / fsize * 100) > (currentSize + 1.0):
                        currentSize = float(cmpsize) / fsize * 100
                        info = 'download process:%.2f%%' % (float(cmpsize) / fsize * 100)
                        # progress.setValue(int(float(cmpsize) / fsize * 100))
                        # progress.setValue(int(float(cmpsize) / fsize * 100))
                        messageList.addItem(info)
                        # tableWidgets.setCellWidget(2, 3, progress)
                lwrite.close()
                self.ftp.voidcmd('NOOP')
                self.ftp.voidresp()
                conn.close()
                downFlag = True
            except Exception as e:
                print(e)
                downFlag = False
        if downFlag:
            messageList.addItem("文件下载完成!")
            t1 = Thread(target=self.MessageBox, args=())
            t1.start()

    def upload(self, path):
        try:
            name = path.split('/')[-1]
        except:
            name = path
        print(name)
        print(path)
        try:
            self.ftp.storbinary('STOR {}'.format(name), open(path, 'rb'))
            return True
        except Exception as e:
            print(e)
            return False

    # 更改名字
    def rename(self, oldname, newname):
        back = None
        try:
            back = self.ftp.rename(oldname, newname)
        except Exception as e:
            print(e)
        return back

    def delete_file(self, filename):
        back = None
        try:
            back = self.ftp.delete(filename)
        except Exception as e:
            print(e)
        return back

    def sort_files(self):
        files = []
        fileList = self.getList()
        for folder in fileList:
            if folder.find(".") == -1:
                n = folder
                fileList.remove(folder)
                fileList.append(n)
        for folder in fileList:
            if folder.find(".") != -1:
                self.ftp.cwd("../")
                files.append((folder, self.size(folder)))
                # pass
            else:
                self.ftp.cwd("../")
                self.ftp.cwd(folder)
                tempList = self.getList()
                for temp in tempList:
                    files.append((folder + '/' + temp, self.size(temp)))
        self.ftp.cwd("../")
        return files


if __name__ == '__main__':
    client = FTPClient(host='172.117.15.3')
    # fileList = client.getList()
    print(client.sort_files())

    # client.upload(r"F:/ftp_files/login/test/2.jpg")
