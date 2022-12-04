from string import ascii_letters, digits

#define as listas constantes
#LETTERS recebe todas as letras do alfabeto + _
#DIGITS recebe todos os numeros
LETTERS, DIGITS = ascii_letters + "_", digits
TYPES = ["int", "char", "bool", "float", "double"]

entrie = input("Entrada: ").split()

def automato(entrie: list[str]):
  if entrie[0] not in TYPES: return False             #Se a primeira palavra não for um tipo, retorna falso
  for word in entrie[1:]:                             #Pega o resto da string
    if word[0] not in LETTERS: return False           #Se a primeira não for uma letra do alfabetor, retorna falso
    if word[-1] not in [",", ";"]: return False       #Se o final da palavra não tiver , ou ; retorna falso
    for letter in word[1:-1]:                         #Pega o resto da palavra
      if letter not in LETTERS + DIGITS: return False #Verifica se o resot da palavra tem somente letras e digitos
  return True

print(f"Aceita: {automato(entrie)}")