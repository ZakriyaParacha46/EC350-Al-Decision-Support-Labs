import numpy as np
def perceptron(data, learning_rate ,threshold, itt):
    
    num_samples = len(data)
    num_features = len(data[0]) - 1  

    # Initialize weights and threshold
    weights = np.zeros(num_features)

    # Training loop
    for iteration in range(itt):
        for sample in data:
            features = np.array(sample[:-1])  # Features

            target = sample[-1]  # Target class
            dot_product = np.dot(weights, features)
            output = 1 if dot_product >= threshold else 0
            error = learning_rate * (target - output)
            weights += error * features

        predicted_outputs = [1 if np.dot(weights, np.array(sample[:-1])) >= threshold else 0 for sample in data]
        accuracy = np.sum(predicted_outputs == np.array(data)[:, -1]) / num_samples
        print(f"Iteration {iteration + 1}, Accuracy: {accuracy}")
    return weights

# Example usage:
# Replace 'your_data' with your actual dataset
threshold= 0.5
learning_rate= 0.1
dataset = [[1,0,0,1], 
           [1,0,1,1], 
           [1,1,0,1],
           [1,1,1,0]] 

weights = perceptron(dataset,learning_rate,threshold, 100)
print("Final Weights:", weights)
