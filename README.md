# Palindrome 
## A number, word or a sentence which when read backwards remains same.

Python code to check a palindrome (be it spaces or any other symbols included)

### Code

```python

  x = input('Enter your phrase: ') 
  x = list(x)                                      # converts list to string 
  targets = ''' `~.'"():;<>/?[{]}!@#$%^&*-+_='''     # creates a string of sample of which characters are to be excluded 
  for word in targets:                             # compares sample to input phrase    
      if word in x:  
          x.remove(word)  
  y = x   
  x.reverse()
  x = ''.join(x)                                   # converts list to string 
  y = ''.join(y)  
  if x.lower() == y.lower():   
      print('Yes, it is a palindrome')   
  else:  
      print('No, it is a palindrome')  
  k = input('Press close to exit')  

