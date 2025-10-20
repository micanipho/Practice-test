"""Learning Outcome: Functions"""
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
    try:
        sum = 0
        for i in range(1, n + 1):
            sum += i **2
        return sum
    except ValueError:
        return f"Enter a postive number"

def evaluate_performance(grades: list, min_pass: int):
    """
    Evaluate the performance based on a list of grades and a minimum passing grade.

    Parameters:
    grades (list): A list of integers representing student grades.
    min_pass (int): The minimum average grade required to pass.

    Returns:
    str: "Pass" if the average grade is greater than or equal to min_pass, otherwise "Fail".
    """
    count = 0

    for i in grades:
        count += i
    
    if count/len(grades) >= min_pass:
        return f"pass"
    else:
        return f"fail"

def calculate_cumulative_performance(scores: dict):
    """
    Calculate the cumulative performance based on student scores.

    Parameters:
    scores (dict): A dictionary where keys are subject names and values are the corresponding scores.

    Returns:
    dict: A dictionary containing the average score and a list of subjects where the score is below average.
    """
    average_score = 0
    my_dict = {}
    list_below_average = []
    for x, y in scores.items():
        average_score += y
    average_score = average_score/len(scores)

    for x, y in scores.items():
        if y < average_score:
            list_below_average.append(x)

    my_dict[average_score] = list_below_average

    return my_dict

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
    even_num_list = []

    if n > 0:
        for i in range(1, n + 1):
            if i%2 == 0:
                even_num_list.append(i)

    return even_num_list

def odd_numbers(n: int):
    """
    Generate a list of odd numbers from 1 to n.

    Parameters:
    n (int): The upper limit for generating odd numbers.

    Returns:
    list: A list of odd integers from 1 to n.
    """
    odd_num_list = []

    if n > 0:
        for i in range(1, n + 1):
            if i%3 == 0:
                odd_num_list.append(i)

    return odd_num_list

def sum_multiples_of_num(num: int, length: int):
    """
    Calculate the sum of multiples of a given number up to a specified length.

    Parameters:
    num (int): The number whose multiples are to be summed.
    length (int): The upper limit for the range of multiples.

    Returns:
    int: The sum of multiples of num from 1 to length.
    """
    multiples_list = []
    sum = 0
    count = 1
    while len(multiples_list) < length:
        
        if count % num == 0:
            multiples_list.append(count)
        count += 1

    for x in multiples_list:
        sum += x

    return sum

def skip_num(n: int, length: int):
    """
    Generate a list of numbers from 1 to length, skipping a specific number.

    Parameters:
    n (int): The number to skip.
    length (int): The upper limit for generating numbers.

    Returns:
    list: A list of integers from 1 to length, excluding n.
    """
    my_list = []
    count = 0

    while count < length:
        count += 1
        if count == n:
            continue
        my_list.append(count)
        
    return my_list

def break_test(n: int, length: int):
    """
    Generate a list of numbers from 1 to length, stopping when a specific number is encountered.

    Parameters:
    n (int): The number at which to stop adding to the list.
    length (int): The upper limit for generating numbers.

    Returns:
    list: A list of integers from 1 to length, excluding n and stopping before it.
    """
    my_list = []
    for i in range(1, length + 1):
        if i == n:
            break
        my_list.append(i)
    
    return my_list

def sum_numbers_until_zero(nums: list):
    """
    Calculate the sum of numbers in a list until a zero is encountered.

    Parameters:
    nums (list): A list of integers.

    Returns:
    int: The sum of integers in the list up to (but not including) the first zero.
    """
    sum = 0
    for i in nums:
        sum += i
    
    return sum

def count_positive_numbers(nums: list):
    """
    Count the number of positive integers in a list.

    Parameters:
    nums (list): A list of integers.

    Returns:
    int: The count of positive integers in the list.
    """
    count = 0
    for i in nums:
        if i > 0:
            count += 1
    
    return count

def sum_dictionary_values(dictionary: dict):
    """
    Calculate the sum of all values in a dictionary.

    Parameters:
    dictionary (dict): A dictionary with numeric values.

    Returns:
    int: The sum of all values in the dictionary.
    """
    sum = 0
    for x, y in dictionary.items():
        sum += y
    
    return sum

def sum_unique_elements(elements: list):
    """
    Calculate the sum of unique elements in a list.

    Parameters:
    elements (list): A list of integers.

    Returns:
    int: The sum of unique integers in the list.
    """
    sum = 0
    for i in tuple(elements):
        sum += i
    
    return sum

def skip_divisible_by_num(n: int, length: int):
    """
    Generate a list of numbers from 1 to length, skipping those that are divisible by a specific number.

    Parameters:
    n (int): The number to skip multiples of.
    length (int): The upper limit for generating numbers.

    Returns:
    list: A list of integers from 1 to length, excluding those divisible by n.
    """
    my_list = []
    for i in range(1, length):
        if i % n == 0:
            continue
        my_list.append(i)
    
    return my_list

"""Learning Outcome: Processing Data"""

def square_numbers(nums: list):
    """
    Calculate the square of each number in a list.

    Parameters:
    nums (list): A list of integers.

    Returns:
    list: A list containing the squares of the input integers.
    """
    my_list = []
    for i in nums:
        x = i**2
        my_list.append(x)
    
    return my_list

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
    total = sum(nums)
    average = total/len(nums)

    return (total, average)

def word_frequency_count(words: list[str]):
    """
    Count the frequency of each word in a list.

    Parameters:
    words (list[str]): A list of words.

    Returns:
    dict: A dictionary with words as keys and their frequencies as values.
    """
    my_dict = {}
    for word in words:
        count = words.count(word)
        my_dict[word] = count
    
    return my_dict

def filter_even_numbers(nums: list[int]):
    """
    Filter out even numbers from a list.

    Parameters:
    nums (list[int]): A list of integers.

    Returns:
    list: A list containing only the even integers from the input list.
    """
    my_list = []
    for num in nums:
        if num % 2 == 0:
            my_list.append(num)
    
    return my_list

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
    if not nums:
        raise ValueError("Your list is empty")
    nums.sort()
    n = len(nums)
    if n % 2== 0:
        md1 = nums[n//2 - 1]
        md2 = nums[n//2]
        median = (md1 + md2)/2
        return median
    if n % 2 != 0:
        median = nums[n//2]
        return median

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
    """
    Find the largest number in a list.

    Parameters:
    nums (list[int]): A list of integers.

    Returns:
    int or None: The largest number in the list, or None if the list is empty.
    """
    max_num = 0
    for num in nums:
        if max_num < num:
            max_num = num
    
    return max_num

def is_prime(n: int):
    """
    Check if a number is prime.

    Parameters:
    n (int): The number to check.

    Returns:
    bool: True if the number is prime, False otherwise.
    """
    for i in range(2, n):
        if n % i != 0:
            return True
        else:
            return False
            
def count_character_occurrences(word_sentence: str, char_count: str):
    """
    Count the occurrences of a character in a given sentence.

    Parameters:
    word_sentence (str): The sentence in which to count occurrences.
    char_count (str): The character to count.

    Returns:
    int: The number of occurrences of the character in the sentence.
    """
    count = 0
    for i in word_sentence:
        if char_count == i:
            count += 1
    
    return count