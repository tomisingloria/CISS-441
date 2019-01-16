import csv
import json

"""
who: Tomisin Odetoyinbo
when: 1.15.19
what: a1 assignment
"""

student_data = []
student_total_count = 0

with open('StudentsPerformance.csv', 'r') as csvfile:

   student_stream = csv.DictReader(csvfile, delimiter=',', quotechar='"')

   for student_data_row in student_stream:
        student_total_count += 1

        student_gender = student_data_row['gender']
        student_race = student_data_row['race/ethnicity']
        student_parent_education = student_data_row['parental level of education']

        # only show the first 20 rows. 
        if student_total_count <= 20:
            print(student_total_count, student_gender, student_race, student_parent_education)
            student_data.append({student_total_count: [student_gender, student_race, student_parent_education]
                })

"""
    print("I found " + str(student_total_count) + " heros.")
print("I am all done processing data!!!")

print(json.dumps(student_data))
  
  """
