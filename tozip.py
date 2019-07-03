# -*- coding：utf-8 -*-
import os
import glob
import zipfile


def to_zipfile(filename, is_remove=True):
    local_path = os.path.dirname(filename)
    ori_basename = os.path.basename(filename)
    fname, ext = os.path.splitext(ori_basename)
    if ext != '.zip':
        zip_basename = ori_basename.replace(ext, '.zip')
        zipfilename = os.path.join(local_path, zip_basename)
        # 创建压缩文件
        azip = zipfile.ZipFile(zipfilename, 'w')  # zipfilename为完整路径
        # 写入原文件
        azip.writestr(ori_basename, open(filename, 'rb').read(), compress_type=zipfile.ZIP_DEFLATED)
        azip.close()
    else:
        zipfilename = ori_basename
    if is_remove:
        os.remove(filename)
    return zipfilename


# 压缩文件并删除原文件
def to_zip(localpath_or_localfile, is_remove=True):
    zipfilenames = []
    if os.path.isdir(localpath_or_localfile):
        for filename in glob.glob(os.path.join(localpath_or_localfile, '*.*')):
            zipfilename = to_zipfile(filename, is_remove)
            zipfilenames.append(zipfilename)
    elif os.path.isfile(localpath_or_localfile):
        zipfilename = to_zipfile(localpath_or_localfile, is_remove)
        zipfilenames.append(zipfilename)
    else:
        print('输入错误,请输入文件完整路径或路径 或文件是否存在')
    return zipfilenames


if __name__ == '__main__':
    localpath_or_localfile = r'D:\PycharmProjects\tongyong_history\model_output\test'
    try:
        zipfiles = to_zip(localpath_or_localfile, False)
        print(zipfiles)
    except:
        print(F'somethins is wrong with {localpath_or_localfile}')
