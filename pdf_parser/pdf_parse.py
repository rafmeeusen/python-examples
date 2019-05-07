import argparse
from pdfminer.pdfparser import PDFParser
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfpage import PDFPage

class PdfParser(object):
    ''' basic CLI tool to extra info from a pdf,
        based on PDFMiner
        https://github.com/pdfminer/pdfminer.six '''
    def __init__(self, fp):
        parser = PDFParser(fp)
        self.doc = PDFDocument(parser)
    def nrofpages(self):
        pages = PDFPage.create_pages(self.doc)
        nrpages = 0
        for p in pages:
            nrpages += 1
        return nrpages
    def getdocinfo(self):
        return self.doc.info[0]




if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Parse pdf files')
    parser.add_argument('filename', help='Filename of pdf file')
    parser.add_argument('-i', '--info', action="store_true", help='Print info about the pdf')
    args = parser.parse_args()

    openedpdffile = open(args.filename,'rb')
    mypdfparser = PdfParser(openedpdffile)

    info = mypdfparser.getdocinfo()
    nrpages = mypdfparser.nrofpages()

    if args.info:
        for key in info.keys():
            print(key, ":", info[key])
        print('Nr of pages:', nrpages)

'''
[{'Author': b'Registered to: SD WORX ', 'CreationDate': b'8/28/2018 21:54:47', 'Creator': b'HP Exstream Version 9.0.107 64-bit', 'Title': b'Loonbrief'}]
'''
