class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Order:
    def __init__(self, qtty, customer):
        self.customer = customer
        self.qtty = qtty

    def print_order(self):
        print(f"     Cliente: {self.customer}\n     Cantidad: {self.qtty}\n     ------------")

class OrderQueue:
    def __init__(self):
        self.top = self.rear = None
        self.size = 0

    def enqueue(self, order):
        new_node = Node(order)
        if self.top is None:
            self.top = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node
        self.size += 1

    def dequeue(self):
        if self.top is None:
            return None
        removed_order = self.top.data
        self.top = self.top.next
        if self.top is None:
            self.rear = None
        self.size -= 1
        return removed_order

    def queue_dump(self):
        print(f"********* ESTADO DE LA COLA *********\n   Tamaño: {self.size}")
        node, i = self.top, 1
        while node:
            print(f"   ** Elemento {i}")
            node.data.print_order()
            node = node.next
            i += 1
        print("*************************************")


queue = OrderQueue()

queue.enqueue(Order(20, "cliente1"))
queue.enqueue(Order(30, "cliente2"))
queue.enqueue(Order(40, "cliente3"))
queue.enqueue(Order(50, "cliente3"))

queue.queue_dump()
