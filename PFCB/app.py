import streamlit as st
import json
import datetime
from typing import List, Dict, Any
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from finance_knowledge import FinanceKnowledge
from financial_calculators import FinancialCalculators
from budget_tracker import BudgetTracker
from investment_advisor import InvestmentAdvisor

# Page configuration
st.set_page_config(
    page_title="FINBOT - Personal Finance Advisor",
    page_icon="💰",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for better styling
st.markdown("""
<style>
    .main-header {
        font-size: 2.5rem;
        font-weight: bold;
        color: #1f77b4;
        text-align: center;
        margin-bottom: 2rem;
    }
    .chat-message {
        padding: 1rem;
        border-radius: 10px;
        margin: 0.5rem 0;
        max-width: 80%;
        color: #e0e0e0;
        font-weight: 500;
    }
    .user-message {
        background-color: #2d2d2d;
        margin-left: auto;
        text-align: right;
        border: 1px solid #404040;
    }
    .bot-message {
        background-color: #1a1a1a;
        margin-right: auto;
        border: 1px solid #333333;
    }
    .stButton > button {
        background-color: #1f77b4;
        color: white;
        border-radius: 20px;
        border: none;
        padding: 0.5rem 1rem;
    }
    .stButton > button:hover {
        background-color: #1565c0;
    }
    .chat-message strong {
        color: #ffffff;
        font-weight: 600;
    }
</style>
""", unsafe_allow_html=True)

class FinanceChatbot:
    def __init__(self):
        self.knowledge = FinanceKnowledge()
        self.calculators = FinancialCalculators()
        self.budget_tracker = BudgetTracker()
        self.investment_advisor = InvestmentAdvisor()
        
    def initialize_session_state(self):
        """Initialize session state variables"""
        if 'messages' not in st.session_state:
            st.session_state.messages = []
        if 'user_profile' not in st.session_state:
            st.session_state.user_profile = {
                'name': '',
                'age': 25,
                'income': 50000,
                'savings_goal': 100000,
                'risk_tolerance': 'moderate'
            }
        if 'budget_data' not in st.session_state:
            st.session_state.budget_data = []
        if 'investment_portfolio' not in st.session_state:
            st.session_state.investment_portfolio = {}
    
    def display_header(self):
        """Display the main header"""
        st.markdown('<h1 class="main-header">💰 FINBOT - Personal Finance Advisor</h1>', unsafe_allow_html=True)
        st.markdown("---")
    
    def display_sidebar(self):
        """Display sidebar with user profile and quick actions"""
        with st.sidebar:
            st.header("👤 Your Profile")
            
            # User profile form
            with st.form("user_profile_form"):
                st.subheader("Update Profile")
                name = st.text_input("Name", value=st.session_state.user_profile['name'])
                age = st.number_input("Age", min_value=18, max_value=100, value=st.session_state.user_profile['age'])
                income = st.number_input("Annual Income ($)", min_value=0, value=st.session_state.user_profile['income'])
                savings_goal = st.number_input("Savings Goal ($)", min_value=0, value=st.session_state.user_profile['savings_goal'])
                risk_tolerance = st.selectbox(
                    "Risk Tolerance",
                    ["conservative", "moderate", "aggressive"],
                    index=["conservative", "moderate", "aggressive"].index(st.session_state.user_profile['risk_tolerance'])
                )
                
                if st.form_submit_button("Update Profile"):
                    st.session_state.user_profile = {
                        'name': name,
                        'age': age,
                        'income': income,
                        'savings_goal': savings_goal,
                        'risk_tolerance': risk_tolerance
                    }
                    st.success("Profile updated!")
            
            st.markdown("---")
            
            # Quick actions
            st.header("🚀 Quick Actions")
            if st.button("📊 View Budget"):
                self.show_budget_dashboard()
            if st.button("💹 Investment Analysis"):
                self.show_investment_dashboard()
            if st.button("🧮 Financial Calculators"):
                self.show_calculators()
            if st.button("📈 Savings Progress"):
                self.show_savings_progress()
    
    def display_chat_interface(self):
        """Display the main chat interface"""
        st.header("💬 Chat with FINBOT")
        
        # Display chat messages
        for message in st.session_state.messages:
            with st.container():
                if message["role"] == "user":
                    st.markdown(f'<div class="chat-message user-message"><strong>You:</strong> {message["content"]}</div>', 
                              unsafe_allow_html=True)
                else:
                    st.markdown(f'<div class="chat-message bot-message"><strong>FINBOT:</strong> {message["content"]}</div>', 
                              unsafe_allow_html=True)
        
        # Chat input
        if prompt := st.chat_input("Ask me anything about personal finance..."):
            self.handle_user_input(prompt)
    
    def handle_user_input(self, user_input: str):
        """Process user input and generate response"""
        # Add user message to chat
        st.session_state.messages.append({"role": "user", "content": user_input})
        
        # Generate bot response
        response = self.generate_response(user_input)
        
        # Add bot response to chat
        st.session_state.messages.append({"role": "assistant", "content": response})
        
        # Rerun to display new messages
        st.rerun()
    
    def generate_response(self, user_input: str) -> str:
        """Generate response based on user input"""
        user_input_lower = user_input.lower()
        
        # Check for specific financial topics
        if any(word in user_input_lower for word in ['budget', 'expense', 'spending']):
            return self.handle_budget_question(user_input)
        elif any(word in user_input_lower for word in ['invest', 'investment', 'portfolio', 'stock', 'bond']):
            return self.handle_investment_question(user_input)
        elif any(word in user_input_lower for word in ['save', 'saving', 'emergency fund']):
            return self.handle_savings_question(user_input)
        elif any(word in user_input_lower for word in ['debt', 'loan', 'credit', 'pay off']):
            return self.handle_debt_question(user_input)
        elif any(word in user_input_lower for word in ['retirement', '401k', 'ira', 'pension']):
            return self.handle_retirement_question(user_input)
        elif any(word in user_input_lower for word in ['calculate', 'calculator', 'compute']):
            return self.handle_calculation_request(user_input)
        else:
            return self.knowledge.get_general_advice(user_input)
    
    def handle_budget_question(self, user_input: str) -> str:
        """Handle budget-related questions"""
        return self.budget_tracker.analyze_budget_question(user_input, st.session_state.user_profile)
    
    def handle_investment_question(self, user_input: str) -> str:
        """Handle investment-related questions"""
        return self.investment_advisor.get_investment_advice(user_input, st.session_state.user_profile)
    
    def handle_savings_question(self, user_input: str) -> str:
        """Handle savings-related questions"""
        profile = st.session_state.user_profile
        current_savings = profile.get('current_savings', 0)
        goal = profile['savings_goal']
        
        if 'emergency fund' in user_input.lower():
            emergency_fund = profile['income'] * 3  # 3 months of income
            return f"""Based on your income of ${profile['income']:,}, I recommend building an emergency fund of ${emergency_fund:,} (3 months of expenses).

Here's how to build it:
1. Start with $1,000 as your first milestone
2. Automate monthly transfers of 10-20% of your income
3. Keep it in a high-yield savings account
4. Don't touch it except for true emergencies

You're currently at ${current_savings:,} towards your goal of ${goal:,}. Keep going! 💪"""
        
        return f"""Great question about savings! Here are some strategies:

1. **Pay yourself first**: Automate 20% of your income to savings
2. **Set specific goals**: You're aiming for ${goal:,} - break it into monthly targets
3. **Use the 50/30/20 rule**: 50% needs, 30% wants, 20% savings
4. **Track your progress**: Monitor monthly to stay motivated

Current progress: ${current_savings:,} / ${goal:,} ({(current_savings/goal*100):.1f}%)"""
    
    def handle_debt_question(self, user_input: str) -> str:
        """Handle debt-related questions"""
        return """Here's my advice on managing debt:

**Debt Payoff Strategies:**
1. **Debt Snowball**: Pay minimums on all debts, extra on smallest balance
2. **Debt Avalanche**: Pay minimums on all debts, extra on highest interest rate
3. **Debt Consolidation**: Combine multiple debts into one lower-rate loan

**Priority Order:**
1. High-interest credit cards (15%+)
2. Personal loans
3. Auto loans
4. Student loans
5. Mortgage

**Quick Tips:**
- Never miss minimum payments
- Consider balance transfer cards for high-interest debt
- Look into refinancing options
- Build emergency fund to avoid new debt

Would you like me to help you create a specific debt payoff plan?"""
    
    def handle_retirement_question(self, user_input: str) -> str:
        """Handle retirement-related questions"""
        profile = st.session_state.user_profile
        age = profile['age']
        income = profile['income']
        
        # Calculate retirement needs
        retirement_age = 65
        years_to_retirement = retirement_age - age
        annual_retirement_need = income * 0.8  # 80% of current income
        total_retirement_need = annual_retirement_need * 25  # 25x rule
        
        return f"""Retirement planning for a {age}-year-old earning ${income:,}:

**Your Retirement Numbers:**
- Years to retirement: {years_to_retirement}
- Annual retirement need: ${annual_retirement_need:,.0f}
- Total retirement goal: ${total_retirement_need:,.0f}

**Action Plan:**
1. **Maximize 401(k)**: Contribute up to employer match (free money!)
2. **Open IRA**: $6,500/year limit (2023)
3. **Roth vs Traditional**: Roth if you expect higher taxes in retirement
4. **Target Date Funds**: Simple, diversified approach
5. **Regular Rebalancing**: Adjust as you age

**Monthly Savings Needed:**
- For 10% return: ${(total_retirement_need * 0.1 / 12):,.0f}/month
- For 7% return: ${(total_retirement_need * 0.07 / 12):,.0f}/month

Start now - compound interest is your best friend! 🚀"""
    
    def handle_calculation_request(self, user_input: str) -> str:
        """Handle calculation requests"""
        if 'compound interest' in user_input.lower():
            return self.calculators.compound_interest_calculator()
        elif 'mortgage' in user_input.lower():
            return self.calculators.mortgage_calculator()
        elif 'loan' in user_input.lower():
            return self.calculators.loan_calculator()
        else:
            return "I can help with various financial calculations! Try asking about:\n- Compound interest\n- Mortgage payments\n- Loan calculations\n- Investment returns\n\nWhat would you like to calculate?"
    
    def show_budget_dashboard(self):
        """Display budget tracking dashboard"""
        st.header("📊 Budget Dashboard")
        
        if not st.session_state.budget_data:
            st.info("No budget data yet. Start by adding some expenses in the chat!")
            return
        
        # Convert to DataFrame for visualization
        df = pd.DataFrame(st.session_state.budget_data)
        
        # Monthly spending by category
        monthly_spending = df.groupby('category')['amount'].sum().reset_index()
        
        col1, col2 = st.columns(2)
        
        with col1:
            # Pie chart of spending
            fig = px.pie(monthly_spending, values='amount', names='category', 
                        title="Monthly Spending by Category")
            st.plotly_chart(fig, use_container_width=True)
        
        with col2:
            # Bar chart of spending
            fig = px.bar(monthly_spending, x='category', y='amount',
                        title="Monthly Spending by Category")
            st.plotly_chart(fig, use_container_width=True)
        
        # Spending trends over time
        df['date'] = pd.to_datetime(df['date'])
        daily_spending = df.groupby(df['date'].dt.date)['amount'].sum().reset_index()
        
        fig = px.line(daily_spending, x='date', y='amount',
                     title="Daily Spending Trend")
        st.plotly_chart(fig, use_container_width=True)
    
    def show_investment_dashboard(self):
        """Display investment analysis dashboard"""
        st.header("💹 Investment Analysis")
        
        profile = st.session_state.user_profile
        risk_tolerance = profile['risk_tolerance']
        
        # Asset allocation recommendations
        if risk_tolerance == 'conservative':
            allocation = {'Bonds': 60, 'Stocks': 30, 'Cash': 10}
        elif risk_tolerance == 'moderate':
            allocation = {'Bonds': 40, 'Stocks': 50, 'Cash': 10}
        else:  # aggressive
            allocation = {'Bonds': 20, 'Stocks': 70, 'Cash': 10}
        
        col1, col2 = st.columns(2)
        
        with col1:
            # Asset allocation pie chart
            fig = px.pie(values=list(allocation.values()), 
                        names=list(allocation.keys()),
                        title=f"Recommended Asset Allocation ({risk_tolerance.title()})")
            st.plotly_chart(fig, use_container_width=True)
        
        with col2:
            # Investment recommendations
            st.subheader("Investment Recommendations")
            if risk_tolerance == 'conservative':
                st.write("""
                **Conservative Portfolio:**
                - 40% Total Bond Market Index
                - 20% Total Stock Market Index
                - 20% International Bonds
                - 10% High-Yield Savings
                - 10% REITs
                """)
            elif risk_tolerance == 'moderate':
                st.write("""
                **Moderate Portfolio:**
                - 50% Total Stock Market Index
                - 20% International Stock Index
                - 20% Total Bond Market Index
                - 10% High-Yield Savings
                """)
            else:
                st.write("""
                **Aggressive Portfolio:**
                - 60% Total Stock Market Index
                - 20% International Stock Index
                - 10% Small-Cap Stock Index
                - 5% Emerging Markets
                - 5% High-Yield Savings
                """)
    
    def show_calculators(self):
        """Display financial calculators"""
        st.header("🧮 Financial Calculators")
        
        tab1, tab2, tab3 = st.tabs(["Compound Interest", "Mortgage", "Loan Payment"])
        
        with tab1:
            self.calculators.compound_interest_calculator()
        
        with tab2:
            self.calculators.mortgage_calculator()
        
        with tab3:
            self.calculators.loan_calculator()
    
    def show_savings_progress(self):
        """Display savings progress tracking"""
        st.header("📈 Savings Progress")
        
        profile = st.session_state.user_profile
        current_savings = profile.get('current_savings', 0)
        goal = profile['savings_goal']
        
        # Progress bar
        progress = min(current_savings / goal, 1.0)
        st.progress(progress)
        st.write(f"Progress: ${current_savings:,} / ${goal:,} ({(progress*100):.1f}%)")
        
        # Savings projection
        monthly_income = profile['income'] / 12
        monthly_savings = monthly_income * 0.2  # 20% savings rate
        
        months_to_goal = (goal - current_savings) / monthly_savings if monthly_savings > 0 else float('inf')
        
        st.metric("Months to Goal", f"{months_to_goal:.1f}")
        st.metric("Monthly Savings Target", f"${monthly_savings:,.0f}")
    
    def run(self):
        """Main application runner"""
        self.initialize_session_state()
        self.display_header()
        
        col1, col2 = st.columns([3, 1])
        
        with col1:
            self.display_chat_interface()
        
        with col2:
            self.display_sidebar()

# Run the application
if __name__ == "__main__":
    chatbot = FinanceChatbot()
    chatbot.run()
