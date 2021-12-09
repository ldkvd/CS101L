#############################################################################
##
## CS 101 Lab
## Lab 13
## Lily Dang
## ldkvd@mail.umkc.edu
##
## PROBLEM:
##
## ALGORITHM:
##  1. Start.
##  2. Import unittest, import Grades, import math.
##  3. Create a class called Grade_test that will test all the test methods.
##      a. Create a method called test_total_returns_total_of_list that will
##         test that total returns 33 when the list 2, 5, 9 is passed.
##      b. Create a method called test_total_returns_0 that will test that
##         total returns 0 when an empty list is passed.
##      c. Create a method called test_average_one that will test that 
##         average returns 5.33333 when the list 2, 59 is passed.
##      d. Create a method called test_average_two that will test that 
##         average returns something 4 decimals close 12.0000 when the list
##      e. Create a method called test_average_returns_nan that will test
##         that average returns math.nan when an empty list is passed.
##      f. Create a method called test_median_when_odd that will test that
##         median returns the median value of list when the length of the 
##         list passed is odd.
##      g. Create a method called test_median_when_even that will test that
##         median returns the median value of list when the lenght of the
##         list passed is even.
##      h. Create a method called test_median when_empy that will test that
##         median raises a ValueError when the list passed is mempty.
##  4. Call unittest in the main. 
##  5. Stop.
##
## ERROR HANDLING:
##      Any Special Error handling to be noted.  Wager not less than 0. etc
##
## OTHER COMMENTS:
##      Any special comments
##
##############################################################################



import unittest
import Grades
import math

class Grade_Test(unittest.TestCase):
    
    def test_total_returns_total_of_list(self):

        result = Grades.total([1, 10,22])
        self.assertEqual(result, 33, 'The total function should return 33')


    def test_total_returns_0(self):
        
        result = Grades.total([])
        self.assertEqual(result, 0, 'The total function should return 0')

    def test_average_one(self):

        result = Grades.average([2, 5, 9])
        self.assertAlmostEqual(result, 5.3333, 4, 'The average function should return 5.3333') 

    def test_average_two(self):

        result = Grades.average([2, 15, 22, 9])
        self.assertAlmostEqual(result, 12, 4, 'The average function should return 12') 

    def test_average_returns_nan(self):

        result = Grades.average([])
        self.assertIs(math.nan, result, 'The average function should return nan') 

    def test_median_one(self):
        '''Test for median when list has an odd amount of numbers'''

        result = Grades.median([2, 5, 1])
        self.assertEqual(result, 2, 'The median function should return 2')

    def test_median_two(self):
        '''Test for median when list has an event amount of numbers'''

        result = Grades.median([5, 2, 1, 3])
        self.assertEqual(result, 2.5, 'The median function should return 2.5')

    def test_median_three(self):
        '''Test that median returns a ValueError when an empty is passed'''

        with self.assertRaises(ValueError):
            result = Grades.median([])

unittest.main()
