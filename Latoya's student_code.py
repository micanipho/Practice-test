"""Learning Outcome: Functions"""
def sum_of_squares(n: int):
    for i in range(1, n + 1):
        sum = i ** 2
    return sum
    if n < 0:
        raise ValueError("n must be a postive integer")

def evaluate_performance(grades: list, min_pass: int):
    avg = sum(grades) / len(grades)
    return "Pass" if avg >= min_pass else "Fail"
    if not grades:
        return "Fail"

def calculate_cumulative_performance(scores: dict):
    average = sum(scores.values()) / len(scores)
    below_average = []
    for subject, score in scores.items():
        if score < avg:
        below_average.append(subject)
    return {"average": average, "below_average_subjects": below_average}

    if not scores:
        return {"average": 0, "below_average_subjects": []}

def analyze_improvement(scores: list):
    if len(scores) < 2:
        return {"trend": "neutral", "improved": False}

    diff = scores[-1] - scores[0]

    if diff > 0:
        return {"trend": "positive", "improved": True 
    elif diff < 0:
        return {"trend": "negative", "improved": False}
    else:
         return {"trend": "neutral", "improved": False}
    

def rank_students(students: list[tuple[str, int]]):
    sorted_students = sorted(students, key=get_score, reverse=True)
    return sorted_students

"""Learning Outcome: Basic Loops"""
def even_numbers(n: int):
    for i in range(1, n + 1):
        if i % 2 == 0:
            return i
    pass

def odd_numbers(n: int):
    for i in range(1, n + 1):
        if i % 2 != 0:
            return i

def sum_multiples_of_num(num: int, length: int):
    for i in range(1, length + 1):
        sum = num * i
        return sum
    pass

def skip_num(n: int, length: int):
    for i in range(1, length + 1):
        if i != n:
            return i
def break_test(n: int, length: int):
    result = []
    for i in range(1, length + 1):
        if i == n:
            break
        result.append(i)
    return result
    pass

def sum_numbers_until_zero(nums: list):
    total = 0
    for num in nums:
        if num == 0:
            break
        total += num
    return total
    pass

def count_positive_numbers(nums: list):
    count = 0
    for num in nums:
        if num > 0:
            count += 1
    return count
    pass

def sum_dictionary_values(dictionary: dict):
    return sum(dictionary.values())
    pass

def sum_unique_elements(elements: list):
    return sum(set(elements))
    pass

def skip_divisible_by_num(n: int, length: int):
    result = []
    for i in range(1, length + 1):
        if i % n != 0:
            result.append(i)
    return result
    pass

"""Learning Outcome: Processing Data"""

def square_numbers(nums: list):
    for num in nums:
        square = num ** 2
        return square
    pass

def transform_string(input: str, transform: str):
    if transform == "capitalize":
        return input.capitalize()
    elif transform == "upper":
        return input.upper()
    elif transform == "lower":
        return input.lower()
    else:
        raise ValueError("Unknown transformation type")
    pass

def sum_and_average(nums: list[int]):
    total = sum(nums)
    average = total / len(nums)
    return (total, average)
    if not nums:
        return (0, 0)
    pass

def word_frequency_count(words: list[str]):
    freq = {}
    for word in words:
        freq[word] = freq.get(word, 0) + 1
    return freq
    pass

def filter_even_numbers(nums: list[int]):
    for num in nums:
        if num % 2 == 0:
            return num
    pass

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

def reverse_string(input: str):
    reversed_text = input("Enter Text: ")
    for char in input:
        reversed_text = char + reversed_text
    return reversed_text

    pass

def largest_number(nums: list[int]):
    largest = nums[0]
    for num in nums:
        if num > largest:
            largest = num
    return largest

    if not nums:
        return None
    pass

def is_prime(n: int):
    """
    Check if a number is prime.

    Parameters:
    n (int): The number to check.

    Returns:
    bool: True if the number is prime, False otherwise.
    """
    pass

def count_character_occurrences(word_sentence: str, char_count: str):
    return word_sentence.count(char_count)
    pass
