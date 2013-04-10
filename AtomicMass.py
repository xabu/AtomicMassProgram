#!/usr/bin/env python3

perTable = open('periodic_table.txt')
am = {} # Dictionary going from atomic symbols to masses
for i in perTable:
    if i:
        line = i.split(',')
        atomicSymbol = line[-1][:-1] #[:-1] to shred off the \n
        atomicMass = float(line[1])
        am[atomicSymbol] = atomicMass
perTable.close()
print("Sample input: 'H 2 O 1 13.2' for 13.2 grams of H2O")
question = input().split(' ')
elements = question[:-1:2]
numbers = question[1::2]
m = float(question[-1])
numFirst = 0
MM = 0
i = 0
while i<len(elements):
    MM+=am[elements[i]]*int(numbers[i])
    if elements[i] == elements[0]:
        numFirst+=int(numbers[i])
    i+=1
n = m/MM
particles = n * numFirst * 6.022141 * 10**23
print('MM = '+ str(MM))
print('n = '+str(n))
print('# of first particle = '+str(particles))
