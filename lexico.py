from sly import Lexer

class LexerAnalyzer(Lexer):
    # tokens por ORDEM ALFABETICA
    tokens = { AND, BOOLEAN, CLASS, COLON, DOT, ELSE, EQUAL, EXTENDS, FALSE, ID, IF, INT, KEYWORD, LENGTH, 
        MAIN, NEW, LBRACE, LBRACK, LESS, LPAREN, MINUS,  NEW, NOT, NUM, PLUS, PUBLIC, RBRACK, RETURN, 
        RBRACE, RPAREN, SCOLON, STATIC, STRING, THIS, TIMES, TRUE, VOID, WHILE, WRITE }

    # keywords por ORDEM ALFABETICA
    keywords = { BOOLEAN, CLASS, ELSE, EXTENDS, FALSE, IF, INT, LENGTH, MAIN, NEW, PUBLIC, RETURN, STATIC, 
        STRING, THIS, TRUE, VOID, WHILE }

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
    ID['public']    = PUBLIC
    ID['return']    = RETURN
    ID['static']    = STATIC
    ID['String']    = STRING
    ID['this']      = THIS
    ID['true']      = TRUE
    ID['void']      = VOID
    ID['while']     = WHILE    
    WRITE           = r'System\.out\.println'

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
    # solicita ao usuário o nome do arquivo de entrada e abre no modo somente leitura
    file = open(input('Informe o nome do arquivo de entrada: '), 'r')
    # quebra o texto do arquivo informado em palavras e imprime conforme o analisador lexico descrito no trabalho
    for tok in LexerAnalyzer().tokenize(file.read()):
        if tok.type in LexerAnalyzer().keywords:
            print('[ %s, KEYWORD, "%s" ]' % (tok.lineno, tok.value))
        else:
            print('[ %s, %s, "%s" ]' % (tok.lineno, tok.type, tok.value))
    # fecha o arquivo de entrada
    file.close()
