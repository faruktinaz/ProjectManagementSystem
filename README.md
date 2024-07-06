# ProjectManagementSystem
**Project management system built with Django, PostgreSQL, Django REST Framework, Vue JS 3, Vuetify 3**

## **How to run on your local machine?**

**Clone the repo:**

```bash
git clone https://github.com/faruktinaz/ProjectManagementSystem.git
cd ProjectManagementSystem
cd project_management_system
```

**Create a new Python Virtual Environment:**

```bash
python3 -m venv venv
```

**Activate the venv and install Django dependencies:**

```bash
source ./venv/bin/activate
pip install -m ./requirements.txt
```

**Apply Django migrations:**

```bash
python3 manage.py migrate
```

**Run Django Server:**

```bash
python3 manage.py runserver
```

This starts at port 8000.

**Install Node dependencies and Start the node server:**

```bash
cd frontend
npm install & npm run serve
```

This starts at port 8080.
