import qf1 as qf1


def main():

    print("-------------------------")
    print("| codedrome.com         |")
    print("| Quadratic Functions 1 |")
    print("-------------------------\n")

    qf = qf1.QuadraticFunction()

    qf.evaluate(xminmax=(0.0, 12.1), interval=0.5)

    print(f"{qf.equation_str}\n")

    qf.print_values()

    qf.plot()


if __name__ == "__main__":

    main()