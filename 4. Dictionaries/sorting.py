from typing import List


students: dict[str, List[int]] = {
    "anirudh": [43, 65, 21, 65, 76],
    "vandana": [65, 76, 12, 81, 54],
    "nihar": [87, 98, 76],
    "sanjay": [76, 12, 76, 37, 17],
    "akul": [87, 45, 12, 66, 67, 434, 43],
}


print(dict(sorted(students.items(), key=lambda x: sum(x[1]), reverse=True)))
