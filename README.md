# Bank Customer Deposit Prediction
 The streamlit app is developed upon a classification model that is trained on a [Portuguese banking institution](https://archive.ics.uci.edu/dataset/222/bank+marketing) data to make predictions whether a bank customer would subscribe to a term deposit. For model training, full data set is deployed, with approximately 41.4k rows and 21 columns. Then, the trained model is prepared for cloud deployment. The full workflow can be found down below.

# Streamlit Application
The model is uploaded to [streamlit](https://dfavenfre-customer-deposit-classifier-app-oyvffw.streamlit.app/) for public use to demonstrate applicability and performance of the trained model. The model is consisted of 6 features, which are selected by RFECV algorithm as the most significant variables in terms of variance explanability. Trained model is capable of making prediction with approximately 95% accuracy with following features;
- Occupation
- Last contact day of the week
- Number of contacts performed during this campaign and for this client
- Outcome of the previous marketing campaign
- Consumer price index - monthly indicator
- Euribor 3 month rate - daily indicator

![image](https://github.com/dfavenfre/customer_deposit_classifier/assets/118773869/bd411b6b-04e6-4200-ab02-3896cbca0ffc)

# Model Workflow
![Ekran görüntüsü 2023-06-12 131936](https://github.com/dfavenfre/customer_deposit_classifier/assets/118773869/1dbbd37d-72be-4066-b691-ee9316285c77)

# Solving The Imbalance Issue
 Responses are converted to binary variables, which were labeled as "Yes" and "No" originally, for model development purposes. Approximately, 89% of the labels are "No", or 0, and the remaining are "Yes", or 1. Thereon, two different approaches were followed to develop the best model in terms of higher prediction capability.
 
![image](https://github.com/dfavenfre/customer_deposit_classifier/assets/118773869/948c7552-7625-4aaa-a561-c6bcd5c7baa3)

 First, due to the imbalanced nature of the target variable, the under-sampled target variable "yes" is synthetically re-populated using [SMOTE](https://imbalanced-learn.org/stable/references/generated/imblearn.over_sampling.SMOTE.html). Thereon, the main performance metric is selected as the accuracy score of prediction. Next, under-sampled target variable, which is not be re-populated, and thus, the main performance metric is Precision - Recall Curve and scores. 
 
 Moreoever, feature selection is conducted using [Recursive Feature Elimination (RFE)](https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.RFE.html). RFE allows model to assign importance for each feature deployed. Later, the weighted features are ranked in an accordance with their corresponding importance score. The least significant features, in terms of ranking, are pruned from the model.

# Model Performance
## ROC Curve
![image](https://github.com/dfavenfre/customer_deposit_classifier/assets/118773869/861d0fc0-b25c-4f1b-b267-bcfc9afb4368)

### Confusion Matrix Report
![image](https://github.com/dfavenfre/customer_deposit_classifier/assets/118773869/deabf16d-ff15-4ae2-9ef4-02b84471434d)
## Precision + Recall Curve 
![image](https://github.com/dfavenfre/customer_deposit_classifier/assets/118773869/de3388c0-d14c-4dfb-a509-357d3cc2d4d8)
### Confusion Matrix Report
![image](https://github.com/dfavenfre/customer_deposit_classifier/assets/118773869/ff70b620-9e36-4f96-99b5-e98fb69fa643)

# Conclusion
Two different approaches yielded almost identical performances in terms of making predictions. 

| Model | Performance Metric | Score|
| ------|-------------------| -----|
| Imbalanced XGBClassifier| Precision + Recall| 0.95|
| Balanced XGBClassifier| Accuracy | 0.943 |

However, upon completion of feature selection, RFECV algorithm concluded significantly less features as the most important ones, with balanced data. On the contrary, Imbalanced data required more features to be able to achieve this accuracy score. 

Conclusion, balanced data performed superior with less data requirement. Therefore, the streamlit app will be built upon using the features selected by RFECV as the most important with balanced data.  



