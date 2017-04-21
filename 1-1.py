import sys
import re
import operator
import os

class Word_Freq:
    def __init__(self):
        self.word_dict = {}

    # opens file and tokenizes it, adding it into a dictionary
    def open_file(self, f):
        try:
            with open(f, 'r') as file:
                if os.stat(f).st_size == 0:
                    print("This file is empty: {0}".format(f))
                    return
                for i in file:
                    i = i.lower()
                    i = re.sub(r'\\n+', ' ', i)
                    i = re.sub(r'\W+|_+', ' ', i)
                    i = i.split()
                    for j in i:
                        if j not in self.word_dict:
                            self.word_dict[j] = 1
                        else:
                            self.word_dict[j] += 1
        except IOError:
            print("This file does not exist: {0}".format(f))

    #sorts the dict in descending order and prints it
    def print_word_dict(self):
        for k, v in sorted(self.word_dict.items(), key=operator.itemgetter(1), reverse=True):
            print("{0} - {1}".format(k, v))

if __name__ == "__main__":
    try:
        w = Word_Freq()
        w.open_file(sys.argv[1])
        w.print_word_dict()
    except IndexError:
        print("No file was entered.")
