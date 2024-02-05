import streamlit as st
import pandas as pd
import altair as alt

data = pd.read_csv('diabetes.csv')
# Assigning the input and output variable
# Check if 'Outcome' column exists in the dataset
if 'Outcome' in data.columns:
    # Assigning the input and output variables
    X = data.drop('Outcome', axis=1)  # Drop 'Outcome' to get features
    y = data['Outcome']  # Assign 'Outcome' as the target variable
else:
    print("Column 'Outcome' not found in the dataset.")

# Sidebar with filtering option
st.sidebar.title("Diabetes Data Explorer")

# Filter outcome by (0 or 1)
outer_filter = st.sidebar.multiselect('Filter by Outcome,', [0,1], [0,1])
filtered_data = data[data['Outcome'].isin(outer_filter)]

# Scatter plot with customizable axes
st.subheader('Scatter Plot')
x_axis = st.selectbox('X-axis',data.columns[:-1])
y_axis = st.selectbox('Y-axis', data.columns[:-1], index=1)
scatter = alt.Chart(filtered_data).mark_circle().encode(
    x=x_axis,
    y=y_axis,
    color='Outcome:N'
).interactive()
st.altair_chart(scatter, use_container_width=True)

# Bar Chart
st.subheader('Bar Chart')
vertical_axis = st.selectbox('Vertical-axis', data.columns[:-1])
horizontal_axis = st.selectbox('Horizontal-axis', data.columns[:-1], index=1)
bar = alt.Chart(filtered_data).mark_bar().encode(
    x=vertical_axis,
    y=horizontal_axis,
    color='Outcome:N'
).interactive()
st.altair_chart(bar, use_container_width=True)

# Line Chart
st.subheader('Line Chart')
abscissa = st.selectbox('Abscissa', data.columns[:-1])
ordinate = st.selectbox('Ordinate', data.columns[:-1],index=1)
line = alt.Chart(filtered_data).mark_line().encode(
    x=abscissa,
    y=ordinate,
    color='Outcome:N'
).interactive()
st.altair_chart(line, use_container_width=True)

# Box Plot
st.subheader('Box Plot')
X_axis = st.selectbox('X-coordinate', data.columns[:-1])
Y_axis = st.selectbox('Y-ordinate', data.columns[:-1], index=1)
box_plot = alt.Chart(filtered_data).mark_boxplot().encode(
    x=X_axis,
    y=Y_axis,
    color='Outcome:N'
).interactive()
st.altair_chart(box_plot, use_container_width=True)

# Histogram
st.subheader('Histogram')
histogram_data = data.melt(value_vars=data.columns[:-1])
selected_variable = st.selectbox('Select a Variable',data.columns[:-1])
filtered_hist = alt.Chart(histogram_data).mark_bar().encode(
    x=alt.X('value', bin=alt.Bin(maxbins=30)),
    y='count()',
    color='Outcome:N'
).transform_filter(
    alt.FieldOneOfPredicate(field='variable', oneOf=[selected_variable])
).interactive()
st.altair_chart(filtered_hist, use_container_width=True)

# Correlation Matrix
st.subheader('Correlation Matrix')
correlation_matrix = data.corr()
st.text('Correlation Matrix: ')
st.write(correlation_matrix)

# Heat Map of the Correlation Matrix
st.subheader('Correlation Matrix HeatMap')
heat_map = alt.Chart(correlation_matrix.reset_index().melt('index')).mark_rect().encode(
    x='index:N',
    y='Variable:N',
    color='value:Q',
)
st.altair_chart(heat_map, use_container_width=True)





