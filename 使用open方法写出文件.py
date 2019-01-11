# -*- coding: UTF-8 -*-
with open('log.txt','r',encoding='utf-8') as f:
    f.write('hello world')
''' 
# 常用参数说明
> open(file,mode,encoding)
1. file:写出文件的路径
2. mode:写出模式，常用模式有r(写出),a(以追加形式写出)
mode说明
'r'       open for reading (default)
'w'       open for writing, truncating the file first
'x'       create a new file and open it for writing
'a'       open for writing, appending to the end of the file if it exists
'b'       binary mode
't'       text mode (default)
'+'       open a disk file for updating (reading and writing)
'U'       universal newline mode (deprecated)
3. encoding:编码方式，常用utf-8,utf-16,gbk
'''


   
