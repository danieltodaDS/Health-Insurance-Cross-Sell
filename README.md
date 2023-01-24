# Health Insurance Cross-Sell
## Ordering a potential client list by propensity score for a car insurance cross-sell

<img src="/img/chuttersnap-gts_Eh4g1lk-unsplash.jpg"
  alt="Alt text"
  title="cover image"
  style="display: inline-block; margin: 0 auto; max-width: 600px;height:600px">

*This project was proposed in the study trail of the Meigarom Lopes Data Science Community*

# 1. Business Problem.
  *Disclaimer: the business problem presented below is fictcious as well as Life Safety company. The dataset was collected from Kaggle's competition [Health Insurance Cross Sell](https://www.kaggle.com/datasets/anmolkumar/health-insurance-cross-sell-prediction).*
  
  Life Safety is a B2C company whose core business is offering health insurance to individuals. Now it plans to implement a cross sell strategy focused on distribuiting car insurance to its customer base. 
  
  Given that the budget for the sales is limited, it is necessary to prioritize those customers who are more likely to purchase the product. Then, a Data Scientist was consulted to build **a model to order the customer base by propensity score**. 
  
  To deal with this *learn to rank* machine learning challenge, Life Safety undertook a survey with 381000 customers, and they answered whether they were interested or not in insurance car offer. The train dataset was produced with the customers attributes and theirs responses to this survey   
 
  Two **data products** was developed to assist business team:
   
   1. Cumulative gains curve to suport sizing of sales operation
   2. Google Spreadsheet for automatic predictions of a given dataset
  


# 2. Business Assumptions.

Here are some assumptions about the business context:
  
  - B2C is a arrangement in which the company sells directly to individuals
  - Cross-sell is to sell related or complementary products to a customer, in addiction to that product that started the commercial relationship 
  - Insurance business is an arrangement that garantee a compensation for a given loss, damage, illness, or death, in return for the payment of a premium. A premium is a sum of money that the customer needs to pay regularly to an insurance company for this guarantee.
  - Cumulative gains curve is an evaluation curve that shows the percentage of targets reached when considering a certain percentage of the population with the highest probability to be target according to the model. It enables to compare that performance with a random pick. 

<details>
  <summary>Click to see the description of the columns</summary>
  
|Feature 	            | Definition |
|:---                | :---          |
|id                   |	Unique ID for the customer|
|Gender               |	Gender of the customer|
|Age 	                | Age of the customer|
|Driving_License      |	0 : Customer does not have DL, 1 : Customer already has DL|
|Region_Code          |	Unique code for the region of the customer|
|Previously_Insured   |	1 : Customer already has Vehicle Insurance, 0 : Customer doesn't have Vehicle Insurance|
|Vehicle_Age          |	Age of the Vehicle|
|Vehicle_Damage 	    | 1 : Customer got his/her vehicle damaged in the past. 0 : Customer didn't get his/her vehicle damaged in the past.|
|Annual_Premium       |	The amount customer needs to pay as premium in the year|
|Policy_Sales_Channel |	Anonymized Code for the channel of outreaching to the customer ie. Different Agents, Over Mail, Over Phone, In Person, etc.|
|Vintage 	            | Number of Days, Customer has been associated with the company|
|Response             | 1 : Customer is interested, 0 : Customer is not interested|
  
  
</details>


# 3. Solution Strategy

Having a understanding about the business problem, 3 deliverables (previously presented) were defined as a result of this first development cicle. This cicle is divided in 10 steps, based on CRISP-DM process, presented below: 

**Step 01. Data Description:**
  - A data overview about this dataset, like the shape, types, columns description, and first order descriptive statistics. This first analysis helped to understanding how data is distribuited, which feature deserve a deeper analysis and what transformations may be necessary for a better performance of the model
  
**Step 02. Feature Engineering:**
  - Firstly, a mental map of hypothesis was drawn and based on it I stated some hypothesis. Given the data constraints, I selected 10 hypothesis to be answered and then derived 5 features to help at analysis task, as well to give more inputs at feature selection 

**Step 03. Data Filtering:**

**Step 04. Exploratory Data Analysis:**

**Step 05. Data Preparation:**

**Step 06. Feature Selection:**

**Step 07. Machine Learning Modelling:**

**Step 08. Hyperparameter Fine Tunning:**

**Step 09. Convert Model Performance to Business Values:**

**Step 10. Deploy Modelo to Production:**

# 4. Top 3 Data Insights

**Hypothesis 01:**

**True/False.**

**Hypothesis 02:**

**True/False.**

**Hypothesis 03:**

**True/False.**

# 5. Machine Learning Model Applied

# 6. Machine Learning Modelo Performance

# 7. Business Results

# 8. Conclusions

# 9. Lessons Learned

# 10. Next Steps to Improve

  - Apply another encoders like PCA
  - Apply other ML algorithms like LightGBM 
  - Apply Pipeline Class 
  - Split this dataset in 3 slices (train, validation and test) and obtain the final error from this test dataset 
  
# LICENSE

# References

- https://www.investopedia.com/terms/c/cross-sell.asp
- https://towardsdatascience.com/meaningful-metrics-cumulative-gains-and-lyft-charts-7aac02fc5c14
- https://www.kaggle.com/datasets/anmolkumar/health-insurance-cross-sell-prediction
