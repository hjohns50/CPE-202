from hash_quad import *
import string

class Concordance:

    def __init__(self):
        self.stop_table = None          # hash table for stop words
        self.concordance_table = None   # hash table for concordance
    #str -> None
    #takes in a file of stop words and creates a hash table of them
    def load_stop_table(self, filename):
        """ Read stop words from input file (filename) and insert each word as a key into the stop words hash table.
        Starting size of hash table should be 191: self.stop_table = HashTable(191)
        If file does not exist, raise FileNotFoundError"""
        self.stop_table = HashTable(191)
        try:
            file_in = open(filename)
        except FileNotFoundError:
            raise FileNotFoundError("File Not Found")
        for line in file_in:
            self.stop_table.insert(line.splitlines()[0])
        file_in.close()

    #Str -> None
    #Creates a hash table that uses words as a key and line number as the data
    def load_concordance_table(self, filename):
        """ Read words from input text file (filename) and insert them into the concordance hash table, 
        after processing for punctuation, numbers and filtering out words that are in the stop words hash table.
        Do not include duplicate line numbers (word appearing on same line more than once, just one entry for that line)
        Starting size of hash table should be 191: self.concordance_table = HashTable(191)
        If file does not exist, raise FileNotFoundError"""
        self.concordance_table = HashTable(191)
        try:
            file_in = open(filename)
        except FileNotFoundError:
            raise FileNotFoundError("File Not Found")
        line_num = 0
        for line in file_in: #loops through file by line
            line_str = "" #string that will be split
            line_num += 1 #keeps track of line number
            line_dic = {} #dictionary to quickly check if a word has appeared more than once on a line
            line_str += line #loads up line string to for operations
            for char in line: #loops through the line
                if char == "'":
                    line_str = line_str.replace(char, "") #modifies line_str 
                if char in string.punctuation:
                    line_str = line_str.replace(char, " ")
                if char == "\n":
                    line_str = line_str.replace(char, " ")
            line_lst = line_str.split(" ") #splits into list
            for i in line_lst: #makes sure each item is alpha and lowercase and not already added
                if i.isalpha():
                    add = i.lower()
                    if line_dic.get(add) == None:
                        if self.stop_table.in_table(add) == False:
                            line_dic[add] = line_num 
                            self.concordance_table.insert(add, line_num)
        file_in.close()
        
        
    def write_concordance(self, filename):
        """ Write the concordance entries to the output file(filename)
        See sample output files for format."""
        try:
            file_out = open(filename, "w")
        except FileNotFoundError:
            raise FileNotFoundError("File Not Found")
        word_lst = self.concordance_table.get_all_keys() #gets a list of all the words
        word_lst.sort() #orders it
        for i in word_lst:
            ln_num = self.concordance_table.get_value(i) #line number list
            ln_str = "" #string that will be written to file
            for c in ln_num:
                ln_str += " " + str(c) #loads line numbers as a string
            file_out.write(i + ":" + ln_str + "\n")
        file_out.close()