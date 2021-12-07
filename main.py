import string
import sys
import re
def print_hi():
        global sp1
        with open(sys.argv[1],'r') as f1 ,open(sys.argv[2],'r') as f2:
            line_file1:string = f1.read()
            line_file2:string = f2.read()

        line_file1 = line_file1.replace("\n"," ")
        line_file1=re.sub('\s+',' ',line_file1)
        line_file2 = line_file2.replace("\n", " ")
        line_file2 = re.sub('\s+', ' ', line_file2)
        print('\n'+line_file1+'\n\n'+line_file2+'\n')

        sp_file1 = re.split('; |,|\*|\.|\?|\!',line_file1)
        sp_file2 = re.split('; |,|\*|\.|\?|\!',line_file2)


        sp_file1 = str(sp_file1).replace("\n","")
        sp_file2 = str(sp_file2).replace("\n","")

        print(sp_file1+'\n\n'+sp_file2+'\n')

        # for i,j in sp_file1,sp_file2:
        #     if(sp_file1[i] == sp_file2[j]):
        #         print('Propozitia comuna este: '+sp_file1)

        aux=[]
        for i in range(0,len(sp_file1)):
            for j in range(0,len(sp_file2)):
                if(sp_file1[i]==sp_file2[j]):
                    aux.append(sp_file1[i])
                    str1 =' '.join([str(elem) for elem in aux])

        print(str1)




        # file3 = list(set(sp_file1) & set(sp_file2))
        # print(file3)

        # sp_file1_as_set = set(sp_file1)
        # intersection = sp_file1_as_set.intersection(sp_file2)
        # intersection_as_list = list(intersection)
        # print(intersection_as_list)









        f1.close()
        f2.close()



if __name__ == '__main__':

     print_hi()
