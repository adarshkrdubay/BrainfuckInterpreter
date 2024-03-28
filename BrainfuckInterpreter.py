import argparse

class BrainfuckInterpreter:
    def __init__(self):
        # Initialize memory tape with 30,000 cells, pointer, and instruction pointer
        self.memory = [0] * 30000
        self.pointer = 0
        self.instruction_pointer = 0
        self.input_buffer = []  # Buffer for input characters
        self.output_buffer = []  # Buffer for output characters

    def execute(self, code=None, input_text=None):
        # If no code is provided, return an error message
        if code is None:
            return "No Brainfuck code provided."

        # If input text is provided, store it in the input buffer
        if input_text:
            self.input_buffer = list(input_text)

        # Reset memory, pointers, and output buffer
        self.memory = [0] * 30000
        self.pointer = 0
        self.instruction_pointer = 0
        self.output_buffer = []

        # Execute the Brainfuck code
        while self.instruction_pointer < len(code):
            command = code[self.instruction_pointer]

            # Brainfuck commands implementation
            if command == '>':
                self.pointer += 1
            elif command == '<':
                self.pointer -= 1
            elif command == '+':
                self.memory[self.pointer] = (self.memory[self.pointer] + 1) % 256
            elif command == '-':
                self.memory[self.pointer] = (self.memory[self.pointer] - 1) % 256
            elif command == '.':
                self.output_buffer.append(chr(self.memory[self.pointer]))
            elif command == ',':
                if self.input_buffer:
                    self.memory[self.pointer] = ord(self.input_buffer.pop(0))
                else:
                    self.memory[self.pointer] = 0
            elif command == '[':
                # Handle loops
                if self.memory[self.pointer] == 0:
                    loop_depth = 1
                    while loop_depth != 0:
                        self.instruction_pointer += 1
                        if code[self.instruction_pointer] == '[':
                            loop_depth += 1
                        elif code[self.instruction_pointer] == ']':
                            loop_depth -= 1
            elif command == ']':
                # Handle loops
                loop_depth = 1
                while loop_depth != 0:
                    self.instruction_pointer -= 1
                    if code[self.instruction_pointer] == '[':
                        loop_depth -= 1
                    elif code[self.instruction_pointer] == ']':
                        loop_depth += 1
                self.instruction_pointer -= 1

            # Move to the next instruction
            self.instruction_pointer += 1

        # Return the output as a string
        return ''.join(self.output_buffer)

if __name__ == "__main__":
    # Command line arguments parsing
    parser = argparse.ArgumentParser(description='Brainfuck Interpreter')
    parser.add_argument('-f', '--file', help='Path to Brainfuck code file')
    parser.add_argument('-t', '--text', help='Input text for the Brainfuck program')
    args = parser.parse_args()

    # Initialize the interpreter
    interpreter = BrainfuckInterpreter()

    # Read Brainfuck code from file or use provided text
    if args.file:
        with open(args.file, 'r') as file:
            code = file.read()
    elif args.text:
            code = args.text
    else:
        code = ""

    # Execute the Brainfuck code with provided input text
    output = interpreter.execute(code, input_text="")
    
    # Print the output
    if output:
        print("Output:", output)
