from typing import List

import numpy as np
import matplotlib.pyplot as plt


def plot(qfs: List) -> None:

    '''
    Plots the QuadraticFunction objects in the qfs argument.
    '''

    for qf in qfs:

        plt.plot(qf.xvalues,
                 qf.yvalues,
                 label=qf.equation_str)

    plt.xlabel("x")
    plt.ylabel("y")
    plt.legend()
    plt.grid(True)

    plt.show()