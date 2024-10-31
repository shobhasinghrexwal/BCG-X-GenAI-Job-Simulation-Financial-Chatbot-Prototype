# © Shobha Singh, 2024
# This project is licensed under the Apache License 2.0

import pandas as pd 

# Load financial data reports
final_report = pd.read_csv("final_report.csv") 
summary_report = pd.read_csv("summary_report.csv")

# Define the financial chatbot function
def financial_chatbot(company_input, fiscal_year, user_query):
    try:
        if user_query == "What is the total revenue?":
            revenue = final_report[(final_report['Year'] == fiscal_year) & (final_report['Company'] == company_input)]['Total Revenue'].values[0]
            return f"The Total Revenue for {company_input} in fiscal year {fiscal_year} is ${revenue:,.2f}."
        
        elif user_query == "What is the Net Income?":
            net_income = final_report[(final_report['Year'] == fiscal_year) & (final_report['Company'] == company_input)]['Net Income'].values[0]
            return f"The Net Income for {company_input} in fiscal year {fiscal_year} is ${net_income:,.2f}."
        
        elif user_query == "What is the sum of total assets?":
            total_assets = final_report[(final_report['Year'] == fiscal_year) & (final_report['Company'] == company_input)]['Total Assets'].values[0]
            return f"The sum of Total Assets for {company_input} in fiscal year {fiscal_year} is ${total_assets:,.2f}."
        
        elif user_query == "What is the sum of total liabilities?":
            total_liabilities = final_report[(final_report['Year'] == fiscal_year) & (final_report['Company'] == company_input)]['Total Liabilities'].values[0]
            return f"The sum of Total Liabilities for {company_input} in fiscal year {fiscal_year} is ${total_liabilities:,.2f}."
        
        elif user_query == "What is cash flow from operating activities?":
            cash_ops = final_report[(final_report['Year'] == fiscal_year) & (final_report['Company'] == company_input)]['Cash Flow from Operating Activities'].values[0]
            return f"The Cash Flow from Operating Activities for {company_input} in fiscal year {fiscal_year} is ${cash_ops:,.2f}."
        
        elif user_query == "What is the revenue growth(%) ?":
            revenue_growth = final_report[(final_report['Year'] == fiscal_year) & (final_report['Company'] == company_input)]['Revenue Growth (%)'].values[0]
            return f"The Revenue Growth(%) for {company_input} in fiscal year {fiscal_year} is {revenue_growth:.2f} %."
        
        elif user_query == "What is the net income growth(%) ?":
            net_income_growth = final_report[(final_report['Year'] == fiscal_year) & (final_report['Company'] == company_input)]['Net Income Growth (%)'].values[0]
            return f"The Net Income Growth(%) for {company_input} in fiscal year {fiscal_year} is {net_income_growth:.2f} %."
        
        elif user_query == "What is the year by year average revenue growth rate(%)?":
            year_avg_revenue_growth = summary_report[summary_report['Company'] == company_input]['Revenue Growth (%)'].values[0]
            return f"The Year By Year Average Revenue Growth Rate(%) for {company_input} from 2021 to 2023 is {year_avg_revenue_growth:.2f} %."
        
        else:
            return "Sorry, I can only provide information on specific financial queries. Please ask something else!"

    except IndexError:
        return "Data not available for the given query. Please check the company name and fiscal year."

# Main loop to interact with the chatbot
print("Welcome to BCG X's FinBot by Shobha!")
print("I'm here to help you with financial data queries related to Microsoft, Tesla, and Apple.")
print("Please note that I can provide data for the fiscal years 2021, 2022, and 2023 only.")

while True:
    hello = input("\nType 'hello' to begin your query session or 'exit' to leave: ").strip().lower()
    
    if hello == "exit":
        print("Thank you for using BCG X's FinBot by Shobha! Have a great day!")
        break
    elif hello == "hello":
        company_input = input("\nPlease enter the company name (Microsoft, Tesla, Apple): ").capitalize()
        if company_input not in ['Apple', 'Microsoft', 'Tesla']:
            print("Oops! That's not a valid company name. Please restart the chatbot session.")
            continue
        
        try:
            fiscal_year = int(input("Please enter the fiscal year (2021, 2022, 2023): "))
            if fiscal_year not in [2021, 2022, 2023]:
                print("Invalid year! Please enter a valid fiscal year.")
                continue
        except ValueError:
            print("Oops! That wasn't a number. Please restart the chatbot session.")
            continue
        
        user_query = input("What would you like to know? ").strip()
        response = financial_chatbot(company_input, fiscal_year, user_query)
        print(response)
    else:
        print("Hmm, that wasn't a valid input. Please type 'hello' or 'exit'.")

# Branding at the bottom
print("\nBCG X's FinBot by Shobha")
