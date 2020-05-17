from functools import reduce
people = [{'name': 'Mary', 'height': 160},
          {'name': 'Isla', 'height': 80},
          {'name': 'Sam'}]

heights = list(map(lambda x: x['height'],filter(lambda x: 'height' in x, people)))

if len(heights) > 0:
    from operator import add
    average_height = reduce(add, heights) / len(heights)
print(average_height)   