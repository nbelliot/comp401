from rope import *

TEXT_FILE = 'chapter1.txt'

if __name__ == "__main__":
    data_file = open(TEXT_FILE, 'r')
    R = Rope()
    for line in data_file:
        R.concat(Rope(line.rstrip()))
    data_file.close()
    R.report()