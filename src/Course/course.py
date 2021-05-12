from src.common.letter_to_gpa import LETTER_TO_GPA


class CourseClass:
    def __init__(self,
                 name: str,
                 grades_weights_dict: dict,
                 passing_grade: int,
                 benchmarks: dict,
                 pnp: bool = False,
                 desired_letter_grade: str = "A",
                 assignment_to_desired_lg: str = None
                 ):
        self.name = name
        self.grades_weights_dict = grades_weights_dict
        self.passing_grade = passing_grade
        self.benchmarks = benchmarks
        self.pnp = pnp
        self.percentage_grade = self.get_final_grade()
        self.gpa = self.get_gpa()
        self.letter_grade = self.get_letter_grade()
        self.desired_letter_grade = desired_letter_grade
        self.assignment_to_desired_lg = assignment_to_desired_lg

    def get_final_grade(self) -> float:
        total = 0
        for assignment in self.grades_weights_dict:
            total += self.grades_weights_dict[assignment][0] * \
                self.grades_weights_dict[assignment][1]
        return round(total, 2)

    def is_passing(self) -> bool:
        return self.get_final_grade() > self.passing_grade

    def get_letter_grade(self) -> str:
        final_grade = self.get_final_grade()

        if not self.pnp:
            for letter in self.benchmarks:
                if final_grade > self.benchmarks[letter]:
                    return letter
            return "F for 'you're Fucked'"

    def get_gpa(self) -> float:
        if not self.pnp:
            return LETTER_TO_GPA[self.get_letter_grade()]

    def what_assigment_score_to_letter(self,
                                       assignment_name: str,
                                       desired_letter_grade: str
                                       ) -> float:
        return self.what_assignment_score_to_percent_grade(
            assignment_name,
            self.benchmarks[desired_letter_grade]
        )

    def what_assignment_score_to_percent_grade(self,
                                               assignment_name: str,
                                               percent_grade: float
                                               ) -> float:
        cumulative_before_finals = 0
        for assignment in self.grades_weights_dict:
            if assignment != assignment_name:
                cumulative_before_finals += self.grades_weights_dict[assignment][0] * \
                    self.grades_weights_dict[assignment][1]
        return round(
            (percent_grade - cumulative_before_finals) /
            self.grades_weights_dict[assignment_name][1] * 100,
            2
        )

    def print_course_stats(self) -> None:
        print("\n")
        print(f"---- YOUR GRADE FOR {self.name} ----")
        for key in self.grades_weights_dict:
            print(
                f"""- {key} {round(self.grades_weights_dict[key][0]*100, 2)
                } % | weight: {self.grades_weights_dict[key][1]} %""")
        print("Percentage:", str(self.get_final_grade()) + "%")
        print("Passing:", self.is_passing())
        if self.assignment_to_desired_lg:
            if not self.pnp:
                print(f"Final's grade to get an {self.desired_letter_grade}:",
                      str(self.what_assigment_score_to_letter("final", self.desired_letter_grade)) + "%")
            else:
                print(f"Final's grade to pass:",
                      str(self.what_assignment_score_to_percent_grade("final",
                          self.passing_grade)) + "%"
                      )
        if not self.pnp:
            print("Letter grade:", self.get_letter_grade())
            print("Course GPA:", self.gpa)
