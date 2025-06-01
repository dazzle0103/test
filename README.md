# Python Template Project

## 🛠️ Setup Instructions

### 1. Clone the Template and Start a New Project

```bash
# Clone the template into a new folder
git clone --depth=1 https://github.com/dazzle0103/000_template my-new-project
cd my-new-project

# Remove the old Git history so this becomes a fresh project
rm -rf .git


# Create virtual environment
python -m venv venv

# Activate (Windows)
venv\Scripts\activate

#Create a new repository on github


# Initialize Git and connect to the new GitHub repo
git init
git remote add origin https://github.com/dazzle0103/my-new-project.git

# Install dependencies (if any are listed)
pip install -r requirements.txt

# Commit and push your initial code
git add .
git commit -m "Initial commit"
git push -u origin main
```
