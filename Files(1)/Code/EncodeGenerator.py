import cv2
import os
import face_recognition
import pickle
import json

# Load the JSON file
json_file_path = 'students.json'
with open(json_file_path, 'r') as f:
    student_data = json.load(f)

# Folder containing the images
folderPath = r'C:\Users\malee\OneDrive\Desktop\Face Recognition Attendence System\Files(1)\Code\Images'
PathList = os.listdir(folderPath)
imgList = []
studentIds = []

# Load images and match with JSON file
for path in PathList:
    student_id = os.path.splitext(path)[0]  # Extract student ID from filename
    if student_id in student_data:  # Ensure the student ID exists in the JSON
        imgList.append(cv2.imread(os.path.join(folderPath, path)))
        studentIds.append(student_id)
    else:
        print(f"Warning: {student_id} from Images folder is not in the JSON file!")

print("Student IDs:", studentIds)

# Function to find face encodings
def findEncodings(imagesList):
    encodeList = []
    for img in imagesList:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        try:
            encode = face_recognition.face_encodings(img)[0]
            encodeList.append(encode)
        except IndexError:
            print("Warning: No face found in one of the images. Skipping...")
    return encodeList

print('Encoding Started...')
encodeListKnown = findEncodings(imgList)

# Combine encodings with student IDs and data from the JSON file
encodeListKnownWithIds = []
for idx, encode in enumerate(encodeListKnown):
    student_id = studentIds[idx]
    student_info = student_data[student_id]  # Fetch student data from JSON
    encodeListKnownWithIds.append({
        "id": student_id,
        "name": student_info["name"],
        "major": student_info["major"],
        "year": student_info["year"],
        "image_path": student_info["image"],  # Optional: Store the image path from JSON
        "encoding": encode
    })

print('Encoding Complete')

# Save the encoding list with IDs to a pickle file
file = open("EncodeFile.p", 'wb')
pickle.dump(encodeListKnownWithIds, file)
file.close()
print('File Saved')
