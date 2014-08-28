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
                
def run_turtle(var, start, rules, iters, angle, size, scale):
    """Var, start, rules and iters, correspond to (V, w, P, n) of the 
    l-system function. The distance moved is scaled down from size.
    
    Instructions are defined as the following:
    F, G: Draw forward
    M, N: Move forward
    [, ]: Push and pop angle and location
    +, -: Turn left and right by angle degrees   
    """

    #wn = turtle.Screen()
    terry = turtle.Turtle()
    terry.pensize(1)
    terry.pencolor("blue")
    terry.speed(0)
    
    dist = size / ((iters + 1) ** scale)
    positions = []
    angles = []
    
    instructions = l_system(var, start, rules, iters)
    
    for instr in instructions:
        if instr in ('F', 'G'):
            terry.forward(dist)
            
        elif instr in ('M', 'N'):
            terry.penup()
            terry.forward(dist)
            terry.pendown()
            
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
            
    turtle.mainloop()
    
def right_koch():
    run_turtle(('F',), 'F', {'F':'F+F-F-F+F'}, 5, 90, 500, 3)
    
right_koch()
            
        

