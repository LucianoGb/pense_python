fin = open('words.txt')

# print(fin.readline())

# for line in fin:
#     word = fin.readline()
#     if len(word) >= 20:
#         print(word)

for line in fin:
    word = fin.readline()
    if 'e' not in word:
        print(word)
    
        
        