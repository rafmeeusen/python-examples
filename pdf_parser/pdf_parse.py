import argparse
from pdfminer.pdfparser import PDFParser
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfpage import PDFPage
from itertools import islice

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
    def getpage(self, pagenr):
        pages = PDFPage.create_pages(self.doc)
        ''' pagenr starts at 1, index in islice at 0 '''
        return next(islice(pages,pagenr-1,pagenr))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Parse pdf files')
    parser.add_argument('filename', help='Filename of pdf file')
    parser.add_argument('-i', '--info', action="store_true", help='Print info about the pdf')
    parser.add_argument('-p', '--page', type=int, help='Print detailed info on specific page in the pdf')
    args = parser.parse_args()

    openedpdffile = open(args.filename,'rb')
    mypdfparser = PdfParser(openedpdffile)

    info = mypdfparser.getdocinfo()
    nrpages = mypdfparser.nrofpages()

    if args.info:
        for key in info.keys():
            print(key, ":", info[key])
        print('Nr of pages:', nrpages)
    if args.page:
        ''' note: value 0 is ignored this way; pages start at 1 '''
        print('Detailed info for page ',args.page)
        print(mypdfparser.getpage(args.page))


