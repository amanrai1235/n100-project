import streamlit as st

st.set_page_config(
    page_title="N100 Financial Analytics Dashboard",
    page_icon="📊",
    layout="wide"
)

st.title("📊 N100 Financial Analytics Dashboard")

st.markdown("""
Welcome to the **N100 Financial Analytics Dashboard**.

Use the sidebar to navigate between different modules.
""")

st.sidebar.success("Select a page from the sidebar.")

st.subheader("Available Modules")

modules = [
    "🏠 Home",
    "🏢 Company Profile",
    "📊 Stock Screener",
    "👥 Peer Comparison",
    "📈 Trend Analysis",
    "🏭 Sector Analysis",
    "💰 Capital Allocation",
    "📄 Annual Reports"
]

for module in modules:
    st.write(f"✅ {module}")

st.info("Dashboard scaffold created successfully.")