while True: #Input First Row
    amount=input("Enter amount of loan: ")
    try:
        ans=float(amount) #計算
        break
    except ValueError: #Not value
        print("Error! The input should be numbers.")
        
while True: #Input Second Row
    rate=input("Enter interest rate: ") 
    try:
        ans=ans+ans*(float(rate)/100)/12 #計算
        break
    except ValueError: 
        print("Error! The input should be numbers.")
            
while True: #Input Third Row
    payment=input("Enter monthly payment: ")
    try:
        ans=ans-float(payment) #計算
        break
    except ValueError: 
        print("Error! The input should be numbers.")

print("Balance remaining after first payment: ",ans) #Answer
    
