"""
Financial Calculators - Various financial calculation tools
"""

import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime, timedelta

class FinancialCalculators:
    def __init__(self):
        pass
    
    def compound_interest_calculator(self):
        """Compound Interest Calculator"""
        st.subheader("🧮 Compound Interest Calculator")
        
        col1, col2 = st.columns(2)
        
        with col1:
            principal = st.number_input("Initial Investment ($)", min_value=0.0, value=10000.0, step=1000.0)
            monthly_contribution = st.number_input("Monthly Contribution ($)", min_value=0.0, value=500.0, step=50.0)
            annual_rate = st.number_input("Annual Interest Rate (%)", min_value=0.0, max_value=50.0, value=7.0, step=0.1)
            years = st.number_input("Investment Period (Years)", min_value=1, max_value=50, value=20, step=1)
        
        with col2:
            # Calculate compound interest
            monthly_rate = annual_rate / 100 / 12
            total_months = years * 12
            
            # Future value of initial investment
            fv_principal = principal * (1 + monthly_rate) ** total_months
            
            # Future value of monthly contributions (annuity)
            if monthly_rate > 0:
                fv_annuity = monthly_contribution * (((1 + monthly_rate) ** total_months - 1) / monthly_rate)
            else:
                fv_annuity = monthly_contribution * total_months
            
            total_future_value = fv_principal + fv_annuity
            total_contributions = principal + (monthly_contribution * total_months)
            total_interest = total_future_value - total_contributions
            
            # Display results
            st.metric("Total Future Value", f"${total_future_value:,.2f}")
            st.metric("Total Contributions", f"${total_contributions:,.2f}")
            st.metric("Total Interest Earned", f"${total_interest:,.2f}")
            st.metric("Return on Investment", f"{(total_interest/total_contributions*100):.1f}%")
        
        # Create projection chart
        if st.button("Generate Projection Chart"):
            self._create_compound_interest_chart(principal, monthly_contribution, annual_rate, years)
    
    def _create_compound_interest_chart(self, principal, monthly_contribution, annual_rate, years):
        """Create a chart showing compound interest growth over time"""
        monthly_rate = annual_rate / 100 / 12
        total_months = years * 12
        
        # Calculate values for each year
        years_data = []
        principal_values = []
        contribution_values = []
        total_values = []
        
        for year in range(years + 1):
            months = year * 12
            if months == 0:
                principal_val = principal
                contribution_val = 0
                total_val = principal
            else:
                # Future value of principal
                principal_val = principal * (1 + monthly_rate) ** months
                
                # Future value of contributions
                if monthly_rate > 0:
                    contribution_val = monthly_contribution * (((1 + monthly_rate) ** months - 1) / monthly_rate)
                else:
                    contribution_val = monthly_contribution * months
                
                total_val = principal_val + contribution_val
            
            years_data.append(year)
            principal_values.append(principal_val)
            contribution_values.append(contribution_val)
            total_values.append(total_val)
        
        # Create the chart
        fig = go.Figure()
        
        fig.add_trace(go.Scatter(
            x=years_data,
            y=principal_values,
            mode='lines',
            name='Initial Investment Growth',
            line=dict(color='blue', width=2)
        ))
        
        fig.add_trace(go.Scatter(
            x=years_data,
            y=contribution_values,
            mode='lines',
            name='Monthly Contributions Growth',
            line=dict(color='green', width=2)
        ))
        
        fig.add_trace(go.Scatter(
            x=years_data,
            y=total_values,
            mode='lines',
            name='Total Portfolio Value',
            line=dict(color='red', width=3)
        ))
        
        fig.update_layout(
            title="Compound Interest Growth Over Time",
            xaxis_title="Years",
            yaxis_title="Value ($)",
            hovermode='x unified',
            template="plotly_white"
        )
        
        st.plotly_chart(fig, use_container_width=True)
    
    def mortgage_calculator(self):
        """Mortgage Payment Calculator"""
        st.subheader("🏠 Mortgage Payment Calculator")
        
        col1, col2 = st.columns(2)
        
        with col1:
            home_price = st.number_input("Home Price ($)", min_value=0.0, value=300000.0, step=10000.0)
            down_payment = st.number_input("Down Payment ($)", min_value=0.0, value=60000.0, step=5000.0)
            interest_rate = st.number_input("Interest Rate (%)", min_value=0.0, max_value=20.0, value=6.5, step=0.1)
            loan_term = st.selectbox("Loan Term", [15, 20, 30], index=2)
        
        with col2:
            # Calculate loan amount
            loan_amount = home_price - down_payment
            
            # Calculate monthly payment
            monthly_rate = interest_rate / 100 / 12
            total_payments = loan_term * 12
            
            if monthly_rate > 0:
                monthly_payment = loan_amount * (monthly_rate * (1 + monthly_rate) ** total_payments) / ((1 + monthly_rate) ** total_payments - 1)
            else:
                monthly_payment = loan_amount / total_payments
            
            total_paid = monthly_payment * total_payments
            total_interest = total_paid - loan_amount
            
            # Display results
            st.metric("Loan Amount", f"${loan_amount:,.2f}")
            st.metric("Monthly Payment", f"${monthly_payment:,.2f}")
            st.metric("Total Interest", f"${total_interest:,.2f}")
            st.metric("Total Paid", f"${total_paid:,.2f}")
            st.metric("Down Payment %", f"{(down_payment/home_price*100):.1f}%")
        
        # Payment breakdown
        if st.button("Show Payment Breakdown"):
            self._create_mortgage_breakdown_chart(loan_amount, interest_rate, loan_term)
    
    def _create_mortgage_breakdown_chart(self, loan_amount, interest_rate, loan_term):
        """Create a chart showing principal vs interest payments over time"""
        monthly_rate = interest_rate / 100 / 12
        total_payments = loan_term * 12
        
        # Calculate monthly payment
        if monthly_rate > 0:
            monthly_payment = loan_amount * (monthly_rate * (1 + monthly_rate) ** total_payments) / ((1 + monthly_rate) ** total_payments - 1)
        else:
            monthly_payment = loan_amount / total_payments
        
        # Calculate payment breakdown for each year
        years_data = []
        principal_payments = []
        interest_payments = []
        remaining_balance = []
        
        balance = loan_amount
        for year in range(loan_term + 1):
            year_principal = 0
            year_interest = 0
            
            for month in range(12):
                if balance > 0:
                    interest_payment = balance * monthly_rate
                    principal_payment = monthly_payment - interest_payment
                    
                    if principal_payment > balance:
                        principal_payment = balance
                    
                    year_principal += principal_payment
                    year_interest += interest_payment
                    balance -= principal_payment
            
            years_data.append(year)
            principal_payments.append(year_principal)
            interest_payments.append(year_interest)
            remaining_balance.append(balance)
        
        # Create stacked bar chart
        fig = go.Figure()
        
        fig.add_trace(go.Bar(
            x=years_data,
            y=principal_payments,
            name='Principal',
            marker_color='green'
        ))
        
        fig.add_trace(go.Bar(
            x=years_data,
            y=interest_payments,
            name='Interest',
            marker_color='red'
        ))
        
        fig.update_layout(
            title="Annual Principal vs Interest Payments",
            xaxis_title="Year",
            yaxis_title="Payment Amount ($)",
            barmode='stack',
            template="plotly_white"
        )
        
        st.plotly_chart(fig, use_container_width=True)
    
    def loan_calculator(self):
        """General Loan Payment Calculator"""
        st.subheader("💳 Loan Payment Calculator")
        
        col1, col2 = st.columns(2)
        
        with col1:
            loan_amount = st.number_input("Loan Amount ($)", min_value=0.0, value=25000.0, step=1000.0)
            interest_rate = st.number_input("Interest Rate (%)", min_value=0.0, max_value=50.0, value=8.5, step=0.1)
            loan_term = st.number_input("Loan Term (Years)", min_value=1, max_value=30, value=5, step=1)
            loan_type = st.selectbox("Loan Type", ["Personal Loan", "Auto Loan", "Student Loan", "Other"])
        
        with col2:
            # Calculate monthly payment
            monthly_rate = interest_rate / 100 / 12
            total_payments = loan_term * 12
            
            if monthly_rate > 0:
                monthly_payment = loan_amount * (monthly_rate * (1 + monthly_rate) ** total_payments) / ((1 + monthly_rate) ** total_payments - 1)
            else:
                monthly_payment = loan_amount / total_payments
            
            total_paid = monthly_payment * total_payments
            total_interest = total_paid - loan_amount
            
            # Display results
            st.metric("Monthly Payment", f"${monthly_payment:,.2f}")
            st.metric("Total Interest", f"${total_interest:,.2f}")
            st.metric("Total Paid", f"${total_paid:,.2f}")
            st.metric("Interest Rate", f"{interest_rate:.2f}%")
            st.metric("Loan Type", loan_type)
        
        # Amortization schedule
        if st.button("Show Amortization Schedule"):
            self._create_amortization_schedule(loan_amount, interest_rate, loan_term, monthly_payment)
    
    def _create_amortization_schedule(self, loan_amount, interest_rate, loan_term, monthly_payment):
        """Create an amortization schedule table"""
        monthly_rate = interest_rate / 100 / 12
        total_payments = loan_term * 12
        
        # Create amortization schedule
        schedule_data = []
        balance = loan_amount
        
        for month in range(1, total_payments + 1):
            interest_payment = balance * monthly_rate
            principal_payment = monthly_payment - interest_payment
            
            if principal_payment > balance:
                principal_payment = balance
                monthly_payment = principal_payment + interest_payment
            
            balance -= principal_payment
            
            schedule_data.append({
                'Month': month,
                'Payment': f"${monthly_payment:.2f}",
                'Principal': f"${principal_payment:.2f}",
                'Interest': f"${interest_payment:.2f}",
                'Balance': f"${balance:.2f}"
            })
            
            if balance <= 0:
                break
        
        # Display first 12 months and last 12 months
        df = pd.DataFrame(schedule_data)
        
        st.subheader("Amortization Schedule")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.write("**First 12 Months:**")
            st.dataframe(df.head(12), use_container_width=True)
        
        with col2:
            st.write("**Last 12 Months:**")
            st.dataframe(df.tail(12), use_container_width=True)
        
        # Download option
        csv = df.to_csv(index=False)
        st.download_button(
            label="Download Full Schedule (CSV)",
            data=csv,
            file_name=f"amortization_schedule_{loan_amount}_{interest_rate}%.csv",
            mime="text/csv"
        )

