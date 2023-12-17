import streamlit as st
import openai

openai.api_key = "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"

def page_personal():
    
    

    def main():
        st.title("Personalized Budgeting Plan")
        job_title = st.text_input("Enter your job title:")     

        st.subheader("Income Sources:")
        regular_salary = st.number_input("Regular Salary:")
        investment_income = st.number_input("Investment Income (dividends, interest):")
        rental_income = st.number_input("Rental Income:")
        other_income = st.number_input("Other:")

        st.subheader("Expenses:")
        rent_mortgage = st.number_input("Rent/Mortgage:")
        utilities = st.number_input("Utilities (electricity, water, gas):")
        loan_payments = st.number_input("Loan Payments (mortgage, car loans):")
        income_taxes = st.number_input("Income Taxes:")
        groceries = st.number_input("Groceries:")
        monthly_transportation = st.number_input("Monthly Transportation (fuel, public transport):")
        dining_out = st.number_input("Dining Out/Entertainment:")
        medical_expenses = st.number_input("Medical Expenses - Medicines:")
        other_expenses = st.number_input("Others:")

        st.subheader("Savings and Investments:")
        emergency_funds = st.number_input("Emergency Funds:")

        st.subheader("Debts and Liabilities:")
        credit_card_balances = st.number_input("Credit Card Balances:")
        loans = st.number_input("Loans (personal loans, student loans):")
        outstanding_debts = st.number_input("Outstanding Debts:")

        st.subheader("Financial Goals:")
        financial_goals = st.text_area("Enter your financial goals:")

        budget_period = st.selectbox("Budget Period:", ["Monthly", "Quarterly", "Annual"])
        if (st.button("Submit")):
            prompt = f"Act as a Chartered Accountant and Consider me as your client. Design a personalized budget plan based on the following inputs:\n\nJob title={job_title}\n\nIncome Sources: Regular Salary={regular_salary}, Investment Income={investment_income}, Rental Income={rental_income}, Other Income={other_income}\n\nExpenses: Rent/Mortgage={rent_mortgage}, Utilities={utilities}, Loan Payments={loan_payments}, Income Taxes={income_taxes}, Groceries={groceries}, Monthly Transportation={monthly_transportation}, Dining Out/Entertainment={dining_out}, Medical Expenses={medical_expenses}, Other Expenses={other_expenses}\n\nSavings and Investments: Emergency Funds={emergency_funds}\n\nDebts and Liabilities: Credit Card Balances={credit_card_balances}, Loans={loans}, Outstanding Debts={outstanding_debts}\n\nFinancial Goals: {financial_goals}\n\nBudget Period: {budget_period}\n**AI Instructions:**\n1. Identify areas in the budget that can be optimized for improved financial health\n 2. If applicable, provide recommendations for achieving financial goals and mitigating identified risks."
            gpt3_response = openai.Completion.create(
                engine="text-davinci-002",
                prompt=prompt,
                max_tokens=300
            )
            st.subheader("Response:")
            st.write(gpt3_response.choices[0].text)
            

    if __name__ == "__main__":
        main()


def page_family():
    def main():
        st.title("Family Budgeting Plan")

        # User inputs
        family_members = st.number_input("Number of Family Members", min_value=1, value=1, step=1)

        # Income Sources
        st.header("Income Sources")
        primary_earner = st.number_input("Primary Earner's Salary", min_value=0.0, value=0.0, step=1000.0)
        spouse_income = st.number_input("Spouse/Partner's Income", min_value=0.0, value=0.0, step=1000.0)
        investment_income = st.number_input("Investment Income", min_value=0.0, value=0.0, step=100.0)
        rental_income = st.number_input("Rental Income", min_value=0.0, value=0.0, step=100.0)
        other_income = st.number_input("Other Income", min_value=0.0, value=0.0, step=100.0)

        # Expenses
        st.header("Expenses")
        rent_mortgage = st.number_input("Rent/Mortgage", min_value=0.0, value=0.0, step=100.0)
        utilities = st.number_input("Utilities", min_value=0.0, value=0.0, step=50.0)
        loan_payments = st.number_input("Loan Payments", min_value=0.0, value=0.0, step=50.0)
        income_taxes = st.number_input("Income Taxes", min_value=0.0, value=0.0, step=50.0)
        groceries = st.number_input("Groceries", min_value=0.0, value=0.0, step=50.0)
        transportation = st.number_input("Monthly Transportation", min_value=0.0, value=0.0, step=50.0)
        childcare_education = st.number_input("Childcare/Education Expenses", min_value=0.0, value=0.0, step=50.0)
        dining_entertainment = st.number_input("Dining Out/Entertainment", min_value=0.0, value=0.0, step=50.0)
        medical_expenses = st.number_input("Medical Expenses - Medicines", min_value=0.0, value=0.0, step=50.0)
        other_expenses = st.number_input("Other Family Expenses", min_value=0.0, value=0.0, step=50.0)

        # Savings and Investments
        st.header("Savings and Investments")
        emergency_funds = st.number_input("Emergency Funds", min_value=0.0, value=0.0, step=100.0)

        # Debts and Liabilities
        st.header("Debts and Liabilities")
        credit_card_balances = st.number_input("Credit Card Balances", min_value=0.0, value=0.0, step=50.0)
        loans = st.number_input("Loans", min_value=0.0, value=0.0, step=50.0)
        outstanding_debts = st.number_input("Outstanding Debts", min_value=0.0, value=0.0, step=50.0)

        # Financial Goals
        st.header("Financial Goals")
        financial_goals = st.text_area("Enter your financial goals")

        # Budget Period
        st.header("Budget Period")
        budget_period = st.selectbox("Budget Period:", ["Monthly", "Quarterly", "Annual"])
        if (st.button("Submit")):
            prompt = f"Act as a Chartered Accountant and Consider me as your client. Design a family budget plan for my based on the following inputs:\n\nFamily Members:{family_members}\n\nIncome Sources:\n- Primary Earner's Salary: {primary_earner}\n- Spouse/Partner's Income: {spouse_income}\n- Investment Income: {investment_income}\n- Rental Income: {rental_income}\n- Other Income: {other_income}\n\nExpenses:\n- Rent/Mortgage: {rent_mortgage}\n- Utilities: {utilities}\n- Loan Payments: {loan_payments}\n- Income Taxes: {income_taxes}\n- Groceries: {groceries}\n- Monthly Transportation: ${transportation}\n- Childcare/Education Expenses: {childcare_education}\n- Dining Out/Entertainment: {dining_entertainment}\n- Medical Expenses - Medicines: {medical_expenses}\n- Other Family Expenses: {other_expenses}\n\nSavings and Investments:\n- Emergency Funds: {emergency_funds}\n\nDebts and Liabilities:\n- Credit Card Balances: {credit_card_balances}\n- Loans: {loans}\n- Outstanding Debts: {outstanding_debts}\n\nFinancial Goals:\n{financial_goals}\n\nBudget Period: {budget_period}\n**AI Instructions:**\n1. An analysis of the family's overall financial situation, including potential risks and opportunities for improvement.\n 2. If applicable, provide recommendations for achieving family financial goals and mitigating identified risks"
            gpt3_response = openai.Completion.create(
                engine="text-davinci-002",
                prompt=prompt,
                max_tokens=300
            )
            st.subheader("Response:")
            st.write(gpt3_response.choices[0].text)
            # return prompt

    if __name__ == "__main__":
        main()



# Define the app pages
pages = {
    "Personalized": page_personal,
    "Family": page_family,
}

# Sidebar with dropdown and buttons
st.sidebar.title("Budgeting")
selected_page = st.sidebar.selectbox("Select a page", list(pages.keys()))


# Display the selected page
pages[selected_page]()
