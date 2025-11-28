import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load data
data_path = 'CarSalesDashboard/data/Car_sales.csv'

@st.cache_data
def load_data(path):
    return pd.read_csv(path)

df = load_data(data_path)

st.title("🚗 Car Sales Data Dashboard")
st.write("Interactive analytics dashboard for car sales dataset.")

# Clean data
df = df[['Manufacturer','Model','Sales_in_thousands','Vehicle_type','Latest_Launch']]
df.dropna(inplace=True)
# ====================================
# Sidebar filters or sidebar widgets
# ====================================
st.sidebar.header("Filters")
selected_manufacturer = st.sidebar.multiselect(
    "Select Manufacturer", options=df['Manufacturer'].unique(), default=None
)
selected_vehicle_type = st.sidebar.multiselect(
    "Select Vehicle Type", options=df['Vehicle_type'].unique(), default=None
)
#------------------Apply filters-------------------------
filtered_df = df.copy()
# Apply manufacturer filter
if selected_manufacturer:
    filtered_df = filtered_df[filtered_df['Manufacturer'].isin(selected_manufacturer)]
# Apply vehicle type filter
if selected_vehicle_type:
    filtered_df = filtered_df[filtered_df['Vehicle_type'].isin(selected_vehicle_type)]

st.subheader("Filtered Dataset Preview")
st.dataframe(filtered_df.head())

# ====================================
# Chart 1 — Sales by Model (Bar Chart)
# ====================================
st.subheader("📊 Sales by Model (Top Models)")

if filtered_df.empty:
    st.warning("⚠ No data available for the selected filters.")
else:
    sales_by_model = filtered_df.groupby('Model')['Sales_in_thousands'].sum() \
                                .sort_values(ascending=False).head(15)

    fig1, ax1 = plt.subplots(figsize=(12, 6))
    sales_by_model.plot(kind='bar', ax=ax1)
    plt.title("Top Selling Car Models")
    plt.xlabel("Car Model")
    plt.ylabel("Sales in Thousands")
    plt.tight_layout()
    st.pyplot(fig1)


# ====================================
# Chart 2 — Sales Trend Over Years (Line)
# ====================================
st.subheader("📈 Sales Trend by Latest Launch Year")

sales_trend = filtered_df.groupby('Latest_Launch')['Sales_in_thousands'].sum()

fig2, ax2 = plt.subplots(figsize=(10, 5))
sales_trend.sort_index().plot(kind='line', marker='o', ax=ax2)
plt.title("Sales Trend Over Launch Years")
plt.xlabel("Launch Year")
plt.ylabel("Total Sales (Thousands)")
plt.grid()
st.pyplot(fig2)

# ====================================
# Chart 3 — Sales Distribution (Histogram)
# ====================================
st.subheader("📉 Sales Distribution (Histogram)")

fig3, ax3 = plt.subplots(figsize=(10, 5))
sns.histplot(filtered_df['Sales_in_thousands'], bins=20, ax=ax3)
plt.title("Distribution of Car Sales")
plt.xlabel("Sales in Thousands")
st.pyplot(fig3)

# ====================================
# Chart 4 — Sales by Manufacturer (Pie Chart)
# ====================================
st.subheader("🥧 Sales Share by Manufacturer")

sales_by_manufacturer = filtered_df.groupby('Manufacturer')['Sales_in_thousands'].sum()

fig4, ax4 = plt.subplots(figsize=(8, 8))
sales_by_manufacturer.plot(kind='pie', autopct='%1.1f%%', ax=ax4)
plt.ylabel("")
plt.title("Manufacturer Sales Share")
st.pyplot(fig4)

# ====================================
# Chart 5 — Scatter Plot (Sales vs Latest Launch Year)
# ====================================
st.subheader("🔵 Scatter Plot: Sales vs Launch Year")

fig5, ax5 = plt.subplots(figsize=(10, 6))
sns.scatterplot(data=filtered_df, x='Latest_Launch', y='Sales_in_thousands', hue='Manufacturer', ax=ax5)
plt.title("Sales vs Launch Year")
plt.xlabel("Launch Year")
plt.ylabel("Sales (Thousands)")
plt.grid()
st.pyplot(fig5)

# ====================================
# Chart 6 — Correlation Heatmap
# ====================================
st.subheader("🔥 Correlation Heatmap")
# Convert Latest_Launch to datetime
filtered_df['Latest_Launch'] = pd.to_datetime(filtered_df['Latest_Launch'], errors='coerce')

# Extract year for analysis
filtered_df['Launch_Year'] = filtered_df['Latest_Launch'].dt.year

numeric_df = filtered_df[['Sales_in_thousands', 'Launch_Year']]
corr = numeric_df.corr()

fig6, ax6 = plt.subplots(figsize=(6, 4))
sns.heatmap(corr, annot=True, cmap="coolwarm", ax=ax6)
plt.title("Correlation Matrix")
st.pyplot(fig6)

# ====================================
# Metrics
# ====================================
st.subheader("📌 Summary Metrics")

col1, col2 = st.columns(2)
col1.metric("Average Sales", round(filtered_df['Sales_in_thousands'].mean(), 2))
col2.metric("Total Models in Filter", filtered_df['Model'].nunique())
col1.metric("Total Sales", round(filtered_df['Sales_in_thousands'].sum(), 2))
col2.metric("Unique Manufacturers", filtered_df['Manufacturer'].nunique())
