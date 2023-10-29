# RowdyMiracleData
This was a miracle of data
---

# 📚 CSV to MySQL Uploader

This script allows you to automatically create a table in your MySQL database and populate it using data from a CSV file.

## 🛠️ Setup

1. **Dependencies**:
    - Python 3.x
    - `mysql-connector-python`

   Install the required module using:
   ```bash
   pip install mysql-connector-python
   ```

2. **Configuration**:

   Before running the script, make sure to modify the `config` dictionary in the script:
   ```python
   config = {
       'user': 'YOUR USER NAME',
       'password': 'YOUR PASSWORD',
       'host': 'YOUR HOST',
       'database': 'YOUR DATABASE NAME'
   }
   ```

3. **CSV File**:

   Ensure that your CSV file is formatted correctly to match the table structure defined in the script. Update the file path and encoding format in this line:
   ```python
   with open('PATH/YOURFILE.csv', 'r',encoding='YOUR FILE FORMAT', errors='replace') as file:
   ```
