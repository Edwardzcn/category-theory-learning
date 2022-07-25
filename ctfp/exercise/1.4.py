# Implement the identity function
# The identity function is a unary function that returns its argument.

# Challenges 1.4.1 implement the identity function
def id_f(x): return x

# Challenges 1.4.2 implement the composition function
def comp_f(x, y):
    return lambda z: x(y(z))


def plus_1(x):
    return x + 1


def plus_2(x):
    return x + 2


def plus_3(x):
    return comp_f(plus_1, plus_2)(x)

assert(plus_3(1)==4)
assert(comp_f(plus_1,id_f)(2) == comp_f(id_f,plus_1)(2))

# Challenge 1.4.4
# Is the world-wide web a category in any sense? Are links morphisms?
# No. If we can only visit website B link in A. Neither the loop to itself.

# Challenge 1.4.6
# When is a directed graph a category
# If it is a chain and each pair has a directed edge. (Every node need a self loop?)
