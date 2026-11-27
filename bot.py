import os
import json
import csv
from dotenv import load_dotenv
load_dotenv()
BOT_NAME = os.getenv("BOT_NAME", "PythonBot")
class ChatBot:
    def __init__(self, name):
        self.name = name
        self.history = []
        self.load_history()
    def add_message(self, role, message):
        self.history.append({
            "role": role,
            "message": message
        })
        self.save_history()
    def get_reply(self, message):
        self.add_message("user", message)
        if "hello" in message.lower():
            reply = "Hello! How can I help you?"
        elif "name" in message.lower():
            reply = f"My name is {self.name}"
        elif "python" in message.lower():
            reply = "Python is a programming language."
        elif "bye" in message.lower():
            reply = "Goodbye! Have a nice day!"
        else:
            reply = "Sorry, I don't understand."
        self.add_message("bot", reply)
        return reply
    def save_history(self):
        with open("chat_history.json", "w") as file:
            json.dump(self.history, file, indent=4)
    def load_history(self):
        try:
            with open("chat_history.json", "r") as file:
                self.history = json.load(file)
        except FileNotFoundError:
            self.history = []
            print("New chat history created.")
def student_summary():
    with open("students.csv", "r") as file:
        reader = csv.DictReader(file)
        students = list(reader)
    marks = [int(student["Marks"]) for student in students]
    print("\n--- Student Summary ---")
    print("Total Students:", len(students))
    print("Average Marks:", sum(marks) / len(marks))
    print("Highest Marks:", max(marks))
    print("Lowest Marks:", min(marks))
if __name__ == "__main__":
    bot = ChatBot(BOT_NAME)
    print(f"\nWelcome! I am {BOT_NAME}.")
    print("Type 'bye' to exit.\n")
    while True:
        user_message = input("You: ")
        reply = bot.get_reply(user_message)
        print(f"{BOT_NAME}: {reply}")
        if user_message.lower() == "bye":
            break
    student_summary()