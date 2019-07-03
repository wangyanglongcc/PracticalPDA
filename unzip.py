# -*- coding: utf-8 -*-
import zipfile
import glob
import os


# 1- 解压
def unzip_file(filename, is_remove=True):
    local_path = os.path.dirname(filename)
    if os.path.basename(filename).endswith('.zip'):
        try:
            z = zipfile.ZipFile(filename, 'r')
            z.extractall(path=local_path)
            z.close()
            if is_remove:
                os.remove(filename)
        except BaseException:  # bad zip
            return filename


def unzip(localpath_or_localfile, is_remove=True):
    bad_files = []
    if os.path.isdir(localpath_or_localfile):
        for filename in glob.glob(
            os.path.join(
                localpath_or_localfile,
                '*.zip')):
            bad_file = unzip_file(filename, is_remove)
            bad_files.append(bad_file)
    elif os.path.isfile(localpath_or_localfile):
        bad_file = unzip_file(localpath_or_localfile, is_remove)
        bad_files.append(bad_file)
    else:
        print('输入错误,请输入文件完整路径或路径 或检查文件是否存在')
    return bad_files


if __name__ == '__main__':
    localpath_or_localfile = r'D:\PycharmProjects\tongyong2018m9\model_output\ttt\19_20180916_pcauto_article.zip'
    unzip(localpath_or_localfile)
