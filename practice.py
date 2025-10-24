def rank_students(students: list[tuple[str, int]]):

    """
    Rank students based on their scores.

    Parameters:
    students (list): A list of tuples where each tuple contains a student's name and their score.

    Returns:
    list: A sorted list of tuples in descending order based on scores.
    """

    return sorted(students)

print(rank_students([("Alice", 85), ("Bob", 70), ("Charlie", 90)]))