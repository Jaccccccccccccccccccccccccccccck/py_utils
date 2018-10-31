import urllib.request
from io import BytesIO

from pdfminer.converter import PDFPageAggregator
from pdfminer.layout import *
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfinterp import PDFPageInterpreter
from pdfminer.pdfinterp import PDFResourceManager
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfpage import PDFTextExtractionNotAllowed
from pdfminer.pdfparser import PDFParser


def Pdf2Txt(DataIO, Save_path):  # 来创建一个pdf文档分析器
    parser = PDFParser(DataIO)  # 创建一个PDF文档对象存储文档结构
    document = PDFDocument(parser)
    if not document.is_extractable:
        raise PDFTextExtractionNotAllowed
    else:
        # 创建一个PDF资源管理器对象来存储共赏资源
        rsrcmgr = PDFResourceManager()  # 设定参数进行分析
        laparams = LAParams()  # 创建一个PDF设备对象
        # device=PDFDevice(rsrcmgr)
        device = PDFPageAggregator(rsrcmgr, laparams=laparams)  # 创建一个PDF解释器对象
        interpreter = PDFPageInterpreter(rsrcmgr, device)
        # 处理每一页
        for page in PDFPage.create_pages(document):
            interpreter.process_page(page)  # 接受该页面的LTPage对象
            layout = device.get_result()
            for x in layout:
                try:
                    if (isinstance(x, LTTextBoxHorizontal)):
                        with open('%s' % (Save_path), 'a') as f:
                            f.write(x.get_text().encode('utf-8') + '\n')
                except:
                    print("Failed!")


# convert online pdf

url = "http://www.neeq.com.cn/disclosure/2018/2018-08-23/1535036305_416510.pdf"
html = BytesIO(urllib.request.urlopen(urllib.request.Request(url)).read())
#DataIO = BytesIO(html.read())
Pdf2Txt(html, r'C:\workspace\python\converter\resource\b2.txt')

# convert local pdf
# with open(r'C:\Users\许相虎\Desktop\CTK2018q0.pdf', 'rb') as html:
#     DataIO = BytesIO(html.read())
#     Pdf2Txt(DataIO, r'C:\workspace\python\converter\resource\b3.txt')
