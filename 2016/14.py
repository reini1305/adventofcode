#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 14 17:58:39 2016

@author: reini
"""

#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  5 17:42:33 2016

@author: reini
"""

import hashlib
import re 
input = 'ahsbgdzn'
#input = 'abc'
test_int = 0
hashes = []
indices = []
while len(indices)<64:
    # if hash already exists, we don't have to calculate it
    if test_int>=len(hashes):
        hashes.append(hashlib.md5(input+str(test_int)).hexdigest())
    match = re.search(r"(.)\1{2}", hashes[test_int])
    if match:
        tosearch = ''.join(list(match.group(0)[0] for i in range(0,5)))
        
        valid = False
        for i in range(test_int+1,test_int+1001):
            # if hash already exists, we don't have to calculate it
            if i>=len(hashes):
                hashes.append(hashlib.md5(input+str(i)).hexdigest())
            if tosearch in hashes[i]:
                valid = True
                break
        if valid:
            indices.append((test_int))
    test_int = test_int +1
print indices[-1]

test_int = 0
hashes = []
indices = []
while len(indices)<64:
    # if hash already exists, we don't have to calculate it
    if test_int>=len(hashes):
        hv = hashlib.md5(input+str(test_int)).hexdigest()
        for k in range(2016):
            hv = hashlib.md5(hv).hexdigest()
        hashes.append(hv)
    match = re.search(r"(.)\1{2}", hashes[test_int])
    if match:
        tosearch = ''.join(list(match.group(0)[0] for i in range(0,5)))
        
        valid = False
        for i in range(test_int+1,test_int+1001):
            # if hash already exists, we don't have to calculate it
            if i>=len(hashes):
                hv = hashlib.md5(input+str(i)).hexdigest()
                for k in range(2016):
                    hv = hashlib.md5(hv).hexdigest()
                hashes.append(hv)
            if tosearch in hashes[i]:
                valid = True
                break
        if valid:
            indices.append((test_int))
    test_int = test_int +1
print indices[-1]