import json

# Path to your JSON file
json_file_path = "students.json"

# Load the existing data from the JSON file
try:
    with open(json_file_path, 'r') as f:
        data = json.load(f)
except FileNotFoundError:
    data = {}
# Data to save, including image file references
data = {
    "22ug1-0041": {
        "name": "Dhananjaya Yatigammana",
        "major": "Information and Communication Engineering",
        "batch": '2026A',
        "total_attendance": 7,
        "standing": "G",
        "year": 3,
        "last_attendance_time": "2024-11-30 10:54:34",
        "image": "Images/22ug1-0041.png.jpg"  # Image file path
    },
    "22ug1-0582": {
        "name": "Vishwa Gamage",
        "major": "Telecommunication Engineering",
        "batch": '2026A',
        "total_attendance": 8,
        "standing": "N",
        "year": 3,
        "last_attendance_time": "2024-12-30 11:30:14",
        "image": "Images/22ug1-0582.png.jpg"  # Image file path
    },
    "22ug1-0363": {
        "name": "Ama Kaweesha",
        "major": "Accounting and Finance",
        "batch": '2026A',
        "total_attendance": 10,
        "standing": "G",
        "year": 3,
        "last_attendance_time": "2024-11-30 10:54:34",
        "image": "C:\\Users\\malee\\OneDrive\\Desktop\\Face Recognition Attendence System\\Files(1)\\Code\\22ug1-0363.png"  # Image file path
    },

    "22ug1-0490": {
        "name": "Maleesha Chandrasekara",
        "major": "Information and Communication Engineering",
        "batch": '2026A',
        "total_attendance": 9,
        "standing": "G",
        "year": 3,
        "last_attendance_time": "2024-11-30 10:54:34",
        "image": "C:\\Users\\malee\\OneDrive\\Desktop\\Face Recognition Attendence System\\Files(1)\\Output Images\\Maleesha.jpg"  # Image file path
    }
}

# Save data to a JSON file
with open('students.json', 'w') as f:
    json.dump(data, f, indent=4)
# Read data from the JSON file
