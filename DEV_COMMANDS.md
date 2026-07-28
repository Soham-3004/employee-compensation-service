# Employee Compensation Service - Development Commands

---

# Python

## Check Python version

```bash
python3 --version
```

---

# pip

## Check pip version

```bash
pip3 --version
```

## Upgrade pip

```bash
python -m pip install --upgrade pip
```

---

# Virtual Environment

## Create Virtual Environment

```bash
python3 -m venv .venv
```

## Activate Virtual Environment (Linux / WSL)

```bash
source .venv/bin/activate
```

## Deactivate Virtual Environment

```bash
deactivate
```

---

# Install Project Dependencies

```bash
pip install -r requirements.txt
```

## Save Installed Packages

```bash
pip freeze > requirements.txt
```

---

# Azure Functions Core Tools

## Create New Azure Function Project

```bash
func init
```

Choose:

```
Python
```

---

## Create a New Function

```bash
func new
```

Choose:

```
HTTP Trigger
```

Authorization:

```
Anonymous
```

---

## Start Azure Function App

```bash
func start
```

---

# SQLite

## Install SQLite

```bash
sudo apt update
sudo apt install sqlite3 -y
```

## Check SQLite Version

```bash
sqlite3 --version
```

---

## Create / Open Database

```bash
sqlite3 employee.db
```

If the database does not exist, SQLite creates it automatically.

---

## Execute SQL File

```sql
.read schema.sql
```

---

## Execute Seed File

```sql
.read seed.sql
```

---

## Show All Tables

```sql
.tables
```

---

## Show Schema of One Table

```sql
.schema Employee
```

```sql
.schema Department
```

---

## Show Entire Database Schema

```sql
.schema
```

---

## Show Data

```sql
SELECT * FROM Employee;
```

```sql
SELECT * FROM Department;
```

---

## Exit SQLite

```sql
.quit
```

or

```text
Ctrl + D
```

---

# Linux Commands

## Current Directory

```bash
pwd
```

---

## List Files

```bash
ls
```

---

## List Files with Details

```bash
ls -la
```

---

## Change Directory

```bash
cd folder_name
```

Go back one directory:

```bash
cd ..
```

---

## Create Folder

```bash
mkdir folder_name
```

---

## Create Multiple Folders

```bash
mkdir database models services utils
```

---

## Create Empty File

```bash
touch filename.py
```

Example:

```bash
touch employee_service.py
```

---

# Git

## Check Status

```bash
git status
```

---

## Add Files

```bash
git add .
```

---

## Commit

```bash
git commit -m "Your message"
```

---

## Push

```bash
git push
```

---

# Useful Testing

## Browser

```
http://localhost:7071/api/HelloFunction
```

Query Parameter

```
http://localhost:7071/api/HelloFunction?name=Soham
```

---

## GET using curl

```bash
curl http://localhost:7071/api/HelloFunction
```

---

## POST using curl

```bash
curl -X POST \
-H "Content-Type: application/json" \
-d '{"name":"Soham"}' \
http://localhost:7071/api/HelloFunction
```