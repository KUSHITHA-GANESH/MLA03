import random

students = [
    "Beginner",
    "Intermediate",
    "Advanced"
]

lessons = [
    "Easy Lesson",
    "Medium Lesson",
    "Hard Lesson"
]

Q = {}

for student in students:
    for lesson in lessons:
        Q[student, lesson] = 0

for episode in range(1000):

    student = random.choice(students)
    lesson = random.choice(lessons)

    if student == "Beginner" and lesson == "Easy Lesson":
        reward = 10
    elif student == "Intermediate" and lesson == "Medium Lesson":
        reward = 10
    elif student == "Advanced" and lesson == "Hard Lesson":
        reward = 10
    else:
        reward = -2

    Q[student, lesson] += 0.1 * (
        reward - Q[student, lesson]
    )

print("PERSONALIZED EDUCATION SYSTEM")
print("------------------------------")

for student in students:

    best = max(
        lessons,
        key=lambda x: Q[student, x]
    )

    print("Student Level:", student)
    print("Recommended Lesson:", best)
    print()

print("Reinforcement Learning completed.")