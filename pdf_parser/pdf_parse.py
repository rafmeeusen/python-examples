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

    ''' instantiate for given page or default for all page layouts '''
    def __init__(self, fp, pagenr=None):
        parser = PDFParser(fp)
        self.doc = PDFDocument(parser)
        laparams = LAParams()
        rsrcmgr = PDFResourceManager()
        self.device = PDFPageAggregator(rsrcmgr, laparams=laparams)
        self.interpreter = PDFPageInterpreter(rsrcmgr, self.device)
        pages = PDFPage.create_pages(self.doc)
        self.nrpages = 0
        self.pagelayouts = []
        # count all pages, but only store requested pagelayout (or all if None)
        for p in pages:
            self.nrpages += 1
            # pagenr starts at 1, index in islice at 0
            if not pagenr or (pagenr and (pagenr==self.nrpages)):
                self.interpreter.process_page(p)
                layout = self.device.get_result()
                self.pagelayouts.append(layout)
    def nrofpages(self):
        return self.nrpages
    def getdocinfo(self):
        return self.doc.info[0]
#    def getpagelayout(self, pagenr):
#        return self.pagelayouts[pagenr-1]

    ''' search all objects in pagelayout for given string '''
    def __searchpagestr(self, pagelayout, searchstring):
        objects=[]
        for child_object in pagelayout:
            if isinstance(child_object, LTTextBoxHorizontal) or isinstance(child_object, LTTextLineHorizontal):
                object_text = child_object.get_text()
            if searchstring in object_text:
                objects.append(child_object)
        return objects
    def __searchpagey(self, pagelayout, yval, maxerr):
        miny = yval-maxerr
        maxy = yval+maxerr
        objects=[]
        for child_object in pagelayout:
            if isinstance(child_object, LTTextBoxHorizontal) or isinstance(child_object, LTTextLineHorizontal):
                object_y0 = child_object.y0
            if object_y0 > miny and object_y0 < maxy:
                objects.append(child_object)
        return objects

    ''' return all text objects where search string is found,
        note: this is a flat list, even when searching over multiple pages
    '''
    def searchstr(self,searchstring):
        searchresult=[]
        for pl in self.pagelayouts:
            pageobjects=self.__searchpagestr(pl, searchstring)
            searchresult.extend(pageobjects)
        return searchresult

    ''' search all text objects within y0 in maxerr range from given yval '''
    def searchy(self, yval, maxerr):
        searchresult=[]
        for pl in self.pagelayouts:
            pageobjects=self.__searchpagey(pl, yval, maxerr)
            searchresult.extend(pageobjects)
        return searchresult


def printsplittext(txtobject):
    txtstr=txtobject.get_text()
    txtlst=txtstr.split('\n')
    print(txtlst)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Parse pdf files')
    parser.add_argument('filename', help='Filename of pdf file')
    parser.add_argument('-i', '--info', action="store_true", help='Print info about the pdf/page. Default action if no other command given.')
    parser.add_argument('-p', '--page', type=int, help='Specify page number to operate on.')
    parser.add_argument('-s', '--search', type=str, help='Search text string in text objects')
    parser.add_argument('-sy', '--searchy0', type=int, help='Search for given y0 page location in text objects')
    args = parser.parse_args()

    openedpdffile = open(args.filename,'rb')
    # instance mypdfparser will have limited scope if page is selected:
    if args.page:
        mypdfparser = PdfParser(openedpdffile, args.page)
    else:
        mypdfparser = PdfParser(openedpdffile)

    # print info if requested
    if args.info:
        info = mypdfparser.getdocinfo()
        print('PDF info:')
        for key in info.keys():
            print(key, ":", info[key])
        nrpages = mypdfparser.nrofpages()
        print('Nr of pages:', nrpages)

    # search for text if requested
    if args.search:
        searchstring=args.search
        print('search string',searchstring)
        #mypdfparser.searchstr(searchstring)
        searchresults=mypdfparser.searchstr(searchstring)
        for o in searchresults:
            print('Found',searchstring,'in following object:')
            printsplittext(o)
            print('Object coordinates (x0,y0,x1,y1): ', round(o.x0), round(o.y0), round(o.x1), round(o.y1))

    if args.searchy0:
        searchresults=mypdfparser.searchy(args.searchy0, 5)
        for o in searchresults:
            print('Found similar y in: ')
            printsplittext(o)
            print('Object coordinates (x0,y0,x1,y1): ', round(o.x0), round(o.y0), round(o.x1), round(o.y1))


