#Main
filename=input("Enter the file name: " ) 
f=open(filename) #Open file
#line=f.readlines()
count=0
for line in f:
    line=line.rstrip() #Read 
    if line.startswith('Subject: [sakai] svn commit:'): #如果lineSubject: [sakai] svn commit: 
        end=line.find('/')
        line=line[len('Subject: [sakai] svn commit: '):end] 
        #print(line)
        
        start=0
        while not line.find(' ',start+1) == -1:
            start=line.find(' ',start+1) 
        #print(line.split(' '))
        print(line.split(' ')[0],line[start+1:end])
        count=count+1
        #print(start,' ',end)
f.close()
print("There were",count,"subject lines")

        

    