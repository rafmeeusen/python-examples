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

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Parse pdf files')
    parser.add_argument('filename', help='Filename of pdf file')
    parser.add_argument('-p', '--pages', action="store_true", help='Print number of pages')
    args = parser.parse_args()

    openedpdffile = open(args.filename,'rb')
    mypdfparser = PdfParser(openedpdffile)

    if args.pages:
        print('Finding out nr of pages in pdf')
        print('Nr of pages:', mypdfparser.nrofpages())
