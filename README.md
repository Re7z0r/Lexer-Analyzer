# LexerAnalyzer-MiniJava
Desenvolvimento de um Analisador Léxico em Python com SLY para a linguagem MiniJava.

## 1. Especificações do Analisador Léxico
1.1. <b>Gramática:</b> baseia-se no Manual de Referência da linguagem MiniJava, "Modern Compiler Implementation in Java", páginas 484-486, Appel e Palsberg's).
http://www.cs.tufts.edu/~sguyer/classes/comp181-2006/minijava.html

1.1. <b>Entrada:</b> consiste de um arquivo informado pelo usuário, contendo o código fonte a ser processado pelo analisador léxico.

1.2. <b>Saída:</b> segue o seguinte padrão estabelecido: 
```bash
[ <número_da_linha>, <átomo_reconhecido>, <lexema_correspondente> ]
```

Em caso de caractere ilegal: 
```bash
Linha: <número_da_linha> - Caractere ilegal: <fluxo_correspondente>
```

## 2. Instalação passo a passo (Linux)
2.1 Instalando o python3
```bash
    sudo apt-get update
    sudo apt-get install python3
```
2.2 Instalando o pacote pip
```bash
    sudo apt-get install python3-pip
```
2.3 Instalando o SLY
```bash
    pip3 install sly 
```    

## 3. Execução
```bash
    python3 main.py
```
