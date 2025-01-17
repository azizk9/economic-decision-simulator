import streamlit as st
import plotly.express as px

# عنوان التطبيق
st.title("محاكي القرارات الاقتصادية")

# إدخال البيانات الأساسية
st.sidebar.header("إعدادات المشروع")
initial_budget = st.sidebar.number_input("الميزانية المبدئية ($)", value=10000, step=500)
monthly_revenue = st.sidebar.number_input("الإيرادات الشهرية ($)", value=2000, step=100)
monthly_expenses = st.sidebar.number_input("النفقات الشهرية ($)", value=1500, step=100)
marketing_investment = st.sidebar.number_input("الاستثمار في التسويق ($)", value=500, step=100)
months = st.sidebar.slider("عدد الأشهر للتوقع", min_value=1, max_value=24, value=12)

# حساب التوقعات
monthly_profit = monthly_revenue - monthly_expenses - marketing_investment
cumulative_budget = [initial_budget]

for month in range(1, months + 1):
    cumulative_budget.append(cumulative_budget[-1] + monthly_profit)

# عرض النتائج
st.subheader("التوقعات المالية")
st.write(f"الأرباح الشهرية: ${monthly_profit}")
st.write(f"الميزانية المتوقعة بعد {months} شهرًا: ${cumulative_budget[-1]}")

# رسم البيانات
fig = px.line(
    x=list(range(0, months + 1)),
    y=cumulative_budget,
    labels={"x": "الشهر", "y": "الميزانية ($)"},
    title="التوقعات المالية على مدى الأشهر"
)
st.plotly_chart(fig)
