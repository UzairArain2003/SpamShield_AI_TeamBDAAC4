import streamlit as st


def show_metrics():

    st.subheader("📊 Model Performance")

    c1, c2, c3 = st.columns(3)

    with c1:
        st.metric(
            "Accuracy",
            "98.2%"
        )

    with c2:
        st.metric(
            "Precision",
            "97.8%"
        )

    with c3:
        st.metric(
            "Recall",
            "96.4%"
        )