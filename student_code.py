import random


"""Learning Outcome: Functions"""
def sum_of_squares(n: int):
    total = 0
    try:
        if n == 0:
            return n
        elif n > 0:
            for _ in range(1, n + 1):
                sum = n * n
                total += sum
        return sum
    except:
        raise ValueError

sum_of_squares(5)

def evaluate_performance(grades: list, min_pass: int):
    total_grade = 0
    num_of_grades = 0
    for grade in grades:
        total_grade += grade
    
    # print(total_grade)

    for _ in range(len(grades)):
        num_of_grades += 1

    # print(num_of_grades)

    
    ave_of_grades = total_grade / num_of_grades

    # print(ave_of_grades)

    if ave_of_grades >= min_pass:
        return "Pass"
    elif 0 <= ave_of_grades < min_pass:
        return "Fail"

grades = [15, 35, 55, 75, 95]

min_pass = 39

evaluate_performance(grades, min_pass)
    

def calculate_cumulative_performance(scores: dict):
    """
    Calculate the cumulative performance based on student scores.

    Parameters:
    scores (dict): A dictionary where keys are subject names and values are the corresponding scores.

    Returns:
    dict: A dictionary containing the average score and a list of subjects where the score is below average.
    """
    pass

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
    even_numbers_list = []

    for i in range(1, n + 1):
        if i % 2 == 0:
            even_numbers_list.append(i)

    return even_numbers_list

even_numbers(19)

def odd_numbers(n: int):
    """
    Generate a list of odd numbers from 1 to n.

    Parameters:
    n (int): The upper limit for generating odd numbers.

    Returns:
    list: A list of odd integers from 1 to n.
    """
    odd_numbers_list = []

    for i in range(1, n + 1):
        if i % 2 != 0:
            odd_numbers_list.append(i)

    return odd_numbers_list

odd_numbers(19)

def sum_multiples_of_num(num: int, length: int):
    """
    Calculate the sum of multiples of a given number up to a specified length.

    Parameters:
    num (int): The number whose multiples are to be summed.
    length (int): The upper limit for the range of multiples.

    Returns:
    int: The sum of multiples of num from 1 to length.
    """
    total = 0

    for i in range(1, length + 1):
        sum = i * num
        total += sum

    return total

sum_multiples_of_num(2, 6)

def skip_num(n: int, length: int):
    """
    Generate a list of numbers from 1 to length, skipping a specific number.

    Parameters:
    n (int): The number to skip.
    length (int): The upper limit for generating numbers.

    Returns:
    list: A list of integers from 1 to length, excluding n.
    """
    numbers_list = []

    for i in range(1, length + 1):
        if i == n:
            continue
        else:
            numbers_list.append(i)
    return numbers_list

skip_num(17, 50)       

def break_test(n: int, length: int):
    """
    Generate a list of numbers from 1 to length, stopping when a specific number is encountered.

    Parameters:
    n (int): The number at which to stop adding to the list.
    length (int): The upper limit for generating numbers.

    Returns:
    list: A list of integers from 1 to length, excluding n and stopping before it.
    """
    list_of_numbers = []
    break_list = []

    while len(list_of_numbers) < length:
        list_of_numbers.append(random.randint(1, 10))

    for i in list_of_numbers:
        if i == n:
            return break_list
        else:
            break_list.append(i)

    return break_list

break_test(1, 10)

def sum_numbers_until_zero(nums: list):
    """
    Calculate the sum of numbers in a list until a zero is encountered.

    Parameters:
    nums (list): A list of integers.

    Returns:
    int: The sum of integers in the list up to (but not including) the first zero.
    """
    sum_of_numbers = 0

    for i in nums:
        if i == 0:
            return sum_of_numbers
        else:
            sum_of_numbers += i

sum_numbers_until_zero_nums = [12, 13, 20, 0, 100]

sum_numbers_until_zero(sum_numbers_until_zero_nums)

def count_positive_numbers(nums: list):
    """
    Count the number of positive integers in a list.

    Parameters:
    nums (list): A list of integers.

    Returns:
    int: The count of positive integers in the list.
    """
    count = 0

    for i in count_positive_numbers_nums:
        if i >= 0:
            count += 1

    return count

count_positive_numbers_nums = [1, -2, 3, -4, 5, -6, 7, -8]

count_positive_numbers(count_positive_numbers_nums)

def sum_dictionary_values(dictionary: dict):
    """
    Calculate the sum of all values in a dictionary.

    Parameters:
    dictionary (dict): A dictionary with numeric values.

    Returns:
    int: The sum of all values in the dictionary.
    """
    pass

def sum_unique_elements(elements: list):
    """
    Calculate the sum of unique elements in a list.

    Parameters:
    elements (list): A list of integers.

    Returns:
    int: The sum of unique integers in the list.
    """
    total = 0
    sum_unique_elements_set = set(sum_unique_elements_nums)

    for i in sum_unique_elements_set:
        total += i

    return(total)

sum_unique_elements_nums = [1, 2, 3, 4, 5, 2, 3]

sum_unique_elements(sum_unique_elements_nums)

def skip_divisible_by_num(n: int, length: int):
    """
    Generate a list of numbers from 1 to length, skipping those that are divisible by a specific number.

    Parameters:
    n (int): The number to skip multiples of.
    length (int): The upper limit for generating numbers.

    Returns:
    list: A list of integers from 1 to length, excluding those divisible by n.
    """
    num_list = []
    for i in range(1, length + 1):
        if i % n == 0:
            continue
        else:
            num_list.append(i)
    return num_list

# print(skip_divisible_by_num(3, 16))

"""Learning Outcome: Processing Data"""


def square_numbers(nums: list):
    """
    Calculate the square of each number in a list.

    Parameters:
    nums (list): A list of integers.

    Returns:
    list: A list containing the squares of the input integers.
    """
    squared_numbers = []

    for i in list_of_square_num:
        square_num = i * i
        squared_numbers.append(square_num)

    return squared_numbers

list_of_square_num = [1, 2, 3, 4, 5]

square_numbers(list_of_square_num)

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

def sum_and_average(nums: list[int]):
    """
    Calculate the sum and average of a list of numbers.

    Parameters:
    nums (list[int]): A list of integers.

    Returns:
    tuple: A tuple containing the sum and average of the numbers.
    """
    total = 0

    new_list = []

    for i in sum_and_average_list:
        total += i

    average = total / len(sum_and_average_list)

    new_list.append(total)
    new_list.append(average)
    sum_and_average_set = set(new_list)
     
    return sum_and_average_set

sum_and_average_list = [1, 2, 3, 4, 5]

sum_and_average(sum_and_average_list)

def word_frequency_count(words: list[str]):
    """
    Count the frequency of each word in a list.

    Parameters:
    words (list[str]): A list of words.

    Returns:
    dict: A dictionary with words as keys and their frequencies as values.
    """
    pass

def filter_even_numbers(nums: list[int]):
    """
    Filter out even numbers from a list.

    Parameters:
    nums (list[int]): A list of integers.

    Returns:
    list: A list containing only the even integers from the input list.
    """
    even_nums = []

    for i in filtering_nums:
        if i % 2 == 0:
            even_nums.append(i)

    return even_nums

filtering_nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]

filter_even_numbers(filtering_nums)

"""Learning Outcome: Simple Algorithms(Problem Solving)"""

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

median_nums = [1, 2, 3, 4, 5]

# print(find_median(median_nums))

def reverse_string(input: str):
    """
    Reverse the given string.

    Parameters:
    input (str): The string to be reversed.

    Returns:
    str: The reversed string.
    """
    return reverse_string_input[::-1]

reverse_string_input = "qwerty"

reverse_string(reverse_string_input)

def largest_number(nums: list[int]):
    """
    Find the largest number in a list.

    Parameters:
    nums (list[int]): A list of integers.

    Returns:
    int or None: The largest number in the list, or None if the list is empty.
    """
    largest_num = 0

    for i in largest_number_nums:
        if i > largest_num:
            largest_num = i
            # print(largest_num)
    return largest_num

largest_number_nums = [1, 3, 5, 9, 3, 7, 4, 6]

largest_number(largest_number_nums)

def is_prime(n: int):
    """
    Check if a number is prime.

    Parameters:
    n (int): The number to check.

    Returns:
    bool: True if the number is prime, False otherwise.
    """
    for i in range(2, n):
        if i % n == 0:
            return False
        else:
            return True
    
is_prime(7)

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
