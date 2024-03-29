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
            '/': lambda a,b: int(a/b),
            '%': lambda a,b: int(a%b),
        }


    def _resultado_parentesis(self, expression):
        if len(expression) == 1: return expression
        
        print(expression)
        
        c = expression[0]
        i = 0
        while c.isdigit():
            i += 1
            c = expression[i]

        expression = expression.split(c)
        
        if len(expression) >= 2:
            return str(self.operators[c](int(expression[0]), int(expression[1])))
        else:
            return expression
    
    
    
    def _expresion_sin_parentesis(self, expression):
        expression = expression.replace(' ','')
        if '(' in expression:
            if expression.count('(') > 1:
                return expression[:expression.find('(')+1] + \
                    self._expresion_sin_parentesis(expression[expression.find('(')+1: expression.rfind(')') ]) + \
                    expression[expression.rfind(')'):]
            else:
                return expression[:expression.find('(')] + \
                    self._expresion_sin_parentesis(expression[expression.find('(')+1: expression.rfind(')') ]) + \
                    expression[expression.rfind(')')+1:]
        else:
            #return self._resultado_parentesis(expression)
            return self._resultado_prioridad(expression)


    def _resultado_prioridad_mas(self, expression):
        priority_expression = ''
        lista_suma = []
        if '+' in expression:
            for exp1 in expression.split('+'):
                exp1 = exp1.replace(' ','')
                if not exp1.isdigit():
                    lista_suma.append(self._resultado_parentesis(exp1))
                else:
                    lista_suma.append(exp1)
            expression = priority_expression + '+'.join(lista_suma)
        return expression

    def _resultado_prioridad_menos(self, expression):
        priority_expression = ''
        lista_resta = []
        if '-' in expression:
            for exp1 in expression.split('-'):
                exp1 = exp1.replace(' ','')
                if not exp1.isdigit():
                    lista_resta.append(self._resultado_parentesis(exp1))
                else:
                    lista_resta.append(exp1)
            expression = priority_expression + '-'.join(lista_resta)
        return expression


    def _resultado_prioridad(self, expression):
        asignar=''
        if '=' in expression:
            asignar, expression = expression.split('=')[0], expression.split('=')[1]
            asignar = f'{asignar}='
        
        expression = self._resultado_prioridad_mas(expression)
        expression = self._resultado_prioridad_menos(expression)
        expression = expression.replace(' ','')
        regex = re.compile("[-+*\/\%]+")
        tokens = [s for s in regex.findall(expression) if not s.isspace()]
        if len(tokens) == 1:
            expression = expression.split(tokens[0])
            valor_a = self.vars[expression[0]] if not expression[0].isdigit() else expression[0]
            valor_b = self.vars[expression[1]] if not expression[1].isdigit() else expression[1]
            return asignar + str(self.operators[tokens[0]](int(valor_a), int(valor_b)))
        
        return asignar + expression
    
    
    

    def input(self, expression):
        expression = expression.replace(' ','')
        regex = re.compile("[-+*\/\%]+")
        tokens = [s for s in regex.findall(expression) if not s.isspace()]
        if not tokens and expression.isdigit():
            raise Exception('deberia ir un operador')
        
        
        while '(' in expression:
            inicio = expression.find('(')+1
            fin = expression.find(')')
            subexp = expression[inicio:fin]
            if not '(' in subexp:
                nueva_exp = self._resultado_prioridad(subexp)
                expression = expression[:inicio-1] + nueva_exp + expression[fin+1:]
            else:
                expression = self._expresion_sin_parentesis(expression)
        
        expression = self._resultado_prioridad(expression)
        
        tokens = tokenize(expression)
        if not tokens: return ''
        resultado = 0
        
        
        while tokens:
            print(tokens, end=': ')
            if tokens[0].isdigit() and len(tokens) >= 3:
                if tokens[1] in self.operators.keys():
                    resultado = self.operators.get(tokens[1])(int(tokens[0]), int(tokens[2]))
                    tokens = tokens[3:]
                else:
                    raise Exception('deberia ir un operador')
            elif tokens[0].isalpha() and len(tokens) >= 3:
                if tokens[1] == '=':
                    if tokens[2].isdigit():
                        self.vars[tokens[0]] = int(tokens[2])
                    elif tokens[2] in self.vars.keys():
                        self.vars[tokens[0]] = self.vars[tokens[2]]
                    else:
                        raise Exception('no existe variable')
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
            
            elif len(tokens) == 1 and tokens[0].isdigit():
                resultado = int(tokens[0])
                tokens.pop()
            else:
                raise Exception('no existe variable')
        
        print(resultado)
        return resultado



if __name__ == '__main__':
        
    interpreter = Interpreter()
    
    """
    ecuacion2 = "(7 + 3) / (2 * 2 + 1)"
    print(ecuacion2)
    while '(' in ecuacion2:
        ecuacion2 = interpreter._expresion_sin_parentesis(ecuacion2)
    
    print(ecuacion2)
    """
    assert interpreter.input("(7 + 3) / (2 * 2 + 1)") == 2

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
    assert interpreter.input("4 / 2 * 3") ==  6
    # estas pruebas no funcionan aun
    assert interpreter.input('(10 / (8 - (4 + 2))) * 3') == 15
    assert interpreter.input('3 * ( 4 + 2 )') == 18
    assert interpreter.input('( 4 + 2 ) * 3') == 18
    assert interpreter.input('3 * ( 4 + 2 )') == 18
    assert interpreter.input("4 + 2 * 3") ==  10
    assert interpreter.input("(7 + 3) / (2 * 2 + 1)") == 2
    
    
    assert interpreter.input("(8 - (4 + 2)) * 3") == 6
    
    assert interpreter.input("y=x") == 1
    
    assert interpreter.input("y = x + 5") == 6
    
    assert interpreter.input("y") ==  6
    
    