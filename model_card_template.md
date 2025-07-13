# Model Card

For additional information see the Model Card paper: https://arxiv.org/pdf/1810.03993.pdf

## Model Details
This model is a Random Forest Classifier. 

## Intended Use
To predict whether an individual earns more than $50K per year based on demographic and employment-related attributes. The model was built using **scikit-learn**, and was trained and evaluated using census data that includes features such as marital status, occupation, education level, sex, age, and hours worked per week.

## Training Data
The model was trained on a subset of the U.S. Census Income dataset (often referred to as the "Adult" dataset). The data includes attributes such as:
- Age
- Work class
- Education
- Marital status
- Occupation
- Relationship
- Race
- Sex
- Capital gain/loss
- Hours per week
- Native country

## Evaluation Data
Evaluation was conducted using a hold-out portion of the same dataset, with a stratified train-test split to preserve class distributions. No external data was used for validation.

## Metrics
Model performance on the test data:
- **Precision:** 0.7629
- **Recall:** 0.6277
- **F1 Score:** 0.6888

## Ethical Considerations
- **Bias and Fairness:** The model relies on potentially sensitive features such as race, sex, and marital status. These may introduce bias, and caution is required when interpreting results.
- **Privacy:** Although no personally identifiable information is included, using real census data mandates respectful handling and privacy awareness.
- **Misuse:** The model should not be used for any consequential decision-making, such as employment screening or financial profiling.

## Caveats and Recommendations
- The dataset is outdated and may not reflect current income distributions or socioeconomic conditions. As a result, predictions may be less accurate when applied to modern populations.
- The Random Forest Classifier, while powerful, can suffer from overfitting—especially when used without careful tuning or on noisy data. This can negatively impact generalization to new or unseen data.
