from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot import languages

chatbot = ChatBot('Demo',
        tagger_language=languages.JPN,
        logic_adapters=[
            {
                'import_path': 'chatterbot.logic.BestMatch',
                'default_response': 'ごめんなさい。よく分かりません。',
                'maximum_similarity_threshold': 0.90
            }
        ],
        read_only=True)

trainer_corpus = ChatterBotCorpusTrainer(chatbot)

# Use the built-in english corpus files to train it.
# trainer_corpus.train("chatterbot.corpus.japanese")

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
    if request == "さようなら":
        print("Bot: さようなら!")
        break
    else:
        response = chatbot.get_response(request)
        print("Bot: ", response)
