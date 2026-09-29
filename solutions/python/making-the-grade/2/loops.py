"""Functions for organizing and calculating student exam scores."""


def round_scores(student_scores):
    """Round all provided student scores.

    Parameters:
        student_scores (list[float]): Student exam scores.

    Returns:
        list[int]: Student scores *rounded* to the nearest integer value.
    """
    rounded_score_list = []
    for student_score in student_scores:
        rounded_score_list.append(round(student_score))

    return rounded_score_list
        


def count_failed_students(student_scores):
    """Count the number of failing students out of the group provided.

    Parameters:
        student_scores (list[int]): Student scores as ints.

    Returns:
        int: The count of student scores at or below 40.
    """

    failing_students_count = 0
    for student_score in student_scores:
        if student_score <= 40:
            failing_students_count = failing_students_count + 1

    return failing_students_count


def above_threshold(student_scores, threshold):
    """Determine how many of the provided student scores were 'the best' based on the provided threshold.

    Parameters:
        student_scores (list[int]): Integer scores.
        threshold (int): The threshold to cross to be the "best" score.

    Returns:
        list[int]: Integer scores that are at or above the "best" threshold.
    """

    above_threshold_count = []
    for student_score in student_scores:
        if student_score >= threshold:
            above_threshold_count.append(student_score)

    return above_threshold_count


def letter_grades(highest: int) -> list[int]:
    """Create a list of grade lower thresholds for D, C, B, and A intervals.

    Parameters:
        highest (int): The value of the highest exam score.

    Returns:
        list[int]: Lower threshold scores for each grade interval ["D", "C", "B", "A"].
    """
    failing_threshold = 40
    passing_range = highest - failing_threshold
    
    # Divide the range above failing evenly across 4 grade bands (D, C, B, A)
    step = passing_range // 4
    
    # D starts at failing_threshold + 1, followed by C, B, and A
    return [failing_threshold + 1 + i * step for i in range(4)]
        


def student_ranking(student_scores, student_names):
    """Organize the student's rank, name, and grade information in descending order.

    Parameters:
        student_scores (list): Scores in descending order.
        student_names (list[str]): Student names by exam score in descending order.

    Returns:
        list[str]: Strings in format ["<rank>. <student name>: <score>"].
    """
    rank_list = []
    for i in range(0,len(student_scores)):
        rank_list.append(f"{i+1}. {student_names[i]}: {student_scores[i]}")

    return rank_list
        


def perfect_score(student_info):
    """Create a list that contains the name and grade of the first student to make a perfect score on the exam.

    Parameters:
        student_info (list[list[str, int]]): List of [<student name>, <score>] lists.

    Returns:
        list: First `[<student name>, 100]` found OR `[]` if no student score of 100 is found.
    """
    value = []
    for info in student_info:
        if info[1] == 100:
            value = info
            break
            
    return value
