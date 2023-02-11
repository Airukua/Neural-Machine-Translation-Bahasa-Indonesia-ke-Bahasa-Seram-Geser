import streamlit as st

# Title for the page and nice icon
st.set_page_config(page_title="MalukuAI | Aplikasi Penerjemah Bahasa", page_icon="🤖")
# Header
st.title("Demo NMT Indonesia-Geser")
st.subheader("Menyelamatkan Warisan Budaya: Bahasa Geser Terancam Punah")
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)
st.text("""Bahasa Geser adalah bahasa yang sangat kaya akan warisan dan budaya. 
Namun, sayangnya bahasa ini mulai terlupakan dan terancam punah. Seiring berjalannya 
waktu,generasi muda mulai meninggalkan bahasa tradisional ini dan 
bahasa Geser mulai menghilang dari masyarakat.""")

import streamlit as st
with st.form("my_form"):

    option = st.selectbox(
    "Pilih Bahasa",
    ("Indonesia-Geser", "Geser-Indonesia"))
    #st.write('You selected:', option)

    # Textarea to type the source text.
    user_input = st.text_area("Source Text", max_chars=200)

    # Create a button
    submitted = st.form_submit_button("Terjemahkan")
