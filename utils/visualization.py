import plotly.express as px
import streamlit as st


def show_prediction_chart(prediction):

    labels = ["Spam", "Safe"]

    if prediction == "spam":
        values = [1, 0]
    else:
        values = [0, 1]

    fig = px.pie(
        names=labels,
        values=values,
        hole=0.6,
        title="Prediction Result"
    )

    st.plotly_chart(fig, use_container_width=True)


def show_email_stats(email):

    stats = {
        "Words": len(email.split()),
        "Characters": len(email),
        "Digits": sum(c.isdigit() for c in email),
        "Uppercase": sum(c.isupper() for c in email),
        "Special": sum(
            not c.isalnum() and not c.isspace()
            for c in email
        )
    }

    fig = px.bar(
        x=list(stats.keys()),
        y=list(stats.values()),
        title="Email Statistics"
    )

    st.plotly_chart(fig, use_container_width=True)