import pandas as pd
# series = pd.Series([11,12,13,14])
# print(series)

data = {
    "Name":["shivam","suraj","aditya"],
    "city":["lucknow","sitapur","kanpur"],
    "course":["IT","CSE","AIML"],
    "marks":[85,98,75]
}
df = pd.DataFrame(data)
# print(df)
# print(df.info())
# print(df.describe())
df.to_csv("karantech4b.csv")
studentdetails = pd.read_csv("karantech4b.csv")
# print(studentdetails)
df = pd.DataFrame(studentdetails)
print(df)
print(df.head(10))
print(df.tail(10))
print(df.info())
print(df.describe())
print(df["marks"])
