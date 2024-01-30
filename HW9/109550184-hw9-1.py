#MAIN
hour_count={}
f=open('mbox-short.txt')
for line in f:
    line=line.rstrip()
    if line.startswith("From "):
        time=line.split(" ")[6]#00:00:00
        hour=time.split(":")[0]  
        hour_count[hour]=hour_count.get(hour,0)+1 #count

hours=[]
for hour,count in hour_count.items():
    hours.append((hour,count))

for hour,count in sorted(hours):
    print(hour,count) #Answer
f.close()
