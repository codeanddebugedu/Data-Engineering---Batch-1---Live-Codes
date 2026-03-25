students: dict[str, dict[str, str | int]] = {
    "anirudh": {"gender": "Male", "marks": 453},
    "vandana": {"gender": "Male", "marks": 288},
    "nihar": {"gender": "Male", "marks": 358},
    "sanjay": {"gender": "Male", "marks": 218},
    "akul": {"gender": "Male", "marks": 277},
}

for name, details in students.items():
    print(f"name = {name}....details = {details['marks']}")
