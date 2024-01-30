import re

#Main
f=open('wifi_log.txt') #Open file
details=f.readlines() #Read file
f.close() #Close file

#1 Calculate average frames
frames=re.findall("inputEAPOLFrame: Received non-key EAPOL frame \(([0-9]*)\)", str(details)) #([0-9]*)
count_frames=0
total_frames=0
for frame in frames: 
    count_frames=count_frames+1 #Count
    total_frames=total_frames+int(frame) #Total
result=total_frames/count_frames #Average frames
print("Average of the received non-key EAPOL frames:",round(result,3)) #.03f

#2 Count IPs
IPs=re.findall("[0-9]*\.[0-9]*\.[0-9]*\.[0-9]*",str(details)) #Find all IP in file
count_IPs={} #dict()
for IP in IPs:
    count_IPs[IP]=count_IPs.get(IP,0)+1 #count 
print(count_IPs) #Output answer
