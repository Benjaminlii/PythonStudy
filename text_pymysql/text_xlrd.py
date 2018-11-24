"""
    对excel操作的xlrd和xlwt库

    2018.11.24
    author:Benjamin
"""
import xlwt

# 创建工作簿,设置编码
oneExcel = xlwt.Workbook(encoding = 'utf-8')
# 添加工作表
oneSheet = oneExcel.add_sheet("table1")
oneSheet.write(0, 0, "121212")

oneExcel.save("50tables.xls")

