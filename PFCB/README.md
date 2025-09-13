# 💰 Personal Finance Advisor Chatbot

A comprehensive personal finance chatbot built with Streamlit that provides personalized financial advice, budget tracking, investment guidance, and financial calculations.

## 🚀 Features

### 💬 Chat Interface
- Interactive chat with a personal finance advisor
- Natural language processing for financial questions
- Contextual responses based on user profile

### 📊 Budget Management
- Personalized budget creation using 50/30/20 rule
- Expense tracking and categorization
- Spending analysis and insights
- Money-saving tips and strategies

### 💹 Investment Advice
- Portfolio recommendations based on risk tolerance
- Asset allocation guidance
- Retirement planning strategies
- Diversification and rebalancing advice

### 🧮 Financial Calculators
- Compound interest calculator
- Mortgage payment calculator
- Loan payment calculator
- Investment return projections

### 👤 User Profile
- Personalized financial advice
- Age and income-based recommendations
- Risk tolerance assessment
- Goal tracking

## 🛠️ Installation

### Prerequisites
- Python 3.8 or higher
- pip (Python package installer)

### Setup
1. **Clone or download this repository**
   ```bash
   git clone <repository-url>
   cd personal-finance-chatbot
   ```

2. **Install Python dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**
   ```bash
   streamlit run app.py
   ```

4. **Open your browser**
   - The app will automatically open at `http://localhost:8501`
   - If it doesn't open automatically, copy the URL from the terminal

## 📱 Usage

### Getting Started
1. **Update your profile** in the sidebar with your:
   - Name
   - Age
   - Annual income
   - Savings goals
   - Risk tolerance

2. **Start chatting** with the finance advisor about:
   - Budgeting and expenses
   - Investment strategies
   - Saving goals
   - Debt management
   - Retirement planning

### Quick Actions
Use the sidebar buttons for:
- **View Budget** - See spending analysis and charts
- **Investment Analysis** - Portfolio recommendations
- **Financial Calculators** - Various financial tools
- **Savings Progress** - Track your savings goals

### Example Questions
- "How do I create a budget?"
- "What should I invest in?"
- "Help me save for retirement"
- "How much should I save for an emergency fund?"
- "Calculate compound interest for $10,000 at 7% for 20 years"

## 🏗️ Project Structure

```
personal-finance-chatbot/
├── app.py                    # Main Streamlit application
├── finance_knowledge.py      # Financial advice and responses
├── financial_calculators.py  # Financial calculation tools
├── budget_tracker.py         # Budget tracking and analysis
├── investment_advisor.py     # Investment advice and portfolio management
├── requirements.txt          # Python dependencies
└── README.md                # This file
```

## 🎯 Key Features Explained

### Budget Tracking
- **50/30/20 Rule**: 50% needs, 30% wants, 20% savings
- **Expense Categorization**: Automatic categorization of expenses
- **Spending Analysis**: Visual charts and insights
- **Money-Saving Tips**: Personalized recommendations

### Investment Advice
- **Risk-Based Portfolios**: Conservative, moderate, and aggressive
- **Asset Allocation**: Stocks, bonds, and cash recommendations
- **Retirement Planning**: Age-appropriate investment strategies
- **Diversification**: Geographic and sector diversification

### Financial Calculators
- **Compound Interest**: Calculate future value of investments
- **Mortgage Payments**: Calculate monthly mortgage payments
- **Loan Payments**: General loan payment calculations
- **Investment Projections**: Visual growth charts

## 🔧 Customization

### Adding New Features
1. **New Financial Topics**: Add to `finance_knowledge.py`
2. **New Calculators**: Add to `financial_calculators.py`
3. **New Budget Features**: Add to `budget_tracker.py`
4. **New Investment Advice**: Add to `investment_advisor.py`

### Styling
- Modify the CSS in the `st.markdown()` section of `app.py`
- Update colors, fonts, and layout as needed

## 📊 Data Storage

The application uses Streamlit's session state for data storage:
- **User Profile**: Personal information and preferences
- **Budget Data**: Expense tracking and categorization
- **Investment Portfolio**: Current investment holdings
- **Chat History**: Conversation history

## ⚠️ Important Notes

### Financial Advice Disclaimer
This chatbot provides general financial education and guidance. It is not a substitute for professional financial advice. Always consult with a qualified financial advisor for personalized advice.

### Data Privacy
- All data is stored locally in your browser session
- No data is sent to external servers
- Clear your browser data to remove stored information

### Accuracy
- Financial calculations are for educational purposes
- Past performance doesn't guarantee future results
- Market conditions can change rapidly

## 🚀 Future Enhancements

- [ ] Database integration for persistent data storage
- [ ] User authentication and multiple profiles
- [ ] Real-time market data integration
- [ ] Advanced portfolio optimization
- [ ] Tax planning features
- [ ] Goal tracking and milestones
- [ ] Export functionality for reports
- [ ] Mobile app version

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## 📄 License

This project is open source and available under the MIT License.

## 🆘 Support

If you encounter any issues or have questions:
1. Check the troubleshooting section below
2. Review the code comments
3. Create an issue in the repository

## 🔧 Troubleshooting

### Common Issues

**1. Module not found error**
```bash
pip install -r requirements.txt
```

**2. Streamlit not found**
```bash
pip install streamlit
```

**3. Port already in use**
```bash
streamlit run app.py --server.port 8502
```

**4. Browser doesn't open automatically**
- Copy the URL from the terminal output
- Usually `http://localhost:8501`

### Performance Tips
- Close unused browser tabs
- Restart the application if it becomes slow
- Clear browser cache if needed

## 📞 Contact

For questions or support, please open an issue in the repository.

---

**Happy Financial Planning! 💰🚀**

