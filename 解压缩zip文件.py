# -*- coding: utf-8 -*-
import zipfile
import glob
import os
# 1- 解压
def un_zip(filepath):
    filepath = filepath.strip('\\')
    BadZipFiles = []
    for file in glob.glob(os.path.join(filepath,'*.zip')):
        try :
            z = zipfile.ZipFile(file, 'r')
            z.extractall(path=filepath)
            z.close()
            os.remove(file)
        except:
            BadZipFiles.append(file)
    print(BadZipFiles)
    return BadZipFiles
    
if __name__ == '__main__':
    un_zip('D:/zips')
