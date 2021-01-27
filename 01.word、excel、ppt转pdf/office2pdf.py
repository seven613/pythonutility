#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@文件        :PDFConverter.py
@说明        :批量转pdf，但是很慢，因为每次都要单独创建一个word实例
@时间        :2021/01/25 14:36:58
@作者        :张强
@版本        :1.0
'''
'''
安装包    pip install -i https://pypi.tuna.tsinghua.edu.cn/simple pywin32
'''

# 2、office文件 (word, ppt, excel等) 转为pdf
# -*- coding:utf-8 -*-
class PDFConverter:
    def __init__(self, pathname, export='.'):
        self._handle_postfix = ['doc', 'docx', 'ppt', 'pptx', 'xls', 'xlsx'] # 支持转换的文件类型
        self._filename_list = list()  #列出文件
        self._export_folder = os.path.join(os.path.abspath('.'), 'file_server/pdfconver')
        if not os.path.exists(self._export_folder):
            os.mkdir(self._export_folder)
        self._enumerate_filename(pathname)

    def _enumerate_filename(self, pathname):
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
            for relpath, _, files in os.walk(full_pathname):
                for name in files:
                    filename = os.path.join(full_pathname, relpath, name)
                    if self._is_legal_postfix(filename):
                        self._filename_list.append(os.path.join(filename))
        else:
            raise TypeError('文件/文件夹 {} 不存在或不合法！'.format(pathname))

    def _is_legal_postfix(self, filename):
        return filename.split('.')[-1].lower() in self._handle_postfix and not os.path.basename(filename).startswith(
            '~')

    def run_conver(self):
        print('需要转换的文件数是：', len(self._filename_list))
        for filename in self._filename_list:
            postfix = filename.split('.')[-1].lower()
            funcCall = getattr(self, postfix)
            print('原文件：', filename)
            funcCall(filename)
        print('转换完成！')
    def doc(self, filename):
        name = os.path.basename(filename).split('.')[0] + '.pdf'
        exportfile = os.path.join(self._export_folder, name)
        print('保存 PDF 文件：', exportfile)
        gencache.EnsureModule('{00020905-0000-0000-C000-000000000046}', 0, 8, 4)
        pythoncom.CoInitialize()
        w = Dispatch("Word.Application")
        pythoncom.CoInitialize()  # 加上防止 CoInitialize 未加载
        doc = w.Documents.Open(filename)
        doc.ExportAsFixedFormat(exportfile, constants.wdExportFormatPDF,
                                Item=constants.wdExportDocumentWithMarkup,
                                CreateBookmarks=constants.wdExportCreateHeadingBookmarks)
        w.Quit(constants.wdDoNotSaveChanges)
    def docx(self, filename):
        self.doc(filename)
    def ppt(self, filename):
        name = os.path.basename(filename).split('.')[0] + '.pdf'
        exportfile = os.path.join(self._export_folder, name)
        gencache.EnsureModule('{00020905-0000-0000-C000-000000000046}', 0, 8, 4)
        pythoncom.CoInitialize()
        p = Dispatch("PowerPoint.Application")
        pythoncom.CoInitialize()
        ppt = p.Presentations.Open(filename, False, False, False)
        ppt.ExportAsFixedFormat(exportfile, 2, PrintRange=None)
        print('保存 PDF 文件：', exportfile)
        p.Quit()

    def pptx(self, filename):
        self.ppt(filename)
    def xls(self, filename):
        name = os.path.basename(filename).split('.')[0] + '.pdf'
        exportfile = os.path.join(self._export_folder, name)
        pythoncom.CoInitialize()
        xlApp = DispatchEx("Excel.Application")
        pythoncom.CoInitialize()
        xlApp.Visible = False
        xlApp.DisplayAlerts = 0
        books = xlApp.Workbooks.Open(filename, False)
        books.ExportAsFixedFormat(0, exportfile)
        books.Close(False)
        print('保存 PDF 文件：', exportfile)
        xlApp.Quit()

    def xlsx(self, filename):
        self.xls(filename) 

if __name__ == "__main__":
    # 支持文件夹批量导入
    #folder = 'tmp'
    #pathname = os.path.join(os.path.abspath('.'), folder)
    # 也支持单个文件的转换
    pathname = "G:/python_study/test.doc"
    pdfConverter = PDFConverter(pathname)
    pdfConverter.run_conver()