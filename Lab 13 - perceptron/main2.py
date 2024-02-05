import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.metrics import confusion_matrix
import seaborn as sns

def perceptron(data, learning_rate ,threshold, itt):
    
    num_samples = len(data)
    num_features = len(data[0]) - 1  
    weights = np.zeros(num_features)

    # Training loop
    for iteration in range(itt):
        for sample in data:
            features = np.array(sample[:-1], dtype= np.float64)  # Features
            target = sample[-1]  # Target class
            
            target = 0 if target == 'R' else 1
            dot_product = np.dot(weights, features)
            output = 1 if dot_product >= threshold else 0
            error = learning_rate * (target - output)
            weights += error * features

        true_labels = np.where(np.array(data)[:, -1] == 'R', 0, 1)
        predicted_outputs = [1 if np.dot(weights, np.array(sample[:-1])) >= threshold else 0 for sample in data]
        accuracy = np.sum(predicted_outputs == true_labels) / num_samples
        print(f"Iteration {iteration + 1}, Accuracy: {accuracy}")
        if(accuracy>0.95): break
    return weights

def predict(weights, data):       
    true_labels = np.where(np.array(data)[:, -1] == 'R', 0, 1)
    predicted_outputs = [1 if np.dot(weights, np.array(sample[:-1])) >= threshold else 0 for sample in data]
    accuracy = np.sum(predicted_outputs == true_labels) / data.shape[0] ,    
    return accuracy[0],true_labels,predicted_outputs

threshold= 0.5
learning_rate= 0.1

df = pd.read_csv('sonar.all-data.csv').to_numpy()
np.random.shuffle(df)
df = np.insert(df, 0, 1, axis=1)

split_index=int(df.shape[0]*0.8)
traindata= df[:split_index,:]
testdata=  df[split_index:,:]
print(traindata.shape, testdata.shape)

weights    = perceptron(traindata, learning_rate, threshold, 1000)
accuracy, actual_labels, predicted_labels = predict(weights, testdata) 

print("Final Weights:", weights)
print("Test data acc:", accuracy)

cm = confusion_matrix(actual_labels, predicted_labels)

# Display the confusion matrix as a heatmap
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', xticklabels=['R', 'M'], yticklabels=['R', 'M'])
plt.xlabel('Predicted')
plt.ylabel('True')
plt.title('Confusion Matrix')
plt.show()