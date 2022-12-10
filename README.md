# Implementação de um AFD para Processar Tipos e Nomes de Variáveis

![linguagem utilizada](https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue)

### Automato tipo_variavel nome_variavel;
<img src="https://user-images.githubusercontent.com/106454449/206871619-66742cb6-2784-405d-9f43-7bd0b06d6fec.png" alt="automato nome variavel">

> O automato aceita os tipos de dados: "int", "char", "bool", "float", "double"; retorna true se aceito e false se recusado, optamos por utilizar uma estrutura para armazenar esses dados primitivos.
---
#### Descrição
> É verificado se os nomes variáveis estão dentro do que foi proposto; implementação voltada para tratar os tipos primitivos da linguagem C++.
  - Se os nomes das variáveis tem letras minúsculas e maiúsculas, números e underscore
(“_”);
 - Se os nomes começam com letras ou “_”;
 - se os nomes não contém caracteres especiais como !, #, %, etc;
 - aceita dados seguindo essa estrutura: tipo_variavel nome_variavel_1, nome_variavel_2,(...).

## 💻 Pré-requisitos

Antes de começar, verifique se você atendeu aos seguintes requisitos:
* Você instalou a versão mais recente de `<python>`
* Você tem uma máquina `<Windows / Linux / Mac>`. O projeto foi testado, exclusivamente, nos sistemas Windows e Linux;

## 🚀 Instalando: Implementação de um AFD para Processar Tipos e Nomes de Variáveis
O projeto não precisa de nenhuma pré instalação, basta realizar as devidas importações:
```
from os import system
from itertools import product
from string import ascii_letters, digits
```

## ☕ Usando: Implementação de um AFD para Processar Tipos e Nomes de Variáveis

Para usar o projeto, siga estas etapas:

```
Atribua um dos tipos primitivos listados:
< "int", "char", "bool", "float", "double" >

Atribua um nome para a variável:
int age;
ou
int age, num;

```
## 🤝 Colaboradores

Agradecemos às seguintes pessoas que contribuíram para este projeto:

<table>
  <tr>
    <td align="center">
      <a href="https://github.com/keanusales" target="_blank">
        <img src="https://avatars.githubusercontent.com/u/100793959?v=4" width="100px;" alt="Foto doKeanu Sales"/><br>
        <sub>
          <b>Keanu Sales</b>
        </sub>
      </a>
    </td>
    <td align="center">
      <a href="https://github.com/ChrisTheDragon" target="_blank">
        <img src="https://avatars.githubusercontent.com/u/88001806?v=4" width="100px;" alt="Foto do Christian Marinho no github"/><br>
        <sub>
          <b>Christian Marinho</b>
        </sub>
      </a>
    </td>
    <td align="center">
      <a href="https://github.com/Julio-C-Oliveira">
        <img src="https://avatars.githubusercontent.com/u/103333573?v=4" width="100px;" alt="Foto do Julio"/><br>
        <sub>
          <b>Julio Oliveira</b>
        </sub>
      </a>
    </td>
    <td align="center">
      <a href="https://github.com/Jp0liveira">
        <img src="https://avatars.githubusercontent.com/u/106454449?v=4" width="100px;" alt="Foto do Joao Paulo Oliveira"/><br>
        <sub>
          <b>João Paulo</b>
        </sub>
      </a>
    </td>
  </tr>
</table>

[⬆ Voltar ao topo](#implementação-de-um-afd-para-processar-tipos-e-nomes-de-variáveis)<br>