# encoding=utf-8
__author__ = 'SR'

import zipfile
import os


class MyZipFileOrDir(object):
    def __init__(self):
        pass

    def zip_files_dirs(self, resDirOrFile, desPathAndName):
        '''压缩单个文件或整个目录,
			 resDirOrFile：要压缩的文件或目录的绝对路径
			 desPathAndName：压缩文件存放的路径及压缩文件名，
			 如果未指定压缩文件存放的目的路径，将会存放到当前文件所在目录。
		'''
        print u"压缩文件..."
        desPathAndName = desPathAndName
        if not os.path.exists(resDirOrFile):
            raise Exception(u"系统找不到%s！" % resDirOrFile)
            exit()

        if not os.path.isabs(desPathAndName):
            # 当前文件所在目录绝对路径
            currentDir = os.path.dirname(os.path.abspath(__file__))
            desPathAndName = os.path.join(currentDir, desPathAndName)
        else:
            zipFilePath = os.path.split(desPathAndName)[0]
            if not os.path.exists(zipFilePath):
                if os.path.exists(os.path.splitdrive(desPathAndName)[0]):
                    os.makedirs(zipFilePath)
                    print u"目标路劲%s不存在，已创建！" % zipFilePath
                else:
                    raise Exception(u"系统找不到驱动器%s，无法创建目标目录%s!" % (os.path.splitdrive(desPathAndName)[0], zipFilePath))
                    exit()

        fileList = []
        if os.path.isfile(resDirOrFile):
            fileList.append(resDirOrFile)
        else:
            for root, dirs, files in os.walk(resDirOrFile):
                if len(files) > 0:
                    for fileName in files:
                        fileList.append(os.path.join(root, fileName))
                else:
                    fileList.append(root)

        zf = zipfile.ZipFile(desPathAndName, 'w', zipfile.zlib.DEFLATED)
        for tar in fileList:
            if os.path.isfile(resDirOrFile):
                arcName = os.path.basename(resDirOrFile)
            else:
                arcName = tar[len(resDirOrFile):]
            print tar
            zf.write(tar, arcName)
        zf.close()
        print u"压缩文件成功！"

    def unzip_files(self, zipFilePath, unzipToDir):
        '''解压缩文件
	  	 zipFilePath：要解压的文件所在的绝对路径
	  	 unzipToDir：文件解压到的目录路径，如果只给了一个目录名，
	  	 将会在当前文件所在目录下创建这个目录，然后将压缩文件解压到这个目录下。
	  '''
        print u"解压文件..."
        unzipToDir = unzipToDir
        if not os.path.exists(zipFilePath):
            raise Exception(u"系统找不到压缩文件%s" % zipFilePath)

        if not os.path.isabs(unzipToDir):
            # 当前文件所在目录绝对路径
            currentDir = os.path.dirname(os.path.abspath(__file__))
            unzipToDir = os.path.join(currentDir, unzipToDir)
            if not os.path.exists(unzipToDir):
                os.makedirs(unzipToDir)
        else:
            if not os.path.exists(unzipToDir):
                # 如果目录路径不存在
                if os.path.exists(os.path.splitdrive(unzipToDir)[0]):
                    os.makedirs(unzipToDir)
                else:
                    raise Exception(u"系统找不到驱动器%s，无法创建目标目录%s" % (os.path.splitdrive(unzipToDir)[0], unzipToDir))
        zfObj = zipfile.ZipFile(zipFilePath, 'r')
        for name in zfObj.namelist():
            name = name.replace('\\', '/')
            if name.endswith('/'):
                os.makedirs(os.path.join(unzipToDir, name))
            else:
                ext_filename = os.path.join(unzipToDir, name)
                ext_dir = os.path.dirname(ext_filename)
                if not os.path.exists(ext_dir):
                    os.mkdir(ext_dir, 0777)
                print ext_filename
                outfile = open(ext_filename, 'wb')
                outfile.write(zfObj.read(name))
                outfile.close()
        print u"解压文件成功！"


if __name__ == '__main__':
    zf = MyZipFileOrDir()
    zf.zip_files_dirs(r'/Users/zhangbingwei/Downloads/ZZZ.txt', r'/Users/zhangbingwei/Downloads/222.zip')
    zf.unzip_files(r'/Users/zhangbingwei/Downloads/111.zip', r'/Users/zhangbingwei/Sikulix')
