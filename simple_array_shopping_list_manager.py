class SimpleArrayShoppingListManagerClass:
    def __init__(self):
        '''Initialize an empty list to act as our array-based stack.
        This list will store all the shopping items.'''
        self.items = []

    def insert_item(self, item):
        '''Insert an item at the front of the array.
        In Python, insert(0, item) places the item at the beginning of the list.
        This simulates stack push behavior from the top. Good to know!'''
        self.items.insert(0, item)

        '''Another way to do this without the insert() is:
        
        self.items = [item] + self.items
        
        
        This basically just places/adds the item to the front of the list (self.items). My brain is more 
        used to this, but the other way is much shorter!'''

    def print_items(self):
        '''Print all items in the list.
        This shows the current contents of the shopping list from top to bottom.'''
        print(self.items)

    def delete_item(self, item):
        '''Remove the first occurrence of an item from the list.
        Uses the remove() method, which throws an error if the item isn't found.
        Using if statement to check if found first due to this.'''
        if item in self.items:
            self.items.remove(item)

    def get_last_item(self):
        '''Get the last item in the list (bottom of the stack).
        If the list is empty, return None.'''
        if self.items:
            # Handy [-1] index trick to get to the last item!
            return self.items[-1]
        return None

    def selection_sort(self):
        '''Sort the array items alphabetically using selection sort.
        This is a basic sorting algorithm that repeatedly finds the smallest item.'''
        for i in range(len(self.items)):
            min_index = i
            for j in range(i + 1, len(self.items)):
                if self.items[j] < self.items[min_index]:
                    min_index = j
            # Swap the found minimum element with the first element
            self.items[i], self.items[min_index] = self.items[min_index], self.items[i]