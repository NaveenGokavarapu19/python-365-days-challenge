'''
program to calculate a student's result based on two examinations 1 sports event
and 3 activities conducted. The weightage of activities = 30 percent,sports = 20 percent
and examination = 50 percent
'''

ACTIVITIES_WEIGHTAGE = 30.0
SPORTS_WEIGHTAGE = 20.0
EXAMS_WEIGHTAGE = 50.0
EXAMS_TOTAL = 200.0
ACTIVITIES_TOTAL = 60.0
SPORTS_TOTAL = 50.0
exam_score1 = int(input("Enter the marks in the first examination (out of 100): "))
exam_score2 = int(input("Enter the marks in second examination (out of 100): "))
sports_score = int(input("Enter the score obtained in sports activities (out of 50): "))
activities_score1 = int(input("Enter the marks in first activity (out of 20): "))
activities_score2 = int(input("Enter the marks in second activity (out of 20): "))
activities_score3 = int(input("Enter the marks in the third activity (out of 20 ): "))

exam_total = exam_score1 + exam_score2 
activities_total = activities_score1 + activities_score2 + activities_score3
exam_percent = float(exam_total * EXAMS_WEIGHTAGE / EXAMS_TOTAL)
sports_percent = float(sports_score * SPORTS_WEIGHTAGE / SPORTS_TOTAL)
activities_percent = float(activities_total * ACTIVITIES_WEIGHTAGE / ACTIVITIES_TOTAL)
total_percent = exam_percent + sports_percent + activities_percent
print("\n\n ********************************* RESULT ***************************************************")
print("\n Total percent in examination:", exam_percent)
print("\n Total percent in activities:",activities_percent)
print("\n Total percent in sports", sports_percent)
print("\n -----------------------------------------------------------------------------------------------")
print("\n Total percentage", total_percent)