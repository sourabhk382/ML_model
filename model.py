#  The goal was to predict apparent temperature for the given humidity, windspeed.
import pandas as pd
import numpy as np
from sklearn import linear_model
import pickle
df = pd.read_csv('Apparenttemperature.csv')
df.head()
df.describe()
df.isnull().sum()
df1 = df[['Temperature (C)', 'Apparent Temperature (C)', 'Humidity', 'Wind Speed (km/h)']]  # required features
reg = linear_model.LinearRegression()
reg.fit(df1.drop('Apparent Temperature (C)', axis='columns'),
        df1['Apparent Temperature (C)'])  # ax+by+cz+d=>apparent temperature
# In[23]:
# 1.12(temp)+1.05(humidity)-0.09(windspeed)-2.33=apparent temp.
# In[24]:
reg.predict([[40, 0.80, 5]])  # Analysis: 40 degree temp with high humidity will feel like 43 degree.
# In[25]:
reg.predict([[40, 0.20, 50]])  # Analysis: 40 degree temp with high windspeed will feel like 38 degree.
# In[26]:
# In[28]:
pickle.dump(reg, open('model.pkl', 'wb'))
model = pickle.load(open('model.pkl', 'rb'))
print(model.predict([[40, 0.20, 50]]))
