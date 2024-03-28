# Brainfuck Interpreter

This is a Brainfuck interpreter implemented in Python. Brainfuck is an esoteric programming language known for its minimalism. It uses a simple set of commands to manipulate an array of memory cells.

## Usage

### Prerequisites

- Python 3.x

### Running the Interpreter

To run the interpreter, execute the following command in your terminal:

```
python brainfuck_interpreter.py [-h] [-f FILE] [-c CODE]

Options:

    -h, --help: Show the help message and exit.
    -f FILE, --file FILE: Path to a file containing Brainfuck code.
    -c CODE, --code CODE: Brainfuck code directly provided as input.
```
Example Usage:
Run Brainfuck code from a file:
```
python brainfuck_interpreter.py -f example.bf
```
Provide Brainfuck code directly:
```
python brainfuck_interpreter.py -c "++++++++[>++++[>++>+++>+++>+<<<<-]>+>+>->>+[<]<-]>>.>---.+++++++..+++.>>.<-.<.+++.------.--------.>>+.>++."
```
Implementation Details

    The interpreter initializes a memory tape with 30,000 cells, a pointer, and an instruction pointer.
    It supports the basic Brainfuck commands: >, <, +, -, ., ,, [, ].
    Input can be provided either from a file or directly as text.
    Output is printed to the console.

Class: BrainfuckInterpreter

    __init__(): Initializes the interpreter with memory, pointer, and buffer variables.
    execute(code): Executes the provided Brainfuck code.

Command Line Arguments

    -f, --file: Path to a file containing Brainfuck code.
    -c, --code: Brainfuck code directly provided as input.

License

This project is licensed under the MIT License - see the LICENSE file for details.
