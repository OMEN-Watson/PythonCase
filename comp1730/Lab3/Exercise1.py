def print_grade(mark):
    if mark >= 80:
        print("High Distinction")
        return
    if mark >= 70:
        print("Distinction")
        return
    if mark >= 60:
        print("Credit")
        return
    if mark >= 50:
        print("Pass")
        return
    else:
        print("Fail")

def print_ball_motion_table():
    """
    Prints a table of the position, at different times, 
    of a ball thrown vertically from the ground level at 
    a velocity of 100 m/s. The interval [0,T] is split 
    into N parts, resulting into N+1 time points at which to 
    calculate and show the position of the ball, that is, N+1 
    rows in the table.
    """
    T=20
    N=4
    t=0.0  # Initialize current time t to 0.0 (s) 
    i=0  # Initialize loop counter to zero
    dt=T/N # Compute Delta_t (s)
    while t<=T: # Loop condition (compare integers!)
        y=100*t-4.9*t*t  # Compute y(t)         
        print(f"t:{t} ,y:{y}")
       
        t+=dt    # Increment loop counter i (by how much?)
        # ___    # Increment current time t (by how much?)

print_ball_motion_table()