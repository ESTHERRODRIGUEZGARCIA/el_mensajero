import sys

def execute_brainfuck(code):
    tape = [0] * 30000
    ptr = 0
    output = []
    loop_stack = []
    i = 0

    while i < len(code):
        command = code[i]
        if command == '>':
            ptr += 1
        elif command == '<':
            ptr -= 1
        elif command == '+':
            tape[ptr] = (tape[ptr] + 1) % 256
        elif command == '-':
            tape[ptr] = (tape[ptr] - 1) % 256
        elif command == '.':
            output.append(chr(tape[ptr]))
        elif command == '[':
            if tape[ptr] == 0:
                depth = 1
                while depth > 0:
                    i += 1
                    if code[i] == '[':
                        depth += 1
                    elif code[i] == ']':
                        depth -= 1
            else:
                loop_stack.append(i)
        elif command == ']':
            if tape[ptr] != 0:
                i = loop_stack[-1]
            else:
                loop_stack.pop()
        i += 1

    return ''.join(output)

if __name__ == "__main__":
    with open('brainfuck_limpio.txt', 'r') as file:
        code = file.read().strip()
    print(execute_brainfuck(code))
