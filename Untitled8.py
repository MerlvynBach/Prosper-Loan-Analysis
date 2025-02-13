#!/usr/bin/env python
# coding: utf-8

# # Python Project - (Prosper loan Dataframe)
# ## by (Bachor Merlvyn Gabriel)
# 
# ## Introduction
# 
# ##### The Prosper Loan dataset is a comprehensive collection of peer-to-peer lending data, provided by Prosper, a leading online lending platform. The dataset contains information on over 113,000 loans issued between 2005 and 2014, including loan characteristics, borrower demographics, and loan performance metrics. This dataset offers a unique opportunity for analysis and insight into the peer-to-peer lending market, enabling researchers and data scientists to explore topics such as credit risk assessment, loan default prediction, and the impact of borrower characteristics on loan outcomes.

# ##### DATA WRANGLING
# - Remove all unwanted columns 
# - Remove duplicates
# - Fill up NAN rows

# In[220]:


import pandas as pd


# In[222]:


df=pd.read_csv('Prosper Loan (2).csv')


# The Prosper Loan dataset is a comprehensive collection of peer-to-peer lending data, containing information on over 113,000 loans issued between 2005 and 2014. The dataset has the following structure:
# 
# Loan Information
# 1. LoanNumber: Unique identifier for each loan
# 2. LoanStatus: Current status of the loan (e.g., "Current", "Defaulted", "Paid")
# 3. LoanAmount: Amount borrowed by the borrower
# 4. InterestRate: Interest rate of the loan
# 5. LoanTerm: Length of the loan (in months)
# 
# Borrower Information
# 1. BorrowerID: Unique identifier for each borrower
# 2. BorrowerName: Name of the borrower
# 3. CreditScore: Credit score of the borrower
# 4. Income: Income of the borrower
# 5. EmploymentStatus: Employment status of the borrower
# 
# Loan Performance
# 1. Defaulted: Indicator of whether the loan defaulted
# 2. Paid: Indicator of whether the loan was paid in full
# 3. LatePayments: Number of late payments made by the borrower
# 4. LoanOriginated: Date the loan was originated
# 
# Additional Features
# 1. CreditGrade: Prosper's credit grade for the borrower
# 2. DebtToIncomeRatio: Borrower's debt-to-income ratio
# 3. IncomeVerifiable: Indicator of whether the borrower's income is verifiable
# 4. Occupation: Borrower's occupation
# 
# This structure provides a comprehensive view of the loan, borrower, and loan performance, enabling analysis and modeling of credit risk, loan default prediction, and other related topics.

# ##### My interest in this dataset is to explore it and understand our customers better,
# ##### Get to know who the majority of our customers are, 
# ##### Does the emolymnet status affect their ability to borrow and repay loan,
# ##### Understand how loans given out are measured
# ##### Which payment plan suits our customers best.

# ##### To solve my insight i am going to be using information from the loan information, borrower information, loan performance

# ##### First step we clean the data by dropping the uncessary columns 

# In[227]:


df=df.drop(columns='OnTimeProsperPayments')


# In[230]:


df=df.drop(columns='GroupKey')


# In[232]:


df=df.drop(columns='ProsperPaymentsLessThanOneMonthLate')


# In[234]:


df=df.drop(columns='ProsperPaymentsOneMonthPlusLate')


# In[236]:


df=df.drop(columns='ProsperPrincipalBorrowed')


# In[237]:


df=df.drop(columns='ProsperPrincipalOutstanding')


# In[239]:


df=df.drop(columns='ScorexChangeAtTimeOfListing')


# In[240]:


df=df.drop(columns='LoanCurrentDaysDelinquent')


# In[242]:


df=df.drop(columns='LoanFirstDefaultedCycleNumber')


# In[243]:


df=df.drop(columns='TotalProsperPaymentsBilled')


# In[245]:


df=df.drop(columns='LP_CustomerPrincipalPayments')


# In[247]:


df=df.drop(columns='LP_ServiceFees')


# In[248]:


df=df.drop(columns='LP_CollectionFees')


# In[250]:


df=df.drop(columns='LP_GrossPrincipalLoss')


# In[251]:


df=df.drop(columns='LP_NonPrincipalRecoverypayments')


# In[253]:


df=df.drop(columns='LP_InterestandFees')


# In[254]:


df=df.drop(columns='LP_NetPrincipalLoss')


# In[256]:


df=df.drop(columns='CreditGrade')


# In[263]:


df=df.drop(columns='TotalProsperLoans')


# In[266]:


df=df.drop(columns='ClosedDate')


# In[267]:


df=df.drop(columns='ProsperRating (numeric)')


# In[270]:


df=df.drop(columns='ProsperRating (Alpha)')


# In[272]:


df=df.drop(columns='ListingCategory (numeric)')


# In[274]:


df=df.drop(columns='EmploymentStatusDuration')


# In[276]:


df=df.drop(columns='EstimatedEffectiveYield')


# In[278]:


df=df.drop(columns='CurrentDelinquencies')


# In[280]:


df=df.drop(columns='AmountDelinquent')


# In[282]:


df=df.drop(columns='InvestmentFromFriendsCount')


# In[284]:


df=df.drop(columns='InvestmentFromFriendsAmount')


# In[286]:


df=df.drop(columns='Recommendations')


# In[288]:


df=df.drop(columns='Investors')


# In[290]:


df=df.drop(columns='EstimatedLoss')


# In[292]:


df=df.drop(columns='EstimatedReturn')


# In[293]:


df=df.drop(columns='LenderYield')


# In[295]:


df=df.drop(columns='BankcardUtilization')


# In[297]:


df=df.drop(columns='TradesNeverDelinquent (percentage)')


# In[298]:


df=df.drop(columns='RevolvingCreditBalance')


# In[299]:


df=df.drop(columns='MemberKey')


# In[301]:


df=df.drop(columns='PercentFunded')


# In[302]:


df=df.drop(columns='ListingKey')


# In[308]:


df=df.drop(columns='LoanKey')


# In[310]:


df.info()


# ##### Change the column name to lower case for easy access( my own preference)

# In[313]:


df.columns=df.columns.str.lower()


# In[315]:


df.listingnumber.value_counts()


# ##### Remove duplicate from the column

# In[318]:


df=df.drop_duplicates('listingnumber', keep='last')


# In[320]:


df


# In[322]:


df.isnull().sum()


# ##### Fill up the unknown value in various columns

# In[325]:


df.prosperscore=df.prosperscore.fillna(0)


# In[327]:


df.borrowerstate=df.borrowerstate.fillna(0)


# In[329]:


df.occupation=df.occupation.fillna('Other')


# In[331]:


df.creditscorerangelower=df.creditscorerangelower.fillna(0)


# In[333]:


df.creditscorerangeupper=df.creditscorerangeupper.fillna(0)


# In[335]:


df.firstrecordedcreditline=df.firstrecordedcreditline.fillna('01/01/2006')


# In[337]:


df.currentcreditlines=df.currentcreditlines.fillna(0)


# In[339]:


df.opencreditlines=df.opencreditlines.fillna(0)


# In[341]:


df.totalcreditlinespast7years=df.totalcreditlinespast7years.fillna(0)


# In[343]:


df.inquirieslast6months=df.inquirieslast6months.fillna(0)


# In[345]:


df.totalinquiries=df.totalinquiries.fillna(0)


# In[347]:


df.delinquencieslast7years=df.delinquencieslast7years.fillna(0)


# In[349]:


df.publicrecordslast10years=df.publicrecordslast10years.fillna(0)


# In[351]:


df.publicrecordslast12months=df.publicrecordslast12months.fillna(0)


# In[353]:


df.availablebankcardcredit=df.availablebankcardcredit.fillna(0)


# In[355]:


df.totaltrades=df.totaltrades.fillna(0)


# In[357]:


df.tradesopenedlast6months=df.tradesopenedlast6months.fillna(0)


# In[359]:


df.debttoincomeratio=df.debttoincomeratio.fillna(0.00)


# In[361]:


df.borrowerapr=df.borrowerapr.fillna(0.00)


# In[363]:


df.isnull().values.any()


# In[365]:


df


# In[367]:


df=df.drop(columns='listingcreationdate')


# In[369]:


df


# In[371]:


df['loanoriginationdate']=pd.to_datetime(df['loanoriginationdate'], errors='coerce')


# ##### After cleaning data has beeen done, we move to visualization

# In[374]:


import numpy as np


# In[376]:


import matplotlib.pyplot as plt


# In[378]:


import seaborn as sns


# ##### UNIVARIATE VISUALIZATION

# #### Q1) WHAT IS THE EMPLOYMNET STATUS OF MAJORITY OF OUR CUSTOMERS?

# In[382]:


sns.countplot(data=df, y='employmentstatus')


# ##### OBSERVATION; 
# FROM THE ABOVE CHART WE CAN DEDUCE THAT A LARGE PERCENT OF OUR CUSTOMERS ARE EMPLOYED AND WORKING, WHILE A FEW OF THEM ARE RETIRED,UNEMPLOYED OR WORK PART TIME.

# ##### Q2) IS MAJORITY OF OUR CUSTOMERS HOUSE OWNERS OR NOT?

# In[386]:


sns.countplot(data=df, x='isborrowerhomeowner')


# ##### OBSERVATION; 
# GIVEN THE CHART ABOVE WE CAN CONCLUDE THAT THE NUMBERS OF CUSTOMERS THAT ARE HOUSE OWNERS ARE SLIGHTLY HIGHER THAN THOSE THAT ARE NOT.

# ##### Q3) WHAT IS THE PRESENT LOAN STATUS OF OUR CUSTOMERS?

# In[390]:


sns.countplot(data=df, y='loanstatus')


# ##### OBSERVATION;
# WE HAVE A LARGE NUMBER OF CUSTOMERS PRESENTLY ON CURRENT ONGOING LOANS,FOLLOWED BY COMPLETED LOAN PAYMENT. THEN WE CAN SEE FROM THE CHART WE HAVE A GOOD NUMBER OF CHARGED OFF LOANS, DEFAULTED AND VERY LITTLE NUMBER OF CUSTOMERS THAT HAVE JUST PASSED THEIR DUE DATE.

# ##### Q4) HOW MANY OF OUR CUSTOMERS HAVE THEIR INCOME BEEN VERIFIED?

# In[394]:


sns.countplot(data=df, x='incomeverifiable')


# ##### OBSERVATION;
# FROM THE CHART IT IS EVIDENT THAT MAJORITY OF OUR COSTUMERS INCOME HAS BEEN VERIFIED

# ##### Q5) WHAT PAYMENT DURATION IS MOST FAVORABLE TO OUR CUSTOMERS?

# In[398]:


sns.countplot(data=df, x='term')


# ##### OBSERVATION;
# MAJORITY OF OUR CUSTOMERS PREFER THE 36 MONTHS PLAN WHICH IS VISIBLE THROUGH THE CHART ABOVE

# ##### BIVARIATE VISUALIZATION

# ##### Q1) WHICH PAYMENT PLAN IS PREFERED BY OUR CUSTOMERS IN THE TOP BORROW STATE?

# In[404]:


sns.countplot(y="borrowerstate", hue="term", data=df, order=df.borrowerstate.value_counts().iloc[:10].index)


# ##### OBSERVATION; 
# AS EARLIER CONFIRMED IN OUR PREVIOUS VISUAL CHART ALL OUR TOP STATES  HAS A HIGH NUMBER OF COSTUMERS OPT FOR THE 36 MONTH REPAYMENT PLAN

# ##### Q2) WAS THE CUSTOMERS INCOME VERIFIABLE IN ALL EMPLOYMENT STATUS?

# In[407]:


sns.violinplot( data=df,  y='employmentstatus', hue='incomeverifiable')


# ##### OBSERVATION;
# WE CAN SEE THROUGH THE CHART ABOVE THAT WE WERE ONLY AGE TO VERIFY THE INCOME OF THE FULL TIME WORKERS AND THE EMPLOYED. WHILE THE REST HAVE NOT BEEN VERIFIED

# ##### Q3) WHATS THE HIGHEST INCOME RANGE OF THE TOP OCCUPATION?

# In[414]:


sns.countplot(y="occupation", hue="incomerange", data=df, order=df.occupation.value_counts().iloc[:10].index)


# ##### OBSERVATION;
# GIVEN THE CHART ABOVE, WE CAN DEDUCE THAT FOR CLERICAL ITS IN THE RANGE OF 25K-50K, ACCOUNTANT IS 50K-75K, SALES IS ALSO 50K-75K, ANALYST ALSO IS 50K-75K, ADMIN ASSISTANT IS 25K-50K, TEACHER IS 50K-75K, EXECUTIVE IS 100K AND ABOVE, COMPUTER PRGRAMMER IS 75K-100K, PROFESSIONAL IS 50K-75K AND OTHERS IS 25K-50K

# ##### Q4) DOES THEIR INCOME RANGE AFFECT THE AMOUNT OF LOAN GIVEN?

# In[453]:


sns.barplot( data=df, y='incomerange', x='loanoriginalamount')


# ##### OBSERVATION; 
# ITS EVIDENT THAT THE AMOUNT OF LOAN GIVEN OUT TO A CUSTOMER IS BASED ON THEIR INCONE RANGE AS SHOWN IN THE CHAT WHERE THOSE THAT EARN $100K AND ABOVE HAS THE HIGHEST LOAN REQUEST

# ##### Q5) WHATS THE LOAN STATUS OF THE TOP BORROWER STATE?

# In[2282]:


sns.countplot(y="borrowerstate", hue="loanstatus", data=df, order=df.borrowerstate.value_counts().iloc[:10].index)


# ##### OBSERVATION;
# THE CHART ABOVE SHOWS THAT OUR CUSTOMERS IN MAJORITY OF THE TOP STATES ARE PRESENTLY ON ONGOING CURRENT LOANS

# ##### NOTE:
# IN MOST OF OUR BIVARIANT VISUALIZATION, GIVEN THE FACT THAT THE MOST OF THE COLUMNS OF INETREST HAS LOTS OF VARIABLES AND IF DISPLAYED LIKE THAT ON THE CHART, IT WOULD LOOK TOO CROWDED SO WHAT I DID WAS PICK THE TOP 10 OF EACH COLUMNS WITH LOTS OF VARIABLE FOR A BETTER REPRESENTATION.

# #### FINAL CONCLUSION
# FROM THE ANALYSIS ABOVE WE CAN COME TO A CONCLUSION THAT OUR LOAN STRUCTURE IS NON DISCRIMINATORY AND TRANSPARENT, OUR CUSTOMERS CONSIST MAJORLY OF EMPLOYED INDIVIDUALS, BUT WE ALSO HAVE UNEMPLOYED, RETIRED AND SO ON.
# OUR COSTUMERS ARE MADE UP OF BOTH YOUNG ADULTS AND OLD INDIVIDUALS FROM ALL WORKS OF LIFE
# REGARDLESS OF YOUR STATUS THERES LOAN FOR EVERYONE. 
# THE LOANS CUT ACROSS ALL CORNERS OF THE UNITED STATE AT LARGE
# LOANS ARE GIVEN OUT BASED ON YOUR INCOME WHICH HELPS IN REPAYMENT AS ITS UNWISE TO GIVE A HUGE AMOUNT OF LOAN TO A PERSON WITHOUT ANY WORK. 
# COSTUMERS PREFER A LENGTHY DURATION TO PAY BACK THEIR LOANS AS IT IS MORE CONVENIENT FOR THEM.
# 
# 
# 

# In[ ]:




