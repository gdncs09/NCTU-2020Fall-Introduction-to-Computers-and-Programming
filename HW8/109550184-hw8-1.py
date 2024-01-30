def Run(total, count):
    f=open(filename) #Open File
    for line in f: 
        line = line.rstrip() #Read
        #1
        if line.startswith("X-DSPAM-Confidence:"): #如果line開頭是X-DSPAM-Confidence:
            #print(line.split(' ')[1]) #Check
            total=total+float(line.split(' ')[1]) #Sum
            count=count+1 #Count number        
    #print("Function: ",total,' ',count) #Check in Run  
    f.close()     
    return total, count 

#Main
total=0
count=0   
filename=input("Enter the file name: " ) #Input 
total, count = Run(total, count) #Function 
#print(total,' ',count) #Check in main
print("Average spam confidence: ",total/count) #Answer
