"""Learning Outcome: Functions"""
def sum_of_squares(n: int):
    if n < 0:
        raise ValueError
    else:
        f = n * (n + 1) * (2 * n + 1)//6
    
    return f
print(sum_of_squares(1))

# ==============================================================================
# Q1
# ==============================================================================
    

def evaluate_performance(grades: list, min_pass: int):
    ave = sum(grades)//len(grades)
    

    for i in grades:
        if ave >= min_pass:
            return "Pass"
        else: 
            return "Fail"
    return 

grades = [22, 54, 32, 17, 2, 20]
min_pass = 30
print(evaluate_performance(grades,min_pass))

# ==============================================================================
# Q2
# ==============================================================================

def calculate_cumulative_performance(scores: dict):
    """
    Calculate the cumulative performance based on student scores.

    Parameters:
    scores (dict): A dictionary where keys are subject names and values are the corresponding scores.

    Returns:
    dict: A dictionary containing the average score and a list of subjects where the score is below average.
    """
    pass

# =================================================================================
# Q3
# =================================================================================

def analyze_improvement(scores: list):
    """
    Analyze the improvement trend based on a list of scores.

    Parameters:
    scores (list): A list of integers representing scores over time.

    Returns:
    dict: A dictionary containing the trend of improvement ("positive", "negative", or "neutral") 
          and a boolean indicating whether there has been an improvement.
    """
    pass


# =================================================================================
# Q4
# =================================================================================


def rank_students(students: list[tuple[str, int]]):
    """
    Rank students based on their scores.

    Parameters:
    students (list): A list of tuples where each tuple contains a student's name and their score.

    Returns:
    list: A sorted list of tuples in descending order based on scores.
    """
    pass

# =================================================================================
# Q5
# =================================================================================

"""Learning Outcome: Basic Loops"""
def even_numbers(n: int):

    even_list = []
    for x in range(n + 1):
        if x%2 == 0:
            even_list.append(x)
    return even_list

even_numbers(10)


# =================================================================================
# Q6
# =================================================================================

def odd_numbers(n: int):
      
    odd_list = []
    for x in range(n + 1):
        if x%2 != 0:
            odd_list.append(x)
    return odd_list

odd_numbers(10)

# =================================================================================
# Q7
# =================================================================================

def sum_multiples_of_num(num: int, length: int):
    """
    Calculate the sum of multiples of a given number up to a specified length.

    Parameters:
    num (int): The number whose multiples are to be summed.
    length (int): The upper limit for the range of multiples.

    Returns:
    int: The sum of multiples of num from 1 to length.
    """
    pass

# =================================================================================
# Q8
# =================================================================================

def skip_num(n: int, length: int):

    list = []

    for x in range(length + 1):
        if x == n:
            continue
        list.append(x)
        
    return list

print(skip_num(2, 10))



# =================================================================================
# Q9
# =================================================================================

def break_test(n: int, length: int):

    list = []

    for x in range(length + 1):
        list.append(x)
        if x == n:
            break
        
    return list

print(skip_num(2, 10))

# =================================================================================
# Q10
# =================================================================================

def sum_numbers_until_zero(nums: list):
    
    list = []    

    for i in nums:
        if i == 0:
            break
        else:
            list.append(i)
    
    return sum(list)

nums = [1, 2, 3, 4, 0, 5, 6, 7]
        
print(sum_numbers_until_zero(nums))



# =================================================================================
# Q2
# =================================================================================

def count_positive_numbers(nums: list):
    """
    Count the number of positive integers in a list.

    Parameters:
    nums (list): A list of integers.

    Returns:
    int: The count of positive integers in the list.
    """
    pass

# =================================================================================
# Q2
# =================================================================================

def sum_dictionary_values(dictionary: dict):
    """
    Calculate the sum of all values in a dictionary.

    Parameters:
    dictionary (dict): A dictionary with numeric values.

    Returns:
    int: The sum of all values in the dictionary.
    """
    pass

# =================================================================================
# Q2
# =================================================================================

def sum_unique_elements(elements: list):
    """
    Calculate the sum of unique elements in a list.

    Parameters:
    elements (list): A list of integers.

    Returns:
    int: The sum of unique integers in the list.
    """
    pass

# =================================================================================
# Q2
# =================================================================================

def skip_divisible_by_num(n: int, length: int):
    """
    Generate a list of numbers from 1 to length, skipping those that are divisible by a specific number.

    Parameters:
    n (int): The number to skip multiples of.
    length (int): The upper limit for generating numbers.

    Returns:
    list: A list of integers from 1 to length, excluding those divisible by n.
    """
    pass

"""Learning Outcome: Processing Data"""

# =================================================================================
# Q2
# =================================================================================

def square_numbers(nums: list):
    """
    Calculate the square of each number in a list.

    Parameters:
    nums (list): A list of integers.

    Returns:
    list: A list containing the squares of the input integers.
    """
    pass

# =================================================================================
# Q2
# =================================================================================

def transform_string(input: str, transform: str):
    """
    Transform a string based on the specified transformation type.

    Parameters:
    input (str): The string to be transformed.
    transform (str): The type of transformation ('capitalize', 'upper', 'lower').

    Returns:
    str: The transformed string.

    Raises:
    ValueError: If the transformation type is unknown.
    """
    pass

# =================================================================================
# Q2
# =================================================================================

def sum_and_average(nums: list[int]):
    """
    Calculate the sum and average of a list of numbers.

    Parameters:
    nums (list[int]): A list of integers.

    Returns:
    tuple: A tuple containing the sum and average of the numbers.
    """
    pass

# =================================================================================
# Q2
# =================================================================================

def word_frequency_count(words: list[str]):
    """
    Count the frequency of each word in a list.

    Parameters:
    words (list[str]): A list of words.

    Returns:
    dict: A dictionary with words as keys and their frequencies as values.
    """
    pass

# =================================================================================
# Q2
# =================================================================================

def filter_even_numbers(nums: list[int]):
    """
    Filter out even numbers from a list.

    Parameters:
    nums (list[int]): A list of integers.

    Returns:
    list: A list containing only the even integers from the input list.
    """
    pass

"""Learning Outcome: Simple Algorithms(Problem Solving)"""

# =================================================================================
# Q2
# =================================================================================

def find_median(nums: list[int]):
    """
    Find the median of a list of numbers.

    Parameters:
    nums (list[int]): A list of integers.

    Returns:
    float: The median value of the list.

    Raises:
    ValueError: If the list is empty.
    """
    pass

# =================================================================================
# Q2
# =================================================================================

def reverse_string(input: str):
    """
    Reverse the given string.

    Parameters:
    input (str): The string to be reversed.

    Returns:
    str: The reversed string.
    """
    pass

# =================================================================================
# Q2
# =================================================================================

def largest_number(nums: list[int]):
    """
    Find the largest number in a list.

    Parameters:
    nums (list[int]): A list of integers.

    Returns:
    int or None: The largest number in the list, or None if the list is empty.
    """
    pass

# =================================================================================
# Q2
# =================================================================================

def is_prime(n: int):
    """
    Check if a number is prime.

    Parameters:
    n (int): The number to check.

    Returns:
    bool: True if the number is prime, False otherwise.
    """
    pass

# =================================================================================
# Q2
# =================================================================================

def count_character_occurrences(word_sentence: str, char_count: str):
    """
    Count the occurrences of a character in a given sentence.

    Parameters:
    word_sentence (str): The sentence in which to count occurrences.
    char_count (str): The character to count.

    Returns:
    int: The number of occurrences of the character in the sentence.
    """
    pass