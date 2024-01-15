import random
import torch
from transformers import BertTokenizer, BertForSequenceClassification
from torch.nn.functional import softmax
import numpy as np
import os
device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
print(device)
PRETRAINED_MODEL_NAME = "bert-base-chinese"
tokenizer = BertTokenizer.from_pretrained(PRETRAINED_MODEL_NAME)
num_classes = 2

loaded_model = BertForSequenceClassification.from_pretrained(
    PRETRAINED_MODEL_NAME, num_labels=num_classes)

loaded_model.config.num_labels = num_classes
loaded_model.classifier = torch.nn.Linear(
    loaded_model.config.hidden_size, num_classes)
checkpoint = torch.load(os.path.join(
    os.getcwd(), "fine_tuned_bert_model.pth"), map_location=device)
loaded_model.load_state_dict(checkpoint['model_state_dict'])
loaded_tokenizer = checkpoint['tokenizer']
loaded_model = loaded_model.to(device)
loaded_model.eval()


def predict(sentence):
    # return random.randint(0, 1)
    if sentence is None or sentence == " " or sentence == "":
        print("empty sentence")
        return "", 2
    inputs = loaded_tokenizer(
        sentence, return_tensors="pt", add_special_tokens=True)
    model = loaded_model.to(device)
    inputs = inputs.to(device)
    with torch.no_grad():
        outputs = model(**inputs)
    logits = outputs.logits
    probabilities = softmax(logits, dim=1).detach().cpu().numpy()
    prediction = int(np.argmax(probabilities))
    print(f"probabilities: {probabilities}")
    print(f"Predicted class is: {prediction}")
    return prediction, ["Negative", "Positive"][prediction]
# if __name__ == '__main__':
#     # load_weights
