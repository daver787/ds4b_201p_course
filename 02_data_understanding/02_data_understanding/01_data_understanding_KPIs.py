# BUSINESS SCIENCE UNIVERSITY
# COURSE: DS4B 201-P PYTHON MACHINE LEARNING
# MODULE 2: DATA UNDERSTANDING
# PART 1: DATA UNDERSTANDING & KPIS
# ----

# GOAL: ----
# - Saw high costs, feedback showed problems
# - Now need to work with departments to collect data and develop project KPIs

# LIBRARIES ----

# Data Analysis:
import pandas as pd
import numpy as np
import plotly.express as px

# New Libraries:
import sweetviz as sv
import sqlalchemy as sql

# Email Lead Scoring: 
import email_lead_scoring as els


# ?els.cost_calc_monthly_unsub_cost_table

els.cost_simulate_unsub_costs(
    email_list_monthly_growth_rate = np.linspace(0, 0.03, 5),
    customer_conversion_rate       = np.linspace(0.4, 0.6, 3),
    sales_emails_per_month         = 5,
    unsub_rate_per_sales_email     = 0.001,
    email_list_size                = 1e5
) \
    .pipe(func=els.cost_plot_simulated_unsub_costs)


# 1.0 CONNECTING TO SQLITE DATABASE ----

url = "sqlite:///00_database/crm_database.sqlite"

engine = sql.create_engine(url)
engine

conn = engine.connect()
conn

inspect = sql.inspect(engine)

table_names = inspect.get_table_names()

# 2.0 COLLECT DATA ----

# Products ----

products_df = pd.read_sql(
    sql = "SELECT * FROM Products",
    con = conn
)

products_df.head()

products_df.shape

products_df.info()

products_df['product_id'] = products_df['product_id'].astype('int')

products_df.info()

products_df.head()
# Subscribers ----

table_names[1]

subscribers_df = pd.read_sql(
    sql = f"SELECT * FROM {table_names[1]}",
    con =conn
)

subscribers_df.info()

subscribers_df.head()

subscribers_df['mailchimp_id'] = subscribers_df['mailchimp_id'].astype('int')

subscribers_df['member_rating'] = subscribers_df['member_rating'].astype('int')

subscribers_df['optin_time'] = subscribers_df['optin_time'].astype('datetime64')


# Tags ----



# Transactions ----



# Website ----



# Close Connection ----
# - Note: a better practice is to use `with`



# 3.0 COMBINE & ORGANIZE DATA ----
# - Problem is related to probability of purchase from email list
# - Need to understand what increases probability of purchase
# - Learning Labs could be a key event
# - Website data would be interesting but can't link it to email
# - Products really aren't important to our initial question - just want to know if they made a purchase or not and identify which are likely

# Make Target Feature



# Who is purchasing?



# By Geographic Regions (Countries)

    

# - Top 80% countries 



# - High Conversion Countries (>8% conversion)



# By Tags (Events)



# 4.0 SWEETVIZ EDA REPORT




# 5.0 DEVELOP KPI'S ----
# - Reduce unnecessary sales emails by 30% while maintaing 99% of sales
# - Segment list - apply sales (hot leads), nuture (cold leads)

# EVALUATE PERFORMANCE -----


    

# WHAT COULD BE MISSED?
# - More information on which tags are most important






