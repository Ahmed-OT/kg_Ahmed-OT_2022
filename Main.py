#Ahmed_Alotaibi
#kargo_Software_Engineer_Intern 

import sys

c=sys.argv[1:]
if len(c)==0:
    print("No Argument Given")
    sys.exit()
    
num={"0":"Zero",
    "1":"One",
    "2":"Two",
    "3":"Three",
    "4":"Four",
    "5":"Five",
    "6":"Six",
    "7":"Seven",
    "8":"Eight",
    "9":"Nine"}
line=""

for x in c:
    for y in x:
        line=line+num[y]
    line=line+","
line=line[0:-1]

print(line)
