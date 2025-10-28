from typing import List

import matplotlib.pyplot as plt


def plot(qfs: List) -> None:

    '''
    Plots the QuadraticFunction objects in the qfs argument.
    '''

    plt.gca().axhline(linewidth=1.5, color="#000000")
    plt.gca().axvline(linewidth=1.5, color="#000000")

    for qf in qfs:

        plt.plot(qf.xvalues,
                 qf.yvalues,
                 label=qf.equation_str)

    plt.xlabel("x")
    plt.ylabel("y")
    plt.legend()
    plt.grid(True)
    
    plt.show()