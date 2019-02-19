# 1. 根据本地`requirement.txt`中的包名及版本导出
```
pip install -r requirement.txt
```
如其中`requirement.txt`中内容如下：
```
pandas==0.23.4
numpy <= 1.15.0
tables
scipy
lxml
openpyxl
xlrd
matplotlib
```

# 2. 将该环境中安装的包名及版本导出
```
pip freeze > reuqirement.txt
```
上述脚本将会将该环境下安装的包及其版本号导出
