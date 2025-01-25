import streamlit as st
import pandas as pd
st.title("Every ahh store for no reason")
col1, col2, col3 = st.columns(3)

df = pd.read_excel('./pages/source.xlsx')
with st.container(border=True):
        with col1:
            selected_Category = st.selectbox("Choose category",options=df['Category'].unique())
        with col2:
            selected_Name = st.selectbox("Choose name kid",options=df['Name'].unique())
        with col3:
            selected_store = st.selectbox("Choose store",options=df['store'].unique())
            
df = df[df['Category'] == selected_Category ]
df = df[df['Name'] == selected_Name ]
st.dataframe(df)




#fofofofpfpfoasdfpfpwcppfpsppfpsllscllwdvxiiivpppdavgppavggpwfgpgpsdpf[fpdppoyopeqvpqweriyradewq
#dbvbpbjhefbbpbphbbbqwehbthpopbwqecphwebfcpbpoewpbhefwpbhpqehggpbppwerbhopbbhp
#bbpohbewrbbvopbpoenbppbpwrgvp0bpbypep0ebvpohbgpobbhpopwjvgoehoujopegegehgpoghgguhruhyh
