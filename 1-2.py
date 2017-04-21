import sys
import re
import os

class Common_Words:
    def __init__(self):
        self.word_set1 = set()
        self.word_set2 = set()

    # opens file and tokenizes it, adding them into sets
    def read_file(self, f1, f2):
        try:
            with open(f1, 'r') as file:
                if os.stat(f1).st_size == 0:
                    print("File 1 is empty: {0}".format(f1))
                    return
                for i in file:
                    i = i.lower()
                    i = re.sub(r'\\n+', ' ', i)
                    i = re.sub(r'\W+|_+', ' ', i)
                    i = i.split()
                    for j in i:
                        self.word_set1.add(j)
        except IOError:
            print("This file does not exist: {0}".format(f1))

        try:
            with open(f2, 'r') as file:
                if os.stat(f2).st_size == 0:
                    print("File 2 is empty: {0}".format(f2))
                    return
                for i in file:
                    i = i.lower()
                    i = re.sub(r'\\n+', ' ', i)
                    i = re.sub(r'\W+|_+', ' ', i)
                    i = i.split()
                    for j in i:
                          if j in self.word_set1:
                            self.word_set2.add(j)
        except IOError:
            print("This file does not exist: {0}".format(f2))

    #sorts the dict in descending order and prints it
    def print_word_set(self):
        if len(self.word_set2) == 0:
            return
        for i in self.word_set2:
            print("{0}".format(i))
        print("There are {0} common words".format(len(self.word_set2)))

if __name__ == "__main__":
    try:
        w = Common_Words()
        w.read_file(sys.argv[1], sys.argv[2])
        w.print_word_set()
    except IndexError:
        print("No file was entered or only 1 file was entered")