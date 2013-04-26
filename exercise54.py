# This is where Exercise 5.4 goes
# Name: Kelly Chiang

def is_triangle(a, b, c):
    if a + b < c:
        print "no"
    if a + c < b:
        print "no"
    if b + c < a:
        print "no"
    else:
        print "yes"
is_triangle(29, 11, 12)

is_triangle(10, 11, 12)

