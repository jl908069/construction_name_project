import streamlit as st 
import pandas as pd

# PANDAS DATABASE CREATION
st.set_page_config(
  page_title="Construction Name Dashboard",
  layout="centered"                 
)
st.title("Construction Name Dashboard")

df = pd.read_csv('df.csv', skiprows=0, encoding="unicode_escape")
#st.dataframe(df)

# SIDEBAR
st.sidebar.header("Search here:")

options0 = df.sort_values('language').language.unique().tolist()
selected_options0 = st.sidebar.multiselect('Select the language:',options0)

options1 = df.sort_values('spacy_constructions_title').spacy_constructions_title.unique().tolist()
selected_options1 = st.sidebar.multiselect('Select the Potential Construction Names:',options1)

df_selection = df[df["spacy_constructions_title"].isin(selected_options1)& df["language"].isin(selected_options0)]

for n, (title,abstract) in enumerate(zip(df_selection['title'], df_selection['abstract']),1):
  st.write(f'''<h3>{title}</h3>

<p>{abstract}</p>

''', unsafe_allow_html=True)


