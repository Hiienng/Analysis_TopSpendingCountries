import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#Logo
# logo_image = r"C:\Users\admin\Downloads\logo.png"  # Thay đổi đường dẫn tới hình ảnh logo của bạn
# st.image(logo_image, width=200)

# Read the dataset
data = pd.read_csv(r'C:\Users\admin\Desktop\Macbook\TD\result.csv')

# Set page title
st.title('Interactive Report')

# Add filters
year_types = sorted(data['Year'].unique().tolist(), reverse=True)
selected_year_type = st.selectbox('Year:', year_types)
month_types = sorted(data['Month'].unique().tolist(), reverse=True)
selected_month_type = st.selectbox('Month:', month_types)

term_cms = ['All'] + data['Term_CM'].unique().tolist()
selected_term_cm = st.selectbox('Term_CM:', term_cms)

term_lms = ['All'] + data['movement_type'].unique().tolist()
selected_term_lm = st.selectbox('movement_type:', term_lms)

currencies = sorted(data['Currency_2'].unique().tolist(), reverse=True) + ['All']
selected_currency = st.selectbox('Currency:', currencies)

# Apply filters
if selected_year_type == 'All':
    filtered_data = data
else:
    filtered_data = data[data['Year'] == selected_year_type]

if selected_month_type == 'All':
    filtered_data = data
else:
    filtered_data = data[data['Month'] == selected_month_type]

if selected_term_cm != 'All':
    filtered_data = filtered_data[filtered_data['Term_CM'] == selected_term_cm]

if selected_term_lm != 'All':
    filtered_data = filtered_data[filtered_data['movement_type'] == selected_term_lm]

if selected_currency != 'All':
    filtered_data = filtered_data[filtered_data['Currency_2'] == selected_currency]

# Display filtered data

st.subheader('Filtered Data')
column_order = ['period', 'Term_CM', 'Currency_2', 'movement_type', 'EOP_LM', 'EOP_CM', 'EOP_CM_FCST']
row_order = filtered_data.sort_values('movement_type', ascending = True).sort_values(by=['period', 'Currency_2', 'Term_CM'], ascending=False).index
st.write(filtered_data.loc[row_order, column_order])

# Visualize data
sns.set(style="ticks")

# Create a single subplot with shared y-axis
if selected_term_lm is not 'All':
    fig, ax = plt.subplots(figsize=(20, 10))
    plt.figure(figsize=(10, 6))
    sns.lineplot(data=filtered_data, x='period', y='EOP_CM', hue='movement_type', color='blue', legend='auto')
    sns.lineplot(data=filtered_data, x='period', y='EOP_CM_FCST', hue='movement_type', color='red', legend='auto')
    plt.xlabel('Period')
    plt.ylabel('Value')
    plt.title('EOP_CM, EOP_LM, and EOP_CM_FCST')
    plt.legend()
    st.pyplot(plt)