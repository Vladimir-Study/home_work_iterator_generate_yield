nested_list = [
    ['a', 'b', 'c'],
    ['d', 'e', 'f', 'h', False],
    [1, 2, None],
]


# TODO №1 Написать итератор, который принимает список списков, и возвращает их плоское представление,
#  т.е последовательность состоящую из вложенных элементов
def flat_iterator(iterations_list):
    result_list = []
    for lst in iterations_list:
        for elem in lst:
            result_list.append(elem)
    return result_list


# for item in flat_iterator(nested_list):
#     print(item)

flat_list = [item for item in flat_iterator(nested_list)]


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


# TODO №4 Написать генератор обрабатывающий списки с любым уровнем вложенности
def deep_generator(gen_list):
    for elem in gen_list:
        if type(elem) is list:
            gen_list.extend(elem)
        else:
            yield elem


# for item in deep_generator(nested_list):
#     print(item)
