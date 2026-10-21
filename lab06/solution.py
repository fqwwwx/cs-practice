#1
def count_items(values: list)->dict:
    counts = {}
    for item in values:
        counts[item] = counts.get(item,0) + 1
    return counts
#2
def unique_sorted(values: list)->list:
    return sorted(set(values))
#3
def common(first:list,second:list)->list:
    return sorted(set(first) & set(second))
#4
def only_in_first(first:list,second:list)->list:
    return sorted(set(first) - set(second))
