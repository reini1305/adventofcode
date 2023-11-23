#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  7 17:55:16 2016

@author: reini
"""

def check_anagram(x):
    start_idx = 0
    end_idx = 4
    while end_idx<=len(x):
        curr_str = x[start_idx:end_idx]
        if curr_str[0]==curr_str[3] and curr_str[1]==curr_str[2] and curr_str[1]!=curr_str[3]:
            return True
        start_idx = start_idx+1
        end_idx = end_idx+1
    
    return False

def get_aba(x):
    aba = list()
    if isinstance(x,basestring):
        start_idx = 0
        end_idx = 3
        while end_idx<=len(x): 
            curr_str = x[start_idx:end_idx]
            if curr_str[0]==curr_str[2] and curr_str[0]!=curr_str[1]:
                aba.append(curr_str)
            start_idx = start_idx+1
            end_idx = end_idx+1
    else:
        for tok in x:
            start_idx = 0
            end_idx = 3
            while end_idx<=len(tok): 
                curr_str = tok[start_idx:end_idx]
                if curr_str[0]==curr_str[2] and curr_str[0]!=curr_str[1]:
                    aba.append(curr_str)
                start_idx = start_idx+1
                end_idx = end_idx+1
    return aba
    
f=open('input_7.txt')
num_tls = 0
for line in iter(f):
    has_tls = False
    must_not = False
    start_idx = 0
    end_idx = len(line)
    while end_idx>0:
        end_idx = line.find('[',start_idx)
        if end_idx<0:
            break
        # string between start_idx and end_idx should be searched
        has_tls = has_tls or check_anagram(line[start_idx:end_idx])
        start_idx = end_idx + 1
        end_idx = line.find(']',start_idx)
        # string between start_idx and end_idx shall not contain an anagram
        must_not = must_not or check_anagram(line[start_idx:end_idx])
        start_idx = end_idx + 1
    has_tls = has_tls or check_anagram(line[start_idx:])
    if(has_tls and not must_not):
        num_tls = num_tls + 1
print num_tls
f.close()

f=open('input_7.txt')
num_ssl = 0
for line in iter(f):
    has_ssl = False
    start_idx = 0
    end_idx = len(line)
    inside = list()
    outside = list()
    while end_idx>0:
        end_idx = line.find('[',start_idx)
        if end_idx<0:
            break
        # string between start_idx and end_idx should be searched
        outside.append(line[start_idx:end_idx])
        start_idx = end_idx + 1
        end_idx = line.find(']',start_idx)
        # string between start_idx and end_idx shall not contain an anagram
        inside.append(line[start_idx:end_idx])
        start_idx = end_idx + 1
    outside.append(line[start_idx:])
    aba = get_aba(outside)
    for t in aba:
        inv_t = t[1]+t[0]+t[1]
        for s in inside:
            if s.find(inv_t)>=0:
                has_ssl = True
    if has_ssl:
        num_ssl = num_ssl + 1
print num_ssl
f.close()