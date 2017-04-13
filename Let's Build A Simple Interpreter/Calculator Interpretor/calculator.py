import operator
from re import findall
from collections import deque


INTEGER, OPERATOR, EOF = 'INTEGER', 'OPERATOR', 'EOF'


class Token:
    def __init__(self, token_type, value):
        # token type: INTEGER, PLUS or EOF
        self.type = token_type
        # token value: 0 to 9 and '+' or None
        self.value = value

    def __str__(self):
        return f"Token({self.type}, {self.value.__repr__()})"

    def __repr__(self):
        return self.__str__()

    def __eq__(self, other):
        if self.type == other:
            return True
        elif type(other) == Token and other.value == self.value:
            return True
        return False

    def __ne__(self, other):
        return not self.__eq__(other)


class Interpreter:
    def __init__(self):
        self.text = None
        self.pos = 0
        self.stack = deque()
        self.values = deque()

    def gen_token(self):
        try:
            char = self.text[self.pos]
        except:
            return Token(EOF, None)

        self.pos += 1

        try:
            return Token(INTEGER, float(char))
        except ValueError:
            if char == '+':
                return Token(OPERATOR, lambda x, y: x+y)
            elif char == '-':
                return Token(OPERATOR, lambda x, y: x-y)
            elif char == '*':
                return Token(OPERATOR, lambda x, y: x*y)
            elif char == '/':
                return Token(OPERATOR, lambda x, y: x/y)
            elif char == '^':
                return Token(OPERATOR, lambda x, y: x**y)
            else:
                raise ValueError(f'Unknown operator {char}.')

    def eval(self, statment):
        # Creates a list of the values and the opertion passed
        self.text = findall(r'[\.0-9]+|[\+\-\*\/\^]+', statment)
        result = None

        while True:
            token = self.gen_token()
            if token == EOF:
                break
            elif token == INTEGER:
                self.stack.append(token.value)
            elif token == OPERATOR:
                # Becuse of the structure of the interpreter the second operand
                # Is not present while the operation callback will be performed
                result = token.value(self.stack.pop(), self.gen_token().value)
                self.stack.append(result)
        return result


if __name__ == '__main__':
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
        interpreter = Interpreter()
        result = interpreter.eval(text)

        print(result)
