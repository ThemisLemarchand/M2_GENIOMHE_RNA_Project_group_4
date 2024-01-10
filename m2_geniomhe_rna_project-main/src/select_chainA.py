import os
import re

import sys

print('cmd entry:', sys.argv)

path = sys.argv[1]+"/"
print(path)
count=0
for f in os.listdir(path):
   # print(f)
    file=path+f
    if(os.path.isfile(file)):
        input_f = open(file,"r")
        lines=input_f.readlines()
        #print(lines)
        input_f.close()

        output=path+"chainA/"+f
        output_f=open(output,"w")

        for line in lines:
            if re.search("ATOM",line):
                field=line.split()
                if(field[4]!='B'):
                    #print(field[4])                
                    
                    output_f.write(line)
                    
                    #print(field)
                    count+=1
    #print(count)
    output_f.close()
    