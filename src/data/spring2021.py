from src.Semester import SemesterClass
from src.Course import CourseClass

gesm120 = CourseClass(
    name="GESM 120",
    grades_weights_dict={
        "paper1": [97/100, 20],
        "paper2": [88/100, 20],
        "paper3": [90/100, 20],
        "discussions": [1, 20],
        "attendance": [1, 15],
    },
    passing_grade=60,
    benchmarks={
        "A": 90,
        "A-": 85,
        "B+": 82,
        "B": 78,
        "B-": 75,
        "C+": 70,
        "C": 65,
        "C-": 60,
        "D+": 57,
        "D": 54,
        "D-": 50
    },
)

csci170 = CourseClass(
    name="CSCI 170",
    grades_weights_dict={
        "midterm": [50/100, 20],
        "homeworks": [13/14, 30],
        "quiz1": [91/100, 10],
        "quiz2": [85/100, 10],
        "final": [30/100, 30]
    },
    passing_grade=60,
    benchmarks={
        "A+": 95,
        "A": 90,
        "A-": 85,
        "B+": 82,
        "B": 78,
        "B-": 75,
        "C+": 70,
        "C": 65,
        "C-": 60,
        "D+": 57,
        "D": 54,
        "D-": 50
    },
    pnp=True
)


csci103 = CourseClass(
    name="CSCI 103",
    grades_weights_dict={
        "midterm_written": [61/66, 15],
        "midterm_programming": [100/100, 20],
        "pas": [100/100, 30],
        "labs": [100/100, 10],
        "final": [90/100, 25]
    },
    passing_grade=56,
    benchmarks={
        "A": 94,
        "A-": 90,
        "B+": 86,
        "B": 82,
        "B-": 78,
        "C+": 75,
        "C": 70,
        "C-": 64,
        "D+": 57,
        "D": 56,
        "D-": 50
    },
    assignment_to_desired_lg="final"
)

math407 = CourseClass(
    name="MATH 407",
    grades_weights_dict={
        "midterm": [34/40, 25],
        "quiz1": [27/30, 15],
        "quiz2": [30/30, 15],
        "final": [100/100, 45],
    },
    passing_grade=56,
    benchmarks={
        "A": 93,
        "A-": 90,
        "B+": 86,
        "B": 82,
        "B-": 78,
        "C+": 75,
        "C": 70,
        "C-": 64,
        "D+": 57,
        "D": 56,
        "D-": 50
    },
    desired_letter_grade="A-",
    assignment_to_desired_lg="final"
)

spring2021 = SemesterClass(courses=[gesm120, math407, csci103, csci170])
