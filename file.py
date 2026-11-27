messages = ["Hi!", "Hello! How can I help?", "Tell me about Python."]
with open("chat_history.txt", "w") as file:
    for message in messages:
        file.write(message + "\n")
with open("chat_history.txt", "r") as file:
    print(file.read())