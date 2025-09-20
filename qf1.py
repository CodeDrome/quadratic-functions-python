from typing import Tuple

import numpy as np
import matplotlib
import matplotlib.pyplot as plt


matplotlib.use('Qt5Agg')


class QuadraticFunction(object):

    '''
    The QuadraticFunction class has properties
    representing the coefficients of a function
    in the general form.
    The class has methods to evaluate the function for 
    given x values, and print and plot x and y.
    '''

    def __init__(self, 
                 a: float=1, # quadratic coefficient
                 b: float=0, # linear coefficient
                 c: float=0): # constant coefficient
        
        self.a = a
        self.b = b
        self.c = c

        self.equation_str = self.__create_eq_str()

        self.xvalues = None
        self.yvalues = None

    
    def evaluate(self, xminmax: Tuple=(-10.0,11.0), interval: float=1.0) -> None:

        '''
        Populates the instance's xvalues and yvalues
        using coefficient properties.
        Arguments:
            xminmax - tuple of min and max x values
            interval - between x values
        Return:
            none
        '''
        
        # create a lambda based on x and coefficients
        func = lambda x: self.a*x**2 + self.b*x + self.c

        self.xvalues = np.arange(xminmax[0], xminmax[1], interval)

        self.yvalues = func(self.xvalues)


    def print_values(self) -> None:

        '''
        Prints intance's xvalues and yvalues in a table format.
        '''

        heading = "       x           y  "

        print("-" * len(heading))
        print(heading)
        print("-" * len(heading))

        for i in range(0, len(self.xvalues)):

            print(f"{self.xvalues[i]:>9.2f}", end="")
            print(f"{self.yvalues[i]:>13.2f}")

        print("-" * len(heading))


    def plot(self, color: str='#FF4000') -> None:

        '''
        Plot the xvalues and yvalues using specified color.
        '''
    
        plt.plot(self.xvalues,
                 self.yvalues,
                 color=color)

        plt.xlabel("x")
        plt.ylabel("y")
        plt.title(f"{self.equation_str}")
        plt.grid(True)

        plt.show()


    def __create_eq_str(self) -> str:    

        return f"y = {self.a}x² + {self.b}x + {self.c}"