#root: https://www.youtube.com/watch?v=VqgUkExPvLY 
#command run pip install streamlit
#command run streamlit run app.py to find the local link -> Local URL: http://localhost:8501 / Network URL: http://192.168.1.4:8501
#command run pip install streamlit-lottie
#command run pip install requests


import requests
import streamlit as st
from streamlit_lottie import st_lottie
from PIL import Image, ImageSequence
import base64
from chatbot import translate_tool

# Find more emojis here: https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title="My Webpage", page_icon=":tada:", layout="wide")


def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


# Use local CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


local_css("style/style.css")

# ---- LOAD ASSETS ----
## Find more animation here https://lottiefiles.com/
lottie_cover = load_lottieurl("https://assets7.lottiefiles.com/packages/lf20_w51pcehl.json")
lottie_python = load_lottieurl("https://assets8.lottiefiles.com/packages/lf20_2znxgjyt.json")
#lottie_sql = load_lottieurl("")
img_ml_1 = load_lottieurl("https://assets9.lottiefiles.com/packages/lf20_v6iZgy.json")
img_ml_2 = Image.open("images/rectable.jpg")
img_ml_3 = load_lottieurl("https://assets7.lottiefiles.com/packages/lf20_kuhijlvx.json")
img_nlp_1 = Image.open("images/square.jpg")
img_cb_1 = load_lottieurl("https://assets3.lottiefiles.com/private_files/lf30_8ugvxzqd.json")
file_ = open("images/img_v_1.gif", "rb")
contents = file_.read()
data_url = base64.b64encode(contents).decode("utf-8")
file_.close()
img_v_2 = Image.open("images/powerbi.jpg")
img_v_3 = Image.open("images/tableau.jpg")


# ---- HEADER SECTION ----
with st.container():
    text_column, image_column = st.columns((3, 1))
    with text_column:
        st.subheader("Hi, I am Hien :wave: , welcome to my blog ")
        #st.title("All things I know about Data Science")
        st.write(
            """
            This blog lists down my projects in different areas of Data Science by  firstly present the results and how I made it. 
            I hope it provides some value to someone.
            """""
        )
        st.markdown("[Visit my github](https://github.com/Hiienng)")
    with image_column:
        st_lottie(lottie_cover, height=200, key="python")

# ---- PROJECTS ----
# Part 1: Machine Learning - NII
with st.container():
    st.write("---")
    st.header("My Projects")
    st.subheader("Part 1: Machine Learning")
    st.write("##")
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st_lottie(img_ml_1, height=300, key="banking")
    with text_column:
        st.subheader("Banking - Net interest income prediction")
        st.write(
            """
            - With Python - Random Forest Algorithm
            - This project using the nature of the bank and it's previous year balance sheet, this year projected disbursement to predict NII
            - Tutors: Self strack
            - Skills: Finance, Machine Learning, 
            """
        )
        #st.markdown("[Click to find more](https://youtu.be/FOULV9Xij_8)")
# Part 1: Machine Learning - anti-fraud
with st.container():
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_ml_2)
    with text_column:
        st.subheader("Education - Anti-fraud algorithm for testing")
        st.write(
            """
            - With Python - Neutral Network
            - A part of mobile application DTEST which is the exercising and testing environment for tutors and learners. This algorithm will help in detect the signs of fraud by timing and touching time per question and also user's personalization.
            """
        )
        #st.markdown("[Click to find more](https://youtu.be/FOULV9Xij_8)")       
# Part 1: Machine Learning - Stock Price Prediction
with st.container():
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st_lottie(img_ml_3, height=300, key="stock")
    with text_column:
        st.subheader("Stock - Stock Price Prediction")
        st.write(
            """
            - With Python - Neutral Network
            - Source: Actual Data
            - Tutors: Kyvi - Part of EUH Master of Finance curiculum
            """
        )
        st.markdown("[Click here for Code and Assets > Github](https://github.com/Hiienng)")
#Part 2: Natural Language Processing
with st.container():
    st.write("##")
    st.subheader("Part 2: Natural Language Processing")
    st.write("##")
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_nlp_1)
    with text_column:
        st.subheader("A real time report telling what clients' saying about your products - Social Network")
        st.write(
            """
            - By only typing your name of product/company. This project create the real-time analysing reports on what user's thinkng on your products.
            - The source of the data is mining from Social Network
            """
        )
        #st.markdown("[Click to find more](https://youtu.be/FOULV9Xij_8)")
#Part 3: Chat bot
with st.container():
    st.write("##")
    st.subheader("Part 3: Chat bot")
    st.write("##")
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st_lottie(img_cb_1, height=300, key="chatbot")
    with text_column:
        st.subheader("A simple chat bot for small-size sellers")
        st.write(
            """
            - With Python
            - This is a tool for online seller, which can auto reply in multiple languages and can be used to give the guide to clients.
            - Tool to be added in website. Sample as below
            """
        )
        #st.markdown("[Click to find more]](https://youtu.be/FOULV9Xij_8)")
        st.write("Sample as below")
        # Get year of birth from user input
        ini_text = st.text_input("","Input the text to be translated here!")
        translate_text = translate_tool(ini_text)
        st.write(f"In Japanese, it is: {translate_text}")


#Part 4: Visualization
with st.container():
    st.write("##")
    st.subheader("Part 4: Visualization")
    # st.write("##")
    # image_column, text_column = st.columns((3, 2))
    # with image_column:
    #     st.markdown(
    #         f'<img src="data:image/gif;base64,{data_url}" alt="excel gif" style="width: 100%; height: 100%;">',
    #         unsafe_allow_html=True,
    #     )
    # with text_column:
    #     st.subheader("A real-time reports in Excel")
    #     st.write(
    #         """
    #         - With Oracle for database and Excel for Visualization,
    #         This part only focuses on how to get and visualize data
    #         """
    #     )
    #         #st.markdown("[Click to find more]](https://youtu.be/FOULV9Xij_8)")
    st.write("##")
    image_column, text_column = st.columns((3, 2))
    with image_column:
        st.image(img_v_2)
    with text_column:
        st.subheader("Power BI")
        st.write(
            """
            - With Oracle for database and Excel for Visualization,
            This part only focuses on how to get and visualize data
            """
        )
            #st.markdown("[Click to find more]](https://youtu.be/FOULV9Xij_8)")
    # st.write("##")
    # image_column, text_column = st.columns((3, 2))
    # with image_column:
    #     st.image(img_v_3)
    # with text_column:
    #     st.subheader("Tableau")
    #     st.write(
    #         """
    #         - With Oracle for database and Excel for Visualization,
    #         This part only focuses on how to get and visualize data
    #         """
    #     )
    #         #st.markdown("[Click to find more]](https://youtu.be/FOULV9Xij_8)")


# ---- CONTACT ----
with st.container():
    st.write("---")
    st.subheader("If you're learning or hiring for part of your work please feel free to message me")
    st.write("##")

    # Documention: https://formsubmit.co/ !!! CHANGE EMAIL ADDRESS !!!
    contact_form = """
    <form action="https://formsubmit.co/hiennguyen280696@gmail.com" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Your name" required>
        <input type="email" name="email" placeholder="Your email" required>
        <textarea name="message" placeholder="Your message here" required></textarea>
        <button type="submit">Send</button>
    </form>
    """
    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.empty()

# ---- NOTES ----
with st.container():
    st.write("---")
    st.write("##")
    st.write(
        """
        This web is written with python, lib streamlit
        """
    )
    #st.markdown("[Click to find more](https://youtu.be/FOULV9Xij_8)")