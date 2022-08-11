nested_list = [['a', 'b', 'c'],
               ['d', 'e', 'f', 'h', False],
               [1, 2, None]
               ]


class FlatIterator():

    def __init__(self, nested_list):
        self.list = nested_list

    def __iter__(self):
        self.coursor = 0
        self.coursor_item = -1
        self.iter_list = iter(self.list)
        self.coursor_end = 0
        return self

    def __next__(self):
        while True:
            if self.coursor == self.coursor_end:
                if self.coursor_item < len(self.list[self.coursor]) - 1:
                    self.coursor_item += 1
                    return self.list[self.coursor][self.coursor_item]
                else:
                    self.coursor += 1
                    self.coursor_end += 1
                    self.coursor_item = -1
            if self.coursor == len(self.list):
                raise StopIteration


for item in FlatIterator(nested_list):
    print(item)

flat_list = [item for item in FlatIterator(nested_list)]
print(flat_list)