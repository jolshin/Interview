
# Нужно реализовать класс Stack со следующими методами:
# is_empty — проверка стека на пустоту. Метод возвращает True или False;
# push — добавляет новый элемент на вершину стека. Метод ничего не возвращает;
# pop — удаляет верхний элемент стека. Стек изменяется. Метод возвращает верхний элемент стека;
# peek — возвращает верхний элемент стека, но не удаляет его. Стек не меняется;
# size — возвращает количество элементов в стеке.

# Используя стек из задания 1, решите задачу на проверку сбалансированности скобок. Сбалансированность скобок означает, 
# что каждый открывающий символ имеет соответствующий ему закрывающий, и пары скобок правильно вложены друг в друга.

# Пример сбалансированных последовательностей скобок:

# (((([{}]))))
# [([])((([[[]]])))]{()}
# {{[()]}}
# Несбалансированные последовательности:

# }{}
# {{[(])]}}
# [[{())}]
# Программа ожидает на вход строку со скобками. На выход сообщение: «Сбалансированно», если строка корректная, и «Несбалансированно», если строка составлена неверно.


class Stack:                                        
    def __init__(self):     
        self._index = []

    def size(self):
        return len(self._index)

    def is_empty(self):
        if self.size() == 0:
            return True
        else:
            return False

    #Extra method to skip unneccessary check for "balance" if string is odd
    def is_even(self):
        if (self.size() % 2) == 0:
            return True
        else:
            return False

    def push(self, item):
        self._index.insert(0, item)

    #Using method push defining method extend
    def extend(self, item):
        for i in item:
            self.push(i)

    def peek(self):
        if self.is_empty():
            raise Exception("Method peek() calls an empty stack.")
        return self._index[0]

    def pop(self, i=0):
        if self.is_empty():
            raise Exception("Method pop() calls an empty stack.")
        return self._index.pop(i)

    def __str__(self):
        return str(self._index)

#Method returns reflected brace pair
def brace_invertor(brace):
    _dict = {'(':')', '[':']', '{':'}', ')':'(', ']':'[', '}':'{'}
    return _dict[brace]

#Method checks if the brace is entered
def is_brace(brace):
    while True:
        try:
            brace_invertor(brace)
            return True
            break
        except KeyError:
            return False

#Method checks if the brace is an openenig
def brace_is_opener(brace):
    if is_brace(brace):
        _dict = {'(': True, '{': True, '[':True, ')':False, ']':False, '}':False}
        return _dict[brace]

#Main method to check for "balance"
def stack_checker(_stack):
    #default answer
    checker_res = "Сбалансировано"
    #auxilary dict for counting types of braces in a stack
    _dict = {'(':0, '[':0, '{':0}

    #if the stack is empty - returns 'empty line'
    if _stack.is_empty(): 
        checker_res = "Пустая строка"
        return checker_res

    #if the stack is not even - unbalanced
    if not _stack.is_even(): 
        checker_res = "Несбалансировано"
        return checker_res

    #"for" loop goes trough the stack, counts types of braces and assignens positive or negative sign if the brace is openning or closing
    #then updates values in auxilary dict with +1 or -1 for each type of braces
    #in case of balanced input there'd be '0' value for each key after loop
    for i in range(_stack.size()):      
        if is_brace(_stack.peek()): #if not brace - returns 'no braces'
            if brace_is_opener(_stack.peek()):
                _dict[_stack.peek()] = _dict[_stack.peek()] + 1
            else:
                _dict[brace_invertor(_stack.peek())] = _dict[brace_invertor(_stack.peek())] - 1
            _stack.pop()

        else:
            checker_res = "Не скобки"
            return checker_res
        #print(_dict)
        i += 1

    #checks for non-zero value
    for value in _dict.values():
        if value != 0:
            checker_res = "Несбалансировано"
    
    return checker_res



if __name__ == '__main__':

    _input = input("Введите строку, состояющую из скобок: ")
    _stack = Stack()
    _stack.extend(_input)
    print(f"Введена строка {str(_stack)}")
    print(stack_checker(_stack))
