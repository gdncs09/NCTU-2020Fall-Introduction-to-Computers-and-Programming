# Lab-10
# Exercise 1
# 'X-DSPAM-Confidence:0.8475'

#1
test_string='X-DSPAM-Confidence:0.8475'
print(float(test_string[test_string.find(':')+1:len(test_string)]),'\n')

# Exercise 2-1
test_data = [
    "1. The lyrics are bad!",
    "2. The lyrics are not bad!",
    "3. The lyrics are not that bad!",
    "4. The lyrics are poor!",
    "5. The lyrics are not poor!",
    "6. The lyrics are not that poor!",
    "7. The lyrics are good!",
    "8. The lyrics are not good!",
    "9. The lyrics are not that good!",
    "10.I'm not sure if he's good."
]

# Exercise 2-2
test_data_2 = [
    "1. I'm not sure he's good.",
    "2. I'm not sure it's a good idea"
]

#2-1
i = 0
for data in test_data:
    '''
    print('Loop: ', i)
    print('not is at index: ', data.find('not'))
    print('bad is at index: ', data.find('bad'))
    print('poor is at index: ', data.find('poor'))
    print('good is at index: ', data.find('good'))
    '''
    if data.find('not')!=-1: #如果在data找到 'not'
        if data.find('bad')!=-1 or data.find('poor')!=-1: #如果在data找到 'bad' 或 'poor'
            print(data[0:data.find('not')-1]+' good!') #Lấy từ vị trí đầu đến trước vị trí 'not'
        elif data.find('good')!=-1: #如果在data找到 'good'
            print(data[0:data.find('not')-1]+' bad!')
    else:
        print(data)
    '''i += 1'''

for data in test_data_2:
    data=data.replace('not sure','sure') #換 'not sure' 成 'sure'
    if data.find('good')!=-1: #如果在data找到 'good'
        data=data.replace('good','bad') #換 'good' 成 'bad'
    elif data.find('bad')!=-1:
        data=data.replace('bad','good')
    print(data)
    