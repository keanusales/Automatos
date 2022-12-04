from string import ascii_letters, digits

LETTERS, DIGITS = ascii_letters + "_", digits
TYPES = ["int", "char", "bool", "float", "double"]

entrie = input("Entrada: ").split()

def automato(entrie: list[str]):
  if entrie[0] not in TYPES: return False
  for word in entrie[1:]:
    if word[0] not in LETTERS: return False
    if word[-1] not in [",", ";"]: return False
    for letter in word[1:-1]:
      if letter not in LETTERS + DIGITS: return False
  return True

print(f"Aceita: {automato(entrie)}")