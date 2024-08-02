from node import Node


class DoubleLinkedList:
    def __init__(self, head=None):
        self.head = head

    def traverse(self):
        # grab the first node
        curr_node = self.head

        # keep going until you reach the end of the list
        while curr_node is not None:
            print(curr_node.data)

            # grab the node after the old current one
            curr_node = curr_node.next_node

    def get_size_list(self):
        # define incrementer
        count = 0

        # grab the first node
        curr_node = self.head

        # keep going until you reach the end of the list
        while curr_node is not None:
            count += 1

            # grab the node after the old current one
            curr_node = curr_node.next_node

        return count

    def insert_beginning(self, data):
        # define a new node
        new_node = Node(data)

        # set the next node equal to old head
        new_node.next_node = self.head

        # because it's the head the previous point will point to nothing
        new_node.prev_node = None

        # handle the non-empty list case
        if self.head is not None:
            self.head.prev_node = new_node

        # update the head
        self.head = new_node

    def insert_end(self, data):
        # define a new node
        new_node = Node(data)

        # at the end of our list, so the next pointer, points to nothing
        new_node.next_node = None

        # handle an empty case scenario
        if self.head is None:
            new_node.prev_node = None
            self.head = new_node
            return

        # first grab the first node
        first_node = self.head

        # go to the end of our list
        while first_node.next_node:
            first_node = first_node.next_node

        # when at the end, set the next node equal to the new node
        first_node.next_node = new_node
        new_node.prev_node = first_node

    def insert_before(self, ref_node, data):
        if self.head is None:
            print("The list is empty")
            return

        # define a new node
        new_node = Node(data)

        new_node.prev_node = ref_node.prev_node
        ref_node.prev_node = new_node
        new_node.next_node = ref_node

        if new_node.prev_node is not None:
            new_node.prev_node.next_node = new_node
        else:
            self.head = new_node

    def insert_after(self, ref_node, data):
        if self.head is None:
            print("The list is empty")
            return

        # define a new node
        new_node = Node(data)
        new_node.next_node = ref_node.next_node
        ref_node.next_node = new_node
        new_node.prev_node = ref_node

        if new_node.next_node is not None:
            new_node.next_node.prev_node = new_node


if __name__ == '__main__':
    dl = DoubleLinkedList()
    dl.insert_beginning(10)
    dl.insert_beginning(20)
    dl.insert_beginning(30)

    dl.traverse()
