from sly import Lexer

class LexerAnalyzer(Lexer):
    # Set of token names. This is always required 
    tokens = { AND, ASSIGN, COLON, DIVIDE, DOT, EQUAL, ID, LBRACE, LBRACK, 
        LESS, LPAREN, MINUS, NOT, NUMBER, PLUS, RBRACK, RBRACE, RPAREN, SCOLON, TIMES, 
        BOOLEAN, CLASS, ELSE, EXTENDS, FALSE, IF, INT, LENGTH, MAIN, NEW, 
        PUBLIC, RETURN, STATIC, STRING, WRITE, THIS, TRUE, VOID, WHILE, WRITE }

    # String containing ignored characters between tokens
    ignore = ' \t\n'
    ignore_comment = '\/\/.*'
    ignore_block_comment = '\/\*[^\*\/]+\*\/'

    # Regular expression rules for tokens in Priority order
    ID      = r'[a-zA-Z_][a-zA-Z0-9_]*'
    NUMBER  = r'\d+'
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
    EQUAL   = r'=='
    ASSIGN  = r'='
    NOT     = r'!'
    LESS    = r'<'
    AND     = r'&&'

    # Words reserved
    ID['class']     = CLASS
    ID['public']    = PUBLIC
    ID['static']    = STATIC
    ID['void']      = VOID
    ID['main']      = MAIN
    ID['String']    = STRING

    ID['extends']   = EXTENDS
    ID['return']    = RETURN

    ID['if']        = IF
    ID['else']      = ELSE
    ID['while']     = WHILE

    ID['true']      = TRUE
    ID['false']     = FALSE

    ID['this']      = THIS
    ID['new']       = NEW

    ID['int']       = INT
    ID['boolean']   = BOOLEAN

    ID['length']    = LENGTH

    ID['System.out.println']    = WRITE


    # Line number tracking
    @_(r'\n+')
    def ignore_newline(self, t):
        self.lineno += t.value.count('\n')


if __name__ == '__main__':
#    data = input('lex > ') 
    # open file named data.in in read mode
    file = open('data.in', 'r')
    data = file.read()
    # print(data)

    lexer = LexerAnalyzer()
    for tok in lexer.tokenize(data):     
        print('type=%r, value=%r lineno=%r index=%r' % (tok.type, tok.value, tok.lineno, tok.index))
    file.close()
