#Program: Max number out of the product of a group of numbers.
#Author: Abdulnasir Mohammed
#Date: 06/10/15


import unittest
 
NUMB = """\
73167176531330624919225119674426574742355349194934\
96983520312774506326239578318016984801869478851843\
85861560789112949495459501737958331952853208805511\
12540698747158523863050715693290963295227443043557\
66896648950445244523161731856403098711121722383113\
62229893423380308135336276614282806444486645238749\
30358907296290491560440772390713810515859307960866\
70172427121883998797908792274921901699720888093776\
65727333001053367881220235421809751254540594752243\
52584907711670556013604839586446706324415722155397\
53697817977846174064955149290862569321978468622482\
83972241375657056057490261407972968652414535100474\
82166370484403199890008895243450658541227588666881\
16427171479924442928230863465674813919123162824586\
17866458359124566529476545682848912883142607690042\
24219022671055626321111109370544217506941658960408\
07198403850962455444362981230987879927244284909188\
84580156166097919133875499200524063689912560717606\
05886116467109405077541002256983155200055935729725\
71636269561882670428252483600823257530420752963450\
"""
 
 
def split_and_multiply(numb_list):
    numb_list = [int(i) for i in numb_list]#splits strings into a list of numbers
    #print numb_list
    n = 1
    for i in numb_list:
        n *= i
    return n
 
def adjacent_digits_product(numb_str, digits_count):
    start = 0
    end = start + digits_count
    max_num = 0
    for x in range(len(numb_str)):
        num = numb_str[start:end]
        store = split_and_multiply(num)
        start += 1
        end += 1
        max_num = max(max_num, store)
        #print 'store :',store
        #print 'max :',max_num
    return max_num
 
 
class AdjTestCase(unittest.TestCase):
 
    def test_4_digits(self):
        self.assertEqual(adjacent_digits_product(NUMB, 4), 5832)
 
    def test_5_digits(self):
        self.assertEqual(adjacent_digits_product(NUMB, 5), 40824)
 
    def test_13_digits(self):
        self.assertEqual(adjacent_digits_product(NUMB, 13), 23514624000)
 
    def test_17_digits(self):
        self.assertEqual(adjacent_digits_product(NUMB, 17), 5292994896000)
 
    def test_25_digits(self):
        self.assertEqual(adjacent_digits_product(NUMB, 25), 94810963968000000)
 
    def test_50_digits(self):
        self.assertEqual(adjacent_digits_product(NUMB, 50), 71245459770757226566778880000000)
 
 
if __name__ == '__main__':
    unittest.main()
    #print adjacent_digits_product(NUMB, 50)
