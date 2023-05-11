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

df['potential_constructions']=df.potential_constructions.astype(str)
options1 = df.sort_values('potential_constructions').potential_constructions.unique().tolist()
options1=[x.lower() for x in options1]
op1=[a for a in options1 if options1.count(a) > 1] #filter out constructions that have a frequency lower than 1
op1 = [*set(op1)]
selected_options1 = st.sidebar.multiselect('Select the Potential Construction Names:',op1)

df_selection = df[df["potential_constructions"].isin(selected_options1)& df["language"].isin(selected_options0)]

for n, (title,abstract) in enumerate(zip(df_selection['title'], df_selection['abstract']),1):
  st.write(f'''<h3>{title}</h3>

<p>{abstract}</p>

''', unsafe_allow_html=True)


