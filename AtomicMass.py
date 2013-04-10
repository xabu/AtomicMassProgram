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
print("Sample input: 'H 2 O 13.2' for 13.2 grams of H2O")
print("Ctrl + c to stop the program.")
while(True):
    question = input().split(' ')
    # Time to parse the input!
    elements = []
    numbers = []
    m = float(question[-1]) # last thing is _always_ the mass
    question = question[:-1] #lose the mass
    i = 0 # we'll do a manual for loop, while-style
    while i < len(question):
        element = question[i]
        #get an element and check if the thing after 1) exists and 2) is a number
        if i < len(question) - 1 and question[i + 1].isdigit():
            number = question[i + 1]
            # if it does, we skip the next thing because it's a number
            i += 1
        else:
            #otherwise assume 1
            number = 1
        elements.append(element)
        numbers.append(number)
        i += 1
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
