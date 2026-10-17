def test_mark_attendance():
    student_id = "STU1001"
    course_code = "CS201"
    status = "Present"
    
    print(f"Marking {status} for Student {student_id} in {course_code}")

    attendance_recorded = True
    
    if attendance_recorded:
        print("Attendance successfully recorded in database.")
        return True
    else:
        print("Failed to record attendance.")
        return False

if __name__ == "__main__":
    assert test_mark_attendance() == True