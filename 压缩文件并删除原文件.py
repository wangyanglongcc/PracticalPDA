import os
import glob
import zipfile

# 压缩文件并删除原文件
def to_zip(local_path, filename):
    ori_basename = os.path.basename(filename)
    fname, ext = os.path.splitext(ori_basename)
    zip_basename = ori_basename.replace(ext, '.zip')
    zipfilename = os.path.join(local_path, zip_basename)
    # 创建压缩文件
    azip = zipfile.ZipFile(zipfilename, 'w')
    # 写入原文件
    azip.writestr(ori_basename, open(filename, 'rb').read(), compress_type=zipfile.ZIP_DEFLATED)
    azip.close()
    # 删除原文件
    os.remove(filename)
    return zipfilename
