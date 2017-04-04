from collections import deque  # coz its faster than list for stacks


class VM:
    """
    * The main VM class.
    * Basically a stack-based VM
    """

    def __init__(self):
        # Initialize the stack
        self.stack = deque()
        # Initialize the environment
        self.env = {}

    def PUSH_VALUE(self, value):
        # Operation to push new values in stack
        self.stack.append(value)

    def ADD(self):
        # Operation to pop to values from stack and push the result
        n1 = self.stack.pop()
        n2 = self.stack.pop()
        self.stack.append(n1+n2)

    def SUBSTRACT(self):
        # Operation to pop two values fron stack and substract them
        # The order depends on the order of how they are pushed in the stack
        n1 = self.stack.pop()
        n2 = self.stack.pop()
        self.stack.append(n2-n1)

    def DIVIDE(self):
        n1 = self.stack.pop()
        n2 = self.stack.pop()
        try:
            res = n2/n1
        except ZeroDivisionError:
            res = 0
        self.stack.append(res)

    def MULTIPLY(self):
        n1 = self.stack.pop()
        n2 = self.stack.pop()
        self.stack.append(n1*n2)

    def GET_RESULT(self):
        # Get the result of the last operation
        print(self.stack.pop())
    
    def LOAD_NAME(self, name):
        val = self.env[name]
        self.stack.append(val)

    def STORE_NAME(self, name, value):
        val = self.stack.pop()
        self.env[name] = val
    
    def parse_argument(self, instruction, argument, what_to_execute):
        numbers = ["PUSH_VALUE", ]
        names = ["LOAD_NAME", "STORE_NAME"]

        if instruction in numbers:
            argument = what_to_execute["numbers"][argument]
        elif instruction in names:
            argument = what_to_execute["numbers"][argument]
        
        return argument

    def run_it(self, what_to_run):
        # Parses instructions and runs them in order

        # Get the instructions from bytecode passed
        instructions = what_to_run['instructions']

        # Get the values in the bytecode
        values = what_to_run["values"]

        # Loop over each instruction and process it
        for instruction in instructions:
            # Unpack the operation and arguments of the instruction
            op, arg = instruction
            argument = self.parse_argument(instruction, arg, what_to_run)

            # Use the python's dynamic attribute resolution to get method name
            method = getattr(self, op)

            if argument is None:
                method()
            else:
                method(argument)
