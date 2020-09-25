# LexerAnalyzer-MiniJava
Desenvolvimento de um Analisador Léxico para a linguagem MiniJava.

## 1. Especificações do Analisador Léxico
- **Gramática:** baseia-se no [Manual de Referência da linguagem MiniJava], "Modern Compiler Implementation in Java", páginas 484-486, Appel e Palsberg's).

- **Entrada:** consiste de um arquivo informado pelo usuário, contendo o código fonte a ser processado pelo analisador léxico.

- **Saída:** especificação de como deve ser a saída do analisador léxico.
    - Segue o seguinte padrão estabelecido:
    *[ <número_da_linha>, <átomo_reconhecido>, <lexema_correspondente> ]*
    - Em caso de caractere ilegal:
    *Linha: <número_da_linha> - Caractere ilegal: <fluxo_correspondente>*

## 2. Instalação passo a passo (Linux)
- Instalação do [python3]
```bash
    sudo apt-get update
    sudo apt-get install python3
```
- Instalação do pacote [pip]
```bash
    sudo apt-get install python3-pip
```
- Instalação da biblioteca [sly]
```bash
    pip3 install sly 
```    

## 3. Execução
```bash
    python3 lexico.py
```


[//]: #https://github.com/Re7z0r/LexerAnalyzer-MiniJava
[Manual de Referência da linguagem MiniJava]: <http://www.cs.tufts.edu/~sguyer/classes/comp181-2006/minijava.html>
[python3]: <https://www.python.org/download/releases/3.0/>
[pip]: <https://pypi.org/project/pip/>
[sly]: <https://sly.readthedocs.io/en/latest/#>
