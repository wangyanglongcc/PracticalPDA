def read_json(inputfile,encoding='utf-8'):
    import pandas as pd
    import json
    # method 1
    def read_json1(inputfile):
        f = open(inputfile,'r+',encoding=encoding)
        df = pd.read_json(f,lines=True,encoding=encoding)
        f.close()
        return df
    # method 2
    def read_json2(inputfile):
        f = open(inputfile,'r+',encoding=encoding)
        df = json.load(f)
        f.close()
        df = pd.DataFrame(df)
        return df
    # method 3
    def read_json3(inputfile):
        with open(inputfile, 'r+', encoding=encoding) as f:
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
    # try-except
    try:
        df = read_json1(inputfile)
#         print(1)
    except:
        try:
            df = read_json2(inputfile)
#             print(2)
        except:
            df = read_json3(inputfile)
#             print(3)
    return df
if __name__ == '__main__':
    df = read_json(r'D:\yuqing\19_2019_3_31_pcauto_article.json')
    print(df.shape)
