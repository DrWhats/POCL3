from transformers import pipeline

# import pytest

def classify(text=None):

    classifier = pipeline("zero-shot-classification", model="MoritzLaurer/mDeBERTa-v3-base-mnli-xnli") # Изменить модель

    candidate_labels = ["Учетная запись", "РПД",
                        "Учебные планы", "Личный кабинет"]

    output = classifier(text, candidate_labels, multi_label=False, use_fast=False)
    return output["labels"][0], output["scores"][0]