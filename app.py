import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from datetime import datetime
import os
import plotly.express as px
import numpy as np
from predictor import predict_email
from chatbot import explain_email
from utils.explainer import highlight_keywords

# ---------------- PAGE CONFIG ---------------- #

st.set_page_config(
    page_title="Spam Email Detector",
    page_icon="📧",
    layout="wide"
)

# ---------------- CSS ---------------- #

st.markdown("""
<style>

.main{
    background:#0E1117;
}

.title{
    text-align:center;
    font-size:46px;
    font-weight:bold;
    color:white;
}

.subtitle{
    text-align:center;
    color:#BBBBBB;
    margin-bottom:25px;
}

.stTextArea textarea{
    border-radius:15px;
    background:#1E1E1E;
    color:white;
}

.stButton>button{
    width:100%;
    height:55px;
    border-radius:12px;
    font-size:18px;
    font-weight:bold;
    background:#4CAF50;
    color:white;
}

.stButton>button:hover{
    background:#2E8B57;
}

</style>
""", unsafe_allow_html=True)

# ---------------- HEADER ---------------- #

st.markdown("""
<div class="title">
📧 Spam Email Detector + AI Assistant
</div>

<div class="subtitle">
Detect Spam Emails using Machine Learning & AI
</div>
""", unsafe_allow_html=True)

# ---------------- INPUT ---------------- #

email = st.text_area(
    "Paste Email Here",
    height=250,
    placeholder="Paste your email here..."
)

# ---------------- BUTTON ---------------- #

if st.button("🚀 Analyze Email"):

    if email.strip() == "":
        st.warning("Please enter an email.")
        st.stop()

    prediction, confidence = predict_email(email)

    # ---------------- SAVE HISTORY ---------------- #

    history = {
        "Date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "Prediction": prediction,
        "Confidence": round(confidence, 2),
        "Words": len(email.split()),
        "Characters": len(email)
    }

    history_df = pd.DataFrame([history])

    try:

        history_file = "history.csv"

        if not os.path.exists(history_file):

            history_df.to_csv(
                history_file,
                index=False
            )

        else:

            history_df.to_csv(
                history_file,
                mode="a",
                header=False,
                index=False
            )

    except PermissionError:

        st.warning(
            "Close history.csv if it is open in Excel or another program."
        )

    # ---------------- RESULT ---------------- #

    st.divider()

    col1, col2 = st.columns(2)

    with col1:

        if prediction == "spam":
            st.error("🚨 Spam Email")
        else:
            st.success("✅ Safe Email")

        st.metric(
            "Confidence",
            f"{confidence:.2f}%"
        )

        st.progress(int(confidence))

    with col2:

        st.subheader("📊 Email Statistics")

        st.write(f"**Words:** {len(email.split())}")
        st.write(f"**Characters:** {len(email)}")
        st.write(f"**Uppercase:** {sum(c.isupper() for c in email)}")
        st.write(f"**Digits:** {sum(c.isdigit() for c in email)}")
        st.write(
            f"**Special Characters:** {sum(not c.isalnum() and not c.isspace() for c in email)}"
        )

    # ---------------- RISK METER ---------------- #

    st.divider()

    st.subheader("📈 Spam Risk Meter")

    fig = go.Figure(go.Indicator(

        mode="gauge+number",

        value=confidence,

        title={"text":"Spam Score"},

        gauge={

            "axis":{"range":[0,100]},

            "bar":{
                "color":"red" if prediction=="spam" else "green"
            },

            "steps":[

                {"range":[0,40],"color":"lightgreen"},
                {"range":[40,70],"color":"gold"},
                {"range":[70,100],"color":"tomato"}

            ]

        }

    ))

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    # ---------------- AI ---------------- #

    st.divider()

    st.subheader("🤖 AI Assistant")

    with st.spinner("Analyzing..."):

        explanation = explain_email(
            email,
            prediction,
            confidence
        )

    st.success(explanation)

    # ---------------- RECOMMENDATION ---------------- #

    st.divider()

    st.subheader("💡 Recommendation")

    if prediction == "spam":

        st.warning("""
### Recommended Actions

❌ Don't click suspicious links

❌ Don't download attachments

❌ Don't reply

✅ Verify sender

✅ Delete the email

""")

    else:

        st.success("""
### Recommended Actions

✅ Email appears safe

✅ Verify unknown senders

✅ Avoid sharing passwords

✅ Stay cautious
""")

st.divider()

st.subheader("🚩 Suspicious Keywords")

keywords = highlight_keywords(email)

if keywords:

    cols = st.columns(3)

    for i, word in enumerate(keywords):

        cols[i % 3].error(word.upper())

else:

    st.success("No suspicious keywords detected.")
# ---------------- ANALYTICS DASHBOARD ---------------- #

st.divider()

st.header("📊 Analytics Dashboard")

history_file = "history.csv"

if os.path.exists(history_file):

    history = pd.read_csv(history_file)

    if not history.empty:

        # Summary Metrics
        total_emails = len(history)
        spam_count = len(history[history["Prediction"] == "spam"])
        safe_count = len(history[history["Prediction"] == "ham"])
        avg_confidence = history["Confidence"].mean()

        c1, c2, c3, c4 = st.columns(4)

        c1.metric("📨 Total Emails", total_emails)
        c2.metric("🚨 Spam Emails", spam_count)
        c3.metric("✅ Safe Emails", safe_count)
        c4.metric("🎯 Avg Confidence", f"{avg_confidence:.2f}%")

        st.divider()

        # ---------------- Charts ---------------- #

        left, right = st.columns(2)

        with left:

            pie = px.pie(
                history,
                names="Prediction",
                title="Spam vs Safe Emails",
                hole=0.5
            )

            pie.update_traces(textposition="inside", textinfo="percent+label")

            st.plotly_chart(
                pie,
                use_container_width=True
            )

        with right:

            bar = px.histogram(
                history,
                x="Confidence",
                color="Prediction",
                nbins=15,
                title="Confidence Distribution"
            )

            st.plotly_chart(
                bar,
                use_container_width=True
            )

        st.divider()

        history["Prediction No."] = np.arange(1, len(history) + 1)

        line = px.line(
            history,
            x="Prediction No.",
            y="Confidence",
            color="Prediction",
            markers=True,
            title="Confidence Trend"
        )

        st.plotly_chart(
            line,
            use_container_width=True
        )
# ---------------- HISTORY ---------------- #

st.divider()

st.subheader("📜 Prediction History")

history_file = "history.csv"

if os.path.exists(history_file):

    try:

        history = pd.read_csv(history_file)

        if history.empty:

            st.info("No predictions yet.")

        else:

            st.dataframe(
                history.iloc[::-1],
                use_container_width=True,
                hide_index=True
            )

    except Exception:

        st.error("history.csv is corrupted. Delete it and run again.")

else:

    st.info("No history available yet.")