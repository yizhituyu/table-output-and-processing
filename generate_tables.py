# Data for Table 1
table1_data = [
    ("A1", 41), ("A2", 18), ("A3", 21), ("A4", 63), ("A5", 2),
    ("A6", 53), ("A7", 5), ("A8", 57), ("A9", 60), ("A10", 93),
    ("A11", 28), ("A12", 3), ("A13", 90), ("A14", 39), ("A15", 80),
    ("A16", 88), ("A17", 49), ("A18", 60), ("A19", 26), ("A20", 28)
]

# Extract values for calculations
value_map = dict(table1_data)

# Table 2 data calculations
table2_data = [
    ("Alpha", value_map["A5"] + value_map["A20"]),
    ("Beta", value_map["A15"] // value_map["A7"]),  # Integer division
    ("Charlie", value_map["A13"] * value_map["A12"])
]

# Generate Table 1 HTML content
def create_table1():
    table1 = "<table><caption><strong>Table 1</strong></caption>"
    table1 += "<tr><th>Index #</th><th>Value</th></tr>"
    for index, value in table1_data:
        table1 += f"<tr><td>{index}</td><td>{value}</td></tr>"
    table1 += "</table>"
    return table1

# Generate Table 2 HTML content
def create_table2():
    table2 = "<table><caption><strong>Table 2</strong></caption>"
    table2 += "<tr><th>Category</th><th>Value</th></tr>"
    for category, value in table2_data:
        table2 += f"<tr><td>{category}</td><td>{value}</td></tr>"
    table2 += "</table>"
    return table2

# HTML content template
html_template = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Dynamic Tables</title>
    <style>
        body {{
            font-family: Arial, sans-serif;
            margin: 20px;
        }}
        table {{
            border-collapse: collapse;
            width: 50%;
            margin: 20px auto;
            text-align: center;
        }}
        th, td {{
            border: 1px solid black;
            padding: 8px;
        }}
        th {{
            background-color: #f2f2f2;
        }}
        caption {{
            font-weight: bold;
            margin-bottom: 10px;
        }}
    </style>
</head>
<body>
    {table1}
    {table2}
</body>
</html>
"""

# Combine the template with the generated tables
html_content = html_template.format(table1=create_table1(), table2=create_table2())

# Save to an HTML file
with open("dynamic_tables.html", "w") as file:
    file.write(html_content)

print("HTML file 'dynamic_tables.html' has been created. Open it in a browser to view the tables.")
