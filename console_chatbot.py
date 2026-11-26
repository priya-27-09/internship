
responses = {
    "hello": "Hello! Welcome to Python Internship.",
    "hi": "Hi! How can I help you?",
    "how are you": "I am fine. Thank you!",
    "what is your name": "I am Python Chatbot.",
    "bye": "Goodbye! Have a nice day."
}
history = []
print("Chatbot Started! Type 'bye' to exit.")
while True:
    user_message = input("You: ").lower()
    if user_message == "bye":
        bot_reply = responses["bye"]
        print("Bot:", bot_reply)
        history.append({
            "user": user_message,
            "bot": bot_reply
        })
        break
    bot_reply = responses.get(
        user_message,
        "Sorry, I don't understand."
    )
    print("Bot:", bot_reply)
    history.append({
        "user": user_message,
        "bot": bot_reply
    })
print("\nConversation History:")
for chat in history:
    print(chat)
