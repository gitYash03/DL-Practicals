import torch
import torch.nn as nn
import torch.optim as optim

x=torch.tensor([[0.,0.],[0.,1.],[1.,0.],[1.,1.]])
y=torch.tensor([[0.],[1.],[1.],[0.]])

model = nn.Sequential(
    nn.Linear(2,2),
    nn.Sigmoid(),
    nn.Linear(2,1),
    nn.Sigmoid()
)

criterion = nn.MSELoss()
optimizer = optim.SGD(model.parameters(),lr=0.5)

epoch=5000

for _ in range(5000):
    output=model(x)
    loss=criterion(output,y)

    optimizer.zero_grad()
    loss.backward()
    optimizer.step()

print("XOR")
with torch.no_grad():
    for data in x:
        print(data.numpy()," -> ", round(model(data).item()))


# import numpy as np

# # Activation functions
# def sigmoid(x):
#     return 1 / (1 + np.exp(-x))

# def sigmoid_derivative(a):
#     return a * (1 - a)

# # Data (XOR)
# X = np.array([[0,0], [0,1], [1,0], [1,1]])
# Y = np.array([[0], [1], [1], [0]])

# # Initialize parameters
# np.random.seed(1)
# W1 = np.random.randn(2, 2)
# b1 = np.random.randn(1, 2)
# W2 = np.random.randn(2, 1)
# b2 = np.random.randn(1, 1)

# learning_rate = 0.5
# epochs = 10000

# # Training loop
# for _ in range(epochs):
#     # Forward pass
#     hidden = sigmoid(X @ W1 + b1)
#     output = sigmoid(hidden @ W2 + b2)

#     # Backpropagation
#     output_error = Y - output
#     output_delta = output_error * sigmoid_derivative(output)

#     hidden_error = output_delta @ W2.T
#     hidden_delta = hidden_error * sigmoid_derivative(hidden)

#     # Update parameters
#     W2 += hidden.T @ output_delta * learning_rate
#     b2 += np.sum(output_delta, axis=0, keepdims=True) * learning_rate

#     W1 += X.T @ hidden_delta * learning_rate
#     b1 += np.sum(hidden_delta, axis=0, keepdims=True) * learning_rate

# # Testing
# print("XOR outputs:")
# for x in X:
#     hidden = sigmoid(x @ W1 + b1)
#     output = sigmoid(hidden @ W2 + b2)
#     print(f"{x} -> {round(output[0][0])}")