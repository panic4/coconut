# Coconut

## Installation

First, make sure you have [Python 3](https://www.python.org/) installed, then clone the repository locally. If you don't know what that means, click the green "<>Code" button near the top of this page, click "Download ZIP", then extract the ZIP file anywhere you'd like.

## Usage
First, make sure Python 3 is in your PATH. If you don't know what that is or how to do it, there's a handy guide [here](https://realpython.com/add-python-to-path/).

Next, open your terminal or command prompt in the directory you cloned in the Installation step.

To run the interpreter, type:
```sh
python coconut.py file_name_here.cn
```
There's also a demo text-based game, island.cn, included with the Coconut interpreter. Feel free to look over it to better understand Coconut's syntax.

## Syntax
### The Registers
🍌, 🧃, 🥑, and 🩳 are the register emojis. To store a value in a register, call one of the emojis followed by the value you wish to store. For example:
```python
🍌'War Eagle!'
```
The above code stores the string "War Eagle!" into register 🍌. Operators in Coconut only accept registers; all data must be placed in a register before it can be operated on.

### Arithmetic Operators
 
🍇 (addition), 🍓 (subtraction), 🍊 (multiplication), and 🍒 (division) are the arithmetic operator emojis. Each of them evaluate and operate on the two registers declared after them, and store them in the third register declared. For example:

```python
🍌3
🥑2
🍓🍌🥑🍌
```

Reads the values stored in 🍌 and 🥑, subtracts the value stored in 🥑 from the one in 🍌, and stores the output (1) in 🍌.

### Logical Operators
🥭 (AND), 🍹 (OR), and 🍍 (NOT) are the logical operators. Most accept two registers with true/false values, perform their respective operations, and store the output in the third register. 🍍 is special, it accepts one register as argument, and inverts it (true=false and false=true).

### Comparative Operators

🍈 (is-equal), 🤿 (greater-than), and 🏝 (less-than) are all comparative operators. They function identically to logical operators, but they accept two non-true/false inputs and give a true/false output.

### Print

🎣 is the printing function. It prints the value of the register following it.

### Input

🌈 is the input function. It prompts the user to input any piece of data and stores it in the register following it.

### Control Structures
🍉 is the if-statement keyword. 🍉 evaluates the register after it for a true/false value. If it's false, it skips lines until it reaches a 🍉 with *no* register after it.

🌸 is the go-to keyword. 🌸 skips to the line number stored in the register after it.

## License

[MIT](https://choosealicense.com/licenses/mit/)
