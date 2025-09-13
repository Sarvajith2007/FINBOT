"""
Budget Tracker - Handles budget analysis and expense tracking
"""

import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime, timedelta
import json

class BudgetTracker:
    def __init__(self):
        self.expense_categories = [
            "Housing", "Food", "Transportation", "Healthcare", 
            "Entertainment", "Shopping", "Utilities", "Insurance",
            "Debt Payments", "Savings", "Other"
        ]
    
    def analyze_budget_question(self, user_input: str, user_profile: dict) -> str:
        """Analyze budget-related questions and provide advice"""
        user_input_lower = user_input.lower()
        
        if 'create budget' in user_input_lower or 'make budget' in user_input_lower:
            return self._create_budget_guide(user_profile)
        elif 'track expense' in user_input_lower or 'add expense' in user_input_lower:
            return self._expense_tracking_guide()
        elif 'budget breakdown' in user_input_lower or 'spending analysis' in user_input_lower:
            return self._analyze_current_budget()
        elif 'save money' in user_input_lower or 'cut expenses' in user_input_lower:
            return self._money_saving_tips()
        else:
            return self._general_budget_advice(user_profile)
    
    def _create_budget_guide(self, user_profile: dict) -> str:
        """Create a personalized budget guide"""
        income = user_profile['income']
        monthly_income = income / 12
        
        # 50/30/20 rule calculations
        needs = monthly_income * 0.5
        wants = monthly_income * 0.3
        savings = monthly_income * 0.2
        
        return f"""Here's your personalized budget based on your ${income:,} annual income:

**📊 50/30/20 Budget Breakdown:**
- **Monthly Income:** ${monthly_income:,.0f}
- **Needs (50%):** ${needs:,.0f}
- **Wants (30%):** ${wants:,.0f}
- **Savings (20%):** ${savings:,.0f}

**🏠 Needs (${needs:,.0f}/month):**
- Housing: ${needs * 0.4:,.0f} (40% of needs)
- Food: ${needs * 0.2:,.0f} (20% of needs)
- Transportation: ${needs * 0.15:,.0f} (15% of needs)
- Utilities: ${needs * 0.1:,.0f} (10% of needs)
- Insurance: ${needs * 0.1:,.0f} (10% of needs)
- Other needs: ${needs * 0.05:,.0f} (5% of needs)

**🎯 Wants (${wants:,.0f}/month):**
- Entertainment: ${wants * 0.3:,.0f}
- Dining out: ${wants * 0.25:,.0f}
- Shopping: ${wants * 0.2:,.0f}
- Hobbies: ${wants * 0.15:,.0f}
- Travel: ${wants * 0.1:,.0f}

**💰 Savings (${savings:,.0f}/month):**
- Emergency fund: ${savings * 0.3:,.0f}
- Retirement: ${savings * 0.4:,.0f}
- Other goals: ${savings * 0.3:,.0f}

**💡 Pro Tips:**
1. Use the envelope method for variable expenses
2. Automate your savings transfers
3. Review and adjust monthly
4. Track every expense for the first month
5. Use apps like Mint, YNAB, or EveryDollar

Would you like me to help you track specific expenses or adjust any categories?"""
    
    def _expense_tracking_guide(self) -> str:
        """Provide guidance on expense tracking"""
        return """Here's how to effectively track your expenses:

**📱 Best Tracking Methods:**
1. **Apps:** Mint, YNAB, EveryDollar, PocketGuard
2. **Spreadsheets:** Excel, Google Sheets
3. **Banking Apps:** Most banks have built-in categorization
4. **Manual:** Receipts + notebook

**📊 What to Track:**
- Every single expense (even $2 coffee!)
- Date, amount, category, description
- Payment method (cash, card, check)
- Whether it was planned or impulse

**🏷️ Categories to Use:**
- Housing (rent, mortgage, utilities)
- Food (groceries, dining out)
- Transportation (gas, public transit, car payment)
- Healthcare (insurance, medical, pharmacy)
- Entertainment (movies, games, subscriptions)
- Shopping (clothes, electronics, household)
- Debt payments (credit cards, loans)
- Savings (emergency fund, retirement)

**⏰ When to Track:**
- Daily: Log expenses as they happen
- Weekly: Review and categorize
- Monthly: Analyze patterns and adjust budget

**🎯 Pro Tips:**
- Set up automatic categorization in apps
- Use cash for discretionary spending
- Take photos of receipts
- Review spending weekly
- Set up budget alerts

Would you like me to help you add some expenses to track?"""
    
    def _analyze_current_budget(self) -> str:
        """Analyze current budget data if available"""
        if 'budget_data' not in st.session_state or not st.session_state.budget_data:
            return """I don't see any budget data yet. Let's start tracking your expenses!

**To get started:**
1. Tell me about recent expenses: "I spent $50 on groceries yesterday"
2. Use the format: "I spent $[amount] on [category] for [description]"
3. I'll help you categorize and track everything

**Example:**
- "I spent $25 on food for lunch with friends"
- "I paid $1200 for rent this month"
- "I bought gas for $45"

Once you start adding expenses, I can show you:
- Spending by category
- Monthly trends
- Budget vs actual analysis
- Money-saving opportunities

What expenses would you like to add?"""
        
        # Analyze existing budget data
        df = pd.DataFrame(st.session_state.budget_data)
        total_spent = df['amount'].sum()
        category_spending = df.groupby('category')['amount'].sum().sort_values(ascending=False)
        
        analysis = f"""**📊 Your Current Spending Analysis:**

**Total Spent:** ${total_spent:,.2f}

**Top Spending Categories:**
"""
        
        for category, amount in category_spending.head(5).items():
            percentage = (amount / total_spent) * 100
            analysis += f"- {category}: ${amount:,.2f} ({percentage:.1f}%)\n"
        
        # Spending insights
        if len(df) > 0:
            avg_daily = total_spent / 30  # Assuming monthly data
            analysis += f"\n**📈 Insights:**\n"
            analysis += f"- Average daily spending: ${avg_daily:.2f}\n"
            
            # Find highest expense
            highest_expense = df.loc[df['amount'].idxmax()]
            analysis += f"- Highest single expense: ${highest_expense['amount']:.2f} on {highest_expense['category']}\n"
            
            # Spending frequency
            analysis += f"- Total transactions: {len(df)}\n"
        
        return analysis
    
    def _money_saving_tips(self) -> str:
        """Provide money-saving tips"""
        return """Here are proven ways to save money and cut expenses:

**🏠 Housing (Biggest Impact):**
- Consider roommates or downsizing
- Negotiate rent renewal
- Shop around for better internet/cable deals
- Use energy-efficient appliances
- Seal windows and doors for better insulation

**🍕 Food (Easy Wins):**
- Meal prep on Sundays
- Buy generic brands
- Use grocery store apps for coupons
- Plan meals around sales
- Limit dining out to 2x per week
- Pack lunch for work

**🚗 Transportation:**
- Carpool or use public transit
- Combine errands into one trip
- Keep up with car maintenance
- Consider a more fuel-efficient vehicle
- Walk or bike for short trips

**💡 Utilities:**
- Use programmable thermostats
- Switch to LED light bulbs
- Unplug electronics when not in use
- Take shorter showers
- Wash clothes in cold water
- Use fans instead of AC when possible

**🛍️ Shopping:**
- Wait 24 hours before buying non-essentials
- Use the 30-day rule for big purchases
- Buy used items when possible
- Cancel unused subscriptions
- Shop with a list and stick to it
- Use cashback apps and credit cards

**📱 Subscriptions:**
- Audit all subscriptions monthly
- Share streaming services with family
- Cancel unused gym memberships
- Use free alternatives when possible

**🎯 Quick Wins:**
- Pack lunch: Save $200-400/month
- Cancel unused subscriptions: Save $50-200/month
- Use coupons: Save $100-300/month
- Buy generic: Save $50-150/month
- Cook at home: Save $300-600/month

**💪 Challenge Yourself:**
- No-spend weekends
- 30-day spending freeze on non-essentials
- $5 challenge (save every $5 bill)
- 52-week savings challenge

What area would you like to focus on first?"""
    
    def _general_budget_advice(self, user_profile: dict) -> str:
        """Provide general budget advice"""
        income = user_profile['income']
        monthly_income = income / 12
        
        return f"""Here's some general budget advice for your ${income:,} annual income:

**🎯 Budget Fundamentals:**
1. **Track everything** - You can't manage what you don't measure
2. **Pay yourself first** - Save before spending
3. **Use the 50/30/20 rule** - 50% needs, 30% wants, 20% savings
4. **Automate savings** - Set up automatic transfers
5. **Review monthly** - Adjust as needed

**📊 Your Income Breakdown:**
- Monthly income: ${monthly_income:,.0f}
- Daily income: ${monthly_income/30:,.0f}
- Hourly income: ${monthly_income/160:,.0f} (assuming 40hr/week)

**💰 Emergency Fund Target:**
- 3 months expenses: ${monthly_income * 3:,.0f}
- 6 months expenses: ${monthly_income * 6:,.0f}

**🏦 Savings Goals:**
- 20% of income: ${monthly_income * 0.2:,.0f}/month
- Annual savings target: ${monthly_income * 0.2 * 12:,.0f}

**📈 Budget Categories to Focus On:**
1. **Housing** - Keep under 30% of income (${monthly_income * 0.3:,.0f})
2. **Transportation** - Keep under 15% of income (${monthly_income * 0.15:,.0f})
3. **Food** - Keep under 15% of income (${monthly_income * 0.15:,.0f})
4. **Debt payments** - Keep under 20% of income (${monthly_income * 0.2:,.0f})

**🚀 Next Steps:**
1. Track expenses for one month
2. Categorize all spending
3. Identify areas to cut back
4. Set up automatic savings
5. Review and adjust monthly

Would you like help with any specific aspect of budgeting?"""
    
    def add_expense(self, amount: float, category: str, description: str = ""):
        """Add an expense to the budget tracker"""
        if 'budget_data' not in st.session_state:
            st.session_state.budget_data = []
        
        expense = {
            'date': datetime.now().strftime('%Y-%m-%d'),
            'amount': amount,
            'category': category,
            'description': description
        }
        
        st.session_state.budget_data.append(expense)
        return f"Added expense: ${amount:.2f} for {category}"
    
    def get_budget_summary(self) -> dict:
        """Get a summary of current budget data"""
        if 'budget_data' not in st.session_state or not st.session_state.budget_data:
            return {"total": 0, "categories": {}, "count": 0}
        
        df = pd.DataFrame(st.session_state.budget_data)
        total = df['amount'].sum()
        categories = df.groupby('category')['amount'].sum().to_dict()
        count = len(df)
        
        return {
            "total": total,
            "categories": categories,
            "count": count
        }

