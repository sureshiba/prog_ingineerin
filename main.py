import streamlit as st
from transformers import pipeline

# Создаем конвейер (pipeline) для классификации текста с использованием модели finbert
pipe = pipeline("text-classification", model="ProsusAI/finbert")

# Определение основного контента приложения
def main():
    # Заголовок
    st.title("Классификация текста с использованием finbert")

    # Поле для ввода текста
    input_text = st.text_input("Введите ваш текст:")

    # Обработка ввода и вывод результата
    if st.button("Классифицировать"):
        result = pipe(input_text)
        st.write(result)

# Запуск основного контента
if __name__ == "__main__":
    main()
