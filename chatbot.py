from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
# from chatterbot.trainers import ChatterBotCorpusTrainer
from cleaner import clean_corpus



CORPUS_FILE = "augustine_sample.txt"

chatbot = ChatBot("Augustine Chatbot")

# chatbot.storage.drop() # use this to "reset" if the chatbot gets trained on unwanted data
# chatbot_corpus_trainer = ChatterBotCorpusTrainer(chatbot)


# Train the chatbot with your specific data
trainer = ListTrainer(chatbot)
cleaned_corpus = clean_corpus(CORPUS_FILE)
trainer.train(cleaned_corpus)


trainer = ListTrainer(chatbot)
cleaned_corpus = clean_corpus(CORPUS_FILE)
trainer.train(cleaned_corpus)


exit_conditions = (":q", "quit", "exit")
while True:
    query = input("> ")
    if query in exit_conditions:
        break
    else:
        response = chatbot.get_response(query)
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
