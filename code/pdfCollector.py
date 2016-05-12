import os
import sys

sourceFilePath = '/root/projects/crawler/pdf/'
destFilePath = '/root/pdf/'

def createDirs(destFilePath):
    mustHaveDirs = os.path.split(destFilePath.rstrip('/'))
    pre = ''
    for part in mustHaveDirs:
        pre += part
        if not os.path.exists(pre):
            os.makedirs(pre)

def collect(sourceFilePath, destFilePath):
    if not os.path.exists(destFilePath):
        createDirs(destFilePath)
    for directory in os.listdir(sourceFilePath):
        if os.path.isdir(sourceFilePath+directory):
            for filename in os.listdir(sourceFilePath+directory):
                path = sourceFilePath + directory + filename
                info = os.stat(path)
                if info.st_size/1000.0 > 30.0:
                    os.rename(path, destFilePath+filename)
        elif directory.endswith('.pdf'):
            info = os.stat(directory)
            if info.st_size/1000.0 > 10.0:
                os.rename(path, destFilePath+filename)

if __name__=='__main__':
    collect(sourceFilePath, destFilePath)
