
# Sales Data Analysis with MySQL & Python

Author: **Snehardha Ghosh**  
Date: **2025-08-15**

This project demonstrates how to connect a MySQL database to Python using `pandas`, run SQL queries for sales data, and visualize the results using `matplotlib`.

---

## 📂 Project Overview
1. **Database Setup**
   - Created a MySQL database and a `sales` table.
   - Inserted sample product sales data.
   - Performed SQL queries to calculate total revenue by product.

2. **Python Integration**
   - Connected to MySQL using `mysql.connector`.
   - Queried the database directly into a `pandas` DataFrame.
   - Saved the DataFrame output to files for documentation.

3. **Data Visualization**
   - Created a bar chart showing revenue by product.
   - Added labels, rotated x-axis, and revenue annotations.
   - Exported the plot as `sales_chart_mysql.png`.

---

## 🛠️ Tech Stack
- **Database:** MySQL
- **Language:** Python 3.x
- **Libraries:**
  - `mysql.connector`
  - `pandas`
  - `matplotlib`

---

## 📊 Example Output
| product     | revenue   |
|-------------|-----------|
| Product A   | 12000     |
| Product B   | 9500      |
| Product C   | 7800      |

---

## 📜 Steps to Reproduce
1. **Clone the repository**
   ```bash
   git clone https://github.com/SnehardhaGhosh/sales-data-analysis-mysql.git
   cd sales-data-analysis-mysql
Install dependencies

```bash
    Copy
    Edit
    pip install pandas matplotlib mysql-connector-python
    Run the Python script
```bash
    Copy
    Edit
    python sales_analysis.py
📁 Folder Structure
lua
Copy
Edit
sales-data-analysis-mysql/
│-- sales_analysis.py
│-- sales_chart_mysql.png
│-- README.md
└-- data_output.csv
