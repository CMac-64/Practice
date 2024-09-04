word = input ('Enter Word')
print("Original String:", word)

size = len(word)

print("Printing only Even Index Chars")
for i in range(0, size - 1, 2):
    print("Index[" + i + "]", word[i])
