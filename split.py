all_data=open('passwords.txt','r')
datas=all_data.readlines()
j=0
for i in datas:
    i=i.strip("\n")
    s=i.split(" ",1)
    print s[0]
    j+=1
    # print s[1]
all_data.close()

print j