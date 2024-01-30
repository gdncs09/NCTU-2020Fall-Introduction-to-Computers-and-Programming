import sys #use sys.exit()
#Init Dictionary
name_of_awards={}
f=open('input.txt','r',encoding='utf-8')
for line in f:
    line=line.rstrip()
    if line.startswith('最佳'):
        key=line
        name_of_awards[key]={}
        continue
    if line == '':
        continue
    line=line.split("|")
    W=line.pop(0)
    if W == 'Winner!':
        nominee=line.pop(0)
        W='\n'+W
    else:
        nominee=W     
        W=''
    values=''
    for value in line:
        if values != '':
            values=values+'\n'
        values=values+value
    name_of_awards[key][nominee]=values+W
f.close()

#Function
def first_layer():#Layer1
    print("====Enter B to go back, enter Q to quit.====")
    for name in name_of_awards:
        print(name)
        
def second_layer(award):#Layer2
    for name in name_of_awards[award]:
        print(name)

def third_layer(award,nominee):#Layer3
    print(name_of_awards[award][nominee])
    print("==The last layer, enter B to go back, enter Q to quit.==")
    
#Main
layer=1 #Start at first layer

while True:
    if layer==1:#First layer
        first_layer()
    try:
        key=input("Please enter: ")   
        if key=='B' and layer==1:
            print("Error message!")
            continue
        if key=='B': #Back
            layer=layer-1 
        elif layer<3: #Because layer only <=3 
            layer=layer+1#Layer MAX =3
            
        if key=='Q': #Quit or layer at Layer0
            sys.exit()
        
        if layer==2:#Second layer
            if key != 'B':
                award=key#存
            second_layer(award)
        
        elif layer==3:#Third layer
            nominee=key
            third_layer(award,nominee)
        
    except KeyError:
        print("Error message!")
        if layer!=3:
            layer=layer-1   