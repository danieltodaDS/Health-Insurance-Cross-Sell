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
  - Cost of acquisition of customers (CAC) is the sum of investments made in customer acquisition divided by total customers acquired

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

Having a understanding about the business problem, 3 deliverables (previously presented) were defined as a result of this first development cicle. Based on CRISP-DM process, this cicle is divided in 10 steps, presented below: 

**Step 01. Data Description:** 
A data overview about this dataset, like the shape, types, columns description, and first order descriptive statistics. Useful to understand the data distribuition and which deeper analysis may be undertook 
  
**Step 02. Feature Engineering:** 
Firstly, a mental map was drawn on coggle.it and based on it I stated some hypothesis. Given the data constraints, I focused on 10 hypothesis and  derived 5 features to analysis tasks and to give more inputs at feature selection 

**Step 03. Data Filtering:**
Simple way to reduce dimensionality of dataset, but no business constraints having influence on this project were considered and no reducing was done

**Step 04. Exploratory Data Analysis:**
Univariate, bivariate and multivariate analysis to answer the hypothesis

**Step 05. Data Preparation:**
Split train & validation dataset, and apply some scaling and encoding techniques

**Step 06. Feature Selection:**
Selected feaures based on feature importance gave by ExtraTreesClassifier

**Step 07. Machine Learning Modelling:**
Selection, training and cross-validation of 3 machine learning models

**Step 08. Hyperparameter Fine Tunning:**
Choose the best parameters of the model selected at previous step 

**Step 09. Convert Model Performance to Business Values:**
Present the business result obtained by the model

**Step 10. Deploy Model to Production:**
I published the model in a cloud environment and make it acessible through a Google Spreadsheet, so it can easily improve decisions of business team

# 4. Top 3 Data Insights

**Hypothesis 01:** Interest is greater at customers older than 40 years old

*True*. From this age there is a higher concentration among interested customers compared to no interested customers

![image](https://user-images.githubusercontent.com/110186368/214349558-798b61f8-d303-4171-af39-b8cff29d35e6.png)


**Hypothesis 02:** Interest rate is greater on newer vehicles

*False*. The table and chart presented below, show a smaller rate of interested on newer vehicle compared to other age

![image](https://user-images.githubusercontent.com/110186368/214350509-a7c17d22-1220-4874-be22-07e6053aad37.png)


**Hypothesis 03:** Interest is higher among customers with health insurance for more than 6 months

*False*. Being older than 6 month as a health insurance customers seems not to influence the interest on car insurance

![image](https://user-images.githubusercontent.com/110186368/214351728-5ec56ad6-0517-48b0-ada2-243bea9a0124.png)


# 5. Machine Learning Model Applied
For this first iteration of project, 3 algorithms was tested: KNN(K-Nearest Neighbors), Logistic Regression and XGBoost. Since this is ranking problem, I used Top@K metrics to compare these models performance after cross-validating (k-fold = 5, k=3000)

|Model             | Precision@k | Recall@k |
|:----             | :------     |:------   |
|KNN               | 0.3144      |0.126     |
|LogistRegresssion | 0.3342      |0.1339    |
|XGBoost           | 0.3443   |   0.1379            |

# 6. Machine Learning Model Performance

The selected model was **XGBoost** since it achieved the better performance. Even so, its parameters was hipertuned and final results are shown below: 

|Model   |  k         | Precision@k | Recall@k |
|:----   |:---          | :------     |:------   |
|XGBoost     |3000          | 0.4281      |0.1388     |
|Random model|3000       | 0.1214      | 0.039|

1. This means a 24% increase in precision@k and 0,6% na recall@k, after the hiperparameter fine tuning. 
2. Compared to a Random model, in which the list of leads is sorted randomly, XGBoost performs +252% in precision@K and +255% in recall@K. In a random model is expected to pick the same percentage of interested as the percentage of sample, resulting in a 45 degree straight line 

This comparisions can be better represented bellow in Cumulative Gains Curve

![image](https://user-images.githubusercontent.com/110186368/214425723-2f93d6f7-602a-498f-ba13-94639a5c4636.png)


# 7. Business Results
To ilustrate the impact in business, consider 20% of this list of 76,222 customers and 9,256 interested (validation dataset).

|Model        | % of list | % of all interested|Total of interested|
|:----        |:------    |:------             |:----              |
|XGBoost      |20         |20                  |1,851              |
|Random model |20         |57.8                |5,349              | 

At this percentile, the model find 2.89x more interested that a random pick. The lift curve below sumarize that increment for whole list.

![image](https://user-images.githubusercontent.com/110186368/214435208-8ff6f4a3-9f5a-4914-b9dd-1d5366a3d698.png)

The table below presents this lift in various percentis from 10 to 90. 

|Percentil|Customers  |Lift      |Interested by model |Random pick | Reduction in CAC|
|:----    |:------    |:------   |:----               |:-----      |:-----           |
|10	      |7622	      |3.22	     |2980	              |925.58      |-0.74            |
|20	      |15245	    |2.89	     |5349	              |1851.27	   |-0.35            |
|30	      |22867	    |2.63	     |7305	              |2776.85	   |-0.22            |
|40	      |30489	    |2.32	     |8573	              |3702.42	   |-0.15            |
|50	      |38112	    |1.98	     |9155	              |4628.12	   |-0.11            |
|60	      |45734	    |1.66	     |9245	              |5553.70	   |-0.07            |
|70	      |53356	    |1.43	     |9246	              |6479.27	   |-0.05            |
|80	      |60978	    |1.25	     |9251	              |7404.85	   |-0.03            |
|90	      |68601	    |1.11	     |9254	              |8330.55	   |-0.01            |

I also calculated the **reduction in CAC** for each percentile at this table. For example, at percentile 20%, it was estimated a reduction of 35% in CAC if used the list sorted by model, compared to a random pick

# 8. Conclusions

# 9. Lessons Learned

# 10. Next Steps to Improve

  - Apply other ML algorithms like LightGBM 
  - Apply Pipeline Class 
  - Try PCA in data preparation step
  - Split this dataset in 3 slices (train, validation and test) and obtain the final error from this test dataset 
  
# LICENSE

# References

- https://www.investopedia.com/terms/c/cross-sell.asp
- https://towardsdatascience.com/meaningful-metrics-cumulative-gains-and-lyft-charts-7aac02fc5c14
- https://www.kaggle.com/datasets/anmolkumar/health-insurance-cross-sell-prediction
