from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer

chatbot = ChatBot('Demo')

trainer_corpus = ChatterBotCorpusTrainer(chatbot)

# Use the built-in chatterbot english corpus files to train it.
# trainer_corpus.train("chatterbot.corpus.english")

# Use custom corpus files to train it.
trainer_corpus.train("./data")

# Create a new trainer for the chatbot using simple conversation sentences.
trainer = ListTrainer(chatbot)

# conversation = [
#     "Hello",
#     "Hi there!",
#     "How are you doing?",
#     "I'm doing great.",
#     "That is good to hear",
#     "Thank you.",
#     "You're welcome.",
#     "How can I create a website?",
#     "To create a website, you can go to www.w3.org, there are lots of example there",
#     "How do you use ftp?",
#     "To use ftp, you can find a good tutorial here: http://tutorial.org.",
#     "What's your name?",
#     "I'm called Chatterbot",
# ]

# trainer.train(conversation)


# Main interaction loop
while True:
    request = input("User: ")
    if request.lower() == "bye":
        print("Bot: Bye!")
        break
    else:
        response = chatbot.get_response(request)
        print("Bot: ", response)
