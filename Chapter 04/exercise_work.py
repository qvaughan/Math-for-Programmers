from vectors import *
from teapot import *
from draw_model import *
from transforms import *


#
# Exercise 4.1 Implement a translate_by function (referred to in section 4.1.2),
# taking a translation vector as input and returning a translation function as
# output.
#

def translate_by(v1):
    def translate_vector(v2):
        return add(v1, v2)

    return translate_vector

def exercise_4_1():
    draw_model(polygon_map(translate_by((1, 0, 0)), load_triangles()))


#
# Exercise 4.2 Render the teapot translated by 20 units in the negative
# z direc- tion. What does the resulting image look like?
#

def exercise_4_2():
    draw_model(polygon_map(translate_by((0, 0, -20)), load_triangles()))

# Exercise 4.4
# First apply translate1left to the teapot and then apply scale2. How is
# the result different from the opposite order of composition? Why?
def exercise_4_4():
    draw_model(polygon_map(compose(translate_by((-1, 0, 0)), scale_by(2)), load_triangles()))


# Exercise 4.7
# Write a curry2(f) function that takes a Python function f(x,y) with
# two arguments and returns a curried version. For instance, once you write
# g = curry2(f), the two expressions f(x,y) and g(x)(y) should return the
# same result.
def curry2(f):
    def outer(x):
        def inner(y):
            return f(x, y)
        return inner
    return outer

def exercise_4_7():
    f = lambda x,y: x - y
    g = curry2(f)
    print(f(4, 6) == g(4)(6))


# Exercise 4.9 Write a function stretch_x(scalar,vector) that scales the target
# vector by the given factor but only in the x direction. Also write a curried
# version stretch_x_by so that stretch_x_by(scalar)(vector) returns the same
# result.
def stretch_x(scalar, v):
    return (v[0] * scalar, v[1], v[2])


def stretch_x_by(scalar):
    def new_func(vector):
        return stretch_x(scalar, vector)
    return new_func

def exercise_4_9():
    draw_model(polygon_map(stretch_x_by(2), load_triangles()))

exercise_4_9()