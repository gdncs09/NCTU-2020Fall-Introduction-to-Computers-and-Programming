total = 0
count = 0
a = "done"
while True:
    num=input("Enter a number: ")
    if num == "done":
            break
    try:
        total=total+int(num)
        count=count+1
    except ValueError: 
        print("Invalid Input: ",num)
if count>0:
    avg=total/count
else:
    avg=0
    
print("Total = ",total," , Count = ",count," , Average = ",avg)

        
            
        
        
