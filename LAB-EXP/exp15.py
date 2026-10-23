from sklearn.tree import DecisionTreeClassifier

x = [[1, 1], [1, 0], [0, 1], [0, 0]]
y = ['Yes', 'Yes', 'No', 'No']

model = DecisionTreeClassifier()
model.fit(x, y)

result = model.predict([[1, 1]])

print("Prediction:", result[0])
