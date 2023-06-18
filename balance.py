class Stack:
    def __init__(self):
        self._sequence = []

    def is_empty(self) -> bool:
        if self._sequence:
            return False
        else:
            return True

    def push(self, element: str) -> None:
        self._sequence.append(element)

    def pop(self) -> str:
        return self._sequence.pop()

    def peek(self) -> str:
        return self._sequence[-1]

    def size(self) -> int:
        return len(self._sequence)


class Balance:
    @staticmethod
    def check(sequence: str) -> str:
        if len(sequence) == 0:
            return 'Это пустая строка!'
        else:
            stack = Stack()
            for elem in sequence:
                match elem:
                    case '[' | '(' | '{':
                        stack.push(elem)
                    case ']':
                        if stack.size() > 0:
                            last_elem = stack.peek()
                            if last_elem == '[':
                                stack.pop()
                            else:
                                return 'Не сбалансировано'
                        else:
                            return 'Не сбалансировано'
                    case ')':
                        if stack.size() > 0:
                            last_elem = stack.peek()
                            if last_elem == '(':
                                stack.pop()
                            else:
                                return 'Не сбалансировано'
                        else:
                            return 'Не сбалансировано'
                    case '}':
                        if stack.size() > 0:
                            last_elem = stack.peek()
                            if last_elem == '{':
                                stack.pop()
                            else:
                                return 'Не сбалансировано'
                        else:
                            return 'Не сбалансировано'
                    case _:
                        return 'Последовательность должна содержать только скобки'
            if stack.is_empty():
                return 'Сбалансировано'
            else:
                return 'Не сбалансировано'


if __name__ == '__main__':
    balance = Balance()
    while True:
        string = input('Введите последовательность скобок: ')
        print(balance.check(string))



