# -*- coding: UTF-8 -*-
with open('log.txt','w',encoding='utf-8') as f:
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
# 在爬虫的时候有时候需要把文件已json格式写出，且编码为utf-8时，有以下处理方式
import json
with open('file.json','a',encoding='utf-8') as f:
    # content为要写出的内容，是一个字典类型的文本
    f.write(json.dumps(content,ensure_ascii = False) + '\n')# 需要指定ensure_ascii为False才能以正确的编码方式写出

   
