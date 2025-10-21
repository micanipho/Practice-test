"""Learning Outcome: Functions"""
import statistics
def sum_of_squares(n: int):
    """
    Calculate the sum of the squares of all integers from 1 to n.

    Parameters:
    n (int): A non-negative integer up to which the squares will be summed.

    Returns:
    int: The sum of the squares of all integers from 1 to n.

    Raises:
    ValueError: If n is a negative integer.

    """
    if n < 0:
        return ValueError
    total = 0
    for i in range(n):
        total += i ** 2
    return total

def evaluate_performance(grades: list, min_pass: int):
    
    """
    Evaluate the performance based on a list of grades and a minimum passing grade.

    Parameters:
    grades (list): A list of integers representing student grades.
    min_pass (int): The minimum average grade required to pass.

    Returns:
    str: "Pass" if the average grade is greater than or equal to min_pass, otherwise "Fail".
    """

    for grade in grades:
        if grade >= min_pass:
            return "Pass" 
        else:
            return "False"
def calculate_cumulative_performance(scores: dict):
    """
    Calculate the cumulative performance based on student scores.

    Parameters:
    scores (dict): A dictionary where keys are subject names and values are the corresponding scores.

    Returns:
    dict: A dictionary containing the average score and a list of subjects where the score is below average.
    """
    outcome = {
        "average": 0,
        "below_average": []
    }
    average = sum_dictionary_values(scores) / len(scores)

    outcome["average"] = average

    for subjects in scores:
        if scores[subjects] < average:
            outcome["below_average"]
 



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

def rank_students(students: list[tuple[str, int]]):

    """
    Rank students based on their scores.

    Parameters:
    students (list): A list of tuples where each tuple contains a student's name and their score.

    Returns:
    list: A sorted list of tuples in descending order based on scores.
    """
    pass

"""Learning Outcome: Basic Loops"""
def even_numbers(n: int):
    """
    Generate a list of even numbers from 1 to n.

    Parameters:
    n (int): The upper limit for generating even numbers.

    Returns:
    list: A list of even integers from 1 to n.
    """
    even_numbers = []
    for i in range(1, n+1):
        if i % 2 == 0:
            even_numbers.append(i)
    return even_numbers

def odd_numbers(n: int):

    odd_numbers =  []
    for i in range(n):
        if i % 2 != 0:
            odd_numbers.append(i)
    """
    Generate a list of odd numbers from 1 to n.

    Parameters:
    n (int): The upper limit for generating odd numbers.

    Returns:
    list: A list of odd integers from 1 to n.
    """
    return odd_numbers
def sum_multiples_of_num(num: int, length: int):
    """
    Calculate the sum of multiples of a given number up to a specified length.

    Parameters:
    num (int): The number whose multiples are to be summed.
    length (int): The upper limit for the range of multiples.

    Returns:below_average
    int: The sum of multiples of num from 1 to length.
    """

def skip_num(n: int, length: int):

    """
    Generate a list of numbers from 1 to length, skipping a specific number.

    Parameters:
    n (int): The number to skip.
    length (int): The upper limit for generating numbers.

    Returns:
    list: A list of integers from 1 to length, excluding n.
    """

    num_list = []
    for i in range(1, length + 1):
        if i == n:
            continue
        else:
            num_list.append(i)

    return num_list

def break_test(n: int, length: int):

    """
    Generate a list of numbers from 1 to length, stopping when a specific number is encountered.

    Parameters:
    n (int): The number at which to stop adding to the list.
    length (int): The upper limit for generating numbers.

    Returns:
    list: A list of integers from 1 to length, excluding n and stopping before it.
    """

    num_list = []
    for i in range(1, length):
        if i == n:
            break
        else:
            num_list.append(i)
    return num_list

def sum_numbers_until_zero(nums: list):

    """
    Calculate the sum of numbers in a list until a zero is encountered.

    Parameters:
    nums (list): A list of integers.

    Returns:
    int: The sum of integers in the list up to (but not including) the first zero.
    """

    total = 0
    for i in range(len(nums)):
        if nums[i] == 0:
            break
        else:
            total += nums[i]
    return total

def count_positive_numbers(nums: list):

    """
    Count the number of positive integers in a list.

    Parameters:
    nums (list): A list of integers.

    Returns:
    int: The count of positive integers in the list.
    """
    
    total = 0
    for i in range(len(nums)):
        if nums[i] > 0:
            total += 1
    return total

def sum_dictionary_values(dictionary: dict):
    """
    Calculate the sum of all values in a dictionary.

    Parameters:
    dictionary (dict): A dictionary with numeric values.

    Returns:
    int: The sum of all values in the dictionary.
    """
    total = 0
    for value in dictionary:
        total += dictionary[value]

    return total


def sum_unique_elements(elements: list):

    """
    Calculate the sum of unique elements in a list.

    Parameters:
    elements (list): A list of integers.

    Returns:
    int: The sum of unique integers in the list.
    """

    unique_elements = []
    for number in elements:
        if number not in unique_elements:
            unique_elements.append(number)

    return sum(unique_elements)
        

def skip_divisible_by_num(n: int, length: int):
    num_list = []
    for i in range(length):
        if i % n == 0:
            continue
        else:
            num_list.append(i)
    """
    Generate a list of numbers from 1 to length, skipping those that are divisible by a specific number.

    Parameters:
    n (int): The number to skip multiples of.
    length (int): The upper limit for generating numbers.

    Returns:
    list: A list of integers from 1 to length, excluding those divisible by n.
    """
    return num_list

"""Learning Outcome: Processing Data"""

def square_numbers(nums: list):
    nums_list = [num * num for num in nums]
    """
    Calculate the square of each number in a list.

    Parameters:
    nums (list): A list of integers.

    Returns:
    list: A list containing the squares of the input integers.
    """
    return nums_list

def transform_string(input: str, transform: str):

    if transform.lower() == 'capitalize':
        return input.capitalize()
    
    elif transform.lower() == "upper":
        return input.upper()
    
    elif transform.lower() == "lower":
        return input.lower()
    
    else:
        raise ValueError
    """
    Transform a string based on the specified transformation type.

    Parameters:
    input (str): The string to be transformed.
    transform (str):     passThe type of transformation ('capitalize', 'upper', 'lower').

    Returns:
    str: The transformed string.

    Raises:
    ValueError: If the transformation type is unknown.
    """
def sum_and_average(nums: list[int]):
    """
    Calculate the sum and average of a list of numbers.

    Parameters:
    nums (list[int]): A list of integers.

    Returns:
    tuple: A tuple containing the sum and average of the numbers.
    """
    return (sum(nums), (sum(nums)/len(nums)))

def word_frequency_count(words: list[str]):

    """
    Count the frequency of each word in a list.

    Parameters:
    words (list[str]): A list of words.

    Returns:
    dict: A dictionary with words as keys and their frequencies as values.
    """
    word_count = {}

    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    return word_count


def filter_even_numbers(nums: list[int]):

    nums_list = [num for num in nums if num % 2 == 0]
    """
    Filter out even numbers from a list.

    Parameters:
    nums (list[int]): A list of integers.

    Returns:
    list: A list containing only the even integers from the input list.
    """
    return nums_list

"""Learning Outcome: Simple Algorithms(Problem Solving)"""

def find_median(nums: list[int]):

    return statistics.median(nums)
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
def reverse_string(input: str):
    """
    Reverse the given string.

    Parameters:
    input (str): The string to be reversed.

    Returns:
    str: The reversed string.
    """
    return input[::-1]

def largest_number(nums: list[int]):
    if len(nums) == 0:
        return None
    else:
        nums = sorted(nums)
        largest_number = nums[-1]
    """
    Find the largest number in a list.

    Parameters:
    nums (list[int]): A list of integers.

    Returns:
    int or None: The largest number in the list, or None if the list is empty.
    """
    return largest_number
def is_prime(n: int):
    factors = []
    for i in range(1, n+1):
        if n % i == 0:
            factors.append(i)
    if len(factors) == 2:
        return True
    else:
        return False
    """
    Check if a number is prime.

    Parameters:
    n (int): The number to check.

    Returns:
    bool: True if the number is prime, False otherwise.
    """


def count_character_occurrences(word_sentence: str, char_count: str):

    char_counter = 0

    for el in word_sentence:
        if el == char_count:
            char_counter += 1
    """
    Count the occurrences of a character in a given sentence.

    Parameters:
    word_sentence (str): The sentence in which to count occurrences.
    char_count (str): The character to count.

    Returns:
    int: The number of occurrences of the character in the sentence.
    """
    return char_counter
