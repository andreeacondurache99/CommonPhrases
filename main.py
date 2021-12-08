import string
import sys
import re

def eliminate_punctuation(sentence):
        sentence = sentence.replace(",", "")
        sentence = sentence.replace(";", "")
        sentence = sentence.replace("-", "")
        sentence = sentence.replace(":", "")
        sentence = sentence.replace("(", "")
        sentence = sentence.replace(")", "")
        sentence = sentence.replace("{", "")
        sentence = sentence.replace("}", "")
        sentence = sentence.replace("[", "")
        sentence = sentence.replace("]", "")
        sentence = sentence.replace("\"", "")
        sentence = sentence.replace("\'", "")
        sentence = sentence.replace("#", "")
        sentence = sentence.replace(" ","")
        return sentence

def commonPhrases():
        global sp1
        with open(sys.argv[1],'r') as f1 ,open(sys.argv[2],'r') as f2:
            line_file1:string = f1.read()
            line_file2:string = f2.read()

        line_file1 = line_file1.replace("\n"," ")
        line_file1=re.sub('\s+',' ',line_file1)
        line_file2 = line_file2.replace("\n", " ")
        line_file2 = re.sub('\s+', ' ', line_file2)

        sp_file1 = re.split('\*|\.|\?|\!',line_file1)
        sp_file2 = re.split('\*|\.|\?|\!',line_file2)
        sp_file2_nospace = []
        sp_file2_nopunctuation = []
        for sentence in sp_file2:
                sp_file2_nospace.append(sentence.replace(" ", "").upper())
                sp_file2_nopunctuation.append(eliminate_punctuation(sentence).upper())

        print("Propozitii comune(caz 1):\n")
        index= 1
        #print(sp_file1)
        for sentence in sp_file1:
                aux = sentence.replace(" ","").upper()
                if(aux in sp_file2_nospace and sentence != ''):
                        print(str(index) + ".", sentence)
                        index += 1
        print("-------------------------------------------------------------------------------------------------------------------------------------------\n")
        print("Propozitii comune(caz 2):\n")
        index = 1
        for sentence in sp_file1:
                aux = eliminate_punctuation(sentence).upper()
                if (aux in sp_file2_nopunctuation and sentence != ''):
                        print(str(index) + ".", sentence)
                        index += 1
        f1.close()
        f2.close()



if __name__ == '__main__':
        commonPhrases()
