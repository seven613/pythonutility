# 读excel文件
def readExcel(readExcelNameOrPath='', readSheets=None, contentType='json'):
    import xlrd, os, json
    # 参数说明
    # readExcelNameOrPath  读取excel的文件名称（aa.xls）或文件的绝对路径（r"E:\test\aa.xls"），如果为文件名称，必须放到当前目录下
    # readSheets   要读取的sheet表名称，如果不设置默认读取第一个表，如果设置为all代表读取全部的sheet的内容，注意：只有['all']这种情况下才读取全部sheet
    # contentType   设置返回值的类型
    # 注意：如果路径中出现转义字符，如\t，\n等，路径前面加r，如 r"E:\test\aa.xls"
    # 返回值格式：{sheetName:[{"row": 0, "col": 0, "content": content}, ..., {"row": m, "col": n, "content": content}]}

    readExcelNameOrPath = str(readExcelNameOrPath)
    contentType = str(contentType).lower()
    readSheetsContent = {}  # key为sheet表名称，value为对应sheet的内容list
    readSheetsInfoList = []

    try:
        # 处理传参错误时的情况
        if not os.path.isfile(os.path.abspath(readExcelNameOrPath)):
            readSheetsContent['文件错误'] = '文件名称或路径设置错误[%s]' % (readExcelNameOrPath, )
            readSheetsContent['规则'] = '只设置文件名称，需要将文件放到当前目录下；如果设置路径，必须为文件的绝对路径，如%s' % (r"E:\test\aa.xls", )
            if contentType != 'dict':
                readSheetsContent = json.dumps(readSheetsContent, ensure_ascii=False)
            return readSheetsContent
        if not (os.path.abspath(readExcelNameOrPath).endswith('.xls') or os.path.abspath(readExcelNameOrPath).endswith('.xlsx')):
            readSheetsContent['文件错误'] = ' 文件格式错误，必须为excel文件，后缀名只能为.xls和.xlsx'
            if contentType != 'dict':
                readSheetsContent = json.dumps(readSheetsContent, ensure_ascii=False)
            return readSheetsContent
        # 打开文件
        excelInfo = xlrd.open_workbook(readExcelNameOrPath)

        # 需要读取的sheet表参数传参异常时默认读取第一个
        if not isinstance(readSheets, list) or not readSheets:
            temSheet = excelInfo.sheet_by_index(0)
            readSheetsInfoList.append(temSheet)
        else:
            # 如果设置为all，处理全部sheet表格
            if len(readSheets) == 1 and str(readSheets[0]).lower() == 'all':
                for sheetIndex in range(0, excelInfo.nsheets):
                    temSheet = excelInfo.sheet_by_index(sheetIndex)
                    readSheetsInfoList.append(temSheet)

            # 按设置的sheet表名称进行处理
            else:
                for sheetName in readSheets:
                    sheetName = str(sheetName)
                    try:
                        temSheet = excelInfo.sheet_by_name(sheetName)
                        readSheetsInfoList.append(temSheet)
                    except:
                        # sheet表名称找不到时返回提示信息，注意：区分大小写
                        readSheetsContent[sheetName] = ['该sheet表不存在']

        # 开始处理sheet表数据
        for sheetInfo in readSheetsInfoList:
            dataRows = sheetInfo.nrows
            dataCols= sheetInfo.ncols
            if dataRows > 0:
                temDict = []
                for row in range(0, dataRows):
                    for col in range(0, dataCols):
                        temD = {}
                        temD['row'] = row + 1
                        temD['col'] = col + 1
                        temD['content'] = sheetInfo.cell_value(row, col)
                        temDict.append(temD)
                readSheetsContent[sheetInfo.name] = temDict
            else:
                readSheetsContent[sheetInfo.name] = []

        # 处理返回结果的数据类型，字典或json
        if contentType != 'dict':
            readSheetsContent = json.dumps(readSheetsContent, ensure_ascii=False)
        return readSheetsContent
    except Exception as e:
        return e

#3.1 正常读取-全部sheet
# if __name__ == '__main__':
#     testRead = readExcel(readExcelNameOrPath=r'E:\test\mytest\aa.xls', readSheets=['all'], contentType='json')
#     print(testRead)

#3.2 正常读取-指定sheet
if __name__ == '__main__':
    testRead = readExcel(readExcelNameOrPath=r'C:\Users\seven\Desktop\保定疫情核实统计表2（救治组）(1).xlsx', readSheets=['工信部推送疫情密接数据192人','51人'], contentType='json')
    print(testRead)
#3.3 文件设置错误
# if __name__ == '__main__':
#     testRead = readExcel(readExcelNameOrPath=r'hello', readSheets=['all'], contentType='json')
#     print(testRead)
