import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

# --- 1. Page Configuration ---
st.set_page_config(
    page_title="Executive Sales Dashboard",
    page_icon="📊",
    layout="wide"
)

# --- 2. Data Loading (Cached) ---
@st.cache_data
def load_data():
    """Generates synthetic sales data for demonstration."""
    np.random.seed(42)
    dates = pd.date_range(start="2024-01-01", end="2024-12-31", freq="D")
    n_rows = len(dates) * 5 # More volume
    
    products = ['Laptop Pro', 'Ergo Mouse', '4K Monitor', 'Mech Keyboard', 'Noise-Cancel Headset']
    regions = ['North America', 'Europe', 'Asia Pacific', 'Latin America']
    status_options = ['Completed', 'Pending', 'Returned']
    
    data = {
        'Date': np.random.choice(dates, n_rows),
        'Product': np.random.choice(products, n_rows),
        'Region': np.random.choice(regions, n_rows),
        'Status': np.random.choice(status_options, n_rows, p=[0.8, 0.15, 0.05]),
        'Units_Sold': np.random.randint(1, 20, n_rows),
        'Unit_Price': np.random.uniform(50, 2500, n_rows)
    }
    
    df = pd.DataFrame(data)
    df['Total_Revenue'] = df['Units_Sold'] * df['Unit_Price']
    return df

df = load_data()

# --- 3. Sidebar Filters ---
st.sidebar.header("🎯 Control Panel")
st.sidebar.markdown("Use filters to segment the view.")

# Region Filter
selected_region = st.sidebar.multiselect(
    "Select Region:",
    options=df['Region'].unique(),
    default=df['Region'].unique()
)

# Product Filter
selected_product = st.sidebar.multiselect(
    "Select Product:",
    options=df['Product'].unique(),
    default=df['Product'].unique()
)

# Applying Filters
df_filtered = df.query(
    "Region == @selected_region & Product == @selected_product"
)

# --- 4. Main Dashboard ---
st.title("📊 Executive Sales Performance")
st.markdown("Real-time monitoring of sales KPIs and product trends.")
st.markdown("---")

# Safety check for empty data
if df_filtered.empty:
    st.warning("⚠️ No data available based on current filters!")
    st.stop()

# --- 5. KPI Metrics Row ---
total_revenue = df_filtered['Total_Revenue'].sum()
avg_ticket = df_filtered['Total_Revenue'].mean()
total_units = df_filtered['Units_Sold'].sum()
# Calculating growth (simulation vs fake target)
revenue_target = 5000000 
delta_rev = ((total_revenue - revenue_target) / revenue_target) * 100

col1, col2, col3 = st.columns(3)
with col1:
    st.metric(label="Total Revenue", value=f"${total_revenue:,.2f}", delta=f"{delta_rev:.1f}% vs Target")
with col2:
    st.metric(label="Average Ticket", value=f"${avg_ticket:,.2f}")
with col3:
    st.metric(label="Units Sold", value=f"{total_units:,}")

st.markdown("---")

# --- 6. Charts Layout ---
chart_col1, chart_col2 = st.columns(2)

with chart_col1:
    st.subheader("🏆 Revenue by Product")
    fig_bar = px.bar(
        df_filtered.groupby('Product')['Total_Revenue'].sum().reset_index().sort_values(by='Total_Revenue'),
        x='Total_Revenue',
        y='Product',
        orientation='h',
        text_auto='.2s',
        color='Total_Revenue',
        color_continuous_scale='Blues'
    )
    fig_bar.update_layout(xaxis_title="Revenue ($)", yaxis_title="")
    st.plotly_chart(fig_bar, use_container_width=True)

with chart_col2:
    st.subheader("📅 Monthly Trend")
    # Resampling to Month Start
    df_monthly = df_filtered.set_index('Date').resample('ME')['Total_Revenue'].sum().reset_index()
    
    fig_line = px.line(
        df_monthly,
        x='Date',
        y='Total_Revenue',
        markers=True,
        line_shape='spline'
    )
    fig_line.update_traces(line_color='#FF4B4B', line_width=3)
    fig_line.update_layout(xaxis_title="Month", yaxis_title="Revenue ($)")
    st.plotly_chart(fig_line, use_container_width=True)

# --- 7. Data Grid ---
with st.expander("📂 View Raw Data"):
    st.dataframe(df_filtered.sort_values(by='Date', ascending=False))