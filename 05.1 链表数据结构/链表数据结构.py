# 节点
class Node:
    def __init__(self, elem):
        self.elem = elem
        self.prev = None
        self.next = None


# 双向链表
class LinkedList:
    def __init__(self):
        self.head = None  # 链表头节点
        self.tail = None  # 链表尾节点

    def append(self, elem):
        """ 链表尾部添加数据 """
        new_node = Node(elem)  # 新节点
        if self.tail is None:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

    def prepend(self, elem):
        """链表头部添加数据"""
        new_node = Node(elem)
        if self.head is None:
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def delete(self, elem):
        """删除链表节点"""
        current = self.head
        while current is not None:
            # 找到删除的节点
            if current.elem == elem:
                current.prev.next = current.next
                current.next.prev = current.prev
                # 删除头节点
                if current is self.head:
                    self.head = self.head.next
                    self.head.prev = None
                # 删除尾节点
                elif current is self.tail:
                    self.tail = current.prev
                    self.tail.next = None

            current = current.next

    def display(self, elem):
        """访问节点"""
        current = self.head
        while current is not None:
            if current.elem == elem:
                print(current.elem)
                break

            current = current.next

        print(f"未找到该节点")


if __name__ == '__main__':
    # 创建链表
    linked_list = LinkedList()
    # 添加节点
    linked_list.append("1")
    linked_list.append("2")
    linked_list.append("3")

    # 访问节点
    linked_list.display("3")

    # 删除节点
    linked_list.delete("3")
    linked_list.display("3")
