import os


#function to check the signature
def check_sign(sign_header,sign_footer,hex_raw):
    pos_head=hex_raw.find(sign_header)
    pos_foot=hex_raw.find(sign_footer)
    return pos_head,pos_foot


#Please copy the raw hex into raw.txt and save in the same directory
f1=open("raw.txt",'r')
hex_raw=f1.read()

#string for saving the formatted output
newhex=""

#sign.txt contains the signature of some common file extensions
f2=open("sign.txt",'r')

#reading all the lines and extrcting the headers and footers
for sign in f2.readlines():
    sign_header=" "
    sign_footer=" "
    sign_list=sign.split()
    sign_header=sign_list[1]
    sign_ext=sign_list[0]

    #some file extensions have no footer 
    try:
        check_footer=sign_list[2]
        if(len(check_footer)<=1):
            pass
        else:
            sign_footer=sign_list[2]
    except:
        pass


    start,before_end=check_sign(sign_header,sign_footer,hex_raw)
    
    #adding the length of footer to the end as the find fuction returns the staring point of footer
    adds=len(sign_footer)
    end=before_end+adds

    #extracting the formatted hex
    if(start>=0 and end>=start):
        for i in range(start,end):
            newhex=newhex + (hex_raw[i])
        outputfile="Output.txt"
        out=open(outputfile,'w')
        out.write(newhex)
        print("File is of type ",sign_ext)
        
print("File formatted output is saved as Output.txt")