def bubble_sum(lst):
    sort_fn = lambda x: sum(x)
    return sorted(lst, key=sort_fn)

print(bubble_sum([(3, 5), (1, 3), (6, 5), (2, 8)])) #> [(1, 3), (3, 5), (2, 8), (6, 5)]
