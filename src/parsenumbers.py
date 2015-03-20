#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Created on Jan 7, 2013

@author: J Carroll
@emaill: jrcarroll@jrcresearch.net
'''

file = open('/home/jnam/workspace/sandbox/trash/numbers.txt', 'rw')

number = []

for i in file:
    i = i.rstrip('\n')
    line = i.split(' ')
    # Capture the next number of lines important to us
    
    # Iterate over the number of lines
    for i in range(0, int(line[1]), 1):
        print "Line #", i
    raw_input("paused")

raw_input("aefaef")

for i in file:
    print i

