# check what integers exist in pair of 2.
l = [1, 2, 7, 2, 4, 4, 5, 6]
pair = set([value for value in l if l.count(value) == 2])
print("{} exist in pair.".format(pair))
