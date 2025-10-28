import qf2
import qfplotter as qfp


def main():

    print("-------------------------")
    print("| codedrome.com         |")
    print("| Quadratic Functions 3 |")
    print("-------------------------\n")

    # the x values to evaluate the functions over
    xmin = -12
    xmax = 12.1
    interval = 0.5

    # list for our QuadraticFunction objects
    quadfuncs = []

    # vertical transforms
    coeffs_v_t = ((1,0,72),
                  (1,0,0),                  
                  (1,0,-72))
    
    # invert and vertical transforms
    coeffs_i_v_t = ((-1,0,72),
                    (-1,0,0),
                    (-1,0,-72))
    
    # horizontal and vertical translate
    coeffs_h_v_t = ((1,0,0),
                    (1,5,0),
                    (1,-10,0))
    
    # horizontal stretch and squash
    coeffs_h_s_s = ((1,0,-24),
                  (0.5,0,-48),
                  (2.0,0,-72))
    
    # UNCOMMENT ONE OF THESE LINES TO SELECT REQUIRED COEFFICIENTS
    for coeffs in coeffs_v_t:
    # for coeffs in coeffs_i_v_t:
    # for coeffs in coeffs_h_v_t:
    # for coeffs in coeffs_h_s_s:

        qf = qf2.QuadraticFunction(*coeffs)
        qf.evaluate(xminmax=(xmin, xmax), interval=interval)

        quadfuncs.append(qf)

    qfp.plot(quadfuncs)


if __name__ == "__main__":

    main()