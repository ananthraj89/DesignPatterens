'''
THe interpreter pattern helps to convert information from one language to other.
The language can be of anything, such as words in a sentence, numerical formulas or even a software code.
The process to convert the source information, into an Abstract Syntax tree(AST) of terminal and Non-terminal expressions that
all implement an interpret() method.

A non terminal expression is a combination of other non-terminal and/or terminal expression.
Terminal means terminated, i.e, there is no further processing involved.

An AST root starts with a Non-Terminal expression and then resolves down each branch until all expressions
terminates.

example: Expression A+B
The A and B are the terminal expressions and the + is Non-terminal because it depends on the two
other terminal expressions

Terminology: Abstract expression: Describe the method(s) that terminal and non terminal expressions should implement
NOn-Terminal expression: A composite of terminal and/or Non-terminal expressions.
Terminal Expression: A leaf node expression
Context: Context is a stste that can be passed through intrepet operations if necessary.
Client: Builds or is given an Abstract Syntax Tree to Intrepret or in a simple words A MotherFucker
who is a fucking idiot and wants us to work with less pay.

'''

class AbstractExpression():
    'All terminal and Non-terminal expressions will be implemnt an interpret method'
    @staticmethod
    def interpret():
        'This method gets called recursively for each AbstractExpression'

class Number(AbstractExpression):
    'Terminal Expression'
    def __init__(self, value):
        self.value = int(value)

    def interpret(self):
        return self.value

    def __repr__(self):
        return  str(self.value)

class Add(AbstractExpression):
    'A Non terminal Expression'
    def __init__(self,left,right):
        self.left = left
        self.right = right

    def interpret(self):
        return f"({self.left} + {self.right})"

class Substract(AbstractExpression):
    'A Non terminal expression'
    def __init__(self, left,right):
        self.left = left
        self.right = right

    def interpret(self):
        return self.left.interpret() - self.right.interpret()

    def __repr__(self):
        return f"({self.left} Substract {self.right})"

#THE CLIENT

SENTENCE = "5+4-3+7-2"
print(SENTENCE)

TOKENS = SENTENCE.split(" ")
print(TOKENS)

'''AST: list[AbstractExpression] = []
AST.append(Add(Number(TOKENS[0]), Number(TOKENS[2])))
AST.append(Substract(AST[0], Number(TOKENS[4])))
AST.append(Add(AST[1], Number(TOKENS[6])))
AST.append(Substract(AST[2], Number(TOKENS[8])))

AST_ROOT = AST.pop()

print(AST_ROOT.interpret())

print(AST_ROOT)
'''
