from sly import Lexer

class LexerAnalyzer(Lexer):

    # Lista de variaveis para a lib Lex.
    tokens = { AND, COLON, DIVIDE, DOT, EQUAL, KEYWORD, ID, LBRACE, LBRACK, 
        LESS, LPAREN, MINUS, NOT, NUM, PLUS, RBRACK, RBRACE, RPAREN, SCOLON, TIMES, WRITE }

    # Expressões regulares do texto que deve ser ignorado
    ignore = r' \t\n'
    ignore_comment = r'\/\/.*'
    ignore_block_comment = r'\/\*[^\*\/]+\*\/'

    # Expressões regulares dos tokens na ordem de prioridade
    WRITE   = r'System\.out\.println'
    DOT     = r'\.'
    COLON   = r','
    SCOLON  = r';'
    LBRACE  = r'\{'  
    RBRACE  = r'\}'
    LBRACK  = r'\['
    RBRACK  = r'\]'
    LPAREN  = r'\('
    RPAREN  = r'\)'
    TIMES   = r'\*'
    DIVIDE  = r'/'
    PLUS    = r'\+'
    MINUS   = r'-'
    EQUAL   = r'='
    NOT     = r'!'
    LESS    = r'<'
    AND     = r'&&'
    ID      = r'[a-zA-Z_][a-zA-Z0-9_]*'
    NUM  = r'\d+'

    # Words reserved
    ID['class']     = KEYWORD
    ID['public']    = KEYWORD
    ID['static']    = KEYWORD
    ID['void']      = KEYWORD
    ID['main']      = KEYWORD
    ID['String']    = KEYWORD
    ID['extends']   = KEYWORD
    ID['return']    = KEYWORD
    ID['if']        = KEYWORD
    ID['else']      = KEYWORD
    ID['while']     = KEYWORD
    ID['true']      = KEYWORD
    ID['false']     = KEYWORD
    ID['this']      = KEYWORD
    ID['new']       = KEYWORD
    ID['int']       = KEYWORD
    ID['boolean']   = KEYWORD
    ID['length']    = KEYWORD

    # guarda numero da linha lida
    @_(r'\n+')
    def ignore_newline(self, t):
        self.lineno += t.value.count('\n')


    def t_error(self, t):
        print('[ %r ]' % (t.value))

if __name__ == '__main__':
    filename = input('arquivo de entrada > ') 
    # abre para leitura o arquivo informado
    file = open(filename, 'r')
    # inicia leitura do arquivo
    data = file.read()

    #instancia objeto da lib Lex
    o_libLex = LexerAnalyzer()

    # o_libLex.error = o_libLex.t_error

    # extrai tokens do arquivo
    for token in o_libLex.tokenize(data):     
        # imprime [ <número_da_linha>, <átomo_reconhecido>, <lexema_correspondente> ]
        print('[ %r, %r, %r ]' % (token.lineno, token.type, token.value))
        
    #fecha arquivo
    file.close()
