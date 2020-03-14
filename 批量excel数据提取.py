import os
import pandas as pd
import xlrd
import shutil 
 
def file_name(file_dir): 
    for root, dirs, files in os.walk(file_dir):
        return files #当前路径下所有非目录子文件  
 
#例如D:/jupyter/test/data
path = input('请键入需要整理的文件夹地址：')  
sheet_name = input('请键入要复制的sheet表名字：')  
m= input('请键入要复制的单元格所在行数：') 
n= input('请键入要复制的单元格所在列数：') 
 
files = file_name(path)
 
 
result = pd.DataFrame(columns=['file', 'value'])
 
for i in range(0,len(files)):
    data = xlrd.open_workbook(path+'/'+files[i])
    print(path+'/'+files[i])
    table = data.sheet_by_name(sheet_name)
    cell = table.cell(int(m),int(n)).value
    result.loc[i] = [files[i], cell]
 
result.to_csv(path + '/result.csv')
————————————————
版权声明：本文为CSDN博主「花青色」的原创文章，遵循 CC 4.0 BY-SA 版权协议，转载请附上原文出处链接及本声明。
原文链接：https://blog.csdn.net/xuan314708889/article/details/80622409
