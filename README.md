# Bank Customer Deposit Prediction
 The streamlit app is developed upon a classification model that is trained on a [Portuguese banking institution](https://archive.ics.uci.edu/dataset/222/bank+marketing) data to make predictions whether a bank customer would subscribe to a term deposit. For model training, full data set is deployed, with approximately 41.4k rows and 21 columns. Then, the trained model is prepared for cloud deployment. The full workflow can be found down below.

## Model Workflow
![Ekran görüntüsü 2023-06-12 131936](https://github.com/dfavenfre/customer_deposit_classifier/assets/118773869/1dbbd37d-72be-4066-b691-ee9316285c77)

# Solving The Imbalance Issue
 Responses are converted to binary variables, which were labeled as "Yes" and "No" originally, for model development purposes. Approximately, 89% of the labels are "No", or 0, and the remaining are "Yes", or 1. Thereon, two different approaches were followed to develop the best model in terms of higher prediction capability.
 
![image](https://github.com/dfavenfre/customer_deposit_classifier/assets/118773869/a115ce1f-9c88-47ce-a3de-9f862117adb6)

 First, due to the imbalanced nature of the target variable, the under-sampled target variable "yes" is synthetically re-populated using SMOTE. Thereon, the main performance metric is selected as the accuracy score of prediction. Next, under-sampled target variable, which is not be re-populated, and thus, the main performance metric is Precision - Recall Curve and scores.

# Model Performance
## Precision + Recall Curve 
![image](https://github.com/dfavenfre/customer_deposit_classifier/assets/118773869/be849e16-3ce4-478b-a9bb-044479b4eb5d)
## Confusion Matrix Report
![image](https://github.com/dfavenfre/customer_deposit_classifier/assets/118773869/14a97359-6bcc-4d61-b615-7af28515c515)


