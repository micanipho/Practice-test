# def analyze_improvement(scores: list):
#     """
#     Analyze the improvement trend based on a list of scores.

#     Parameters:
#     scores (list): A list of integers representing scores over time.

#     Returns:
#     dict: A dictionary containing the trend of improvement ("positive", "negative", or "neutral") 
#           and a boolean indicating whether there has been an improvement.
#     """
#     pass

#     scores = [90, 70, 76, 78, 90, 67]

#     improvement = {"positive": True, "negative": False, "neutral": None }
    
# def rank_students(students: list[tuple[str, int]]):
#     """
#     Rank students based on their scores.

#     Parameters:
#     students (list): A list of tuples where each tuple contains a student's name and their score.

#     Returns:
#     list: A sorted list of tuples in descending order based on scores.
#     """
#     pass

# students = [(["aisha", 90]), (["ash", 20]), (["mthunzi", 100]), (["ayanda", 90]), (["ntsika", 60])]
# sort_student = students.sort(reverse=True)
# print(sort_student)
#     # for x in students:

# def sum_multiples_of_num(num: int, length: int):
#     """
#     Calculate the sum of multiples of a given number up to a specified length.

#     Parameters:
#     num (int): The number whose multiples are to be summed.
#     length (int): The upper limit for the range of multiples.

#     Returns:
#     int: The sum of multiples of num from 1 to length.
#     """
#     pass

    # f = x * n * (n + 1)//2
    # return f


def sum_of_squares(n: int):
    if n < 0:
        raise ValueError
    else:
        f = n * (n + 1) * (2 * n + 1)//6
    
    return f
print(sum_of_squares(-5))
    
    





    
