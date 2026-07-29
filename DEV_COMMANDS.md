# Development Commands

## Install WSL Ubuntu

```powershell
wsl --install -d Ubuntu
```

---

## Install Required Packages

```bash
sudo apt update

sudo apt install -y \
python3 \
python3-pip \
python3-venv \
sqlite3 \
curl

curl https://packages.microsoft.com/keys/microsoft.asc | gpg --dearmor > microsoft.gpg

sudo install -o root -g root -m 644 microsoft.gpg /etc/apt/trusted.gpg.d/

sudo sh -c 'echo "deb [arch=amd64] https://packages.microsoft.com/repos/azure-cli/ jammy main" > /etc/apt/sources.list.d/azure-cli.list'

sudo apt update

sudo apt install azure-cli

npm install -g azure-functions-core-tools@4 --unsafe-perm true
```

---

## Clone Repository

```bash
git clone <repository-url>

cd employee-compensation-service
```

---

## Create Database

```bash
sqlite3 database/employee.db < database/schema.sql

sqlite3 database/employee.db < database/seed.sql
```

---

## Configure Local Settings

```bash
cp local.settings.example.json local.settings.json
```

---

## Create Virtual Environment

```bash
python3 -m venv .venv
```

---

## Activate Virtual Environment

```bash
source .venv/bin/activate
```

---

## Install Python Dependencies

```bash
pip install -r requirements.txt
```

---

## Start Azure Function

```bash
func start
```

---

# Testing Commands

## Create Employee

```bash
curl -X POST http://localhost:7071/api/employees \
-H "Content-Type: application/json" \
-d '{
    "FirstName":"John",
    "LastName":"Doe",
    "DepartmentID":1,
    "Salary":70000,
    "Bonus":5000,
    "HireDate":"2026-07-29"
}'
```

---

## Get All Employees

```bash
curl http://localhost:7071/api/employees
```

---

## Get Employee By ID

```bash
curl http://localhost:7071/api/employees/1
```

---

## Update Employee

```bash
curl -X PUT http://localhost:7071/api/employees/1 \
-H "Content-Type: application/json" \
-d '{
    "FirstName":"John",
    "LastName":"Doe",
    "DepartmentID":1,
    "Salary":75000,
    "Bonus":6000,
    "HireDate":"2026-07-29"
}'
```

---

## Delete Employee

```bash
curl -X DELETE http://localhost:7071/api/employees/1
```

---

## Total Bonus

```bash
curl http://localhost:7071/api/reports/total-bonus
```

---

## Employees With No Bonus

```bash
curl http://localhost:7071/api/reports/no-bonus
```

---

## Bonus Percentage

```bash
curl http://localhost:7071/api/reports/bonus-percentage
```

---

## High Bonus Departments

```bash
curl http://localhost:7071/api/reports/high-bonus-departments
```

---

## Bonus Ranking

```bash
curl http://localhost:7071/api/reports/bonus-ranking
```

---

## Highest Compensation

```bash
curl http://localhost:7071/api/reports/highest-compensation
```