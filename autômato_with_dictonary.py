from string import ascii_letters, digits

LETTERS, DIGITS = ascii_letters + "_", digits
TYPES = ["int", "char", "bool", "float", "double"]

entrie = input("Entrada: ").split()

def automato(entrie: list[str]):
  def automato(entrie: str):
    if entrie[0] not in LETTERS: return False
    if entrie[-1] not in [",", ";"]: return False
    for letter in entrie[1:-1]:
      if letter not in LETTERS + DIGITS: return False
    return True
  
  dictdata = {}
  dictdata[entrie[0]] = (entrie[0] in TYPES)
  for word in entrie[1:]:
    dictdata[word[:-1]] = automato(word)
  
  return dictdata

for word, aceita in automato(entrie).items():
  print(f"{word} - Aceita: {aceita}")