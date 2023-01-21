from typing import List
from textblob import TextBlob

def hello(name):
    output = f'Hello {name}'
    return output


def extract_sentiment(text):
    text = TextBlob(text)

    return text.sentiment.polarity


def text_contain_word(word: str, text: str):
    return word in text

def bubble_sort(list_of_numbers):
    for i in range(len(list_of_numbers) - 1, 0, -1):
        for j in range(i):
            if list_of_numbers[j] > list_of_numbers[j + 1]:
                placeholder = list_of_numbers[j]
                list_of_numbers[j] = list_of_numbers[j + 1]
                list_of_numbers[j + 1] = placeholder

    return list_of_numbers