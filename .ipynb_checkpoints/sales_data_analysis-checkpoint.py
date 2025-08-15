# ---
# jupyter:
#   jupytext:
#     formats: py:percent
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.17.1
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# %%
import mysql.connector
import pandas as pd
import matplotlib.pyplot as plt
import warnings

# %%
# 1️⃣ Connect to MySQL
conn = mysql.connector.connect(
    host="localhost",  # or your server IP
    port=3306,
    database="sales_data",   # Your MySQL database name
    user="root",             # Your MySQL username
    password="Snehardha19@" # Your MySQL password
)

print("Connected to MySQL successfully!")


# %%

# 2️⃣ Query to aggregate sales
QUERY = """
SELECT 
    product, 
    SUM(quantity) AS total_qty, 
    SUM(quantity * price) AS revenue
FROM sales
GROUP BY product
"""

# %%
warnings.filterwarnings("ignore", category=UserWarning)

df = pd.read_sql(QUERY, conn)

# %%
# 4️⃣ Close the connection
conn.close()

# %%
# 5️⃣ Print results
print(df.to_string(index=False))

# %%
bars = plt.bar(df["product"], df["revenue"], color="skyblue")

# Add value labels on top of bars
for bar, rev in zip(bars, df["revenue"]):
    plt.text(bar.get_x() + bar.get_width()/2, bar.get_height(),
             f"${rev:,.0f}", ha="center", va="bottom", fontsize=8)

# Axis labels
plt.xlabel("Product", fontsize=12)
plt.ylabel("Revenue ($)", fontsize=12)

# Rotate x-ticks
plt.xticks(rotation=45)

plt.tight_layout()
plt.savefig("sales_chart_mysql.png", dpi=300)
plt.show()


