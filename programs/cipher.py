import string
#print(string.ascii_letters)
dict={}
file=open("file2.txt","w")
for i in range(len(string.ascii_letters)):
    dict[string.ascii_letters[i]]=string.ascii_letters[i-1]
print(dict)
with open("file1.txt") as f:
    while True:
        c=f.read(1)
        if not c:
            print("end of file")
            break
        if c in dict:
            data=dict[c]
        else:
            data=c
        file.write(data)
        print(data)
file.close()