import json
messages = [
    {"user": "Hi", "bot": "Hello!"},
    {"user": "How are you?", "bot": "I am fine!"}
]
with open("chat_history.json", "w") as file:
    json.dump(messages, file, indent=4)
with open("chat_history.json", "r") as file:
    data = json.load(file)
print("Chat History:")
print(data)