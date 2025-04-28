# 节点
class Node:
    def __init__(self, elem):
        self.elem = elem
        self.prev = None
        self.next = None


# 双向链表
class Deque:
    def __init__(self):
        self.head = None  # 队列头部
        self.tail = None  # 队列尾部
        self.size = 0     # 队列的元素个数

    def appendleft(self, elem):
        new_node = Node(elem)
        if self.head is None:
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def append(self, elem):
        new_node = Node(elem)  # 新节点
        if self.tail is None:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

    def popleft(self):
        node = Node(self.head.elem)
        current = self.head.next
        self.head = current
        return node

    def pop(self):
        node = Node(self.tail.elem)
        current = self.tail.prev
        self.tail = current
        return node

    def peekleft(self):
        print(self.head.elem)

    def peek(self):
        print(self.tail.elem)

    def size(self):
        return self.size

    def is_empty(self):
        if self.size == 0:
            print("队列为空")
        else:
            print("队列不为空")


if __name__ == '__main__':
    double_deque = Deque()

