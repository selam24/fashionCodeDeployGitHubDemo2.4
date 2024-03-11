# -*- coding: utf-8 -*-
"""
Created on Sun Feb 18 18:11:55 2024

@author: soul
"""
#class name
class math_operation:
    #forming a constructor
    def __init__(self, Q, W):
      self.Q = Q
      self.W = W
    
    # the Sum of two variables
    def Sum_variables(self):
       A = self.Q + self.W
       return A
      
    # the Product of two variables    
    def Product_variables(self):
        B = self.Q * self.W
        return B

    # the Difference of two variables
    def Difference_variables(self):
        C = self.Q - self.W
        return C

    # the Quotient of two variables
    def Quotient_variables(self):
        D = self.Q / self.W
        return D

week_4math = math_operation(8,6)
add = week_4math.Sum_variables()
mult = week_4math.Product_variables()
sub = week_4math.Difference_variables()
div = week_4math.Quotient_variables()

print(add,mult,sub,div)
