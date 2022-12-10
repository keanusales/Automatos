from os import system
from string import ascii_letters, digits

LETTERS = "_" + ascii_letters
LDIGITS = LETTERS + digits
TYPES = ["int", "char", "bool", "float", "double"]

def autômato(entrie: str):
  def autômato(entrie: str):
    INICIO, FINAL = 1, 3
    def autômato(state: int, word: str):
      if state == 1 and word in LETTERS: return 2
      if state == 2 and word == ",": return 1
      if state == 2 and word in LDIGITS: return 2
      if state == 2 and word == ";": return 3
      return 0
    state = INICIO
    for word in entrie:
      state = autômato(state, word)
    return True if state == FINAL else False
  conver = entrie.split()
  conver = conver[0], "".join(conver[1:])
  return conver[0] in TYPES and autômato(conver[1])

def boolean(entrie: bool):
  return "aceito" if entrie else "recusado"

system("cls||clear")

#Tipos de dados aceitos: "int", "char", "bool", "float", "double";
for x in range( 0, 6):
  resul = autômato(input("Entrada: "))
  print(f"O conteúdo foi {boolean(resul)}!")
