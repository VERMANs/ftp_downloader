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
from PyQt5.QtWidgets import QHeaderView, QComboBox, QMessageBox
import os


class FTPClient:
    def __init__(self, host, user='IUSR', passwd='123'):
        self.ftp = FTP()
        self.ftp.connect(host, port=21)
        self.ftp.login()
        self.ftp.encoding = 'gbk'

    def sendCmd(self, cmd):
        return self.ftp.sendcmd(cmd)

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

    def download(self, name, path):
        if os.path.exists(path):
            lsize = os.path.getsize(path)
            fsize = self.size(name)
            if lsize >= fsize:
                return
            blocksize = 1024 * 1024
            cmpsize = lsize
            try:
                # self.ftp.sendcmd('TYPE I')
                lwrite = open(path, 'ab').write
                print(name)
                conn = self.ftp.retrbinary('RETR {}'.format(name), lwrite, lsize)
                # while True:
                #     data = conn.recv(blocksize)
                #     if not data:
                #         break
                #     lwrite.write(data)
                #     cmpsize += len(data)
                #     print('download process:%.2f%%' % (float(cmpsize) / fsize * 100))
                lwrite.close()
                # self.ftp.voidcmd('NOOP')
                # self.ftp.voidresp()
                return True
            except Exception as e:
                print(e)
                return False
        else:
            try:
                f = open(path, 'wb')
                conn = self.ftp.retrbinary('RETR {}'.format(name), f.write)
                # conn.close()
                f.close()
                return True
            except Exception as e:
                print(e)
                return False

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
