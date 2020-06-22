# 导入数据库驱动
import sqlite3
import xlrd

idList = []
nameList = []
urlList = []
fatherList = []


def readData():
    # 打开excel文件，创建一个workbook对象,book对象也就是fruits.xlsx文件,表含有sheet名
    rbook = xlrd.open_workbook(file)
    # sheets方法返回对象列表,[<xlrd.sheet.Sheet object at 0x103f147f0>]
    rbook.sheets()
    # xls默认有3个工作簿,Sheet1,Sheet2,Sheet3
    rsheet = rbook.sheet_by_index(0)  # 取第一个工作簿
    # 循环工作簿的所有行
    for row in rsheet.get_rows():
        id_column = row[0]  # 品名所在的列
        id_value = id_column.value  # 项目名
        if id_value != '编号':  # 排除第一行
            idList.append(id_value)
            # 读取id
            name_column = row[1]
            name_value = name_column.value
            nameList.append(name_value)
            # 读取名称
            url_column = row[2]
            url_value = url_column.value
            urlList.append(url_value)
            # 读取链接
            father_column = row[3]
            father_value = father_column.value
            fatherList.append(father_value)
            # 读取上级


def creteDB():
    # 连接到数据库
    # 数据库文件是“test.db”
    # 如果数据库不存在的话，将会自动创建一个 数据库
    conn = sqlite3.connect("C:/Users/赵宗天/Desktop/认识Python/test.db", uri=True)
    # conn = sqlite3.connect("AreaDB.db")
    # 创建一个游标 curson
    cursor = conn.cursor()
    # 创建数据表
    sql_create = "CREATE TABLE china(id INTEGER PRIMARY KEY,name NVARCHAR(60) NOT NULL," \
                 "url NVARCHAR(60) NOT NULL," \
                 "father INTEGER" \
                 ")"

    cursor.execute(sql_create)
    # 插入新记录
    for i in range(len(idList)):
        cursor.execute("insert into china values (?,?,?,?)", (int(idList[i]), str(nameList[i]), str(urlList[i]),
                                                              int(fatherList[i])))

    conn.commit()

    '''关闭数据库'''
    # 关闭游标：
    conn.cursor().close()
    # 关闭连接
    conn.close()


if __name__ == '__main__':
    file = 'C:/Users/赵宗天/Desktop/认识Python/爬取文档/中国地区综合.xlsx'
    readData()
    creteDB()
