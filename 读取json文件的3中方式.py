方式1：
```python
#  读取json文件
def read_json(filename):
    import json
    with open(filename, 'r+', encoding='utf-8') as f:
        lines = f.readlines()
    js_lines = []
    for line in lines:
        try:
            js_lines.append(json.loads(line))
        except:
            try:
                temp_line = line[:-2]
                js_lines.append(json.loads(temp_line))
            except:
                print('*' * 20, '\n', line[:-2])
    df = pd.DataFrame(js_lines, index=list(range(len(lines))))
    return df
```
方式2：
```python
def load_json(filepath,encoding='utf-8'):
    import json
    f = open(filepath,'r+',encoding=encoding)
    df = json.load(f)
    f.close()
    return pd.DataFrame(df)
```
方式3：
```python
def load_json(inputfile,encoding='utf-8'):
    import pandas as pd
    f = open(filepath,'r+',encoding=encoding)
    df = pd.read_json(f,lines=True,encoding=encoding)
    f.close()
    return df
```
