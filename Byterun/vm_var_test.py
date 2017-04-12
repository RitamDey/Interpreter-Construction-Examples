from vm import VM

obj = VM()

def book_test():
    global obj

    bytecode = {
        'instructions': [
            ("PUSH_VALUE", 0),
            ("STORE_NAME", 0),
            ("PUSH_VALUE", 1),
            ("STORE_NAME", 1),
            ("LOAD_NAME", 0),
            ("LOAD_NAME", 1),
            ("ADD", None),
            ("GET_RESULT", None)
        ],

        'values': [0, 1, 2, 3, 4, ],
        'names': ['a', 'b']
    }

    obj.run_it(bytecode)

if __name__ == "__main__":
    book_test()