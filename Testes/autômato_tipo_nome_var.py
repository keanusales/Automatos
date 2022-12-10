from string import ascii_letters, digits

# define as listas constantes
# LETTERS recebe todas as letras do alfabeto (maiúsculas e minúsculas) + _
# DIGITS recebe todos os numeros
LETTERS, DIGITS = ascii_letters + "_", digits
TYPES = ["int", "char", "bool", "float", "double"]

def automato(entrie: list[str]):
  if entrie[0] not in TYPES: return False             # Se a primeira palavra não for um tipo, retorna falso
  for word in entrie[1:]:                             # Pega o resto da string
    if word[0] not in LETTERS: return False           # Se a primeira não for uma letra do alfabeto, retorna falso
    if word[-1] not in [",", ";"]: return False       # Se o final da palavra não tiver , ou ; retorna falso
    for letter in word[1:-1]:                         # Pega o resto da palavra
      if letter not in LETTERS + DIGITS: return False # Se o resto da palavra não tiver somente letras e digitos, retorna falso
  return True                                         # Caso a string esteja dentro dos conformes, retorna verdadeiro

#Tipos de dados aceitos: "int", "char", "bool", "float", "double";
for x in range( 0, 7):
  entrie = input("Digite um dos dados de entrada da lista: ").split( )
  automato( entrie )
  print(f"Aceita: {automato(entrie)}")
