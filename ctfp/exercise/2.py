# Challenges 2.1
from random import random, seed
from functools import wraps
from pickle import TRUE


def memoize(f):
    cache = {}

    @wraps(f)
    def wrapper(*args):
        if args not in cache:
            cache[args] = f(*args)
        return cache[args]

    return wrapper


@memoize
def factorial(n):
    if n < 2:
        return 1
    else:
        return n * factorial(n-1)


def mymemoize(f):
    cache = {}

    def mymemoize_f(*args):
        if args not in cache:
            # print("#", *args, "#")
            # if we show the args here we'll find output is '# #' empty args will print a space?
            cache[args] = f(*args)
        return cache[args]
    return mymemoize_f


@mymemoize
def factorial2(n):
    if n < 2:
        return 1
    else:
        return n * factorial(n-1)


print(factorial(100))
# factorial2 = mymemoize(factorial2)
print(factorial2(100))

print("factorial's real name=", factorial.__name__)
print("factorial2's real name=", factorial2.__name__)

# Challenges 2.2
memoize_random = mymemoize(random)
print(memoize_random(), random())
print(memoize_random(), random())
# 0.6641516094395697 0.7600429280377078
# 0.6641516094395697 0.7806773382160002
# It's obvious that memoize_random doesn't work


# Challenge 2.3
def random_with_seed(k):
    seed(k)
    return random()


memorize_random_with_seed = mymemoize(random_with_seed)
print(random_with_seed(10), memorize_random_with_seed(10))
print(random_with_seed(10), memorize_random_with_seed(10))
# 0.5714025946899135 0.5714025946899135
# 0.5714025946899135 0.5714025946899135
# initialized with a seed makes it pure?

# Challenge 2.4
# (a) The factorial function from the example. It's pure.
# (b) std::getchar()

# memorized_input = mymemoize(input)
# a = input()
# b = memorized_input()
# c = memorized_input()
# print(a, b, c)

# 1
# 2
# 1 2 2
# Something interesting. It remember what we input.
# (c)


def f():
    print("Hello!")
    return TRUE


memorize_f = mymemoize(f)
f()
memorize_f()

# (d)

# Challenge 2.5
# We have four functions

# ftt :: Bool -> Bool
# ftt a = case a of
#    True -> True
#    False -> True

# ftf :: Bool -> Bool
# ftf a = case a of
#    True -> True
#    False -> False

# fft :: Bool -> Bool
# fft a = case a of
#    True -> False
#    False -> True

# fff :: Bool -> Bool
# fff a = case a of
#    True -> False
#    False -> False

# Challenge 2.6
# See 2.6.png