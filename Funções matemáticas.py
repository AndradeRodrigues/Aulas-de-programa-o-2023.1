#Funções matemáticas 

#O python tem módulos built-in com importantes funções matemáticas
import math
print(math.sin(2*math.pi/180)) #trigonometria

math.sqrt(144) #Raiz quadrada

print(math.floor(2.543)) 
print(math.trunc(2.543))
print(round(2,543))


#Utilizando métodos aleatórios
import random
random.random() #Gera um númeor randomico entre 0 e 1
escolha = random.choice(["azul", "amarelo", "preto", "branco"])
print(escolha)