registered_users = {}  # Dictionary to store registered user data
quiz_questions = [  # List to store quiz questions
    ("What is the capital of India?", "Delhi"),
    ("What is the largest planet in our solar system?", "Jupiter"),
    ("Who wrote 'Ramayana'?", "Valmiki"),
    ("Who is the presidant of India?", "Narendra Modi")
]

def register():
    print("User Registration\n")
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    registered_users[username] = password
    print("Registration successful!\n")

def login():
    print("User Login\n")
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    if username in registered_users and registered_users[username] == password:
        print("Login successful!\n")
        return True
    else:
        print("Invalid username or password. Please try again.\n")
        return False

def attempt_quiz():
    print("Quiz Time!\n")
    score = 0
    total_questions = len(quiz_questions)
    for i, (question, answer) in enumerate(quiz_questions, 1):
        print(f"Question {i}: {question}")
        user_answer = input("Your answer: ")
        if user_answer.lower() == answer.lower():
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! The correct answer is: {answer}")
        print()
    print(f"Quiz completed! Your score: {score}/{total_questions}\n")

def result():
    print("Result\n")
    print("Sorry, result feature is not available in this version.\n")

def exit_program():
    print("Exiting program. Goodbye!")
    quit()

def main():
    while True:
        print("Menu:")
        print("1. Register")
        print("2. Login")
        print("3. Attempt Quiz")
        print("4. View Result")
        print("5. Exit")
        choice = input("Enter your choice: ")
        print()
        if choice == "1":
            register()
        elif choice == "2":
            if login():
                break
        elif choice == "3":
            if login():
                attempt_quiz()
        elif choice == "4":
            if login():
                result()
        elif choice == "5":
            exit_program()
        else:
            print("Invalid choice. Please try again.\n")

if __name__ == "__main__":
    main()
