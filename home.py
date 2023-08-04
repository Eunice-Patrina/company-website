import streamlit as st
import pandas

st.set_page_config(layout="wide")

st.header("The Best Company")


content = """ A company, abbreviated as co., is a legal entity representing an association of people, 
whether natural, legal or a mixture of both, with a specific objective. Company members share a common purpose 
and unite to achieve specific, declared goals. """
st.write(content)

st.subheader("Our Team")

data = pandas.read_csv("data.csv")

length1 = int((len(data) + 1) / 3)
length2 = length1 * 2
col1, col2, col3 = st.columns(3)


with col1:
    for index, value in data[:length1].iterrows():
        name = "{} {}".format(value["first name"], value["last name"])
        st.subheader(name.title())
        st.write(value["role"])
        st.image(f"images/{value['image']}")

with col2:
    for index, value in data[length1:length2].iterrows():
        name = "{} {}".format(value["first name"], value["last name"])
        st.subheader(name.title())
        st.write(value["role"])
        st.image(f"images/{value['image']}")

with col3:
    for index, value in data[length2:].iterrows():
        name = "{} {}".format(value["first name"], value["last name"])
        st.subheader(name.title())
        st.write(value["role"])
        st.image(f"images/{value['image']}")
