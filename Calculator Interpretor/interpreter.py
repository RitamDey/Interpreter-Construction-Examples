"""
* Token types
* EOF (End-Of-File) token is used to indicate that there is no more input left for 
* lexical analysis
"""


INTEGER, PLUS, EOF = 'INTEGER', 'PLUS', 'EOF'


class Token:
    def __init__(self, token_type, value):
        # token type: INTEGER, PLUS or EOF
        self.type = token_type
        # token value: 0 to 9 and '+' or None
        self.value = value

    def __str__(self):
        """
        String representation of the class
        
        Examples:
            Token(INTEGER, 3)
            Token(PLUS, '+')
        """
        return f"Token({self.type}, {self.value.__repr__()})"
    
    def __repr__(self):
        return self.__str__()


class Interpreter:
    def __init__(self, text):
        # client input string, eg: "3+5"
        self.text = text
        # self.pos is an index into self.text
        self.pos = 0
        # current token instane
        self.current_token = None
    
    def error(self, error_type=Exception, msg='Error parsing input'):
        raise error_type(msg)
    
    def get_next_token(self):
        """
        * Lexical analyzer (also known as scanner or tokenizer)
        * This method is responsible for breaking a sentence
        * apart into tokens. One token at a time.
        """

        text = self.text

        # is self.pos index past the end of the self.text ?
        # if so, then return EOF token because there is no more
        # input left to convert into tokens
        if self.pos > len(text) - 1:
            return Token(EOF, None)