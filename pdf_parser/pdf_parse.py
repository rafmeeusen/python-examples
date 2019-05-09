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
from pdfminer.layout import LTTextBoxHorizontal
from pdfminer.layout import LTTextLineHorizontal
from pdfminer.layout import LTPage

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
        pages = PDFPage.create_pages(self.doc)
        self.nrpages = 0
        self.pagelayouts = []
        for p in pages:
            self.interpreter.process_page(p)
            layout = self.device.get_result()
            self.pagelayouts.append(layout)
            self.nrpages += 1
        ''' pagenr starts at 1, index in islice at 0 '''
        #page_x = next(islice(pages,pagenr-1,pagenr))
    def nrofpages(self):
        return self.nrpages
    def getdocinfo(self):
        return self.doc.info[0]
    def getpagelayout(self, pagenr):
        return self.pagelayouts[pagenr-1]

    ''' search all objects in pagelayout for given string '''
    def __searchpage(self, pagelayout, searchstring):
        objects=[]
        for child_object in pagelayout:
            if isinstance(child_object, LTTextBoxHorizontal) or isinstance(child_object, LTTextLineHorizontal):
                object_text = child_object.get_text()
            if searchstring in object_text:
                objects.append(child_object)
        return objects

    ''' return all text objects where search string is found '''
    def search(self,searchstring,pagenr=None):
        children=[]
        pagenumbers=[]
        if pagenr:
            pagenumbers = [pagenr]
        else:
            pagenumbers = range(1,1+self.nrpages)
        for pagenr in pagenumbers:
            pageobjects=self.__searchpage(self.getpagelayout(pagenr), searchstring)
            children.append(pageobjects)
        return children


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Parse pdf files')
    parser.add_argument('filename', help='Filename of pdf file')
    parser.add_argument('-i', '--info', action="store_true", help='Print info about the pdf/page. Default action if no other command given.')
    parser.add_argument('-p', '--page', type=int, help='Specify page number to operate on.')
    parser.add_argument('-s', '--search', type=str, help='Search text string in text objects')
    args = parser.parse_args()

    openedpdffile = open(args.filename,'rb')
    mypdfparser = PdfParser(openedpdffile)

    info = mypdfparser.getdocinfo()
    nrpages = mypdfparser.nrofpages()

    if args.page:
        pages=[args.page]
    else:
        pages=range(1,1+nrpages)
        print(pages)

    if args.search:
        searchstring=args.search

    if args.info:
        for key in info.keys():
            print(key, ":", info[key])
        print('Nr of pages:', nrpages)

    for p in pages:
        print('page',p)
        print('search string',searchstring)
        pl=mypdfparser.getpagelayout(p)
        # searchresult = findChildWithString(pl, searchstring)
        mypdfparser.search(searchstring)
        searchresults=mypdfparser.search(searchstring,p)
        for r in searchresults:
            print('Found',searchstring,'in following object:')
            print(r)


    if False:
        ''' note: value 0 is ignored this way; pages start at 1 '''
        print('Detailed info for page',p)
        pl=mypdfparser.getpagelayout(p)
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


