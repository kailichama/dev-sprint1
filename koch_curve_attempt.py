
world.clear()
bob = Turtle()


#def draw(t, length, n):
 #   if n == 0:
  #      return
   # angle = 50
   # fd(t, length*n)
   # lt(t, angle)
   # draw(t, length, n-1)
   # rt(t, 2*angle)
   # draw(t, length, n-1)
   # lt(t, angle)
   # bk(t, length*n)
#draw(bob, 20, 5)

# solution koch curve 
#def koch(t, n):
    """Draws a koch curve with length n."""
    #if n < 3:
     #   fd(t, n)
      #  return
    #m = n/3.0
    #koch(t, m)
    #lt(t, 60)
    #koch(t, m)
    #rt(t, 120)
   # koch(t, m)
  #  lt(t, 60)
 #   koch(t, m)
#koch(bob, 50)

def draw(t, x, n):
    if x < 3:
        return 
    angle = 60
    fd(t, x/3)
    lt(t, angle)
    fd(t, x/3)
    rt(t, 2*angle)
    fd(t, x/3)
    lt(t, angle)
    fd(t, x/3)
draw(bob, 100, 1)
