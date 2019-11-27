import sys

student_scores = []
student_list = []
second_min = ''
for _ in range(int(raw_input())):
    name = raw_input()
    score = float(raw_input())
    student_scores.append([name, score])

l = len(student_scores)
for i in range(0, l):
    for j in range(0, l-i-1):
        if (student_scores[j][1] > student_scores[j + 1][1]):
            temp = student_scores[j]
            student_scores[j] = student_scores[j + 1]
            student_scores[j + 1] = temp

for i in  range (0, l):
    if (student_scores[j][1] > student_scores[j + 1][1]):

print student_scores
