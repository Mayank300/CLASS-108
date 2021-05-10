import random 
import plotly.figure_factory as ff

# num1 = random.randint(1,6)
# num2 = random.randint(1,6)
# print("number 1 =", num1, "number 2 =", num2)
# print("sum =", num1 + num2)

result = []
count = []

for num in range(1,100):
    num1 = random.randint(1,6)
    num2 = random.randint(1,6)
    # print("number 1 =", num1, "number 2 =", num2)
    # print("sum =", num1 + num2)
    result.append(num1 + num2)
    count.append(num)

print(result)

fig = ff.create_distplot([result], ["result"])
fig.show()

