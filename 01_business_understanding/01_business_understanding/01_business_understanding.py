# BUSINESS SCIENCE UNIVERSITY
# COURSE: DS4B 201-P PYTHON MACHINE LEARNING
# MODULE 1: BUSINESS UNDERSTANDING
# ----

# LIBRARIES ----
import pandas as pd
import numpy as np
import janitor as jn
import plotly.express as px


# BUSINESS SCIENCE PROBLEM FRAMEWORK ----

# View Business as a Machine ----


# Business Units: 
#   - Marketing Department
#   - Responsible for sales emails  
# Project Objectives:
#   - Target Subscribers Likely To Purchase
#   - Nurture Subscribers to take actions that are known to increase probability of purchase
# Define Machine:
#   - Marketing sends out email blasts to everyone
#   - Generates Sales
#   - Also ticks some members off
#   - Members unsubscribe, this reduces email growth and profitability
# Collect Outcomes:
#   - Revenue has slowed, Email growth has slowed


# Understand the Drivers ----

#   - Key Insights:
#     - Company has Large Email List: 100,000 
#     - Email list is growing at 6,000/month less 2500 unsub for total of 3500
#     - High unsubscribe rates: 500 people per sales email
#   - Revenue:
#     - Company sales cycle is generating about $250,000 per month
#     - Average Customer Lifetime Value: Estimate $2000/customer
#   - Costs: 
#     - Marketing sends 5 Sales Emails Per Month
#     - 5% of lost customers likely to convert if nutured



# COLLECT OUTCOMES ----

email_list_size_1 = 100000

unsub_count_per_sales_email_1 = 500

unsub_rate_1 = unsub_count_per_sales_email_1 / email_list_size_1

unsub_rate_1

sales_emails_per_month_1 = 5

conversion_rate_1 = 0.05

lost_customer_1 = email_list_size_1 * unsub_rate_1 * sales_emails_per_month_1 * conversion_rate_1

average_customer_value = 2000

lost_revenue_per_month_value_1 = lost_customer_1 * average_customer_value

# No-growth scenario $3M cost

cost_no_growth_1 = lost_revenue_per_month_value_1 * 12
cost_no_growth_1

# 2.5% growth scenario: 
#   amount = principle * ((1+rate)**time)



# If reduce unsubscribe rate by 30%



# COST CALCULATION FUNCTIONS ----

# Function: Calculate Monthly Unsubscriber Cost Table ----


# Function: Sumarize Cost ----



# ARE OBJECTIVES BEING MET?
# - We can see a large cost due to unsubscription
# - However, some attributes may vary causing costs to change


# SYNTHESIZE OUTCOMES (COST SIMULATION) ----
# - Make a cartesian product of inputs that can vary
# - Use list comprehension to perform simulation
# - Visualize results

# Cartesian Product (Expand Grid)


# Function



# VISUALIZE COSTS



# Function: Plot Simulated Unsubscriber Costs





# ARE OBJECTIVES BEING MET?
# - Even with simulation, we see high costs
# - What if we could reduce by 30% through better targeting?



# - What if we could reduce unsubscribe rate from 0.5% to 0.17% (marketing average)?
# - Source: https://www.campaignmonitor.com/resources/knowledge-base/what-is-a-good-unsubscribe-rate/



# HYPOTHESIZE DRIVERS

# - What causes a customer to convert of drop off?
# - If we know what makes them likely to convert, we can target the ones that are unlikely to nurture them (instead of sending sales emails)
# - Meet with Marketing Team
# - Notice increases in sales after webinars (called Learning Labs)
# - Next: Begin Data Collection and Understanding



