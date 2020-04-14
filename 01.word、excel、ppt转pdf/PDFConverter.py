#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@文件        :demo.py
@说明        :word、excel、ppt转pdf功能
@时间        :2020/04/13 13:49:10
@作者        :张强
@版本        :1.0
'''



import os
from win32com.client import Dispatch, constants, gencache, DispatchEx


class PDFConverter:
    def __init__(self, pathname, export ='.'):
        self._handle_postfix =['doc', 'docx', 'ppt', 'pptx', 'xls', 'xlsx']
        self._filename_list = list()
        self._export_folder = os.path.join(os.path.abspath('.'), 'pdfconver')
        if not os.path.exists(self._export_folder):
            os.mkdir(self._export_folder)
        self._emumerate_filename(pathname)
    
    def _emumerate_filename(self, pathname):
        '''
        读取所有文件名
        '''
        full_pathname = os.path.abspath(pathname)
        if os.path.isfile(full_pathname):
            if self._is_legal_postfix(full_pathname):
                self._filename_list.append(full_pathname)
            else:
                raise TypeError('文件 {} 后缀名不合法！仅支持如下文件类型：{}。'.format(pathname, '、'.join(self._handle_postfix)))
        elif os.path.isdir(full_pathname):
            for relpath, _, files  in os.walk(full_pathname):
                for name in files:
                    filename = os.path.join(full_pathname, relpath, name)
                    if self._is_legal_postfix(filename):
                        self._filename_list.append(os.path.join(filename))
        else:
            raise TypeError('文件/文件夹 {} 不存在活不合法！'.format(pathname))
    
    def _is_legal_postfix(self, filename):
        return filename.split('.')[-1].lower() in self._handle_postfix and not os.path.basename(filename).startswith('~')

    def run_conver(self):
        '''
        进行批量处理，根据后缀名调用函数执行转换
        '''
        print('需要转换的文件数:', len(self._filename_list))
        for filename in self._filename_list:
            postfix = filename.split('.')[-1].lower()
            funcCall = getattr(self, postfix)
            print('源文件:', filename)
            funcCall(filename)
        print('转换完成！')

    def doc(self, filename):
        '''
        doc 和docx文件转换
        '''
        name = os.path.basename(filename).split('.')[0] + '.pdf'
        exportfile = os.path.join(self._export_folder, name)
        print('保存PDF文件:', exportfile)
        gencache.EnsureModule('{00020905-0000-0000-C000-000000000046}', 0, 8, 4)
        w = Dispatch("Word.Application")
        doc = w.Docouments.open(filename)
        doc.ExportAsFixeFormat(exportfile, constants.wdExportFormatPDF,
            Item=constants.wdExportDocumentWithMarkup,
            CreateBookmarks=constants.wdExportCreateHeadingBookmarks)
        w.Quit(constants.wdDoNotSaveChanges)
    
    def docx(self, filename):
        self.doc(filename)

    def xls(self, filename):
        '''
        xls 和xlsx文件转换
        '''
        name = os.path.basename(filename).split('.')[0]+'.pdf'
        exportfile = os.path.join(self._export_folder, name)
        xlApp = DispatchEx("Excel.Application")
        xlApp.Visible = False
        xlApp.DisplayAlerts = 0
        books = xlApp.Workbooks.Open(filename, False):
        books.ExportAsFixeFormat(0, exportfile)
        books.Close(False)
        print('保存PDF文件：', exportfile)
        xlApp.Quit()

    def xlsx(self, filename):
        self.xls(filename)

    def ppt(self, filename):
        '''
        ppt 和pptx文件转换
        '''        
        name = os.path.basename(filename).split('.')[0]+'.pdf'
        exportfile = os.path.join(self._export_folder,name)
        gencache.EnsureModule('{00020905-0000-0000-C000-000000000046}', 0, 8, 4)
        p = Dispatch("PowerPoint.Application")
        ppt = p.Presentations.Open(filename, False, False, False)
        ppt.ExportAsFixeFormat(exportfile, 2,  PrintRange=None)
        p.Quit()
    
    def pptx(self, filename):
        self.ppt(filename)

if __name__ == "__main__":
    # 支持文件夹批量导入
    folder ='tmp'
    pathname = os.path.join(os.path.abspath('.'), folder)

    #也支持单个文件转换
    # pathname =r'E:\Codes\Python\test.doc'

    pdfConverter = PDFConverter(pathname)
    pdfConverter.run_conver()