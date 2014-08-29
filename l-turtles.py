import turtle

def l_system(V, w, P, n):
    """Generates an L-system run for n rounds.
    They are defined as
    G = (V, w, P)
    
    V = The alphabet (tuple, not actually used)
    w = The start (string)
    P = The production rules (dictionary for replacement)
    """
    # Make sure all production rules are in alphabet
    assert(all(key in V for key in P))
    
    current = w
    for i in range(n):
        current = [P[x] if x in P else x for x in list(current)]
        current = ''.join(current)
        
    return current
                
def run_turtle(var, start, rules, iters, angle):
    """Var, start, rules and iters, correspond to (V, w, P, n) of the 
    l-system function. The distance moved is scaled down from size.
    
    Instructions are defined as the following:
    F, G: Draw forward
    M, N: Move forward (don't draw)
    [, ]: Push and pop angle and location
    +, -: Turn left and right by angle degrees   
    Variables not described can be used as constants.
    """

    # Initialization 
    terry = turtle.Turtle()
    turtle.mode("world") # Coordinate system
    terry.pensize(1)
    terry.pencolor("blue")
    terry.speed(0) # Instant speed
    turtle.tracer(0, 0) # Don't draw anything yet
    turtle.setup(width=800, height=800, startx=None, starty=None) # Square pixels
    terry.hideturtle()
    
    
    dist = 1
    positions = []
    angles = []
    bounds = [0, 0, 0, 0] # llx, lly, urx, ury
    
    instructions = l_system(var, start, rules, iters)
    
    def update_bounds(bounds):
        coords = terry.position()

        bounds[0] = min(bounds[0], coords[0])
        bounds[1] = min(bounds[1], coords[1])
        bounds[2] = max(bounds[2], coords[0])
        bounds[3] = max(bounds[3], coords[1])
    
    # Run turtle
    for instr in instructions:
        if instr in ('F', 'G'):
            terry.forward(dist)
            update_bounds(bounds)
            
        elif instr in ('M', 'N'):
            terry.penup()
            terry.forward(dist)
            terry.pendown()
            update_bounds(bounds)
            
        elif instr == '[':
            positions.append(terry.pos())
            angles.append(terry.heading())
            
        elif instr == ']':
            terry.goto(positions.pop())
            terry.setheading(angles.pop())
            
        elif instr == '+':
            terry.left(angle)
        
        elif instr == '-':
            terry.right(angle)
       
         
    llx, lly, urx, ury = bounds
    width = urx - llx
    height = ury - lly
    
    if width > height: 
        y_center = (ury + lly)/2
        ury = y_center + width/2
        lly = y_center - width/2
    else: 
        x_center = (urx + llx)/2
        urx = x_center + height/2
        llx = x_center - height/2
        
    print(bounds)
    turtle.setworldcoordinates(llx, lly, urx, ury) # Redraw
    turtle.update() # Draw everything
    turtle.exitonclick()
    
def right_koch(iters):
    run_turtle(('F',), 'F', {'F':'F+F-F-F+F'}, iters, 90)
    
def dragon_curve(iters):
    run_turtle(('X', 'Y'), 'FX', {'X':'X+YF', 'Y':'FX-Y'}, iters, 90)
    
dragon_curve(10)

            
        

