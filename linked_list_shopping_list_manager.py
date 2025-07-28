class LinkedListShoppingListManagerClass:
    class Node:
        def __init__(self, data):
            # A node stores data and a reference to the next node.
            self.data = data
            self.next = None

    def __init__(self):
        '''Initialize the top of the stack (head of the linked list) to None.
        This means our shopping list starts empty.'''
        self.head = None

    def insert_item(self, item):
        '''Insert a new node at the front (top of stack).
        This is like the push() behavior of a stack.'''
        new_node = self.Node(item)
        new_node.next = self.head
        self.head = new_node

    def is_list_empty(self):
        '''Check if the stack is empty.
        Returns True if there is no item in the list.
        Thankfully, this is even easier to check since we just look to the head to see if
        data is present or not.'''
        return self.head is None

    def print_item_recursive_from_top(self, current):
        '''Recursively print items from the top to the bottom.
        As long as there is a node/current it loops and prints. 
        current.next is what keeps it moving along the linked list.'''
        if current:
            print(current.data, end=" ")
            self.print_item_recursive_from_top(current.next)

    def print_items_from_top(self):
        '''Start the top-down printing process.
        This needed to call upon the print_item_recursive_from_top method above.'''
        print("[", end=" ")
        self.print_item_recursive_from_top(self.head)
        print("]")

    def print_item_recursive_from_bottom(self, current):
        '''Recursively print items from the bottom to the top.'''
        if current:
            self.print_item_recursive_from_bottom(current.next)
            print(current.data, end=" ")

    def print_items_from_bottom(self):
        '''Start the bottom-up printing process.
        This needed to call upon the print_item_recursive_from_bottom method above.'''
        print("[", end=" ")
        self.print_item_recursive_from_bottom(self.head)
        print("]")

    def print_items(self):
        '''Print all items in the stack from top to bottom iteratively.
        This is a non-recursive version of print method so my shopping_list.py that was provided works.
        ~ Get errors in console without this method.'''
        print("[", end=" ")
        current = self.head
        while current:
            print(current.data, end=" ")
            current = current.next
        print("]")

    def get_last_item(self):
        '''Get the item/node at the top of the stack (the item/node most recently inserted).
        If the list is empty, then just return None.'''
        if self.head:
            return self.head.data
        return None

    def remove_last_item(self):
        '''Remove and return the item from the top of the stack.
        This is like the pop() operation basically.'''
        if self.head:
            removed_item = self.head.data
            self.head = self.head.next
            return removed_item
        return None

    def delete_item(self, target):
        # Delete the first node with the matching data value.
        # Starting points
        current = self.head
        previous = None
        while current:
            # if target found that we need to delete
            if current.data == target:
                # if there is a previous that we need to worry about (pointer change)
                if previous:
                    # update its pointer
                    previous.next = current.next
                else:
                    # otherwise we just update the heads (current) pointer
                    self.head = current.next
                return
            # how we keep searching
            previous = current
            current = current.next

    def find_smallest(self):
        '''Find the item with the smallest value (alphabetically).
        Return None if the list is empty.'''
        if self.head is None:
            return None

        # starting points
        min_val = self.head.data
        current = self.head.next
        while current:
            # where we check which value is lower
            if current.data < min_val:
                # update value
                min_val = current.data
            # keep iterating through until the end
            current = current.next
        return min_val