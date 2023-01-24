word = "ciaociao"

for i in range(len(word)//2+1):
    print(word[i], word[-(i+1)])
lista = [0, 1]
print(lista[(0 or 1)] == 0)