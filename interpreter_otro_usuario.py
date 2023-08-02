from ast import parse, Expr, Assign, BinOp, Name, Num
from operator import add, sub, mul, mod, truediv


class Interpreter:

    def __init__(self):
        self.vars = {}

    def input(self, expression):

        op = {'Sub': sub, 'Add': add, 'Mult': mul, 'Div': truediv, 'Mod': mod}

        def _eval(node):

            if isinstance(node, Expr):
                return _eval(node.value)
            if isinstance(node, Name):
                return self.vars[node.id]
            if isinstance(node, Num):
                return node.n
            if isinstance(node, BinOp):
                return op[type(node.op).__name__](_eval(node.left), _eval(node.right))
            if isinstance(node, Assign):
                name = node.targets[0].id
                self.vars[name] = _eval(node.value)
                return self.vars[name]

        tree = parse(expression)
        return _eval(tree.body[0]) if len(tree.body) else ''
    
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
    