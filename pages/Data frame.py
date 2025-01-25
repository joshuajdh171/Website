import pandas as Gok

data = Gok.read_excel('Source.xlsx')

# print(data)
# too find (down)
criteria1 = data['Category'] == 'Guns'
criteria2 = data['store'] == "AMBATOBOES"
criteria3 = data['price'] > 1200
criteria4 = (data['price'] >= 1200) & (data['price'] < 2070)
criteria5 = (criteria1) & (criteria2) & (criteria3) & (criteria4)

# print(data[criteria5])
print(data[criteria5].sort_values('price',ascending=True))