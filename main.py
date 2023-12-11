from transformers import pipeline

pipe = pipeline("text-classification", model="ProsusAI/finbert")

input_text = input("Введите ваш текст: ")

result = pipe(input_text)

print(result)
