class Queue:  # First In, First Out
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)

    def peek(self):
        if not self.is_empty():
            return self.items[0]

    def print_q(self):
        print(self.items)


def main():
    queue = Queue()

    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)

    queue.print_q()
    print("Peek:", queue.peek())
    queue.print_q()

    print("Dequeue:", queue.dequeue())
    queue.print_q()

    print("Peek:", queue.peek())
    queue.print_q()

    print("Dequeue:", queue.dequeue())
    queue.print_q()

    print("Is Empty:", queue.is_empty())
    queue.print_q()

    print("Dequeue:", queue.dequeue())
    queue.print_q()

    print("Is Empty:", queue.is_empty())
    queue.print_q()

    print("Peek:", queue.peek())
    queue.print_q()

    print("Dequeue:", queue.dequeue())
    queue.print_q()


if __name__ == "__main__":
    main()
