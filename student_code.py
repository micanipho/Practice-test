"""Learning Outcome: Functions"""
def sum_of_squares(n: int):
    
    if n < 0:
        raise ValueError
    
    results = []
    for i in range(n+1):
        square_number = i ** 2
        results.append(square_number)
        
    return sum(results)

def evaluate_performance(grades: list, min_pass: int):
    
    if (sum(grades) / len(grades)) >= min_pass:
        return "Pass"
    else:
        return "Fail"

def calculate_cumulative_performance(scores: dict):
    
    if not scores:
        return {"average": 0, "below_average": []}
    
    total_score = sum(scores.values())
    average_score = round((total_score / len(scores)), 2)
    
    below_average_score = [subject for subject, score in scores.items() if score < average_score]
    
    return {"average": average_score, "below_average": below_average_score}
    

def analyze_improvement(scores: list):

    results = {}
    for i in scores:
        if i < i + 1:
            results["trend"] = "positive"
            results["improved"] = True
        elif i > i + 1:
            results["trend"] = "negative"
            results["improved"] = False
        else:
            results["trend"] = "neutral"
            results["improved"] = False
    
    return results


def rank_students(students: list[tuple[str, int]]):
    
    return sorted(students, key=lambda student: student[1], reverse=True)


"""Learning Outcome: Basic Loops"""
def even_numbers(n: int):
    
    return [num for num in range(1, n + 1) if num % 2 == 0]


def odd_numbers(n: int):
    
    return [num for num in range(1, n + 1) if num % 2 != 0]


def sum_multiples_of_num(num: int, length: int):
    
    sum = 0
    for i in range(1, length + 1):
        sum += i * num

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
    return [num for num in range(1, length + 1) if num != n]


def break_test(n: int, length: int):
    
    results = []
    for i in range(1, length + 1):
        if i == n:
            break
            
        results.append(i)
    return results


def sum_numbers_until_zero(nums: list):
    
    result = []
    for n in nums:
        if 0 == n:
            break
        result.append(n)
    return sum(result)

def count_positive_numbers(nums: list):
    
    count = 0
    for n in nums:
        if n > 0:
            count += 1
    return count


def sum_dictionary_values(dictionary: dict):
    
    return sum(dictionary.values())

def sum_unique_elements(elements: list):
    
    result = []
    for el in elements:
        if el not in result:
            result.append(el)
    return sum(result)


def skip_divisible_by_num(n: int, length: int):
    
    result = []
    for i in range(1, length + 1):
        if i % n == 0:
            continue
        result.append(i)
    return result

"""Learning Outcome: Processing Data"""

def square_numbers(nums: list):
    
    return [n**2 for n in nums]

def transform_string(input: str, transform):
   
    if transform == "capitalize":
        return input.capitalize()
    elif transform == "uppercase":
        return input.upper()
    elif transform == "lowercase":
        return input.lower()
    else:
        raise ValueError

def sum_and_average(nums: list[int]):
    
    sum_of_nums = sum(nums)
    average = sum_of_nums / len(nums)
    return sum_of_nums, average

def word_frequency_count(words: list[str]):
    
    result = {}
    for w in words:
        result[w] = result.get(w, 0) + 1
    return result

def filter_even_numbers(nums: list[int]):
    
    return [n for n in nums if n % 2 == 0] 

"""Learning Outcome: Simple Algorithms(Problem Solving)"""

def find_median(nums: list[int]):
    
    if not nums:
        raise ValueError
    
    nums.sort()
    length = len(nums)
    mid_nums = length // 2

    if length % 2 == 0:
        return (nums[mid_nums - 1] + nums[mid_nums]) / 2
    else:
        return float(nums[mid_nums])

def reverse_string(input: str):
    
    return input[::-1]

def largest_number(nums: list[int]):
    
    if not nums:
        return None
    return max(nums)

def is_prime(n: int):
    
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

def count_character_occurrences(word_sentence: str, char_count: str):
    
    return word_sentence.count(char_count)