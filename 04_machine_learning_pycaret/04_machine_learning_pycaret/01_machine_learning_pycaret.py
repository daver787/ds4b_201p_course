# BUSINESS SCIENCE UNIVERSITY
# COURSE: DS4B 201-P PYTHON MACHINE LEARNING & APIS
# MODULE 4: MACHINE LEARNING | PYCARET
# ----

# Core
import os
import pandas as pd
import numpy as np
import pycaret.classification as clf

# Lead Scoring
import email_lead_scoring as els

# RECAP ----

leads_df = els.db_read_and_process_els_data() 

# 1.0 PREPROCESSING (SETUP) ---- 
# - Infers data types (requires user to say yes)
# - Returns a preprocessing pipeline

leads_df.info()

# Removing unneccesary columns

df = leads_df\
    .drop(['mailchimp_id', 'user_full_name', 'user_email', 'optin_time','email_provider'],
    axis =1)


# Numeric Features

_tag_mask = df.columns.str.match('^tag_')

numeric_features = df.columns[_tag_mask].to_list()

numeric_features.append('optin_days')

# Categorical Features

categorical_features = ['country_code']

# Ordinal Features

df['member_rating'].unique()

ordinal_features ={
    'member_rating': ['1', '2', '3', '4', '5']
}

# Classifier Setup

clf.setup(
    data                       = df,
    target                     = 'made_purchase',
    train_size                 = 0.8,
    preprocess                 = True,
    
    # Imputation
    imputation_type            = 'simple',
    
    # Categorical
    categorical_features       = categorical_features,
    handle_unknown_categorical = True,
    combine_rare_levels        = True,
    rare_level_threshold       = 0.005,
    
    # Ordinal Features
    ordinal_features           = ordinal_features,
    
    # Numeric Features
    numeric_features           = numeric_features,
    
    # K- Fold
    fold_strategy              = 'stratifiedkfold',
    fold                       = 5,
    
    # Job Experiment Logging
    n_jobs                     = -1,
    use_gpu                    = True,
    session_id                 = 123,
    log_experiment             = True,
    experiment_name            = 'email_lead_scoring_0',
    
    # Silent: Turns Off
    silent                     = False
    
)

# 2.0 GET CONFIGURATION ----
# - Understanding what Pycaret is doing underneath
# - Can extract pre/post transformed data
# - Get the Scikit Learn Pipeline


# Transformed Dataset



# Extract Scikit learn Pipeline



# Check difference in columns



# 3.0 MACHINE LEARNING (COMPARE MODELS) ----

# Available Models


# Running All Available Models



# Get the grid



# Top 3 Models



# Make predictions



# Refits on Full Dataset



# Save / load model



# 4.0 PLOTTING MODEL PERFORMANCE -----



# Get all plots 
# - Note that this can take a long time for certain plots
# - May want to just plot individual (see that next)


# - ROC Curves & PR Curves


# Confusion Matrix / Error


# Gain/Lift Plots


# Feature Importance


# Shows the Precision/Recall/F1


# Get model parameters used





# 5.0 CREATING & TUNING INDIVIDUAL MODELS ----



# Create more models




# Tuning Models



# Save xgb tuned


# 6.0 INTERPRETING MODELS ----
# - SHAP Package Integration



# 1. Summary Plot: Overall top features


# 2. Analyze Specific Features ----

# Our Exploratory Function
els.explore_sales_by_category(
    leads_df, 
    'member_rating', 
    sort_by='prop_in_group'
)

# Correlation Plot


# Partial Dependence Plot


# 3. Analyze Individual Observations


# Shap Force Plot



# 7.0 BLENDING MODELS (ENSEMBLES) -----



# 8.0 CALIBRATION ----
# - Improves the probability scoring (makes the probability realistic)




# 9.0 FINALIZE MODEL ----
# - Equivalent of refitting on full dataset


# 10.0 MAKING PREDICTIONS & RANKING LEADS ----

# Prediction

# Scoring


# SAVING / LOADING PRODUCTION MODELS -----



# CONCLUSIONS ----

# - We now have an email lead scoring model
# - Pycaret simplifies the process of building, selecting, improving machine learning models
# - Scikit Learn would take 1000's of lines of code to do all of this


