import argparse


class PdfParser(object):
    ''' basic CLI tool to extra info from a pdf,
        based on PDFMiner
        https://github.com/pdfminer/pdfminer.six '''
    def __init__(self, f):
        print('todo init pdfminer')

    def nrofpages(self):
        return 2

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
