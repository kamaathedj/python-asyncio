filled_dict = {"one": 1, "two": 2, "three": 3}

tup=("mangoes","apples")

# count in a tuple prints the number on occurences of a certain element
print(tup.count('mangoes'))

# tuples are immutble
# tup('pomegranate')
print(tup)

data = """ i am a good {}
perso and i feel it
"""
# you can treat string like array
print(data[4])
# find the legth of a string
print(';;;;;;;;;;;;;')
print(len(data))
print(';;;;;;;;;;;')
print(data.format('kamaa'))


for i in range(3,10,2):
    print(i)

for i in ['dog','cow', 'goat']:
    print('The animal is a {}'.format(i))


phones =['oppo','tecno','infinix','nokia','samsung','iphone']

for i,value in enumerate(phones):
    print(i,value)
    
    
with open('data.txt') as file:
    for line in file:
        print(line, end='😁')

x=True
