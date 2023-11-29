# def clean_corpus(input_file, output_file):
#     with open(input_file, "r") as file:
#         lines = file.readlines()

#     cleaned_lines = []

#     for line in lines:
#         # Split the line into question and answer using a comma
#         parts = line.strip().split(",")
#         if len(parts) == 2:
#             question = parts[0].strip()
#             answer = parts[1].strip()
#             cleaned_lines.append(f"{question}\n{answer}")

#     with open(output_file, "w") as file:
#         file.write("\n".join(cleaned_lines))

# # Define the input and output file names
# input_file = "augustine_sample.txt"  # Replace with the actual file path
# output_file = "chat.txt"

# # Call the clean_corpus function to create the cleaned file
# clean_corpus(input_file, output_file)
import re


def clean_corpus(chat_export_file):
    """Prepare a Sample Q&A about Saint Augustine export for training with chatterbot."""
    cleaned_corpus = remove_chat_metadata(chat_export_file)
    return cleaned_corpus


def remove_chat_metadata(chat_export_file):
    """Remove WhatsApp chat metadata.

    Augustine Q&A info exports come with metadata about each line:

     question           answer   
    ---------------------------------------
    Q: What ..          A: The ..

    This function removes all the metadata up to the text of each message.

    Args:
        chat_export_file (str): The name of the chat export file

    Returns:
        tuple: The text of each message in the conversation
    """
    # question = r"(Q)"  # e.g. "Q: What is Augustine’s Confessions?"
    # qtext = r"([\w\s]+)"
    # answer = r"(A)"  # e.g. "A: Augustine's Confessions is a diverse blend of autobiography..."
    # atext = r"([\w\s]+)"
    # metadata_end = r":\s*"  # ": "
    # emptySpace = "\s*"
    # pattern = question + metadata_end + qtext +emptySpace + answer + metadata_end + atext

#     question = r"(Q:\s*)"  # Match "Q: " at the beginning of a question
#     qtext = r"(.+?)"
#     answer = r"(A:\s*)"  # Match "A: " at the beginning of an answer
#     atext = r"(.+?)"
#     emptySpace = r"\s*"
#     pattern = question + qtext + emptySpace + answer + atext
# #

    with open(chat_export_file, "r") as corpus_file:
        content = corpus_file.read()
    #cleaned_corpus = re.sub(content)
    # cleaned_corpus = re.sub(pattern, "", content)
    return tuple(content.split("\n"))