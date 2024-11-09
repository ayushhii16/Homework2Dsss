import unittest
from math_quiz import originate_number_random, originate_operator_random, originate_question_return_solution


class TestMathGame(unittest.TestCase):

    def test_originate_number_random(self):
        # Test if random numbers generated are within the specified range

        min_val = 1
        max_val = 10
        
        for _ in range(1000):  # Test a large number of random values
            rand_num = originate_number_random(min_val, max_val)
            self.assertTrue(min_val <= rand_num <= max_val)


    def test_originate_operator_random(self):
        # Test whether operator returned belongs to operators mentioned or not

        for _ in range(1000):
        #Test for a large number of random values

            arithmeticOperator = originate_operator_random() 
            # To test the function call

            self.assertIn(arithmeticOperator, ['+', '-', '*']) 
            # To check whether the operator returned is among the mentioned operators or not

            self.assertIsInstance(arithmeticOperator, str) 
            # To check whether datatype of operator returned is a string or not


    def test_originate_question_return_solution(self):
            test_cases = [    
                # Test Cases for small numbers
                # Test Cases for large number
                # Test Cases for zero
                # Test Cases for negative numbers  
                
                (5, 2, '+', '5 + 2', 7),
                (8, 3, '-', '8 - 3', 5),
                (6, 8, '*', '6 * 8', 48,),

                (102837, 75845903, '+' ,'102837 + 75845903',75948740),
                (3352, 98473, '-' ,'3352 - 98473', -95121),
                (563, 4658, '*' ,'563 * 4658', 2622454),

                (8, 0, '+','8 + 0', 8),
                (3, 0, '-', '3 - 0', 3),
                (7, 0, '*', '7 * 0', 0),

                (-3, -2, '+', '-3 + -2', -5),
                (-9, 5, '+', '-9 + 5', -4),
                (-6, -4, '-', '-6 - -4', -2),
                (-8, 1, '-', '-8 - 1', -9),
                (-7, -9, '*', '-7 * -9', 63),
                (-5, 1, '*', '-5 * 1', -5)

            ]
            
            for num1, num2, operator, expected_problem, expected_answer in test_cases:
                
                question, answer = originate_question_return_solution(num1, num2, operator) 
                # To generate questions and their solutions for the above mentioned test cases

                self.assertEqual(question, expected_problem , f"Failed for Question : {question}") 
                # To check whether question matches the expected question

                self.assertEqual(answer, expected_answer , f"Failed for Solution : {answer}")
                # To check whther solution matches the expected solution
                


if __name__ == "__main__":
    unittest.main()
