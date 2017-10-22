print('red/yellow/green')
n=0
for red in range(0,4):
    for yellow in range(0,4):
        for green in range(2,7):
            if red+yellow+green==8:
                n+=1
                print(red,yellow,green)
print('总共有%i种'%n)
