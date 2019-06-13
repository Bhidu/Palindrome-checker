x = input('Enter your phrase: ')
x = list(x)
targets = ''' .'"():;<>/?[{]}!@#$%^&*-+_='''
for word in targets:
    if word in x:
        x.remove(word)
y = x
x.reverse()
x = ''.join(x)
y = ''.join(y)
if x.lower() == y.lower():
    print('Yes, it is a palindrome')
else:
    print('No, it is a palindrome')
k = input('Press close to exit')