from sly import Lexer

class LexerAnalyzer(Lexer):
    # Set of token names. This is always required 
    tokens = { ID, AND, ASSIGN, COLON, DIVIDE, DOT, EQUAL, LBRACE, LBRACK, 
        LESS, LPAREN, MINUS, NOT, NUMBER, PLUS, RBRACK, RBRACE, 
        RPAREN, SCOLON, TIMES, 
        BOOLEAN, CLASS, ELSE, EXTENDS, FALSE, IF, INT, LENGTH, MAIN, NEW, MAIN, 
        NEW, PUBLIC, RETURN, STATIC, STRING, WRITE, THIS, TRUE, VOID, WHILE, WRITE }

    # COMMENT, LCOMMENTBLOCK, RCOMMENTBLOCK,
    
    # String containing ignored characters between tokens
    ignore = r' \t\n'    
    ignore_comment = r'\/\/.*'
    ignore_block_comment = r'\/\*[^\*\/]+\*\/'

    # Regular expression rules for tokens in Priority order
    ID      = r'[a-zA-Z_][a-zA-Z0-9_]*'
    NUMBER  = r'\d+'
    DOT     = r'\.'
    COLON   = r','
    SCOLON  = r';'  
    # COMMENT = r'\/\/'       # //
    # LCOMMENTBLOCK = r'\/\*' # /*
    # RCOMMENTBLOCK = r'\*\/' # *\
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

    # Words reserved in Alphabetical order by type
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
    ID['string']    = STRING
    ID['this']      = THIS
    ID['true']      = TRUE
    ID['void']      = VOID
    ID['while']     = WHILE
    ID['System.out.println']    = WRITE

    # Line number tracking
    @_(r'\n+')
    def ignore_newline(self, t):
        self.lineno += t.value.count('\n')


if __name__ == '__main__':
#    data = input('lex > ') 
    # open archive named data.in in read mode
    archive = open('data.in', 'r')
    data = archive.read()
    # print(data)

    lexer = LexerAnalyzer()
    for tok in lexer.tokenize(data):     
        print('type=%r, value=%r lineno=%r index=%r' % (tok.type, tok.value, tok.lineno, tok.index))
    archive.close()
