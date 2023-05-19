import re

def tokenize(expression):
    if expression == "":
        return []

    regex = re.compile("\s*(=>|[-+*\/\%=\(\)]|[A-Za-z_][A-Za-z0-9_]*|[0-9]*\.?[0-9]+)\s*")
    tokens = regex.findall(expression)
    return [s for s in tokens if not s.isspace()]

class Interpreter:
    def __init__(self):
        self.vars = {}
        self.functions = {}
        self.operators = {
            '+': lambda a,b: a+b,
            '-': lambda a,b: a-b,
            '*': lambda a,b: a*b,
            '/': lambda a,b: a/b,
            '%': lambda a,b: a%b,
        }

    def input(self, expression):
        tokens = tokenize(expression)
        if not tokens: return ''
        resultado = 0
        while tokens:
            print(tokens)
            if tokens[0].isdigit() and len(tokens) >= 3:
                if tokens[1] in self.operators.keys():
                    resultado = self.operators.get(tokens[1])(int(tokens[0]), int(tokens[2]))
                    tokens = tokens[3:]
                else:
                    raise Exception('deberia ir un operador')
            elif tokens[0].isalpha() and len(tokens) >= 3:
                if tokens[1] == '=':
                    self.vars[tokens[0]] = int(tokens[2])
                    resultado += self.vars[tokens[0]]
                else:
                    if tokens[0] in self.vars.keys():
                        resultado = self.operators.get(tokens[1])(self.vars.get(tokens[0]), int(tokens[2]))
                    else:
                        raise Exception('no existe variable')
                tokens = tokens[3:]
            elif tokens[0].isalpha() and len(tokens) == 1:
                if tokens[0] in self.vars.keys():
                        resultado = self.vars.get(tokens[0])
                else:
                        raise Exception('no existe variable')
                tokens = tokens[1:]
                
            elif not tokens[0].isalpha() and len(tokens) >= 2:
                if tokens[0] in self.operators.keys():
                        resultado = self.operators.get(tokens[0])(resultado, int(tokens[1]))
                else:
                        raise Exception('no existe variable')
                tokens = tokens[2:]
            
            else:
                raise Exception('no existe variable')
            
        return resultado


interpreter = Interpreter()

assert interpreter.input("1 + 1") == 2
assert interpreter.input("2 - 1") == 1
assert interpreter.input("2 * 3") == 6
assert interpreter.input("8 / 4") == 2
assert interpreter.input("7 % 4") == 3

# Variables
assert interpreter.input("x = 1") ==  1
assert interpreter.input("x") ==  1
assert interpreter.input("x + 3") ==  4

# pruebas mas grosas
# estas pruebas no funcionan aun
assert interpreter.input("4 / 2 * 3") ==  6
assert interpreter.input('(10 / (8 - (4 + 2))) * 3') == 15
assert interpreter.input("4 + 2 * 3") ==  10
assert interpreter.input('( 4 + 2 ) * 3') == 18
assert interpreter.input('3 * ( 4 + 2 )') == 18
assert interpreter.input('(10 / (8 - (4 + 2))) * 3') == 15

