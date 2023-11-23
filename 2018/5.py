
#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  5 15:20:56 2018
@author: reinbc
"""
import string
with open('input5','r') as file:
    input = file.read().strip()
    
#input = 'dabAcCaCBAcCcaDA'
def fully_react(polymer):
    chars = [ord(x) for x in polymer]
    
    for i in reversed(range(0, len(chars) - 1)):
        try:
            if abs(chars[i]-chars[i+1]) == 32:
                del chars[i:i+2]
        except:
            pass
    return ''.join([chr(x) for x in chars])

# slower because more to copy
def fully_react_v2(polymer):
    chars = [ord(x) for x in polymer]
    i = 0
    while i < len(chars) - 1:
        if abs(chars[i]-chars[i+1]) == 32:
            del chars[i:i+2]
            i -= 1
        else:
            i += 1 
        i = max(0,i)
    return ''.join([chr(x) for x in chars])
  
# Task 1      
print(len(fully_react(input)))
# Task 2
min_length = len(input)
for l,u in zip(string.ascii_lowercase,string.ascii_uppercase):
    reduced = input.replace(l,'').replace(u,'')
    
    curr_len=len(fully_react(reduced))
    min_length = min(min_length,curr_len)
    
print(min_length)
