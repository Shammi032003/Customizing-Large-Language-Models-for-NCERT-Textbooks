from transformers import BertTokenizer, BertForQuestionAnswering

# Choose the model you wish to download, for example 'bert-base-uncased' for a smaller model
# or 'bert-large-uncased-whole-word-masking-finetuned-squad' for a larger model fine-tuned on the SQuAD dataset.
MODEL_NAME = 'bert-base-uncased'

# Initialize tokenizer and model
tokenizer = BertTokenizer.from_pretrained(MODEL_NAME)
model = BertForQuestionAnswering.from_pretrained(MODEL_NAME)

# Save the tokenizer and model to your local disk
tokenizer.save_pretrained('bert')
model.save_pretrained('bert')