import torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import numpy as np


def predict(text):
    label_texts = [
        'Личный кабинет', 'Продукты Microsoft ',
        'Электронно-библиотечная система', 'Ведомости',
        'Система электронной поддержки образовательных курсов',
        'Планы', 'Рабочая программа дисциплины', 'Нагрузка', 'Деканат', 'Диплом мастер'
    ] # изменится в будущем

    tokenizer = AutoTokenizer.from_pretrained('cointegrated/rubert-base-cased-nli-threeway')
    model = AutoModelForSequenceClassification.from_pretrained('cointegrated/rubert-base-cased-nli-threeway')
    
    tokens = tokenizer([text] * len(label_texts), label_texts, truncation=True, return_tensors='pt', padding=True)

    with torch.inference_mode():
        result = torch.softmax(model(**tokens.to(model.device)).logits, -1)
    proba = result[:, model.config.label2id["entailment"]].cpu().numpy()

    proba /= sum(proba)
    
    i = np.argmax(proba)

    return label_texts[i]