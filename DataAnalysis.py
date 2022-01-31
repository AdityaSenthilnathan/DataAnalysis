import pandas as pd
import csv
import plotly.express as px

DataFrame = pd.read_csv("dataVisualisation.csv")
mean = DataFrame.groupby(["student_id", "level"], as_index=False)["attempt"].mean()
figure = px.scatter(mean, x="student_id", y="level", size="attempt", color="attempt")
figure.show()