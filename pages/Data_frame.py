import pandas as pd
import streamlit as st
data = pd.read_excel('./pages/Source.xlsx')
unique_category = data['Category'].unique()
unique_storename = data['store'].unique()
maximum_price = data['price'].max()
minimum_price = data['price'].min()
selected_category = st.multiselect("Select Category",options=unique_category,default=unique_category)
selected_store = st.multiselect("Select store",options=unique_storename,default=unique_storename)
price_point = st.slider("price",min_value=minimum_price,max_value=maximum_price,value=maximum_price)

                               
# print(data)
# too find (down)
criteria1 = data['Category'].isin(selected_category)
criteria2 = data['store'].isin(selected_store)
criteria3 = data['price'] <= price_point


join_criteria = (criteria1) & (criteria2) & (criteria3)


with st.container(border=True):
  data = data[join_criteria]
  data_count = len(data)
  for i in range(data_count)
    product_picture = data.iloc[i]['picture']
    st.image(product_picture)

st.dataframe(data,use_container_width=True)


'''
criteria3 = data['price'] > 1200
criteria4 = (data['price'] >= 1200) & (data['price'] < 2070)
criteria5 = (criteria1) & (criteria2) & (criteria3)
data = data[join_criteria]

# print(data[criteria5])
print(data[criteria5].sort_values('price',ascending=True))
st.dataframe(data)
'''
