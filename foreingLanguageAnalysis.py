import streamlit as st
from googletrans import Translator
from textblob import TextBlob
import os

def main():
    st.title("Translator and Sentimental Analysis")
    st.write("Build with StreamLit and OpenCV")
    activities = ["Translator", "Sentimental_Analysis"]
    choice = st.sidebar.selectbox("Select an activity: ", activities)
    if choice == "Translator":
        from_text = st.text_input("Enter a sentence of your choice: ")
        from_code = st.text_input("Enter the code of the translation language: ")
        if st.button("Translate"):
            translator = Translator()
            try:
                a = (translator.translate(from_text, dest = from_code).text)
                st.success(a)
            except Exception as e:
                a1 = os.system("ping www.google.com")
                if a1 == 1:
                    st.write("Please check you internet connection!")
                else:
                    st.write("Wrong language code!!")
    elif choice == "Sentimental_Analysis":
        from_sent = st.text_input("Enter a sentence of your choice: ")
        if st.button("Analysis"):
            br = TextBlob(from_sent)
            result = br.sentiment.polarity
            if result == 0:
                st.success("This is a 'Neutral' message")
            elif result > 0:
                st.success("This is a 'Positive' message")
            else:
                st.success("This is a 'Negative' message")

if __name__ == "__main__":
    main()
