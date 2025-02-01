

alphabetical = ['a','b','c','d','e','f','g','h']

index_to_chess = {}
counter = 0
for a in alphabetical:
    for i in range(1,9):
        #print(f'{a}{i}')

        index_to_chess[counter] = [a,i]
        counter += 1
print(index_to_chess[0])
