#Emulando condiciones de hacker-rank
#Resultado positivo
n=2
s=' 1 2 '
integer_list=map(int, s.split())
tupla=[]
for value in integer_list:
    tupla.append(value)
#print(tupla_limpia)
print(hash(tuple(tupla)))
