import list_utils

grades = [65, 100, 76, 82, 93, 76]
print(f'original grades: {grades}')

for i in range(0, len(grades)):
    grades = grades[0:i] + list_utils.move_min_to_front(grades[i:])

print(f'sorted grades: {grades}')
