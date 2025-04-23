class A: ...
class B: ...
class C(A, B): ...

# Type anotations
idade: int = 32
salario: float = 35000.50
nome: str = "julius"
casado: bool = True
dados: dict = {"nome": nome, "salario": salario, "idade": idade}
array: list = [2,5, "ju", 25, 25, 25]
tupla: tuple = (2,5, 25, 25)
unico: set = {2,5, "ju", 25, 25, 25}

# print(unico)
# print(nome.upper()) # método builtin
# print(dir(str)) # imprime class com dict
# help(C) # ajuda ver internamente 

nome: str = 'Ana paula'
eh_casado: bool = True

pessoa: A = A() # Tipo personalizado

A.nome = "Maria" # atribuição direto da class
A.cargo = "diretor"

print(A.__dict__) # armazena valores da class