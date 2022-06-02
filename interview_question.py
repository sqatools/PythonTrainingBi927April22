"""
Write a Python class to find the three elements that sum to zero from a set of n real numbers.
Input array : [-25, -10, -7, -3, 2, 4, 8, 10]
Output : [[-10, 2, 8], [-7, -3, 10]]

Write a program to create all combination of a string based on given number.
  - print list(combination('abc',3)

abc, acb, bca, bac cab, cba
"""

class GetSum:

    def __init__(self, input_list):
        self.input_list = input_list

    def get_three_number_sum_zero(self):
        result_list = []
        for i in range(len(self.input_list)):
            for j in range(len(self.input_list)):
                for k in range(len(self.input_list)):
                    if self.input_list[i] + self.input_list[j] + self.input_list[k] == 0:
                        result_list.append([self.input_list[i], self.input_list[j], self.input_list[k]])
        return result_list

    def approach2(self):
        pass

    def get_combintion(self, str1):
        result = []
        for i in range(len(str1)):
            for j in range(i, len(str1)):
                for k in range(j, len(str1)):
                        if i != j and i != k:
                            print(i, j, k)

if __name__ == '__main__':
    obj = GetSum([4, 6, 8])
    print(obj.get_combintion('abc'))






