# from transformers import GPT2LMHeadModel, GPT2Tokenizer
# import torch
# from fuzzywuzzy import fuzz
# # Load the trained tokenizer and model from specified directories
# tokenizer_directory = "accuracy"
# model_directory = "accuracy"

# tokenizer = GPT2Tokenizer.from_pretrained(tokenizer_directory)
# model = GPT2LMHeadModel.from_pretrained(model_directory)

# # Generate text based on user input
# user_input = input("Enter a question: ")
# input_text = f"Q: {user_input} A:"
# input_ids = tokenizer.encode(input_text, return_tensors="pt")

# # Generate text based on the input
# with torch.no_grad():
#     output = model.generate(input_ids, max_length=100, do_sample=True, pad_token_id=tokenizer.eos_token_id)

# generated_text = tokenizer.decode(output[0], skip_special_tokens=True)
# print("Generated Answer: ", generated_text)

# # Evaluate accuracy (compare generated text with expected answer)
# expected_answer = input("Enter the expected answer: ")
# similarity_threshold = 80  # Adjust the threshold based on your requirements
# similarity_score = fuzz.partial_ratio(expected_answer.lower(), generated_text.lower())

# accuracy = int(similarity_score >= similarity_threshold)
# print("Similarity Score: ", similarity_score)
# print("Accuracy: ", accuracy)
from fuzzywuzzy import fuzz

def calculate_accuracy(expected_answer, generated_text, similarity_threshold=80):
    # Calculate similarity score between expected answer and generated text
    similarity_score = fuzz.partial_ratio(expected_answer.lower(), generated_text.lower())
    
    # Determine accuracy based on similarity score and threshold
    accuracy = int(similarity_score >= similarity_threshold)
    
    return accuracy, similarity_score

# Example usage:
expected_answer = "Federalism involves all levels of government in a single authority structure, with power concentrated in the hands of the executive and legislative branches."
generated_text = "What is Federalism?"

accuracy, similarity_score = calculate_accuracy(expected_answer, generated_text)
print("Similarity Score:", similarity_score)
print("Accuracy:", accuracy)
