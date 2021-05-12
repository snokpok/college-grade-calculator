from src.Course import CourseClass
from typing import List


class SemesterClass:
    def __init__(self, gpa: float = None, courses: List[CourseClass] = []):
        self.courses = courses
        self.gpa = gpa

    def get_semester_gpa(self) -> float:
        if len(self.courses) > 0:
            tot_gpa = 0
            non_pnps = 0
            for course in self.courses:
                if not course.pnp:
                    tot_gpa += course.gpa
                    non_pnps += 1
            return round(tot_gpa/non_pnps, 2)
        else:
            return self.gpa

    def print_semester_report(self) -> None:
        for course in self.courses:
            print("\t")
            course.print_course_stats()
        print(
            f"\n---> SEMESTER GPA: {self.get_semester_gpa()} <---"
        )
