import sqlite3
import tkinter as tk
from tkinter import ttk

import xlrd

idList = []  # yingwen
nameList = []  # zhongwen
urlList = []  # suoxie
fatherList = []  # guoqi

lst1 = []
lst2 = []
lst3 = []


def readData():
    try:
        conn = sqlite3.connect("C:/Users/赵宗天/Desktop/认识Python/test.db", uri=True)
        # conn = sqlite3.connect("AreaDB.db")
        # 创建一个游标 curson
    except:
        print("连接失败")

    cursor = conn.cursor()
    cursor.execute("SELECT * from china where father = 0")
    for data1 in cursor:
        lst1.append([data1[0], data1[1], data1[2], data1[3]])
    cursor.execute("SELECT * FROM china WHERE father BETWEEN 1 AND 100")
    for data2 in cursor:
        lst2.append([data2[0], data2[1], data2[2], data2[3]])
    cursor.execute("SELECT * from china where father > 100")
    for data3 in cursor:
        lst3.append([data3[0], data3[1], data3[2], data3[3]])

    # 关闭游标：
    conn.cursor().close()
    # 关闭连接
    conn.close()
    print(lst1)


def ttkData():
    window = tk.Tk()
    # 设置窗口大小
    winWidth = 600
    winHeight = 400
    # 获取屏幕分辨率
    screenWidth = window.winfo_screenwidth()
    screenHeight = window.winfo_screenheight()

    x = int((screenWidth - winWidth) / 2)
    y = int((screenHeight - winHeight) / 2)

    # 设置主窗口标题
    window.title("中国地区")
    # 设置窗口初始位置在屏幕居中
    window.geometry("%sx%s+%s+%s" % (winWidth, winHeight, x, y))
    # 设置窗口图标
    # window.iconbitmap("./image/icon.ico")
    # 设置窗口宽高固定
    window.resizable(0, 0)
    # 定义列的名称
    tree = ttk.Treeview(window, show="tree")
    china = tree.insert("", 0, "中国", text="中国China", values=(path))  # ""表示父节点是根
    # print(len(lst1))

    provinceList = []
    for i in range(len(lst1)):  # 省级循环
        province = tree.insert(china, i, lst1[i][2],
                               text=str(lst1[i][1])+' 编号:' + str(lst1[i][0]) + '链接:' + path + str(lst1[i][2]),
                               values=('编号:' + str(lst1[i][0]) + '链接:' + path + str(lst1[i][2])))
        provinceList.append(province)
        # print(lst2)
        # 将省份索引存进列表

        cityList = []
        for j in range(len(lst2)):  # 市级循环
            '''
            if lst2[j][1] == '市辖区':
                lst2[j][1] = lst1[i][1] + lst2[j][1]
                print(lst2[j][1])
                break  # 跳出循环
            if lst2[j][1] == '省直辖县级行政区划':
                lst2[j][1] = lst1[i][1] + lst2[j][1]
                print(lst2[j][1])
                break  # 跳出循环
            '''
            if lst2[j][3] == lst1[i][0]:
                city = tree.insert(provinceList[i], j, lst2[j][2],
                                   text=str(lst2[j][1])+' 编号:' + str(lst2[j][0]) + '链接:' + path + str(lst2[j][2]),
                                   values=('编号:' + str(lst2[j][0]) + '链接:' + path + str(lst2[j][2])))
                cityList.append(city)
                # print(lst1[j][1])
                # print(provinceList[i])
                for p in range(len(lst3)):  # 区级循环
                    if lst3[p][3] == lst2[j][0]:
                        region = tree.insert(city, p, lst3[p][2],
                                             text=str(lst3[p][1])+' 编号:' + str(lst3[p][0]) + '链接:' + path + str(lst3[p][2]),
                                             value=('编号:' + str(lst3[p][0]) + '链接:' + path + str(lst3[p][2])))

        # ""表示父节点是根
        # city = tree.insert(china, i, nameList[i], text=nameList[i], values=(idList[i]))
        # text表示显示出的文本，values是隐藏的值

    # 鼠标选中一行回调
    def selectTree(event):
        for item in tree.selection():
            item_text = tree.item(item, "values")
            print(item_text)

    # 选中行
    tree.bind('<<TreeviewSelect>>', selectTree)
    tree.pack(expand=True, fill=tk.BOTH)
    window.mainloop()


if __name__ == '__main__':
    path = 'http://www.stats.gov.cn/tjsj/tjbz/tjyqhdmhcxhfdm/2019/'
    readData()
    ttkData()
