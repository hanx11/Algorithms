# -*- coding:utf-8 -*-

class Node:
    def __init__(self, value=None):
        self.data = value
        self._prev = None
        self._next = None

    def __repr__(self):
        return 'Node-%r' % self.data


class DoubleLinkedList:
    def __init__(self):
        self._head = Node()

    def __str__(self):
        temp = self._head
        values = []
        while temp and temp.data:
            values.append(temp.data)
            temp = temp._next
        return 'DoubleLinkedList(%s)' % values

    def __len__(self):
        _length = 0
        temp = self._head
        while temp._next:
            _length += 1
            temp = temp._next
        return _length

    def insert(self, value):
        element = Node(value)
        element._next = self._head
        self._head._prev = element
        self._head = element

    def search(self, value):
        if not self._head._next:
            raise ValueError('the linked list is empty!')

        temp = self._head
        while temp.data != value:
            temp = temp._next
        return temp

    def delete(self, value):
        element = self.search(value)
        if not element:
            raise ValueError('delete error: the value not found')
        
        element._prev._next = element._next
        if element._next is not None:
            element._next._prev = element._prev
        return element.data


if __name__ == '__main__':
    dll = DoubleLinkedList()
    print(dll)
    dll.insert(10)
    print(dll.search(10))
    dll.delete(10)
    print(dll)
