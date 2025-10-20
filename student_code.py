"""Learning Outcome: Functions"""
def sum_of_squares(n: int):
    if n < 0:
        raise ValueError
    elif n == 0:
        f = 0
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
min_pass = 75
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
# Q11
# =================================================================================

def count_positive_numbers(nums: list):
    count = 0

    for i in nums:
        if i >= 0:
            count += 1
    return count

nums = [1,2,0,-1,-2, 4,]

print(count_positive_numbers(nums))

# =================================================================================
# Q2
# =================================================================================

def sum_dictionary_values(dictionary: dict):

    summ = 0
    for value in dictionary.values():
        summ += value

    return summ

dictionary = {1: 4, 2: 3, 3: 2}

print(sum_dictionary_values(dictionary))

# =================================================================================
# Q2
# =================================================================================

def sum_unique_elements(elements: list):

    unique = set(elements)
    a = sum(unique)
    return a

elements = [1,2,3,1,2,4,5]
print(sum_unique_elements(elements))

# =================================================================================
# Q2
# =================================================================================

def skip_divisible_by_num(n: int, length: int):
    
    list = []

    for i in range(1, length):
        if i%n==0:
            continue
        else:
            list.append(i)
    
    return list

print(skip_divisible_by_num(2, 10))

# =================================================================================
# Q2
# =================================================================================

def square_numbers(nums: list):

    list = []

    for i in nums:
        a = i*i
        list.append(a)

    return list

nums = [1,2,3]

print(square_numbers(nums))
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

    a = sum(nums)
    ave = a//len(nums)

    return (a,ave)
nums = [1,2,3,4,5]

print(sum_and_average(nums))


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

    list = []

    for i in nums:
        if i%2==0:
            list.append(i)
    return list
    
nums = [1,2,3,4,5,6,7,8,9,10,11]

print(filter_even_numbers(nums))

# =================================================================================
# Q2
# =================================================================================

def find_median(nums: list[int]):

    if nums == []:
            raise ValueError 

    for i in nums:
        if i%2==0:
            pass #do something
        else:
            return sum(nums)/len(nums)
        
nums = []
nums.sort()        
print(find_median(nums))

# =================================================================================
# Q2
# =================================================================================

def reverse_string(input: str):
    string = input
    reversed_string = input[::-1]

    return reversed_string

print(reverse_string("love"))

# =================================================================================
# Q2
# =================================================================================

def largest_number(nums: list[int]):

    for i in nums:
        i = max(nums)
    return i

nums = [1,3,6,2]

print(largest_number(nums))
# =================================================================================
# Q2
# =================================================================================

def is_prime(n: int):

    if n%2 != 0:
        return True
    else:
        return False
    
print(is_prime(3))

# =================================================================================
# Q2
# =================================================================================

def count_character_occurrences(word_sentence: str, char_count: str):

    count = 0

    for i in word_sentence:
        if i == char_count:
            count +=1

    return count

word_sentence = "wethinkcode"
char_count = "e"

print(count_character_occurrences(word_sentence, char_count))