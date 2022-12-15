from os import system
from itertools import product
from string import ascii_letters, digits
from typing import List

LETTERS = "_" + ascii_letters
LDIGITS = LETTERS + digits
TYPES = ["int", "char", "bool", "float", "double"]

def verifyExclusives(entrie: List[str]):
  for type, elem in product(TYPES, entrie):
    if type in elem: return False
  return True

def autômato(entrie: str):
  everyword = []
  def autômato(entrie: List[str]):
    INICIO, INTER, FINAL = 1, 1, 3
    def autômato(state: int, word: str):
      if state == 1 and word in LETTERS: return 2
      if state == 2 and word == ",": return 1
      if state == 2 and word in LDIGITS: return 2
      if state == 2 and word == ";": return 3
      return 0
    state = INICIO
    for word in entrie[:-1]:
      for carac in word:
        state = autômato(state, carac)
      everyword.append((word[:-1], state == INTER))
    word = entrie[-1]
    for carac in word:
      state = autômato(state, carac)
    everyword.append((word[:-1], state == FINAL))
    return state == FINAL
  convert = entrie.split()
  convert = convert[0], convert[1:]
  resul = verifyExclusives(convert[1])
  resul = resul and convert[0] in TYPES
  resul = resul and autômato(convert[1])
  return resul, convert[0], everyword

def separationTypes(entrie: str):
  lista = entrie.split(";")
  return [f"{elem};" for elem in lista if elem != ""]

def boolean(entrie: bool):
  return "aceito(a)" if entrie else "recusado(a)"

system("cls||clear")
entrie = input("Entrada: ")
entrie = separationTypes(entrie)
resfinal = True
for elem in entrie:
  resul = autômato(elem)
  resfinal = resfinal and resul[0]
  print(f"\nO conteúdo foi {boolean(resul[0])}!")
  print(f"As variáveis são do tipo {resul[1]}.")
  for word in resul[2]:
    print(f"\"{word[0]}\" foi {boolean(word[1])}")
print(f"\nO resultado final é: {boolean(resfinal)}!")