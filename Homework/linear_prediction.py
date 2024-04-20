## COMP1730/6730 - Homework 4

# Your ANU ID: u7568823
# Your NAME: Fan Yue
# I declare that this submission is my own work
# [ref: https://www.anu.edu.au/students/academic-skills/academic-integrity ]

## Implement the function below.
## (The statement "pass" is just a placeholder that does nothing: you
## should replace it.)
## You can define other functions if it helps you decompose the problem
## and write a better organised and/or more readable solution.
import numpy as np
def linear_prediction(x, y, x_test):
    xSorted= []
    print(type(x))
    # if(type(x)==tuple):
    listX= np.array(x)
    xSorted=  listX.copy()

    # xSorted=  x.copy()
    xSorted.sort()
    if x_test in x:
        ind= x.index(x_test )
        target= y[ind]
        return target
    minX=np.min(x)
    maxX=np.max(x)

    XLeftNum=0
    YLeftNum=0
    XRightNum=0
    YRightNum=0
    if x_test<minX:
        XLeftNum=xSorted[0]
        XRightNum=xSorted[1]

        # XleftNumIndex=x.index(XLeftNum)
        # XRightNumIndex=x.index(XRightNum)

        # YLeftNum=y[XleftNumIndex]
        # YRightNum=y[XRightNumIndex]

        # return  calculationMethond(XLeftNum,YLeftNum,XRightNum,YRightNum,x_test)

    elif  x_test>maxX:
        length=len(x)
        XLeftNum=xSorted[length-1]
        XRightNum=xSorted[length-2]

        # XleftNumIndex=x.index(XLeftNum)
        # XRightNumIndex=x.index(XRightNum)

        # YLeftNum=y[XleftNumIndex]
        # YRightNum=y[XRightNumIndex]
    else:
 
        for index in range(len(xSorted)):
           xCurrent= xSorted[index]
           xNext=xSorted[index+1]
           if xCurrent<x_test and x_test<xNext:
               XLeftNum=xCurrent
               XRightNum=xNext
               break
            #    YLeftNum=getOriginY(x,y,XLeftNum)
            #    YRightNum=getOriginY(x,y,XRightNum)
        # return  calculationMethond(XLeftNum,YLeftNum,XRightNum,YRightNum,x_test)
    YLeftNum=getOriginY(x,y,XLeftNum)
    YRightNum=getOriginY(x,y,XRightNum)
    return  calculationMethond(XLeftNum,YLeftNum,XRightNum,YRightNum,x_test)
        
def calculationMethond(x1,y1,x2,y2,xTest):
    a=(y1-y2)/(x1-x2)
    b=y1-a*x1
    result=a*xTest+b
    return result
def getOriginY(xList,yList, xNum):
      index=xList.index(xNum)
      targetY= yList[index]
      return targetY
    
################################################################################
#               DO NOT MODIFY ANYTHING BELOW THIS POINT
################################################################################

def test_linear_prediction():
    '''
    This function runs a number of tests of the linear_prediction function.
    If it works ok, you will just see the output ("all tests passed") at
    the end when you call this function; if some test fails, there will
    be an error message.
    '''

    assert abs(linear_prediction([1.0, 3.0, 5.0], [1.0, 9.0, 25.0], 0.5) - -1.0) < 1e-6
    assert abs(linear_prediction([1.0, 3.0, 5.0], [1.0, 9.0, 25.0], 2.0) - 5.0) < 1e-6
    assert abs(linear_prediction([1.0, 3.0, 5.0], [1.0, 9.0, 25.0], 4.0) - 17.0) < 1e-6
    assert abs(linear_prediction([1.0, 3.0, 5.0], (1.0, 9.0, 25.0), 6.0) - 33.0) < 1e-6
    assert abs(linear_prediction((1.0, 5.0, 3.0), [1.0, 25.0, 9.0], 1.25) - 2.0) < 1e-6
    assert abs(linear_prediction((1.0, 5.0, 3.0), (1.0, 25.0, 9.0), 2.5) - 7.0) < 1e-6

    # test that we get the right answer when x_test is exactly one
    # of the sample points:
    assert abs(linear_prediction([1.0, 3.0, 5.0], [1.0, 9.0, 25.0], 1) - 1.0) < 1e-6
    assert abs(linear_prediction([5.0, 1.0, 3.0], [25.0, 1.0, 9.0], 3) - 9.0) < 1e-6
    assert abs(linear_prediction([3.0, 1.0, 5.0], [9.0, 1.0, 25.0], 5) - 25.0) < 1e-6

    # we should get the same answer also if only the two adjacent
    # sample points are given:
    assert abs(linear_prediction([1.0, 3.0], [1.0, 9.0], 0) - -3) < 1e-6
    assert abs(linear_prediction([3.0, 1.0], [9.0, 1.0], 2.0) - 5.0) < 1e-6
    assert abs(linear_prediction([5.0, 3.0], [25.0, 9.0], 4.0) - 17.0) < 1e-6
    assert abs(linear_prediction([1.0, 3.0], [1.0, 9.0], 4.0) - 13.0) < 1e-6

    print("all tests passed")

import matplotlib.pyplot as plt

def plot_linear_prediction(x, y, x_tests):
    """
    This function visualizes linear_prediction results.
    It takes multiple x_test values as a sequence x_tests and
    data points specified in sequences x and y.
    Args:
        x: sequence of x-values
        y: sequence of corresponding y-values
        x_tests: sequence of testing x-values
    """
    y_tests = [ linear_prediction(x, y, x_test) for x_test in x_tests ]
    xlim_min = min(min(x), min(x_tests))-1
    ylim_min = min(min(y), min(y_tests))-3
    plt.xlim(xlim_min, max(max(x), max(x_tests))+1)
    plt.ylim(ylim_min, max(max(y), max(y_tests))+3)
    plt.plot(x, y, marker = "o", color = "black")
    for x_test, y_test in zip(x_tests, y_tests):
        plt.plot([xlim_min, x_test, x_test], [y_test, y_test, ylim_min], 
            linestyle = 'dashed')
    plt.show()


# plot_linear_prediction([1.0, 3.0, 5.0], [1.0, 9.0, 25.0],[ 0.5])

test_linear_prediction()
