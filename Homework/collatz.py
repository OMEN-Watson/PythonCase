## COMP1730/6730 Homework 3

# Your ANU ID: u7568823
# Your NAME: Fan Yue
# I declare that this submission is my own work
# [ref: https://www.anu.edu.au/students/academic-skills/academic-integrity ]


## You should implement the functions `collatz_step` and `collatz_stopping_time` 
## below. You can define new function(s) if it helps you decompose the problem
## into smaller problems.

def collatz_step(n):
    '''
    ghhg
    '''
    if(n%2==0) :return (n//2);
    else : return (int)(n*3+1);

def collatz_stopping_time(n):
    if(n==1): return 0;
    res=collatz_step(n)
    times=1;
    while res!=1:
     res= collatz_step(res)
     times+=1 #adds one

    return times;


################################################################################
#               DO NOT MODIFY ANYTHING BELOW THIS POINT
################################################################################    

def test_collatz_step():
    '''
    This function runs a number of tests of the collatz step function.
    If it works ok, you will just see the output ("all tests passed") at
    the end when you call this function; if some test fails, there will
    be an error message.
    NOTE: passing all tests does not automatically mean that your code is correct
    because this function only tests a limited number of test cases.
    '''
    assert type(collatz_step(4)) == int, "Test failed!"
    assert type(collatz_step(5)) == int, "Test failed!"
    assert collatz_step(4) == 2, "Test failed!"
    assert collatz_step(5) == 16 , "Test failed!"
    print("all tests passed")

def test_collatz_stopping_time():
    '''
    This function runs a number of tests of the collatz_stopping_time function.
    If it works ok, you will just see the output ("all tests passed") at
    the end when you call this function; if some test fails, there will
    be an error message.
    NOTE: passing all tests does not automatically mean that your code is correct
    because this function only tests a limited number of test cases.
    '''
    assert collatz_stopping_time(27)==111, "Test Failed!"
    assert collatz_stopping_time(1)==0, "Test Failed!"
    assert collatz_stopping_time(2)==1, "Test Failed!"
    assert collatz_stopping_time(2048)==11, "Test Failed!"
    print("all tests passed")

test_collatz_step()
test_collatz_stopping_time()