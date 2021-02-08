import unittest


# define the triangle
def classifyTriangle(a, b, c):
    length = [a, b, c]
    length.sort()
    if (length[0] + length[1] > length[2]):
        if(a == b and a == c):
            return 'Equilateral'
        elif(a == b or a == c or b == c):
            return 'Isosceles'
        elif(length[0]**2 + length[1]**2 == length[2]**2):
            return 'Right'
        else:
            return 'Scalene'
    else:
        return 'Not a Triangle'


# print the result
def runClassifyTriangle(a, b, c):
    print('classifyTriangle(', a, ',', b, ',', c, ')=', classifyTriangle(a, b, c), sep="")


# test
class TestClassifyTriangle(unittest.TestCase):
    # test invalid inputs
    def testSet1(self):
        self.assertEqual(classifyTriangle(3, 4, 5), 'Right')

    def testSet2(self):
        self.assertEqual(classifyTriangle(1, 1, 1), 'Equilateral')

    def testSet3(self):
        self.assertEqual(classifyTriangle(4, 4, 5), 'Equilateral')

    def testSet4(self):
        self.assertEqual(classifyTriangle(4, 5, 3), 'Scalene')

    def testSet5(self):
        self.assertEqual(classifyTriangle(10, 1, 1), 'Not a Triangle')


if __name__ == '__main__':
    unittest.main(exit=False)
