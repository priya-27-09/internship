class ChatBot:
    def __init__(self, name):
        self.name = name
    def greet(self):
        print("Hello! I am", self.name)
    def reply(self, message):
        return "You said: " + message
bot = ChatBot("Priya")
bot.greet()
response = bot.reply("Hello")
print(response)