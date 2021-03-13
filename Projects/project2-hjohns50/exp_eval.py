from stack_array import Stack

# You do not need to change this class
class PostfixFormatException(Exception):
    pass
#str -> int
#evaluate a postfix expression
def postfix_eval(input_str):
    '''Evaluates a postfix expression
    Input argument:  a string containing a postfix expression where tokens 
    are space separated.  Tokens are either operators + - * / ** >> << or numbers.
    Returns the result of the expression evaluation. 
    Raises an PostfixFormatException if the input is not well-formed
    DO NOT USE PYTHON'S EVAL FUNCTION!!!'''
    op_lst = ["+", "-", "*", "/", "**"] #list of operators
    val_lst =  input_str.split(" ") #list of individual tokens
    stack = Stack(len(input_str)) #stack to push and pop our values
    if input_str == "":
        return "" #basecase
    for i in val_lst: #loops throught the input string
        if i not in op_lst:
            try: #checks validity of tokens
                if i.isdigit():  #if i is a digit i is pushed on to stack
                    stack.push(int(i))
                else: #pushes it as float 
                    stack.push(float(i))
            except ValueError: #if cant't be casted as a float then its invalid
                raise PostfixFormatException("Invalid token")
        elif i in op_lst:
            try: #checks to see if theres enough values to do operation
                val2 = stack.pop()
                val1 = stack.pop()
            except IndexError: #if an index error is raised from the stack then theres not enough values
                raise PostfixFormatException("Insufficient operands")
            if i == "+":
                result = val1 + val2
                stack.push(result)
            if i == "-":
                result = val1 - val2
                stack.push(result)
            if i == "/":
                if val2 == 0:
                    raise ValueError("float division by 0")
                else:
                    result = val1 / val2
                    stack.push(result)
            if i == "*":
                result = val1 * val2
                stack.push(result)
            if i == "**" :
                result = val1 ** val2
                stack.push(result)
    if stack.size() == 1:
        return stack.pop()
    else: #if stack has more than one item left after iteration of val_Lst then too many operands 
        raise PostfixFormatException("Too many operands")



    

#str -> str
#convert a prefix expression to a postfix expression
def prefix_to_postfix(input_str):
    '''Converts a prefix expression to an equivalent postfix expression
    Input argument:  a string containing a prefix expression where tokens are 
    space separated.  Tokens are either operators + - * / ** >> << parentheses ( ) or numbers
    Returns a String containing a postfix expression(tokens are space separated)'''
    op_lst = ["+", "-", "*", "/", "**"] #list of operators
    val_lst =  input_str.split(" ") #list of individual tokens
    val_lst.reverse()
    stack = Stack(len(input_str)) #stack to push and pop our values
    if input_str == '':
        return ''
    for i in val_lst:
        if i not in op_lst:
            try: #checks validity of tokens
                a = float(i)   
                if str(abs(int(a))).isdigit():  #if i is a number i is pushed on to stack
                    stack.push(i)
            except ValueError: #if cant't be casted as a float then its invalid
                raise PostfixFormatException("Invalid token")
        elif i in op_lst:
            try: #checks to see if theres enough items to concatenate
                val1 = stack.pop()
                val2 = stack.pop()
            except IndexError: #if an index error is raised from the stack then theres not enough items
                raise PostfixFormatException("Invalid Prefix Expression")
            result = str(val1) + " " + str(val2) + " " + i
            stack.push(result)
    if stack.size() == 1:
        return str(stack.pop())
    else: #not enough operators 
        raise PostfixFormatException("Invalid Prefix Expression")