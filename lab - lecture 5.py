# 1: This code does not run!  Try it and examine the errors, then figure out 
# what needs to be changed to make it work.

a = 10

def first_func(b=20):
    c = 30
    value = second_func() + c + b
    return value

def second_func(d=40):
    e = 50
    return a + d + e

result = first_func()
print(result)


# 2: Take this code from the last lab and write a function so that the form of
# the final answer is:
# answer = {key_func(k):val_func(v) for k, v in start_dict.items()}

import datetime
start_dict = {'noah': '2/23/1999',
              'sarah':'9/1/2001',
              'zach': '8/8/2005'}
# Turn it into {'Noah': datetime(1999, 2, 23),
#               'Sarah':datetime(2001, 9, 1),
#               'Zach': datetime(2005, 8, 8)}
# HINT: The datetime library has a function that turns strings of the right format into dates.

def key_func(k):
    return k.capitalize()

def val_func(v, date_format='%m/%d/%Y'):
   # Hard coding date_format here (instead of defining as a kwarg) works, but is
   #less flexible.
   return datetime.datetime.strptime(v, date_format)

answer = {key_func(k):val_func(v) for k, v in start_dict.items()}
print(answer)
    
  
   
    