def count_elements(input_tuple):
    count_dict = {}
    for element in input_tuple:
        if isinstance(element, list):
            key = tuple(element)
        else:
            key = element
        if key in count_dict:
            count_dict[key] += 1
        else:
            count_dict[key] = 1
    result_tuple = tuple((key, count_dict[key]) for key in count_dict)
    return result_tuple
samples = [
    (55, 6, 777, 54, 6, 76, 7777, 1, 777, 6),
    ('55', '6', '777', 54, 6, 7777, 9, 777, 6),
    ((1,2,3), (['A', 'B']), (1,2,3), (['A']))
]
for sample in samples:
    result = count_elements(sample)
    print(result)

