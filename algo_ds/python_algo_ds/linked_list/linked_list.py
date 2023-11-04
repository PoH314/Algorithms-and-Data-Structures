""" Implementation of a linked list (https://en.wikipedia.org/wiki/Linked_list)  """
from __future__ import annotations
from collections.abc import Iterable
from typing import Any
from nodes import Node


class LinkedList:
    def __init__(self) -> None:
        self._head: Node | None = None
        self._last: Node | None = None
        self._len: int = 0

    def __iter__(self) -> Iterable:
        current = self._head

        while current:
            yield current.data
            current = current.next

    def __str__(self) -> str:
        return ' -> '.join(str(item) for item in self)

    def __len__(self) -> int:
        return self._len

    def _validate_index(self, index: int) -> None:
        if not 0 <= index < len(self):
            raise IndexError('list index out of range')

    def _get_node(self, index: int) -> Node:
        self._validate_index(index)
        current = self._head

        for _ in range(index):
            current = current.next

        return current

    def __getitem__(self, index: int) -> Any:
        return self._get_node(index).data

    def __setitem__(self, index: int, value: Any) -> None:
        node = self._get_node(index)

        node.data = value

    def get_head(self) -> Node:
        return self._head

    def get_last(self) -> Node:
        return self._last

    def append(self, value: Any) -> None:
        new_node = Node(value)

        if not self._head:
            self._head = self._last = new_node
        else:
            self._last.next = new_node
            self._last = new_node

        self._len += 1

    def insert(self, value: Any, index: int) -> None:
        self._validate_index(index)
        new_node = Node(value)

        if not self._head:
            self.append(value)
        elif index == 0:
            new_node.next = self._head
            self._head = new_node
        elif index == len(self) - 1:
            self.append(value)
        else:
            previous_new_node = self._get_node(index - 1)
            new_node.next = previous_new_node.next
            previous_new_node.next = new_node

        self._len += 1

    def delete(self, index: int) -> None:
        self._validate_index(index)

        if len(self) == 1:
            self._head = self._last = None
        elif index == 0:
            self._head = self._head.next
        elif index == len(self) - 1:
            self._last = self._get_node(len(self) - 2)
            self._last.next = None
        else:
            to_delete = self._head
            previous_to_delete = None

            for i in range(index):
                to_delete = to_delete.next
                if i == index - 1:
                    previous_to_delete = to_delete

            previous_to_delete.next = to_delete.next

        self._len -= 1

    def search(self, value: Any) -> Node | None:
        current = self._head

        while current:
            if current.data == value:
                return current
            current = current.next

        return None
