import logging

from PyPDF2 import PdfFileReader


def count_pdf_page(file_path):
    try:
        pdf = PdfFileReader(open(file_path, 'rb'))
        return pdf.getNumPages()
    except:
        logging.getLogger(__file__).error('Error extracting pdf, return None')
        return None


if '__main__' == __name__:
    print(count_pdf_page('C:/PDF/1205494799.PDF'))
    print(count_pdf_page('C:/Users/jack/Desktop/2018q2IQ.pdf'))
    print(count_pdf_page('C:/Users/jack/Desktop/2015q4ubs.pdf'))