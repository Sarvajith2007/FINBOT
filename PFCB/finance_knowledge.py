"""
Finance Knowledge Base - Contains general financial advice and responses
"""

class FinanceKnowledge:
    def __init__(self):
        self.general_responses = {
            "hello": "Hello! I'm FINBOT, your personal finance advisor. I can help you with budgeting, investing, saving, debt management, and retirement planning. What would you like to know?",
            "help": """I can help you with:
            
**💰 Budgeting & Expenses**
- Create and track budgets
- Categorize expenses
- Find ways to save money

**📈 Investing**
- Portfolio recommendations
- Asset allocation advice
- Risk assessment

**💵 Saving Strategies**
- Emergency fund planning
- Goal-based saving
- Compound interest calculations

**💳 Debt Management**
- Payoff strategies
- Debt consolidation options
- Credit improvement tips

**🏖️ Retirement Planning**
- 401(k) and IRA guidance
- Retirement goal setting
- Social Security optimization

**🧮 Financial Calculators**
- Loan payments
- Mortgage calculations
- Investment returns

Just ask me anything about personal finance!""",
            
            "budget": """Here's how to create an effective budget:

**1. Track Your Income**
- List all sources of monthly income
- Use net income (after taxes)

**2. List Your Expenses**
- Fixed expenses (rent, utilities, insurance)
- Variable expenses (groceries, entertainment)
- Periodic expenses (car maintenance, gifts)

**3. Use the 50/30/20 Rule**
- 50% for needs (housing, food, transportation)
- 30% for wants (entertainment, dining out)
- 20% for savings and debt repayment

**4. Choose a Budgeting Method**
- Zero-based budgeting
- Envelope method
- 50/30/20 method
- Apps like Mint, YNAB, or EveryDollar

**5. Review and Adjust Monthly**
- Track actual vs. planned spending
- Adjust categories as needed
- Celebrate wins and learn from overspending

Would you like help setting up a specific budget?""",
            
            "emergency fund": """An emergency fund is your financial safety net! Here's what you need to know:

**How Much to Save:**
- Starter emergency fund: $1,000
- Full emergency fund: 3-6 months of expenses
- For your income level: ${income * 3:,} - ${income * 6:,}

**Where to Keep It:**
- High-yield savings account
- Money market account
- Online banks often offer better rates

**What Counts as an Emergency:**
✅ Job loss
✅ Medical emergency
✅ Major car repair
✅ Home repair
❌ Vacation
❌ Holiday gifts
❌ New clothes

**How to Build It:**
1. Start with $1,000
2. Automate monthly transfers
3. Use windfalls (tax refunds, bonuses)
4. Cut unnecessary expenses

**Pro Tip:** Keep it separate from your regular checking account to avoid temptation!""",
            
            "investing": """Investing is key to building long-term wealth! Here's your investing roadmap:

**Start with the Basics:**
1. **Emergency Fund First** - 3-6 months of expenses
2. **Pay Off High-Interest Debt** - Credit cards, personal loans
3. **Maximize Employer 401(k) Match** - Free money!
4. **Open an IRA** - Additional tax-advantaged savings

**Investment Options:**
- **Index Funds** - Low-cost, diversified
- **ETFs** - Tradeable like stocks
- **Target-Date Funds** - Set it and forget it
- **Individual Stocks** - Higher risk/reward

**Asset Allocation by Age:**
- 20s-30s: 80-90% stocks, 10-20% bonds
- 40s-50s: 60-70% stocks, 30-40% bonds
- 60s+: 40-60% stocks, 40-60% bonds

**Key Principles:**
- Start early (compound interest!)
- Diversify your investments
- Keep costs low
- Stay invested long-term
- Rebalance annually

**Risk Tolerance:**
- Conservative: 40% stocks, 60% bonds
- Moderate: 60% stocks, 40% bonds
- Aggressive: 80% stocks, 20% bonds

Ready to start investing? I can help you create a personalized plan!""",
            
            "debt": """Debt can be a major obstacle to financial freedom. Here's how to tackle it:

**Debt Payoff Strategies:**

**1. Debt Snowball Method**
- Pay minimums on all debts
- Put extra money toward smallest balance
- Build momentum as debts are eliminated
- Best for motivation and quick wins

**2. Debt Avalanche Method**
- Pay minimums on all debts
- Put extra money toward highest interest rate
- Saves the most money in interest
- Best for mathematical efficiency

**3. Debt Consolidation**
- Combine multiple debts into one loan
- Often lower interest rate
- Single monthly payment
- Consider balance transfer cards

**Priority Order:**
1. High-interest credit cards (15%+)
2. Personal loans
3. Auto loans
4. Student loans
5. Mortgage

**Quick Tips:**
- Never miss minimum payments
- Consider the debt-to-income ratio
- Look into refinancing options
- Build emergency fund to avoid new debt
- Use windfalls (bonuses, tax refunds) to pay down debt

**Debt-to-Income Ratio:**
- Good: Under 20%
- Acceptable: 20-36%
- Concerning: Over 36%

Would you like me to help you create a specific debt payoff plan?""",
            
            "retirement": """Retirement planning is crucial for long-term financial security! Here's your roadmap:

**Retirement Savings Vehicles:**

**1. 401(k) - Employer Sponsored**
- Pre-tax contributions (reduces current taxes)
- Employer matching (free money!)
- 2023 limit: $22,500 + $7,500 catch-up (50+)
- Required minimum distributions at 73

**2. IRA - Individual Retirement Account**
- Traditional IRA: Pre-tax contributions
- Roth IRA: After-tax contributions, tax-free growth
- 2023 limit: $6,500 + $1,000 catch-up (50+)
- Income limits for Roth IRA

**3. HSA - Health Savings Account**
- Triple tax advantage
- Use for medical expenses
- Can invest funds
- No required distributions

**Retirement Goal Setting:**
- Rule of thumb: 10-15% of income
- 4% rule: Withdraw 4% annually in retirement
- 25x rule: Save 25x annual expenses
- Consider Social Security benefits

**Asset Allocation by Age:**
- 20s-30s: 80-90% stocks
- 40s-50s: 60-70% stocks
- 60s+: 40-60% stocks

**Key Strategies:**
- Start early (compound interest!)
- Maximize employer match
- Consider Roth vs Traditional
- Regular rebalancing
- Don't touch retirement funds early

**Social Security:**
- Full retirement age: 67 (born 1960+)
- Early retirement: 62 (reduced benefits)
- Delayed retirement: 70 (increased benefits)

Ready to calculate your retirement needs? I can help!"""
        }
    
    def get_general_advice(self, user_input: str) -> str:
        """Get general financial advice based on user input"""
        user_input_lower = user_input.lower()
        
        # Check for specific keywords and return relevant advice
        for keyword, response in self.general_responses.items():
            if keyword in user_input_lower:
                return response
        
        # Default response for unrecognized input
        return """I'd be happy to help with your financial questions! 

Here are some topics FINBOT can assist with:
- 💰 Budgeting and expense tracking
- 📈 Investment strategies and portfolio advice
- 💵 Saving strategies and emergency funds
- 💳 Debt management and payoff strategies
- 🏖️ Retirement planning and 401(k)/IRA guidance
- 🧮 Financial calculations and tools

Could you be more specific about what you'd like to know? For example:
- "How do I create a budget?"
- "What should I invest in?"
- "How much should I save for retirement?"
- "Help me pay off my debt faster"

FINBOT is here to help you achieve your financial goals! 🚀"""
