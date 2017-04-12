from vm import VM


obj = VM()


def vm_mul_test():
    global obj
    bytecode = {
        'instructions': [
            ('PUSH_VALUE', 1),
            ('PUSH_VALUE', 2),
            ('MULTIPLY', None),
            ('PUSH_VALUE', 3),
            ('PUSH_VALUE', 4),
            ('MULTIPLY', None),
            ('GET_RESULT', None)
        ],

        'values': [0, 1, 2, 3, 4, ]
    }

    print("Running multiplication test 1*2*3*4", end=" ")

    obj.run_it(bytecode)


def vm_add_test():
    global obj
    bytecode = {
        'instructions': [
            ('PUSH_VALUE', 0),
            ('PUSH_VALUE', 1),
            ('PUSH_VALUE', 2),
            ('GET_RESULT', None)
        ],

        'values': [5, 5, 10]
    }

    print('Running test for VM addition on 5+5+10', end=" ")
    obj.run_it(bytecode)


def vm_div_test():
    global obj
    bytecode = {
        'instructions': [
            ('PUSH_VALUE', 0),
            ('PUSH_VALUE', 1),
            ('DIVIDE', None),
            ('GET_RESULT', None)
        ],
        'values': [15, 5]
    }

    print("Running divide test 15/5", end=" ")
    obj.run_it(bytecode)


def vm_sub_test():
    global obj

    bytecode = {
        'instructions': [
            ('PUSH_VALUE', 0),
            ('PUSH_VALUE', 1),
            ('SUBSTRACT', None),
            ('GET_RESULT', None),
        ],

        'values': [10, 5],
    }

    print('Running test for substraction for 10-5', end=" ")
    obj.run_it(bytecode)


if __name__ == '__main__':
    vm_add_test()
    vm_sub_test()
    vm_mul_test()
    vm_div_test()
