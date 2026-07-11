import pandas as pd

url = "https://www.w3schools.com/html/html_tables.asp"

tables = pd.read_html(url)

print(tables)