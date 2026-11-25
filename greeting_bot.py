print("===== WELCOME TO GREETING BOT =====")
name = input("Enter your name: ").strip()
if name:
    print(f"Hello {name}!")
    print("Welcome to Python AI/ML Internship.")
    question = input("How are you today? ").lower()
    if question == "good":
        print("That's great! Have a wonderful day.")
    elif question == "bad":
        print("Don't worry! Keep learning and stay positive.")
    else:
        print("Thank you for sharing!")
else:
    print("Please enter your name.")
