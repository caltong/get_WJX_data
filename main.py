from bs4 import BeautifulSoup

import xlwt


#读取html文件
with open('1.html', 'r',encoding='UTF-8') as f:
    html = f.read()
soup = BeautifulSoup(html,'html') #使用bs4
divNumber = range(1,22) #题目编号
data = [] #存储分数
for i in divNumber: #循环遍历所有题目
    divID = 'divTotal' + str(i) #div ID
    #print(divID)

    getContent = soup.find('div',id = 'divStatData').find('div',id = divID) #获取数据表哥所在div
    rows = getContent.findChildren(['th','tr']) #循环遍历所有数据表格 获取具体数据值
    for row in rows:
        cells = row.findChildren('td')
        for cell in cells:
            value = cell.string      #去掉html标签括号
            if cells.index(cell) == 6:     #获取个人单项平均分
                if value != '平均分':
                    data.append(value)    #将所有数据存入data中


#操作Excel
workbook = xlwt.Workbook()
sheet = workbook.add_sheet('sheet1', cell_overwrite_ok=True)

i = 0
for col in range(21):
    for row in range(8):
        sheet.write(row,col,str(data[i]))
        i = i+1

workbook.save('test1.xls')
