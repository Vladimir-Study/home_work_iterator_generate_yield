nested_list = [
    ['a', 'b', 'c'],
    ['d', 'e', 'f', 'h', False],
    [1, 2, None],
]


# TODO №1, 4 Написать итератор, который принимает список списков, и возвращает их плоское представление,
#  т.е последовательность состоящую из вложенных элементов
class FlatIterator:
    def __init__(self, list_iter):
        self.iter_list = list_iter
        self.res_lst = []
        self.next_lst = self.iter_lst()

    def __iter__(self):
        return self

    def iter_lst(self):
        for elem in self.iter_list:
            if type(elem) is list:
                self.iter_list.extend(elem)
            else:
                self.res_lst.append(elem)
        return self.res_lst

    def __next__(self):
        if len(self.next_lst) == 0:
            raise StopIteration
        else:
            return self.next_lst.pop(0)


# for item in FlatIterator(nested_list):
#     print(item)

# flat_list = [item for item in FlatIterator(nested_list)]
# print(flat_list)


# TODO №2 Написать генератор, который принимает список списков, и возвращает их плоское представление.
def flat_generate(generate_list):
    for lst in generate_list:
        for elem in lst:
            yield elem


# for item in flat_generate(nested_list):
# print(item)


# TODO №3 Написать итератор обрабатывающий списки с любым уровнем вложенности
def deep_iterator(iter_list):
    result_list = []
    for elem in iter_list:
        if type(elem) is list:
            iter_list.extend(elem)
        else:
            result_list.append(elem)
    return result_list


# deep_iter = [item for item in deep_iterator(nested_list)]
# print(deep_iter)


