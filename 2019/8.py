import numpy as np

with open('input8.txt','r') as f:
    raw_data = [int(c) for c in f.read().strip('\n')]

image = np.reshape(np.array(raw_data),(-1,6,25))
num_zeros = np.sum(np.sum(image==0,axis=1),axis=1)
num_ones = np.sum(np.sum(image==1,axis=1),axis=1)
num_twos = np.sum(np.sum(image==2,axis=1),axis=1)
least_zeros_id = np.argmin(num_zeros)
print('Day 8, Part 1: {}'.format(num_ones[least_zeros_id] * num_twos[least_zeros_id]))

out = np.zeros((6,25))
for x in range(25):
    for y in range(6):
        pixel = 0
        for z in np.squeeze(image[:,y,x]):
            if z != 2:
                pixel = z
                break
        out[y,x] = pixel
np.set_printoptions(formatter={'all':lambda x: ' ' if x==0 else '*'})
print('Day 8, Part 2: \n{}'.format(out))