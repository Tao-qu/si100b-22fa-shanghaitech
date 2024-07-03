class Polynomial:
    #################### Task1 #######################
    def __init__(self, coeffs):
        self.coeffs = coeffs

    def __str__(self):
        coeffs = self.coeffs[:]
        for i in range(len(coeffs)-1, 0, -1):
            if coeffs[i] == 0:
                del coeffs[i]
            else:
                break
        
        ostr = "0"
        for i in range(len(coeffs)):
            if i == 0:
                ostr = str(coeffs[0])
            elif i == 1:
                ostr = ostr + " + " + str(coeffs[1]) + "x"
            else:
                ostr = ostr + " + " + str(coeffs[i]) + "x^" + str(i)

        return ostr

    def deg(self):
        coeffs = self.coeffs[:]
        for i in range(len(coeffs)-1, 0, -1):
            if coeffs[i] == 0:
                del coeffs[i]
            else:
                break
        
        return str(len(coeffs)-1)

    def evaluate(self, x):
        oeva = self.coeffs[0]
        for i in range(1, len(self.coeffs)):
            oeva = oeva + self.coeffs[i] * x ** i
        return oeva

    #################### Task2 #######################
    def __neg__(self):
        coeffs_neg = self.coeffs[:]
        for i in range(len(coeffs_neg)):
            coeffs_neg[i] = -coeffs_neg[i]
        return Polynomial(coeffs_neg)

    def __add__(self, other):
        coeffs_add = [0 for i in range(
            max(len(self.coeffs), len(other.coeffs)))]
        for i in range(len(coeffs_add)):
            if i >= len(self.coeffs):
                coeffs_add[i] = other.coeffs[i]
            elif i >= len(other.coeffs):
                coeffs_add[i] = self.coeffs[i]
            else:
                coeffs_add[i] = self.coeffs[i] + other.coeffs[i]
        return Polynomial(coeffs_add)

    def __sub__(self, other):
        coeffs_sub = [0 for i in range(
            max(len(self.coeffs), len(other.coeffs)))]
        for i in range(len(coeffs_sub)):
            if i >= len(self.coeffs):
                coeffs_sub[i] = - other.coeffs[i]
            elif i >= len(other.coeffs):
                coeffs_sub[i] = self.coeffs[i]
            else:
                coeffs_sub[i] = self.coeffs[i] - other.coeffs[i]

        return Polynomial(coeffs_sub)

    def __mul__(self, other):
        p1 = self.coeffs[:]
        p2 = other.coeffs[:]

        def add_poly(p1, p2):
            coeffs = []
            if len(p1) > len(p2):
                p1, p2 = p2, p1
            i = 0
            while i < len(p1):
                coeffs.append(p1[i]+p2[i])
                i += 1
            coeffs = coeffs + p2[len(p1):len(p2)]
            return coeffs

        if len(p1) > len(p2):
            p1, p2 = p2, p1
        zero = []
        coeffs_mul = []
        for i in p1:
            temp = zero[:]
            for j in p2:
                temp.append(i*j)
            coeffs_mul = add_poly(coeffs_mul, temp)
            zero = zero+[0]

        return Polynomial(coeffs_mul)

    #################### Task3 #######################
    def derivate(self, m):
        p = self.coeffs[:]
        for m in range(m):
            coeffs_der = []
            for i in range(1, len(p), 1):
                coeffs_der.append(p[i]*i)
            p = coeffs_der[:]
        
        return Polynomial(coeffs_der)

    def integral(self, m):
        pass

    def definite_integral(self, m, x1, x2):
        pass

########## DON'T MODIFY THE CODE BELOW ##########
if __name__ == "__main__":
    print(eval(input()))
