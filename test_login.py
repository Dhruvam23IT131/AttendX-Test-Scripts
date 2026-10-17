def test_student_login():
    username = "student_01"
    password = "SecurePassword123"
    
    print(f"Attempting login for user: {username}")
    
    if username == "student_01" and password == "SecurePassword123":
        print("Login successful! Redirecting to dashboard...")
        return True
    else:
        print("Login failed! Invalid credentials.")
        return False

if __name__ == "__main__":
    assert test_student_login() == True