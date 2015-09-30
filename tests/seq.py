import itertools
# generating infinite sequence of real numbers using step size of 0.25
count_iter = itertools.count(10,0.25)

print list(itertools.ifilter(lambda x:x%2, numbers))