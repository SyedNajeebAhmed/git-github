# patterns for loops practice

for x in range(0, 10):
    for y in range(0, x+1):
        print('*', end='')
    print('*', end='\n')

for x in range(0, 10):
    for y in range(0, 10-x):
        print('*', end='')
    print('*', end='\n')

for x in range(0, 10):
    for y in range(0, x):
        print(' ', end='')
    for z in range(0, 10-x):
        print('*', end='')
    print()

for x in range(0, 10):
    for y in range(0, 9-x):
        print(' ', end='')
    for z in range(0, x+1):
        print('*', end='')
    print()
    
for x in range(0, 10):
    for y in range(0, x):
        print(' ', end='')
    for z in range(0, 10-x):
        print('*', end=' ')
    print()

for x in range(0, 10):
    for y in range(0, 9-x):
        print(' ', end='')
    for z in range(0, x+1):
        print('*', end=' ')
    print()