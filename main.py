#MapPlot.py
#Name:
#Date:
#Assignment:

import coffee
import pandas
import matplotlib.pyplot as plt


coffee = coffee.get_coffee()

types = []
scores = []

#print(coffee[0]["Data"]["Scores"]["Total"])

for bean in coffee:
    #print(bean)
    type = bean["Data"]["Type"]["Species"]
    score = bean["Data"]["Scores"]["Total"]
    if score != 0:
        types.append(type)
        scores.append(score)
    #print(year, score)

df = pandas.DataFrame({"Type": types,
                         "Score": scores})

avg_scores = df.groupby("Type").mean(numeric_only=True)

print(df)
avg_scores.plot(kind = 'bar', legend=False)
plt.ylabel("Average Score")
plt.title("Average Coffee Scores by Species")
plt.tight_layout()
#plt.plot(years, scores, 'ro')
plt.savefig("output")
