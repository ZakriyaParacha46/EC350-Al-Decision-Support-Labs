import pandas as pd
import numpy as np
from scipy.stats import multivariate_normal

#load data
df = pd.read_csv("diabetes.csv")

#Split Data
np_array = df.to_numpy()
np.random.shuffle(np_array)
shuffled_df = pd.DataFrame(np_array, columns=df.columns)
X = shuffled_df.drop('Outcome', axis=1)  # Features
y = shuffled_df['Outcome']  # variable

split_index = int(0.5 * len(shuffled_df))
X_train, X_test = X.iloc[:split_index], X.iloc[split_index:]
y_train, y_test = y.iloc[:split_index], y.iloc[split_index:]

## Calculate posterial prbabilities
def fit(X_train, y_train):
    train_positive = X_train[y_train == 1]
    train_negative = X_train[y_train == 0]

    prior_positive = len(train_positive) / len(X_train)
    prior_negative = len(train_negative) / len(X_train)    

    mean_positive = np.array(train_positive.mean())
    mean_negative = np.array(train_negative.mean())

    covariance_positive = np.cov(train_positive, rowvar=False)
    covariance_negative = np.cov(train_negative, rowvar=False)
    
#    det_postive= np.linalg.det(covariance_positive)
#    det_negative= np.linalg.det(covariance_negative)

    values= {'prior_p':prior_positive,'prior_n':prior_negative,
            'cov_p':covariance_positive, 'cov_n':covariance_negative,
            'mean_p':mean_positive,'mean_n':mean_negative}

    return values
    
values=fit(X_train,y_train)
print(values)

def predict(values, X_test): 
    probabilities_positive = multivariate_normal.pdf(X_test, mean=values['mean_p'], cov=values['cov_p'])
    probabilities_negative = multivariate_normal.pdf(X_test, mean=values['mean_n'], cov=values['cov_n'])

    posterior_positive = probabilities_positive * values['prior_p']
    posterior_negative = probabilities_negative * values['prior_n']

    evidence= posterior_positive+posterior_negative

    posterior_positive = posterior_positive/evidence
    posterior_negative = posterior_negative/evidence

    predictions = (posterior_positive > posterior_negative).astype(int)
    return predictions

predictions= predict(values,X_test)
actual_outcome=y_test.values.astype(int) 
print(np.sum(predictions == actual_outcome)/ len(actual_outcome))