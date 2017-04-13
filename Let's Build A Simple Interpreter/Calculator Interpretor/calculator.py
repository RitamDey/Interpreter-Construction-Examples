import operator
from re import findall
from collections import deque


INTEGER, OPERATOR, EOF = 'INTEGER', 'OPERATOR', 'EOF'
OPERATORS = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv,
    '^': operator.pow,
}  # Opeartor dictionary. Copied from a StackOverflow post


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
        """
        Tokenizar for the interpreter. Converts a character to token one at a time
        """
        try:
            # Try to get the current character from list
            char = self.text[self.pos]
        except IndexError:
            # self.pos is pointing to a value out of the index of the list and
            # that means we have tokenized the entire list
            return Token(EOF, None)

        self.pos += 1  # Points to the next character in list to tokenize

        try:
            # Try to convert the char into a float, if it can be coverted
            return Token(INTEGER, float(char))
        except ValueError:
            # If we are here then it surely means that this character is not a number
            if char in OPERATORS.keys():
                return Token(OPERATOR, OPERATORS[char])
            else:
                # For sanity check
                raise ValueError(f'Unknown operator {char}.')

    def eval(self, statment):
        # Creates a list of the values and the opertion passed, its easier to evaluate
        self.text = findall(r'[\.0-9]+|[\+\-\*\/\^]+', statment)
        result = None  # Just a placeholder for result in method scope

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
