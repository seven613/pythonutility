#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@文件        :pdfConvert1.py
@说明        :单个文件、批量转换pdf
@时间        :2021/01/26 09:04:15
@作者        :张强
@版本        :1.0

安装包    pip install -i https://pypi.tuna.tsinghua.edu.cn/simple pywin32
'''

# -*- coding:utf-8 -*-
import os
from win32com.client import Dispatch,DispatchEx
from win32com.client import constants
from win32com.client import gencache
import re

def getfilenames(filepath='',filelist_out=[],file_ext='all'):
    for fpath, dirs, fs in os.walk(filepath):
        for f in fs:
            fi_d = os.path.join(fpath, f)
            if file_ext == '.doc':
                if os.path.splitext(fi_d)[1] in ['.doc','.docx']:
                    filelist_out.append(re.sub(r'\\','/',fi_d))
            else:
                if  file_ext == 'all':
                    filelist_out.append(fi_d)
                elif os.path.splitext(fi_d)[1] == file_ext:
                    filelist_out.append(fi_d)
                else:
                    pass
        filelist_out.sort()
    return filelist_out

# Word to PDF
def wordtopdf(filelist,targetpath):
    valueList = []
    try:
        gencache.EnsureModule('{00020905-0000-0000-C000-000000000046}', 0, 8, 4)
        # 开始转换
        w = Dispatch("Word.Application")
        for fullfilename in filelist:
            (filepath,filename) = os.path.split(fullfilename)  # 分割文件路径和文件名
            softfilename = os.path.splitext(filename)  # 分割文件名和扩展名
            os.chdir(filepath)
            doc = os.path.abspath(filename)
            os.chdir(targetpath)
            pdfname = softfilename[0] + ".pdf"
            output = os.path.abspath(pdfname)
            pdf_name = output

            try:
                doc = w.Documents.Open(doc, ReadOnly=1)
                doc.ExportAsFixedFormat(output, constants.wdExportFormatPDF,
                                Item=constants.wdExportDocumentWithMarkup,
                                CreateBookmarks=constants.wdExportCreateHeadingBookmarks)
            except Exception as e:
                print(e)
            if os.path.isfile(pdf_name):
                valueList.append(pdf_name)
            else:
                print('转换失败！')
                return False
        w.Quit(constants.wdDoNotSaveChanges)
        return valueList
    except TypeError as e:
        print('出错了！')
        print(e)
        return False
if __name__ == '__main__':
    sourcepath = r"E:/xxx/xxx"  # 指定源路径（Word文档所在路径）
    targetpath = r"E:/xxx/xxx/pdf/"  # 指定目标路径（PDF保存路径）
    filelist = getfilenames(sourcepath,[],'.doc')  # 获取Word文档路径
    valueList = wordtopdf(filelist,targetpath)  # 实现将Word文档批量转换为PDF
    if valueList:
        print("转换成功")
    else:
        print("没有要转换的Word文档或者转换失败！请检查！")