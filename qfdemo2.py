import qf1
import qfplotter as qfp


def main():

    print("-------------------------")
    print("| codedrome.com         |")
    print("| Quadratic Functions 2 |")
    print("-------------------------\n")

    # the x values to evaluate the functions over
    xmin = -12
    xmax = 12.1
    interval = 0.5

    # list for our QuadraticFunction objects
    quadfuncs = []

    # default values do not transform or translate the curve
    coefficients_default = ((1,0,0),)

    # The a coefficient performs vertical transforms,
    # ie "stretching" or "squashing" the curve.
    # Negative values invert the parabola.
    coefficients_a = ((2,0,0), # stretch
                      (1,0,0), # default
                      (0.5,0,0), # squash
                      (0,0,0), # horizontal line
                      (-0.5,0,0), # invert and squash
                      (-1,0,0), # invert, no transform
                      (-2,0,0)) # invert and stretch
    
    # Move the vertex along an inverted parabola
    # which is created by the final coefficients.
    # the final coefficients illustrate the "path" taken by the vertices 
    # of functions with various values of the b coefficient
    coefficients_b = ((1,0,0),
                      (1,10,0),
                      (1,20,0),
                      (1,-10,0),
                      (1,-20,0),
                      (-1,0,0))

    # The c coefficient move the curve up 
    # if positive and down if negative
    coefficients_c = ((1,0,0), # default
                      (1,0,72), # up
                      (1,0,-72)) # down
    
    # UNCOMMENT ONE OF THESE LINES TO SELECT REQUIRED COEFFICIENTS
    for coeffs in coefficients_default:
    # for coeffs in coefficients_a:
    # for coeffs in coefficients_b:
    # for coeffs in coefficients_c:

        qf = qf1.QuadraticFunction(*coeffs)
        qf.evaluate(xminmax=(xmin, xmax), interval=interval)

        quadfuncs.append(qf)

    qfp.plot(quadfuncs)


if __name__ == "__main__":

    main()