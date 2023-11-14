import re
# Funcion casesentive, para contar el numero de coincidencias
# de una cadena de caracteres en una mas grande
def count_substring(string, sub_string):
    string.lower()
    sub_string.lower() 
    count=0
    position = string.rfind(sub_string)
    size = len(sub_string)
    while position!=-1:
        string=string[0:position]+string[position+size-1:]
        position = string.rfind(sub_string)
        count+=1 
    return count

def string_analizer(string):
    # Contiene caracteres alfanumericos
    pattern='.*[a-zA-Z0-9]+.*'
    match=re.search(pattern,string)
    if match is None:
        print(False)
    else:
        print(True)
   # Contiene caracteres alfabeticos
    pattern='.*[a-zA-Z]+.*'
    match=re.search(pattern,string)
    if match is None:
        print(False)
    else:
        print(True)
    # Contiene caracteres numericos
    pattern='.*[0-9]+.*'
    match=re.search(pattern,string)
    if match is None:
        print(False)
    else:
        print(True) 
    # Contiene caracteres en minuscula
    pattern='.*[a-z]+.*'
    match=re.search(pattern,string)
    if match is None:
        print(False)
    else:
        print(True) 
    # Contiene caracteres en mayuscula
    pattern='.*[A-Z]+.*'
    match=re.search(pattern,string)
    if match is None:
        print(False)
    else:
        print(True) 

string_analizer("a1Q#$%^&*&")