import robot

 
def move_to_next_stack():
    '''move robot two steps right'''
    robot.drive_right()
    robot.drive_right()

def pickup_next():
    '''Release the box in gripper (if any) and pick up the one below.
    Assumption: robot is in front of a box/stack; lift is at level 1.'''
    robot.gripper_to_open()
    robot.lift_down()
    robot.gripper_to_closed()
    robot.lift_up()

x=int( input("gibe me a number for width"))
robot.init(width = x, boxes = "flat")
robot.drive_right()
robot.lift_up()

iBox=(x+1)/2
i=1
while i<iBox:
    pickup_next()
    move_to_next_stack()
    i+=1
robot.gripper_to_folded()
robot.lift_down()

