""" 
Token types EOF (End-Of-File) token is used to indicate that there is no more input left for lexical analysis 
"""
from string import whitespace
import operator


INTEGER, OPERATOR, EOF = 'INTEGER', 'OPERATOR', 'EOF'


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

        # get a character at the position self.pos and decide
        # what token to create based on the single character
        current_char = text[self.pos]

        # See if the current character is a whitespace
        if current_char in whitespace:
            self.pos += 1
            return self.get_next_token()

        # if the character is a digit then convert it to
        # integer, create an INTEGER token, increment self.pos
        # index to point to the next character after the digit,
        # and return the INTEGER token
        if current_char.isdigit():
            num = 0
            while current_char.isdigit():
                num = num*10 + int(current_char)
                self.pos += 1
                try:
                    current_char = text[self.pos]
                except IndexError:
                    break
            token = Token(INTEGER, num)
            return token
        else:
            token = Token(OPERATOR, current_char)
            self.pos += 1

            if current_char == '+':
                self.op = operator.add

            elif current_char == '-':
                self.op = operator.sub

            elif current_char == '*':
                self.op = operator.mul

            elif current_char == '^':
                self.op = operator.pow

            else:
                self.op = operator.truediv

            return token

        self.error()

    def eat(self, token_type):
        # compare the current token type with the passed token
        # type and if they match then "eat" the current token
        # and assign the next token to the self.current_token,
        # otherwise raise an exception.

        if self.current_token.type == token_type:
            self.current_token = self.get_next_token()
            # print(self.current_token.type)
            # return self.current_token.type == token_type
        else:
            self.error(ValueError, "Mismatched tokens")

    def expr(self):
        # expr -> INTEGER PLUS INTEGER
        # set current token to the first token taken from the input

        self.current_token = self.get_next_token()

        # We expect the current token to be a single-digit integer
        left = self.current_token
        self.eat(INTEGER)

        # And now a PLUS
        op = self.current_token
        self.eat(OPERATOR)

        # and finally the second one
        right = self.current_token
        self.eat(INTEGER)

        # after the above call the self.current_token is set to EOF token

        # at this point INTEGER PLUS INTEGER sequence of tokens
        # has been successfully found and the method can just
        # return the result of adding two integers, thus
        # effectively interpreting client input
        result = self.op(left.value, right.value)
        return result


def main():
    while True:
        try:
            text = input("calc> ")
        except EOFError:
            print("Exiting...")
            break
        except KeyboardInterrupt:
            print("")
            continue
        if not text:
            continue

        interpreter = Interpreter(text)
        result = interpreter.expr()

        print(result)


if __name__ == '__main__':
    main()
