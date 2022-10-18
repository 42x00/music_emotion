import random
import pandas as pd
import streamlit as st
import altair as alt


@st.cache
def load_data():
    df = pd.read_csv('../data/label/MeanCategoryRatingsUSA.csv')
    df = df.set_index('filename')
    return df


df = load_data()

if 'index' not in st.session_state:
    st.session_state.index = random.randint(0, 1841)

if st.button('Next'):
    st.session_state.index = random.randint(0, 1841)

row = df.iloc[st.session_state.index]

st.text(row.name)

st.audio(f'https://s3.amazonaws.com/musicemo/Verified_Normed/{row.name}')

data = pd.melt(row.reset_index(), id_vars=["index"])
chart = (
    alt.Chart(data)
        .mark_bar()
        .encode(
        x=alt.X("value", type="quantitative", title="", scale=alt.Scale(domain=[0., 1.])),
        y=alt.Y("index", type="nominal", title=""),
        color=alt.Color("variable", type="nominal", title="", legend=None),
    )
)
st.altair_chart(chart, use_container_width=True)
