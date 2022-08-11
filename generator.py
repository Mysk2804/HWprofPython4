nested_list = [['a', 'b', 'c'],
               ['d', 'e', 'f', 'h', False],
               [1, 2, None]
               ]


def flat_generator(nested_list):
    coursor = 0

    while True:
        for item in nested_list:
            for i in item:
                yield i
            coursor += 1
        if coursor == len(nested_list):
            break


for item in flat_generator(nested_list):
    print(item)

flat_list = [item for item in flat_generator(nested_list)]
print(flat_list)