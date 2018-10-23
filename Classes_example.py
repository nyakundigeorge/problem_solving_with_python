# Euclid's Algorithm. states that the greatest common divisor of two integers m and n is n if n divides
# m evenly. However, if n does not divide m evenly, then the answer is the greatest common divisor of n and the 
# remainder of m divided by n.
# The GCD algorithm only works when the denominator is positive.


def gcd(m,n):
    while m % n != 0:
         old_m = m
         old_n = n

         m = old_n
         n = old_m % old_n
    return n


class Fraction:

    def __init__ (self,top,bottom):
        self.num = top
        self.den = bottom

    def __str__ (self):
        return str(self.num) + "/" + str(self.den)


    def __add__ (self, other_fraction):
        new_num = self.num * other_fraction.den + self.den * other_fraction.num
        new_den = self.den * other_fraction.den
        common = gcd(new_num,new_den)

        return Fraction(new_num//common, new_den//common)

    def __eq__(self, other):
        first_num = self.num * other.den
        second_num = other.num * self.den

        return first_num == second_num

    def __truediv__(self,other_one):
        num_1 = self.num * other_one.den
        den_1 = self.den * other_one.num

        something = gcd(num_1, den_1)

        return Fraction(num_1//something, den_1//something)

    def __mul__(self,other_two):
        numerator = self.num * other_two.num
        denominator = self.den * other_two.den

        common_val = gcd(numerator,denominator)

        return Fraction(numerator//common_val, denominator//common_val)

    def __sub__(self,to_subtract):
        upper_1 = (self.num * to_subtract.den) - (self.den * to_subtract.num)
        lower_1 = self.den * to_subtract.den

        common_one = gcd(upper_1, lower_1)

        return Fraction(upper_1//common_one, lower_1//common_one)

    def __gt__(self,to_compare):
        left_side = self.num * to_compare.den
        right_side = self.den * to_compare.num

        return True if left_side > right_side else  False

    def __le__(self,to_compare):
        left_side = self.num * to_compare.den
        right_side = self.den * to_compare.num

        return True if left_side < right_side else  False


   



# my_f = Fraction(4,5)

# print(gcd(20,10))
f1 = Fraction(1,4)
f2 = Fraction(1,2)

f3 = f1 * f2
f4 = f1 / f2
f5 = f1 - f2
f6 = f1 > f2
f7 = f1 < f2

print("Multiplication:\t" + str(f1) +" and " + str(f2) +" = " +str(f3))
print("Division: \t" + str(f1) +" and " + str(f2) +" = " +str(f4))
print("Subtraction: \t" + str(f1) +" and " + str(f2) +" = " +str(f5))
print("Comparison: \t" + str(f1) +" > " + str(f2) +" = " +str(f6))
print("Comparison: \t" + str(f1) +" < " + str(f2) +" = " +str(f7))
