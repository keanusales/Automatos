from os import system
from string import ascii_letters, digits

LETTERS = "_" + ascii_letters
LDIGITS = LETTERS + digits
TYPES = ["int", "char", "bool", "float", "double"]

def process(entrie: str):
  convert = entrie.split()
  return convert[0], "".join(convert[1:])

def automato(entrie: tuple[str, str]):
  def automato(entrie: str):
    def automato(state: int, word: str):
      if state == 1 and word in LETTERS: return 2
      if state == 2 and word == ",": return 1
      if state == 2 and word in LDIGITS: return 2
      if state == 2 and word == ";": return 3
      return 0
    state = 1 # O estado inicial é 1
    for word in entrie:
      state = automato(state, word)
    return True if state == 3 else False
  return entrie[0] in TYPES and automato(entrie[1])

def boolean(entrie: bool):
  return "aceito" if entrie else "recusado"

system("cls||clear")
resul = automato(process(input("Entrada: ")))
print(f"O conteúdo foi {boolean(resul)}!")