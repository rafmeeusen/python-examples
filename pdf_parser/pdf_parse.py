import argparse
from pdfminer.pdfparser import PDFParser
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfpage import PDFPage
from itertools import islice
from pdfminer.pdfinterp import PDFResourceManager
from pdfminer.layout import LAParams
from pdfminer.converter import PDFPageAggregator
from pdfminer.pdfinterp import PDFPageInterpreter
from pdfminer.layout import LTLine
from pdfminer.layout import LTRect
from pdfminer.layout import LTFigure


class PdfParser(object):
    ''' basic CLI tool to extra info from a pdf,
        based on PDFMiner
        https://github.com/pdfminer/pdfminer.six '''
    def __init__(self, fp):
        parser = PDFParser(fp)
        self.doc = PDFDocument(parser)
        laparams = LAParams()
        rsrcmgr = PDFResourceManager()
        self.device = PDFPageAggregator(rsrcmgr, laparams=laparams)
        self.interpreter = PDFPageInterpreter(rsrcmgr, self.device)
    def nrofpages(self):
        pages = PDFPage.create_pages(self.doc)
        nrpages = 0
        for p in pages:
            nrpages += 1
        return nrpages
    def getdocinfo(self):
        return self.doc.info[0]
    def getpagelayout(self, pagenr):
        pages = PDFPage.create_pages(self.doc)
        ''' pagenr starts at 1, index in islice at 0 '''
        page_x = next(islice(pages,pagenr-1,pagenr))
        self.interpreter.process_page(page_x)
        layout = self.device.get_result()
        return layout


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

    pl=None
    if args.page:
        ''' note: value 0 is ignored this way; pages start at 1 '''
        print('Detailed info for page',args.page)
        pl=mypdfparser.getpagelayout(args.page)
        cntr_lines=0
        cntr_rect=0
        cntr_fig=0
        for child_object in pl:
            ''' ignore lines '''
            if isinstance(child_object,LTLine):
                cntr_lines += 1
            elif isinstance(child_object,LTRect):
                cntr_rect += 1
            elif isinstance(child_object,LTFigure):
                cntr_fig += 1
            else:
                print(child_object)
        print("note: skipped following:")
        print("\tLTLine objects:", cntr_lines)
        print("\tLTRect objects:", cntr_rect)
        print("\tLTFigure objects:", cntr_fig)


