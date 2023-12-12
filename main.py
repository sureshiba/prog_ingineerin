import streamlit as st
from transformers import pipeline


pipe = pipeline("text-classification", model="ProsusAI/finbert")


def main():
    # Заголовок
    st.title("классификация текста ")

    # Поле для ввода текста
    input_text = st.text_input("Введите ваш текст:")

    # Обработка ввода и вывод результата
    if st.button("классифицировать"):
        result = pipe(input_text)
        st.write(result)


if __name__ == "__main__":
    main()
