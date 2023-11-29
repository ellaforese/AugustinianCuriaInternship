# # from chatterbot import ChatBot
# # from chatterbot.trainers import ListTrainer

# # CORPUS_FILE = "augustine_sample.txt"

# # chatbot = ChatBot("Chatpot")

# # trainer = ListTrainer(chatbot)

# # # Load question-answer pairs from the text file
# # qa_pairs = []
# # with open(CORPUS_FILE, "r") as file:
# #     lines = file.readlines()
# #     for i in range(0, len(lines), 4):
# #         question = lines[i].strip()
# #         print(question)
# #         answer = lines[i + 2].strip()
# #         print(answer)
# #         qa_pairs.append((question, answer))

# # # Extract questions and answers from the tuple and pass them to the trainer
# # for question, answer in qa_pairs:
# #     trainer.train([question, answer])

# # exit_conditions = (":q", "quit", "exit")
# # while True:
# #     query = input("> ")
# #     if query in exit_conditions:
# #         break
# #     else:
# #         print(f"--> {chatbot.get_response(query)}")
# #         response = chatbot.get_response(query)
# #         print(f"Query: {query}")
# #         print(f"Response: {response}")
# #         print(f"Confidence: {response.confidence}")


# from chatterbot import ChatBot
# from chatterbot.trainers import ListTrainer
# #from cleaner import clean_corpus

# CORPUS_FILE = "augustine_sample.txt"

# chatbot = ChatBot("Chatpot")

# trainer = ListTrainer(chatbot)
# #cleaned_corpus = clean_corpus(CORPUS_FILE)
# trainer.train(CORPUS_FILE)

# exit_conditions = (":q", "quit", "exit")
# while True:
#     query = input("> ")
#     if query in exit_conditions:
#         break
#     else:
#         response = chatbot.get_response(query)
#         print(f"--> {response}")
#         print(f"Query: {query}")
#         print(f"Response: {response}")
#         print(f"Confidence: {response.confidence}")

from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
# from chatterbot.trainers import ChatterBotCorpusTrainer
from cleaner import clean_corpus
#import nltk
#nltk.download()


CORPUS_FILE = "augustine_sample.txt"

chatbot = ChatBot("Augustine Chatbot")

# chatbot.storage.drop() # use this if the chatbot gets trained on unwanted dataß
# chatbot_corpus_trainer = ChatterBotCorpusTrainer(chatbot)


# Train the chatbot with your specific data
trainer = ListTrainer(chatbot)
cleaned_corpus = clean_corpus(CORPUS_FILE)
trainer.train(cleaned_corpus)




trainer = ListTrainer(chatbot)
# trainer = ChatterBotCorpusTrainer(chatbot)
cleaned_corpus = clean_corpus(CORPUS_FILE)
# trainer.train("chatterbot.corpus.english")
trainer.train(cleaned_corpus)


exit_conditions = (":q", "quit", "exit")
while True:
    query = input("> ")
    if query in exit_conditions:
        break
    else:
        response = chatbot.get_response(query)
     
        # print(f"--> {response}")
        print(f"Query: {query}")
        print(f"--> Response: {response}")
        print(f"Confidence: {response.confidence}")

        feedback = input("Was this response helpful? (yes/no): ")
        
        if feedback.lower() == "no":
            print("Please provide the correct answer:")
            correct_answer = input("> ")
            # Save the incorrect question and correct answer for further training
            with open("feedback_data.txt", "a") as feedback_file:
                feedback_file.write(f"{query}\n{correct_answer}\n")
