# importa a classe Lexer da biblioteca sly
from sly import Lexer

class LexerAnalyzer(Lexer):
    # tokens por ORDEM ALFABETICA
    tokens = { AND, BOOLEAN, CLASS, COLON, DOT, ELSE, EQUAL, EXTENDS, FALSE, ID, IF, INT, KEYWORD, LENGTH, 
        MAIN, NEW, LBRACE, LBRACK, LESS, LPAREN, MINUS,  NEW, NOT, NUM, OUT, PLUS, PRINTLN, PUBLIC, RBRACK, RETURN, 
        RBRACE, RPAREN, SCOLON, STATIC, STRING, SYSTEM, THIS, TIMES, TRUE, VOID, WHILE, WRITE }

    # keywords por ORDEM ALFABETICA
    keywords = { BOOLEAN, CLASS, ELSE, EXTENDS, FALSE, IF, INT, LENGTH, MAIN, NEW, OUT, PRINTLN, PUBLIC, RETURN, STATIC, 
        STRING, SYSTEM, THIS, TRUE, VOID, WHILE }

    # espaço, tabulação, comentário e bloco de comentários ignorados
    ignore = ' \t'
    ignore_comment = '\/\/.*'
    ignore_block_comment = '\/\*[^\*\/]+\*\/'

    # átomos que representam as palavras reservadas da linguagem por ORDEM ALFABETICA
    ID['boolean']   = BOOLEAN
    ID['class']     = CLASS
    ID['else']      = ELSE
    ID['extends']   = EXTENDS
    ID['false']     = FALSE
    ID['if']        = IF
    ID['int']       = INT
    ID['length']    = LENGTH
    ID['main']      = MAIN
    ID['new']       = NEW
    ID['out']       = OUT
    ID['println']   = PRINTLN
    ID['public']    = PUBLIC
    ID['return']    = RETURN
    ID['static']    = STATIC
    ID['String']    = STRING
    ID['System']    = SYSTEM
    ID['this']      = THIS
    ID['true']      = TRUE
    ID['void']      = VOID
    ID['while']     = WHILE

    # átomos que representam símbolos da linguagem por ORDEM ALFABETICA
    AND     = r'\&\&'
    COLON   = r'\,'
    DOT     = r'\.'
    EQUAL   = r'\='
    LBRACE  = r'\{' 
    LBRACK  = r'\['
    LESS    = r'\<' 
    LPAREN  = r'\('
    MINUS   = r'\-'
    NOT     = r'\!'
    PLUS    = r'\+'
    RBRACE  = r'\}'
    RBRACK  = r'\]'
    RPAREN  = r'\)'
    SCOLON  = r'\;'
    TIMES   = r'\*'

    # átomos com regras de formação complexa
    ID	= r'[a-zA-Z_][a-zA-Z0-9_]*'
    NUM	= r'\d+'

    # a cada quebra de linha o identificador do número de linha é incrementado
    @_(r'\n+')
    def ignore_newline(self, t):
        self.lineno += t.value.count('\n')

    # imprime a linha e o caractere inválido caso encontre
    def error(self, t):
        print('Linha: %d - Caractere ilegal: "%s"' % (self.lineno, t.value[0]))
        self.index += 1

if __name__ == '__main__':
    try:
        # solicita ao usuário o nome do arquivo de entrada e abre no modo somente leitura
        file = open(input('Informe o nome do arquivo de entrada: '), 'r')
        # tokenize() é um método público da classe Lexer que quebra o texto do arquivo informado em palavras e imprime conforme o analisador lexico implementado
        for tok in LexerAnalyzer().tokenize(file.read()):            
            tipo = tok.type
            # se o token estiver na lista de keywords, entao recebe uma string informando que é uma keyword
            if tok.type in LexerAnalyzer().keywords:
                tipo = 'KEYWORD'
            print('[ %s, %s, "%s" ]' % (tok.lineno, tipo, tok.value))
        # fecha o arquivo de entrada
        file.close()    
    except EOFError:
        pass