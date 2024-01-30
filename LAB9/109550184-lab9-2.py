words='Overturning elections sounds like the stuff of secret deals in \
smoke-filled rooms, but President Donald Trumps not even trying to \
hide his effort to subvert the results of the election as \
President-elect Joe Bidens margin widens to more than 6 million \
votes. Trumps efforts to deny Biden the White House traveled from \
the courts to state legislatures on Friday with Trumps personal \
reception with Republican lawmakers from Michigan -- and their \
counterparts in Pennsylvania may be next on the list. But there \
were signs, even among Republicans, that Trumps efforts need some \
evidence. As legislative leaders, we will follow the law and \
follow the normal process regarding Michigans electors, just as we \
have said throughout this election, Michigan Senate Majority \
Leader Mike Shirkey and Michigan House Speaker Lee Chatfield said \
in a joint statement after their meeting at the White House.'

'''words=words.split(' ') #list
words.sort(reverse=True) #sort
print(words,'\n') #answer

sender_count={} #dict
for word in words:
    sender_count[word[0][0]]= sender_count.get(word[0][0],0)+1 #count the first alphabets appear
print(sender_count)'''


f=open("input.txt") #Open file
lines=f.readlines()
words=[]
for line in lines: 
    line=line.strip()
    words=words+line.split(' ')
words.sort(reverse=True) #sort
print(words,'\n') #answer

sender_count={} #dict
for word in words:
    sender_count[word[0][0]]= sender_count.get(word[0][0],0)+1 #count the first alphabets appear
print(sender_count)
f.close() #Close file






