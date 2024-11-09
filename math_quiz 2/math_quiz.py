import random


def originate_number_random(min, max):
    # changed function name (function_A --> originate_number_random)
    """
    Returns random number within given range.

    Args:
        param1 (int): Start of the range.
        param2 (int): End of the range.

    Returns:
        (int): Random number from the range.

    Raises:
        ValueError: When the input type is not an integer.
    """
    return random.randint(min, max)


def originate_operator_random():
    # changed function name (function_B --> originate_operator_random)
    """
    Returns random operator from the given operators.

    Args:
        None.

    Returns:
        (String): Random operator.        
    """
    return random.choice(['+', '-', '*'])


def originate_question_return_solution(n1, n2, o): 
    # changed function name (function_C --> originate_question_return_solution)
    # renamed variables (a --> computed_answer, p --> question)

    """
    Returns an object with mathematic question and it's solution.

    Args:
        param1 (int): First random number. 
        param2 (int): Second random number.
        param3 (String): an operator from add, subtract, multiply.

    Returns:
        (String),(int): Mathematical question by concatinating input params and operators provided of the generated question.

    Raises:
         ValueError: If the input type in't an integer.        
    """

    question = f"{n1} {o} {n2}" 

    if o == '+': computed_answer = n1 + n2 
    #if o == '+': a = n1 - n2, the n1-n2 will be changed with + sign

    elif o == '-': computed_answer = n1 - n2 
    #elif o == '-': a = n1 + n2, the n1+n2 sign will be changed with - sign 
    
    else: computed_answer = n1 * n2
    return question, computed_answer 

def math_quiz():

    # renamed variable (t_q --> no_of_ques)
    s = 0

    no_of_ques = 2 
    # t_q = 3.14159265359 This is a float value and we can't use this to define range in for loop thus changed the value to an integer value = 3

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    for _ in range(no_of_ques):

        n1 = originate_number_random(1, 10)
        n2 = originate_number_random(1,5)
        # n2 = function_A(1, 5.5) as 5.5 is a float value, I changed it to 5 so that it doesn't throw any error while calling function_A
        o = originate_operator_random()

        QUESTION, COMPUTED_ANSWER = originate_question_return_solution(n1, n2, o)
        print(f"\nQuestion: {QUESTION}")

        try : 
            #using try-except block to handle error when user inputs a value that is not an integer
            useranswer = input("Your answer: ")

        except ValueError:
            print("Enter an Integer Value")
            continue   
            #to the next iteration, skipping this one

        useranswer = int(useranswer)

        if useranswer == COMPUTED_ANSWER:
            print("Correct! You earned a point.")
            s = s+1
            # s += -(-1), overly complicated replaced with s = s+1

        else:
            print(f"Wrong answer. The correct answer is {COMPUTED_ANSWER}.")

    print(f"\nGame over! Your score is: {s}/{no_of_ques}")

if __name__ == "__main__":
    math_quiz()
