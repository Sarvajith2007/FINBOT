"""
Investment Advisor - Provides investment advice and portfolio recommendations
"""

import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime, timedelta
import json

class InvestmentAdvisor:
    def __init__(self):
        self.risk_profiles = {
            'conservative': {
                'stocks': 30,
                'bonds': 60,
                'cash': 10,
                'description': 'Low risk, stable returns, capital preservation'
            },
            'moderate': {
                'stocks': 50,
                'bonds': 40,
                'cash': 10,
                'description': 'Balanced risk and return, steady growth'
            },
            'aggressive': {
                'stocks': 70,
                'bonds': 20,
                'cash': 10,
                'description': 'Higher risk, potential for higher returns'
            }
        }
        
        self.asset_classes = {
            'stocks': {
                'domestic_large_cap': 'Large-cap US stocks (S&P 500)',
                'domestic_small_cap': 'Small-cap US stocks',
                'international_developed': 'International developed markets',
                'emerging_markets': 'Emerging markets',
                'reits': 'Real Estate Investment Trusts'
            },
            'bonds': {
                'treasury': 'US Treasury bonds',
                'corporate': 'Corporate bonds',
                'municipal': 'Municipal bonds',
                'international_bonds': 'International bonds'
            },
            'cash': {
                'savings': 'High-yield savings account',
                'money_market': 'Money market account',
                'cds': 'Certificates of Deposit'
            }
        }
    
    def get_investment_advice(self, user_input: str, user_profile: dict) -> str:
        """Provide investment advice based on user input and profile"""
        user_input_lower = user_input.lower()
        
        if 'portfolio' in user_input_lower or 'asset allocation' in user_input_lower:
            return self._get_portfolio_recommendation(user_profile)
        elif 'start investing' in user_input_lower or 'begin investing' in user_input_lower:
            return self._get_start_investing_guide(user_profile)
        elif 'risk' in user_input_lower or 'risk tolerance' in user_input_lower:
            return self._assess_risk_tolerance(user_profile)
        elif 'retirement' in user_input_lower and 'invest' in user_input_lower:
            return self._get_retirement_investment_advice(user_profile)
        elif 'diversify' in user_input_lower or 'diversification' in user_input_lower:
            return self._get_diversification_advice()
        elif 'rebalance' in user_input_lower:
            return self._get_rebalancing_advice()
        else:
            return self._get_general_investment_advice(user_profile)
    
    def _get_portfolio_recommendation(self, user_profile: dict) -> str:
        """Get personalized portfolio recommendation"""
        risk_tolerance = user_profile.get('risk_tolerance', 'moderate')
        age = user_profile.get('age', 30)
        income = user_profile.get('income', 50000)
        
        # Age-based adjustment
        if age < 30:
            stock_adjustment = 10
        elif age < 50:
            stock_adjustment = 0
        else:
            stock_adjustment = -10
        
        base_allocation = self.risk_profiles[risk_tolerance].copy()
        base_allocation['stocks'] = max(20, min(80, base_allocation['stocks'] + stock_adjustment))
        base_allocation['bonds'] = 100 - base_allocation['stocks'] - base_allocation['cash']
        
        recommendation = f"""**📊 Your Personalized Portfolio Recommendation**

**Risk Profile:** {risk_tolerance.title()}
**Age:** {age} years old
**Annual Income:** ${income:,}

**🎯 Recommended Asset Allocation:**
- **Stocks:** {base_allocation['stocks']}%
- **Bonds:** {base_allocation['bonds']}%
- **Cash:** {base_allocation['cash']}%

**📈 Stock Allocation Breakdown:**
- **US Large-Cap (S&P 500):** {base_allocation['stocks'] * 0.6:.0f}%
- **US Small-Cap:** {base_allocation['stocks'] * 0.15:.0f}%
- **International Developed:** {base_allocation['stocks'] * 0.2:.0f}%
- **Emerging Markets:** {base_allocation['stocks'] * 0.05:.0f}%

**🏦 Bond Allocation Breakdown:**
- **US Treasury Bonds:** {base_allocation['bonds'] * 0.4:.0f}%
- **Corporate Bonds:** {base_allocation['bonds'] * 0.4:.0f}%
- **International Bonds:** {base_allocation['bonds'] * 0.2:.0f}%

**💰 Cash Allocation:**
- **High-Yield Savings:** {base_allocation['cash'] * 0.7:.0f}%
- **Money Market:** {base_allocation['cash'] * 0.3:.0f}%

**🎯 Investment Vehicles:**
1. **401(k) with employer match** - Max this out first!
2. **Roth IRA** - $6,500/year (2023 limit)
3. **Taxable brokerage account** - For additional investing
4. **HSA** - If you have a high-deductible health plan

**📊 Expected Returns (Historical):**
- Stocks: 7-10% annually
- Bonds: 3-5% annually
- Cash: 1-3% annually
- **Portfolio Expected Return:** {self._calculate_expected_return(base_allocation):.1f}%

**⚠️ Important Notes:**
- Past performance doesn't guarantee future results
- Rebalance annually or when allocations drift 5%+
- Consider your time horizon and risk tolerance
- Start with index funds for low costs and diversification

Would you like me to help you implement this portfolio or adjust it based on your preferences?"""
        
        return recommendation
    
    def _calculate_expected_return(self, allocation: dict) -> float:
        """Calculate expected portfolio return"""
        stock_return = 8.5  # Historical average
        bond_return = 4.0   # Historical average
        cash_return = 2.0   # Current high-yield savings
        
        return (allocation['stocks'] * stock_return + 
                allocation['bonds'] * bond_return + 
                allocation['cash'] * cash_return) / 100
    
    def _get_start_investing_guide(self, user_profile: dict) -> str:
        """Get guide for starting to invest"""
        age = user_profile.get('age', 30)
        income = user_profile.get('income', 50000)
        
        # Calculate investment amounts
        monthly_income = income / 12
        recommended_monthly_investment = monthly_income * 0.15  # 15% of income
        
        return f"""**🚀 How to Start Investing (Age {age})**

**Step 1: Build Your Foundation**
- Emergency fund: 3-6 months of expenses (${monthly_income * 4:,.0f})
- Pay off high-interest debt (credit cards, personal loans)
- Max out employer 401(k) match (free money!)

**Step 2: Choose Your Investment Accounts**
1. **401(k)** - If your employer offers one
2. **Roth IRA** - $6,500/year limit (2023)
3. **Traditional IRA** - If you don't qualify for Roth
4. **Taxable Brokerage** - For additional investing

**Step 3: Start Simple**
- **Target-Date Funds** - Pick the year closest to your retirement
- **Index Funds** - S&P 500, Total Stock Market
- **Robo-Advisors** - Betterment, Wealthfront, Vanguard Digital

**Step 4: Determine How Much to Invest**
- **Minimum:** $50-100/month to start
- **Recommended:** 15% of income (${recommended_monthly_investment:,.0f}/month)
- **Maximum:** Up to contribution limits

**Step 5: Automate Everything**
- Set up automatic transfers
- Dollar-cost averaging (invest same amount regularly)
- Don't try to time the market

**📊 Investment Priority Order:**
1. 401(k) up to employer match
2. Roth IRA up to limit
3. 401(k) up to annual limit
4. Taxable brokerage account

**🎯 First Investment Recommendations:**
- **VTSAX** (Vanguard Total Stock Market) - 60%
- **VTIAX** (Vanguard Total International) - 20%
- **VBTLX** (Vanguard Total Bond Market) - 20%

**💡 Pro Tips:**
- Start with $100/month minimum
- Increase contributions with raises
- Don't check your balance daily
- Stay invested during market downturns
- Rebalance annually

**📈 The Power of Starting Early:**
- At age 25: $100/month = $1.2M by age 65 (7% return)
- At age 35: $200/month = $1.1M by age 65 (7% return)
- At age 45: $500/month = $1.0M by age 65 (7% return)

Ready to start? I can help you set up your first investment account!"""
    
    def _assess_risk_tolerance(self, user_profile: dict) -> str:
        """Assess user's risk tolerance"""
        age = user_profile.get('age', 30)
        risk_tolerance = user_profile.get('risk_tolerance', 'moderate')
        
        return f"""**🎯 Risk Tolerance Assessment**

**Your Current Profile:**
- Age: {age}
- Risk Tolerance: {risk_tolerance.title()}
- Time Horizon: {65 - age} years to retirement

**Risk Tolerance Levels:**

**🛡️ Conservative (Low Risk)**
- Stocks: 20-40%
- Bonds: 50-70%
- Cash: 10-20%
- Best for: Near retirement, low risk tolerance
- Expected volatility: Low
- Expected return: 4-6%

**⚖️ Moderate (Balanced)**
- Stocks: 40-60%
- Bonds: 30-50%
- Cash: 10-20%
- Best for: Most investors, balanced approach
- Expected volatility: Medium
- Expected return: 6-8%

**🚀 Aggressive (High Risk)**
- Stocks: 60-80%
- Bonds: 10-30%
- Cash: 10-20%
- Best for: Young investors, high risk tolerance
- Expected volatility: High
- Expected return: 8-10%

**📊 Risk Factors to Consider:**
1. **Time Horizon** - Longer = can take more risk
2. **Financial Stability** - Stable income = more risk tolerance
3. **Investment Knowledge** - More knowledge = potentially more risk
4. **Emotional Tolerance** - Can you handle market swings?
5. **Financial Goals** - Aggressive goals may require more risk

**🎯 Your Recommended Allocation:**
Based on your age of {age}, I recommend a **{risk_tolerance}** approach with:
- **Stocks:** {self.risk_profiles[risk_tolerance]['stocks']}%
- **Bonds:** {self.risk_profiles[risk_tolerance]['bonds']}%
- **Cash:** {self.risk_profiles[risk_tolerance]['cash']}%

**⚠️ Remember:**
- Risk tolerance can change over time
- Review annually or after major life events
- Don't take more risk than you can handle
- Diversification reduces risk

Would you like to adjust your risk tolerance or learn more about any specific risk level?"""
    
    def _get_retirement_investment_advice(self, user_profile: dict) -> str:
        """Get retirement-specific investment advice"""
        age = user_profile.get('age', 30)
        income = user_profile.get('income', 50000)
        years_to_retirement = 65 - age
        
        # Calculate retirement needs
        annual_retirement_need = income * 0.8  # 80% of current income
        total_retirement_need = annual_retirement_need * 25  # 25x rule
        
        # Calculate required monthly savings
        monthly_income = income / 12
        recommended_monthly_savings = monthly_income * 0.15  # 15% of income
        
        return f"""**🏖️ Retirement Investment Strategy (Age {age})**

**Your Retirement Numbers:**
- Years to retirement: {years_to_retirement}
- Current annual income: ${income:,}
- Annual retirement need: ${annual_retirement_need:,.0f}
- Total retirement goal: ${total_retirement_need:,.0f}

**💰 Required Monthly Savings:**
- **Minimum:** ${recommended_monthly_savings:,.0f} (15% of income)
- **Target:** ${monthly_income * 0.2:,.0f} (20% of income)
- **Maximum:** ${monthly_income * 0.25:,.0f} (25% of income)

**🎯 Retirement Account Priority:**
1. **401(k) with employer match** - Free money!
2. **Roth IRA** - $6,500/year (2023)
3. **401(k) additional** - Up to $22,500/year
4. **HSA** - If you have HDHP
5. **Taxable brokerage** - For additional savings

**📊 Age-Based Asset Allocation:**
- **Current (Age {age}):** {max(20, 100 - age)}% stocks, {min(80, age)}% bonds
- **Age 40:** 70% stocks, 30% bonds
- **Age 50:** 60% stocks, 40% bonds
- **Age 60:** 50% stocks, 50% bonds
- **Age 65+:** 40% stocks, 60% bonds

**🚀 Investment Recommendations:**

**For 401(k):**
- Target-date fund closest to your retirement year
- Or: 60% Total Stock Market, 40% Total Bond Market

**For Roth IRA:**
- VTSAX (Total Stock Market) - 70%
- VTIAX (Total International) - 20%
- VBTLX (Total Bond Market) - 10%

**For Taxable Account:**
- VTSAX (Total Stock Market) - 60%
- VTIAX (Total International) - 20%
- VTEB (Tax-Exempt Bonds) - 20%

**📈 Expected Growth:**
- With 7% annual return: ${recommended_monthly_savings * 12 * years_to_retirement * 1.07 ** years_to_retirement:,.0f}
- With 10% annual return: ${recommended_monthly_savings * 12 * years_to_retirement * 1.10 ** years_to_retirement:,.0f}

**💡 Pro Tips:**
- Start now - compound interest is powerful
- Increase contributions with raises
- Don't touch retirement funds early
- Consider Roth vs Traditional carefully
- Rebalance annually
- Review beneficiary designations

**⚠️ Common Mistakes to Avoid:**
- Not taking employer match
- Taking loans from 401(k)
- Cashing out when changing jobs
- Not diversifying investments
- Trying to time the market

Ready to start your retirement investing journey?"""
    
    def _get_diversification_advice(self) -> str:
        """Get diversification advice"""
        return """**🌍 Diversification: Don't Put All Your Eggs in One Basket**

**What is Diversification?**
Spreading your investments across different asset classes, sectors, and geographic regions to reduce risk.

**📊 Types of Diversification:**

**1. Asset Class Diversification:**
- **Stocks** - Growth potential, higher risk
- **Bonds** - Income generation, lower risk
- **Cash** - Liquidity, lowest risk
- **Real Estate** - Inflation hedge, moderate risk
- **Commodities** - Inflation protection, high risk

**2. Geographic Diversification:**
- **Domestic (US)** - 60-70% of stock allocation
- **International Developed** - 20-30% of stock allocation
- **Emerging Markets** - 5-10% of stock allocation

**3. Sector Diversification:**
- **Technology** - Growth potential
- **Healthcare** - Defensive, stable
- **Financials** - Interest rate sensitive
- **Consumer Staples** - Defensive, stable
- **Energy** - Cyclical, commodity-based
- **Utilities** - Defensive, dividend-focused

**4. Company Size Diversification:**
- **Large-Cap** - Established, stable companies
- **Mid-Cap** - Growing companies
- **Small-Cap** - Higher growth potential, higher risk

**🎯 Diversification Benefits:**
- Reduces overall portfolio risk
- Smooths out returns over time
- Protects against single investment failures
- Captures growth in different areas
- Reduces emotional investing

**📈 How to Diversify:**

**Simple Approach:**
- **Total Stock Market Index Fund** - 60%
- **Total International Index Fund** - 20%
- **Total Bond Market Index Fund** - 20%

**Advanced Approach:**
- **US Large-Cap** - 30%
- **US Small-Cap** - 10%
- **International Developed** - 15%
- **Emerging Markets** - 5%
- **US Bonds** - 25%
- **International Bonds** - 10%
- **REITs** - 5%

**⚠️ Common Diversification Mistakes:**
- Over-diversifying (too many funds)
- Not rebalancing regularly
- Chasing performance
- Ignoring correlation between investments
- Not considering your risk tolerance

**🔄 Rebalancing:**
- Review quarterly or annually
- Rebalance when allocations drift 5%+
- Sell high, buy low
- Maintain your target allocation

**💡 Pro Tips:**
- Start with index funds for instant diversification
- Use target-date funds for simplicity
- Consider your time horizon
- Don't overthink it - simple is often better
- Stay disciplined with rebalancing

Remember: Diversification doesn't guarantee profits or protect against losses, but it's a fundamental principle of sound investing!"""
    
    def _get_rebalancing_advice(self) -> str:
        """Get portfolio rebalancing advice"""
        return """**🔄 Portfolio Rebalancing: Keeping Your Investments in Balance**

**What is Rebalancing?**
Adjusting your portfolio back to your target asset allocation by buying and selling investments.

**🎯 Why Rebalance?**
- Maintains your desired risk level
- Forces you to sell high and buy low
- Prevents drift from your investment plan
- Reduces overall portfolio risk
- Keeps you disciplined

**⏰ When to Rebalance:**

**1. Time-Based (Recommended):**
- **Quarterly** - For active investors
- **Annually** - For most investors
- **Semi-annually** - For hands-off investors

**2. Threshold-Based:**
- When any allocation drifts 5% from target
- Example: Target 60% stocks, current 65% stocks
- More responsive to market changes

**3. Hybrid Approach:**
- Check quarterly, rebalance if 5% drift
- Annual rebalancing regardless of drift
- Best of both worlds

**📊 Rebalancing Example:**
**Target Allocation:**
- Stocks: 60%
- Bonds: 30%
- Cash: 10%

**Current Allocation (after market gains):**
- Stocks: 65% (+5%)
- Bonds: 28% (-2%)
- Cash: 7% (-3%)

**Rebalancing Action:**
- Sell 5% of stocks
- Buy 2% more bonds
- Buy 3% more cash

**🛠️ How to Rebalance:**

**Method 1: Sell and Buy**
- Sell overweighted assets
- Buy underweighted assets
- Most precise method

**Method 2: New Money**
- Direct new contributions to underweighted assets
- Gradually rebalances over time
- Avoids selling (and taxes)

**Method 3: Automatic Rebalancing**
- Use target-date funds
- Use robo-advisors
- Set and forget approach

**💰 Tax Considerations:**
- Rebalance in tax-advantaged accounts (401k, IRA)
- Use new money in taxable accounts
- Consider tax-loss harvesting
- Be mindful of capital gains

**⚠️ Common Rebalancing Mistakes:**
- Rebalancing too frequently
- Not rebalancing at all
- Letting emotions drive decisions
- Ignoring tax implications
- Not having a plan

**📈 Rebalancing Benefits:**
- Maintains risk level
- Improves risk-adjusted returns
- Reduces portfolio volatility
- Keeps you disciplined
- Forces contrarian behavior

**🎯 Rebalancing Checklist:**
1. Review your target allocation
2. Calculate current allocation
3. Identify drift (5%+ threshold)
4. Determine rebalancing needs
5. Execute trades (preferably in tax-advantaged accounts)
6. Update your records
7. Set next review date

**💡 Pro Tips:**
- Automate when possible
- Use new money first
- Rebalance in tax-advantaged accounts
- Don't overthink it
- Stay disciplined
- Consider your time horizon

Remember: Rebalancing is about maintaining your investment plan, not timing the market!"""
    
    def _get_general_investment_advice(self, user_profile: dict) -> str:
        """Get general investment advice"""
        age = user_profile.get('age', 30)
        income = user_profile.get('income', 50000)
        
        return f"""**💼 General Investment Advice for Your Situation**

**Your Profile:**
- Age: {age}
- Annual Income: ${income:,}
- Time Horizon: {65 - age} years to retirement

**🎯 Investment Principles:**

**1. Start Early**
- Time is your biggest advantage
- Compound interest is powerful
- Even small amounts add up over time

**2. Stay Invested**
- Don't try to time the market
- Market timing rarely works
- Time in market > timing the market

**3. Keep Costs Low**
- Choose low-cost index funds
- Avoid high-fee mutual funds
- Consider ETFs for low costs

**4. Diversify**
- Don't put all eggs in one basket
- Spread across asset classes
- Include international investments

**5. Stay Disciplined**
- Stick to your plan
- Don't let emotions drive decisions
- Rebalance regularly

**💰 How Much to Invest:**
- **Minimum:** 10% of income (${income * 0.1 / 12:,.0f}/month)
- **Recommended:** 15% of income (${income * 0.15 / 12:,.0f}/month)
- **Maximum:** Up to contribution limits

**📊 Investment Options by Risk:**

**Low Risk:**
- High-yield savings accounts
- Money market accounts
- CDs and Treasury bonds
- Target-date funds (conservative)

**Medium Risk:**
- Balanced mutual funds
- Index funds
- Target-date funds (moderate)
- REITs

**High Risk:**
- Individual stocks
- Sector funds
- International funds
- Small-cap funds

**🚀 Getting Started:**
1. **Emergency fund first** - 3-6 months expenses
2. **Pay off high-interest debt** - Credit cards, personal loans
3. **Max out employer 401(k) match** - Free money!
4. **Open Roth IRA** - Additional tax-advantaged savings
5. **Consider taxable brokerage** - For additional investing

**📈 Expected Returns (Historical):**
- Stocks: 7-10% annually
- Bonds: 3-5% annually
- Cash: 1-3% annually
- **Balanced Portfolio:** 6-8% annually

**⚠️ Common Mistakes to Avoid:**
- Not starting early enough
- Trying to time the market
- Paying high fees
- Not diversifying
- Letting emotions drive decisions
- Not taking employer match
- Cashing out during downturns

**💡 Pro Tips:**
- Automate your investments
- Increase contributions with raises
- Don't check your balance daily
- Stay invested during market downturns
- Consider your risk tolerance
- Review and rebalance annually

**🎯 Next Steps:**
1. Determine your risk tolerance
2. Set up automatic contributions
3. Choose low-cost index funds
4. Start with target-date funds if unsure
5. Increase contributions over time

Ready to start investing? I can help you create a personalized investment plan!"""

