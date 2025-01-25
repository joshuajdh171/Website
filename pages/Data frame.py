import pandas as Gok
import streamlit as st
data = Gok.read_excel('./pages/Source.xlsx')
unique_category = data['category'].unique()
selected_category = st.multiselect("Select Category",options=unique_category)


                               
# print(data)
# too find (down)
criteria1 = data['Category'].isin(selected_category)
criteria2 = data['store'] == "AMBATOBOES"
criteria3 = data['price'] > 1200
criteria4 = (data['price'] >= 1200) & (data['price'] < 2070)
criteria5 = (criteria1) & (criteria2) & (criteria3)
data = data[criteria1]
# print(data[criteria5])
print(data[criteria5].sort_values('price',ascending=True))
st.dataframe(data)
