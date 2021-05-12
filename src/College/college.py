from typing import List


class CollegeClass:
    def __init__(self, semesters: List):
        self.semesters = semesters

    def get_cumulative_gpa(self) -> float:
        cum_gpa: float = 0.0
        semesters_count: int = 0
        for sem in self.semesters:
            cum_gpa += sem.get_semester_gpa()
            semesters_count += 1
        return cum_gpa / semesters_count

    def print_cumulative_college_report(self) -> None:
        for sem in self.semesters:
            sem.print_semester_report()
        print(
            f"\nCUMULATIVE GPA: {self.get_cumulative_gpa()}"
        )
