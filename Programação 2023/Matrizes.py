M = [ [1,2,3], [4,5,6], [7,8,9]]
print(M)

print(M[0][0])

V = [x[1] for x in M]
print(V)

#alterações nessa lista
L = [1,5,6]
print(L)
L[1] = 9
print(L)

#alteração de listas utilizando indexação e slides
L = [1,5,6]
#antes: [1,5,6]

#desejados: [1,9,10,5,6]
L[1:1] = [9,10]
print(L)

#desejado: [1,10,5,6]
L[1:2] = []
print(L)


#alteração com métodos
L = [1,5,6]
print(L)

#adicionando elementos
L.append(9)
print(L)

#removendo elementos
L.pop()
print(L)
#adicionando vários elementos
L = [1,5,6]
print(L)

L.extend([10,11])
print(L)

#removendo elementos por posição
L.pop(3)
print(L)

#outros métodos de alteração
L = [1,9,6,5,2]
print(L)

#inverter a ordem da lista
L.reverse()
print(L)

#removendo por conteúdo
L.remove(6)
print(L)

#ordernar lista
L.sort()
print(L)