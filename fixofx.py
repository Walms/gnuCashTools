#!/usr/bin/python

import sys, getopt,re 

def main(argv):
    inputfile = ''
    outputfile = ''
    try:
        opts, args = getopt.getopt(argv,"hi:o:",["ifile=","ofile="])
    except getopt.GetoptError:
        print __file__  + ' -i <inputfile> -o <outputfile>'
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print __file__ + ' -i <inputfile> -o <outputfile>'
            sys.exit()
        elif opt in ("-i", "--ifile"):
            inputfile = arg
        elif opt in ("-o", "--ofile"):
            outputfile = arg

    strangeNameRe = re.compile('<NAME>(4835 \*{4} \*{4} 0133.*)$')
    memoRe = re.compile('<MEMO>(.*)')

    outfile = open(outputfile, 'w')
    file = open(inputfile, 'r+')
    for line in file:
        match = strangeNameRe.match(line)
        if match:
            print 'found bad name'
            nextline = file.next()
            nextMatch = memoRe.match(nextline)
            if nextMatch:
                print 'found memo after'
                name = match.group(1)
                memo = nextMatch.group(1)
                line = line.replace(name, memo)
                nextline = nextline.replace(memo,name)
                
            outfile.write(line)
            outfile.write(nextline)
        else:
            outfile.write(line)
        

if __name__ == "__main__":
   main(sys.argv[1:])