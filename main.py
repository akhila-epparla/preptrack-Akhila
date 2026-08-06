print("="*50)
print("              PREPTRACK APPLICATION                ")
print("="*50)
while True:
    Student_Name=input("Enter Student Name: ")
    if Student_Name!="":
        break
    else:
        print("No student name entered. Exiting application")
Registration_Number=input("Enter registration number:")
Graduation_year=int(input("Enter Graduation Year: "))
graduation_eligible = (
    Graduation_year >= 2025 and Graduation_year <= 2027
)
while True: 
    Attendance = float(input("Enter attendance percentage: "))
    if Attendance >=0 and Attendance <=100:
        print("Attendance accepted.")
        break
    else:
        print("Invalid attendance. Enter a value between 0 and 100.")

while True:
    project_input = input("Has the student completed the required project? \n Enter yes or no: ")

    if project_input == "yes":
        project_completed = True
        break
    elif project_input == "no":
        project_completed = False
        break
    else:
        print("Invalid input. Enter only yes or no.")



while True:
    profile_input = input("Is the student profile verified? \n Enter yes or no: ")

    if profile_input == "yes":
        profile_verified = True
        break
    elif profile_input == "no":
        profile_verified = False
        break
    else:
        print("Invalid input. Enter only yes or no.")


total_score = 0

attempted_days = 0
absent_days = 0
passed_days = 0
failed_days = 0

strong_days = 0
satisfactory_days = 0
improvement_days = 0
critical_days = 0

highest_score = 0
highest_score_day = 0

lowest_score = 0
lowest_score_day = 0

first_attempt_found = False

critical_score_found = False
first_critical_day = 0
first_critical_score = 0

for day in range(1, 8): 
    while True:
        score = int(input(f"Enter Day {day} score from 0 to 100, or -1 for absent: "))

        if score == -1 or (0 <= score <= 100):
            print("Score accepted.")
            break

        print("Invalid score. Enter -1 or a value between 0 and 100.")
    if score == -1:
        absent_days += 1
        print(f"Day {day} Result: Absent")
        continue

    # Part 16 — Count Attempted Practices  
    attempted_days += 1
    total_score += score
   # Part 17 - Classify Every Attempted Score

    if score >= 75 and score <= 100:
        print(f"Day {day} Result: Strong")
        strong_days += 1

    elif score >= 60 and score <= 74:
        print(f"Day {day} Result: Satisfactory")
        satisfactory_days += 1

    elif score >= 40 and score <= 59:
        print(f"Day {day} Result: Needs Improvement")
        improvement_days += 1

    else:
        print(f"Day {day} Result: Critical")  
# Part 18
    if score >= 60:
        passed_days += 1
    else:
        failed_days += 1
# Part 19
    if not first_attempt_found:
        highest_score = score
        highest_score_day = day

        lowest_score = score
        lowest_score_day = day

        first_attempt_found = True

    else:
        if score > highest_score:
            highest_score = score
            highest_score_day = day

        if score < lowest_score:
            lowest_score = score
            lowest_score_day = day
# Part 20 - First Critical Score

    if score < 40:
        critical_days += 1

        if not critical_score_found:
            critical_score_found = True
            first_critical_day = day
            first_critical_score = score 
# Part 21 - Calculate the Average
if attempted_days > 0:
    average_score = total_score / attempted_days
else:
    average_score = 0
# Part 22 - Placement Readiness Requirements

attendance_eligible = Attendance >= 75
practice_count_eligible = attempted_days >= 6
average_eligible = average_score >= 70
critical_score_clear = not critical_score_found
passed_days_eligible = passed_days >= 4     
placement_ready = (
    graduation_eligible
    and attendance_eligible
    and practice_count_eligible
    and average_eligible
    and critical_score_clear
    and passed_days_eligible
    and project_completed
    and profile_verified
)
# Part 23 - Final Status Priority

if attempted_days == 0:
    final_status = "Practice Not Evaluated"
    primary_blocker = "No practice attempted"
    next_action = "Attempt the required coding practices"

elif critical_score_found:
    final_status = "Critical Support Required"
    primary_blocker = "Critical score exists"
    next_action = "Revise the concepts from the first critical day"

elif attempted_days < 6:
    final_status = "Practice Incomplete"
    primary_blocker = "Fewer than six practices attempted"
    next_action = "Complete at least six practice days"

elif passed_days < 4:
    final_status = "Insufficient Passed Practices"
    primary_blocker = "Fewer than four passed practices"
    next_action = "Pass at least four coding practices"

elif average_score < 70:
    final_status = "Practice Improvement Required"
    primary_blocker = "Average score below 70"
    next_action = "Improve the average score to at least 70"

elif Attendance < 75:
    final_status = "Attendance Improvement Required"
    primary_blocker = "Attendance below 75%"
    next_action = "Improve attendance to at least 75 percent"

elif not graduation_eligible:
    final_status = "Graduation Criteria Not Met"
    primary_blocker = "Graduation year not eligible"
    next_action = "Check the eligible graduation-year requirement"

elif not project_completed:
    final_status = "Application On Hold"
    primary_blocker = "Project incomplete"
    next_action = "Complete the required project"

elif not profile_verified:
    final_status = "Application On Hold"
    primary_blocker = "Profile not verified"
    next_action = "Complete profile verification"

else:
    final_status = "Ready for Mock Interview"
    primary_blocker = "None"
    next_action = "Proceed to placement mock interviews"
print("==================================================")
print("               PREPTRACK REPORT")
print("==================================================")

print("\nSTUDENT PROFILE")
print(f"Student Name            : {Student_Name}")
print(f"Registration Number     : {Registration_Number}")
print(f"Graduation Year         : {Graduation_year}")
print(f"Attendance              : {Attendance}%")
print(f"Project Completed       : {project_completed}")
print(f"Profile Verified        : {profile_verified}")

print("\nPRACTICE SUMMARY")
print("Total Practice Days     : 7")
print(f"Attempted Days          : {attempted_days}")
print(f"Absent Days             : {absent_days}")
print(f"Passed Days             : {passed_days}")
print(f"Failed Days             : {failed_days}")

print(f"Strong Days             : {strong_days}")
print(f"Satisfactory Days       : {satisfactory_days}")
print(f"Needs Improvement Days  : {improvement_days}")
print(f"Critical Days           : {critical_days}")

print("\nPERFORMANCE ANALYSIS")
print(f"Total Score             : {total_score}")
print(f"Average Score           : {average_score}")
if attempted_days > 0:
    print(f"Highest Score           : {highest_score}")
    print(f"Highest Score Day       : Day {highest_score_day}")
    print(f"Lowest Score            : {lowest_score}")
    print(f"Lowest Score Day        : Day {lowest_score_day}")
else:
    print("Highest Score           : Not Available")
    print("Highest Score Day       : Not Available")
    print("Lowest Score            : Not Available")
    print("Lowest Score Day        : Not Available")

print("\nCRITICAL SCORE INFORMATION")
print(f"Critical Score Found    : {critical_score_found}")

if critical_score_found:
    print(f"First Critical Day      : Day {first_critical_day}")
    print(f"First Critical Score    : {first_critical_score}")
else:
    print("First Critical Day      : Not Applicable")
    print("First Critical Score    : Not Applicable")
print("\nFINAL DECISION")
print(f"Final Status            : {final_status}")
print(f"Primary Blocker         : {primary_blocker}")
print(f"Next Action             : {next_action}")
print("==================================================")    
