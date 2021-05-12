from src.data import fall2020, spring2021
from src.College import CollegeClass

semesters = [fall2020, spring2021]
usc = CollegeClass(semesters=semesters)

usc.print_cumulative_college_report()
