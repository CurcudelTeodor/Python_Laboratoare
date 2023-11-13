class Stack:  # Last In, First Out
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()

    def peek(self):
        if not self.is_empty():
            return self.items[-1]

    def print_stack(self):
        if self.is_empty():
            print("Stack is empty")
        else:
            print("Stack:")
            for item in reversed(self.items):
                print(item)


def main():
    stack = Stack()

    stack.push(1)
    stack.push(2)
    stack.push(3)

    stack.print_stack()
    print("Peek:", stack.peek())
    stack.print_stack()

    print("Pop:", stack.pop())
    stack.print_stack()

    print("Peek:", stack.peek())
    stack.print_stack()

    print("Pop:", stack.pop())
    stack.print_stack()

    print("Is Empty:", stack.is_empty())
    stack.print_stack()

    print("Pop:", stack.pop())
    stack.print_stack()

    print("Is Empty:", stack.is_empty())
    stack.print_stack()

    print("Peek:", stack.peek())
    stack.print_stack()

    print("Pop:", stack.pop())
    stack.print_stack()


if __name__ == "__main__":
    main()

# la lab 5 sa verific daca anul < anul curent
# ca are picioare mai multe decat erau
# sa verific daca triunghiul e valid