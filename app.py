import streamlit as st
import pandas as pd
import joblib
import plotly.express as px


# ---------------- PAGE CONFIG ----------------

st.set_page_config(
    page_title="Podcast Intelligence AI",
    page_icon="🎧",
    layout="wide"
)


# ---------------- CUSTOM CSS ----------------

st.markdown(
    """
    <style>

    .stApp {
        background-color: #0b0b0f;
        color: white;
    }

    h1, h2, h3 {
        color: #1DB954;
    }

    .title {
        text-align:center;
        font-size:45px;
        font-weight:bold;
        color:#1DB954;
    }

    .subtitle {
        text-align:center;
        font-size:20px;
        color:#dddddd;
    }


    .card {

        background:#181818;
        padding:20px;
        border-radius:15px;
        text-align:center;
        border:1px solid #333333;

    }


    .card h2 {

        color:#1DB954;

    }


    .result {

        background:#1DB954;
        color:black;
        padding:25px;
        border-radius:20px;
        text-align:center;
        font-size:30px;
        font-weight:bold;

    }


    </style>

    """,
    unsafe_allow_html=True
)



# ---------------- LOAD FILES ----------------

model = joblib.load("podcast_model.pkl")

encoders = joblib.load("label_encoders-3.pkl")

features = joblib.load("features.pkl")



# ---------------- SIDEBAR ----------------

st.sidebar.title("🎧 Podcast AI")

page = st.sidebar.radio(

    "Navigation",

    [

        "🏠 Home",

        "🚀 Prediction Studio",

        "📊 Model Insights",

        "ℹ️ About"

    ]

)



# ---------------- HOME PAGE ----------------


if page == "🏠 Home":


    st.markdown(
        "<div class='title'>🎧 Podcast Intelligence AI</div>",
        unsafe_allow_html=True
    )


    st.markdown(
        "<div class='subtitle'>Machine Learning powered Podcast Listening Time Prediction</div>",
        unsafe_allow_html=True
    )


    st.write("")


    col1, col2, col3 = st.columns(3)



    with col1:

        st.markdown(

            """
            <div class="card">

            <h2>78.16%</h2>

            <p>R² Score</p>

            </div>

            """,

            unsafe_allow_html=True

        )


    with col2:

        st.markdown(

            """
            <div class="card">

            <h2>Random Forest</h2>

            <p>Best Model</p>

            </div>

            """,

            unsafe_allow_html=True

        )



    with col3:

        st.markdown(

            """
            <div class="card">

            <h2>371K+</h2>

            <p>Podcast Records</p>

            </div>

            """,

            unsafe_allow_html=True

        )



    st.write("")


    st.subheader("🤖 Project Overview")


    st.write(

        """

        Podcast Intelligence AI predicts the expected listening time

        of podcast episodes using machine learning.

        

        The model considers:

        - Podcast information

        - Episode details

        - Popularity factors

        - Publishing schedule

        - Advertisement count

        - Sentiment analysis


        """

    )





# ---------------- PREDICTION PAGE ----------------


elif page == "🚀 Prediction Studio":


    st.title("🚀 AI Listening Time Predictor")


    st.write(
        "Enter podcast details to predict expected listening duration."
    )


    col1, col2 = st.columns(2)



    with col1:


        podcast_name = st.selectbox(

            "🎙 Podcast Name",

            encoders["Podcast_Name"].classes_

        )


        episode_title = st.text_input(

            "🎵 Episode Title",

            "Episode 1"

        )


        genre = st.selectbox(

            "📚 Genre",

            encoders["Genre"].classes_

        )


        episode_length = st.slider(

            "⏱ Episode Length (minutes)",

            10.0,

            200.0,

            60.0

        )



        host_popularity = st.slider(

            "⭐ Host Popularity (%)",

            0.0,

            100.0,

            70.0

        )





    with col2:


        publication_day = st.selectbox(

            "📅 Publication Day",

            encoders["Publication_Day"].classes_

        )


        publication_time = st.selectbox(

            "🕒 Publication Time",

            encoders["Publication_Time"].classes_

        )


        guest_popularity = st.slider(

            "👤 Guest Popularity (%)",

            0.0,

            100.0,

            50.0

        )


        ads = st.slider(

            "📢 Number of Ads",

            0,

            5,

            1

        )


        sentiment = st.selectbox(

            "😊 Episode Sentiment",

            encoders["Episode_Sentiment"].classes_

        )





    st.write("")



    if st.button("🤖 Predict Listening Time"):



        input_data = pd.DataFrame({


            "Podcast_Name":[

                encoders["Podcast_Name"].transform([podcast_name])[0]

            ],


            "Episode_Title":[

                encoders["Episode_Title"].transform([episode_title])[0]

                if episode_title in encoders["Episode_Title"].classes_

                else 0

            ],


            "Episode_Length_minutes":[episode_length],


            "Genre":[

                encoders["Genre"].transform([genre])[0]

            ],


            "Host_Popularity_percentage":[host_popularity],



            "Publication_Day":[

                encoders["Publication_Day"].transform([publication_day])[0]

            ],



            "Publication_Time":[

                encoders["Publication_Time"].transform([publication_time])[0]

            ],



            "Guest_Popularity_percentage":[guest_popularity],



            "Number_of_Ads":[ads],



            "Episode_Sentiment":[

                encoders["Episode_Sentiment"].transform([sentiment])[0]

            ]

        })



        prediction = model.predict(input_data)



        st.markdown(

            f"""

            <div class="result">

            🎧 Expected Listening Time

            <br>

            {prediction[0]:.2f} minutes

            </div>

            """,

            unsafe_allow_html=True

        )






# ---------------- MODEL INSIGHTS ----------------


elif page == "📊 Model Insights":


    st.title("📊 Model Performance")


    metrics = pd.DataFrame(

        {

            "Metric":

            [

                "MAE",

                "RMSE",

                "R² Score"

            ],


            "Value":

            [

                9.03,

                12.67,

                0.781

            ]

        }

    )


    st.dataframe(metrics)



    st.subheader("🏆 Selected Model")

    st.success(
        "Random Forest Regressor"
    )



    st.write(

        """

        The Random Forest model achieved the highest

        performance among all tested regression algorithms.

        """

    )





# ---------------- ABOUT PAGE ----------------


elif page == "ℹ️ About":


    st.title("ℹ️ About Project")


    st.write(

        """

        ## Problem

        Predict podcast listener engagement before publishing.



        ## Machine Learning Approach

        Regression models were trained to estimate

        Listening Time in minutes.



        ## Models Used

        - Linear Regression

        - Decision Tree

        - Random Forest

        - Gradient Boosting

        - XGBoost



        ## Best Model

        Random Forest Regressor



        ## Technologies

        Python, Scikit-learn, Pandas, Streamlit

        """

    )