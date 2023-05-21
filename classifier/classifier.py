import torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification

model_checkpoint = 'cointegrated/rubert-base-cased-nli-threeway'
tokenizer = AutoTokenizer.from_pretrained(model_checkpoint)
model = AutoModelForSequenceClassification.from_pretrained(model_checkpoint)
if torch.cuda.is_available():
    model.cuda()


def predict_zero_shot(text, label_texts, model, tokenizer, label='entailment', normalize=True):
    label_texts
    tokens = tokenizer([text] * len(label_texts), label_texts, truncation=True, return_tensors='pt', padding=True)
    with torch.inference_mode():
        result = torch.softmax(model(**tokens.to(model.device)).logits, -1)
    proba = result[:, model.config.label2id[label]].cpu().numpy()
    if normalize:
        proba /= sum(proba)
    return proba


if __name__ == "__main__":
    classes = ['Я доволен', 'Я недоволен']
    print(predict_zero_shot('Какая гадость эта ваша заливная рыба!', classes, model, tokenizer))
    print(predict_zero_shot('Какая вкусная эта ваша заливная рыба!', classes, model, tokenizer))
