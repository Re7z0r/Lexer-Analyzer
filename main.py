from sly import Lexer

class LexerAnalyzer(Lexer):
    # Set of token names. This is always required 
    tokens = { ID, NUMBER, PLUS, MINUS, TIMES,
               DIVIDE, ASSIGN, LPAREN, RPAREN, SCOLON,
               LBRACK, RBRACK, LBRACE, RBRACE, COLON,
               EQUAL, AND, LESS, DOT, NOT }
    
    # String containing ignored characters between tokens
    ignore = ' \t\n'
    
    # Regular expression rules for tokens
    ID      = r'[a-zA-Z_][a-zA-Z0-9_]*'
    NUMBER  = r'\d+'
    PLUS    = r'\+'
    MINUS   = r'-'
    TIMES   = r'\*'
    DIVIDE  = r'/'
    ASSIGN  = r'='
    LPAREN  = r'\('
    RPAREN  = r'\)'
    SCOLON  = r';'
    
    LBRACK = r'\['
    RBRACK = r'\]'
    LBRACE = r'\{'
    RBRACE = r'\}'
    COLON = r','
    EQUAL = r'='
    AND = r'&&'
    LESS = r'<'
    DOT = r'.'
    NOT = r'!'

if __name__ == '__main__':
#    data = input('lex > ') 
    arquivo = open('data.in', 'r')
    data = arquivo.read()
    print(data)

    lexer = LexerAnalyzer()
    for tok in lexer.tokenize(data):
        print('type=%r, value=%r lineno=%r index=%r' % (tok.type, tok.value, tok.lineno, tok.index))
    arquivo.close()