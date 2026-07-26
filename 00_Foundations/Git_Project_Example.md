# Example Workflow: Creating a New Project

This example shows the complete process of creating a local project, tracking it with Git and uploading it to GitHub.

The commands below use **PowerShell**, which is the terminal used in VS Code on Windows.

---

## 1. Choose the location for the project

First, move to the folder where the new project should be created.

```powershell
cd C:\Users\YourName\Desktop
```

### Why?

`cd` means **change directory**.

This command moves the terminal to the Desktop. The new project folder will be created inside the current location.

You can check your current location with:

```powershell
pwd
```

---

## 2. Create the project directory

```powershell
mkdir Sales_Analysis
```

### Why?

`mkdir` means **make directory**.

It creates a new folder called `Sales_Analysis`.

At this stage, the folder is only stored locally on the computer. Git is not tracking it yet.

---

## 3. Enter the project directory

```powershell
cd Sales_Analysis
```

### Why?

This moves the terminal inside the new project folder.

The following commands will now run inside `Sales_Analysis`.

---

## 4. Create the project files

```powershell
New-Item README.md
New-Item analysis.py
New-Item sales_data.csv
```

### Why?

`New-Item` creates a new file in PowerShell.

The files have different purposes:

- `README.md` documents the project.
- `analysis.py` contains the Python analysis.
- `sales_data.csv` contains the dataset.

The project structure now looks like this:

```text
Sales_Analysis/
├── README.md
├── analysis.py
└── sales_data.csv
```

---

## 5. Write and save the files

Open the project in VS Code:

```powershell
code .
```

### Why?

The dot means **the current directory**.

This command opens the entire `Sales_Analysis` folder in VS Code.

Write some content in the files and save them using:

```text
Ctrl + S
```

Saving a file updates the copy stored on the computer. It does not create a Git commit and does not upload anything to GitHub.

---

## 6. Initialise the Git repository

```powershell
git init
```

### Why?

This turns the current folder into a local Git repository.

Git creates a hidden `.git` folder containing:

- repository configuration
- commit history
- branch information
- version-control data

Git now watches changes inside this project.

---

## 7. Check the repository status

```powershell
git status
```

### Why?

This shows the current state of the repository.

New files will normally appear as **untracked**, which means Git can see them but has not been told to include them in a commit.

Example:

```text
Untracked files:
    README.md
    analysis.py
    sales_data.csv
```

---

## 8. Stage the project files

```powershell
git add .
```

### Why?

`git add` moves changes into the **staging area**.

The dot means:

> Stage all new, modified and deleted files inside the current repository.

The staging area allows you to choose exactly what will be included in the next commit.

For a specific file, use:

```powershell
git add README.md
```

After staging, check again:

```powershell
git status
```

The files should now appear under:

```text
Changes to be committed
```

---

## 9. Create the first commit

```powershell
git commit -m "Create initial project structure"
```

### Why?

A commit records the staged changes as a permanent snapshot in the local repository.

The `-m` option allows you to add a short commit message.

A good message explains what changed:

```text
Create initial project structure
```

The commit is still stored only on the local computer at this stage.

---

## 10. Create an empty repository on GitHub

On GitHub:

1. Select **New repository**.
2. Enter the repository name `Sales_Analysis`.
3. Choose whether it should be public or private.
4. Do not add another README if one already exists locally.
5. Create the repository.

### Why?

The GitHub repository will act as the remote online version of the local project.

---

## 11. Connect the local repository to GitHub

Copy the repository URL from GitHub, then run:

```powershell
git remote add origin https://github.com/username/Sales_Analysis.git
```

### Why?

`git remote add` creates a connection between the local repository and a remote repository.

`origin` is the standard name given to the main remote repository.

Check the connection with:

```powershell
git remote -v
```

---

## 12. Confirm the main branch name

```powershell
git branch -M main
```

### Why?

This renames the current branch to `main`.

GitHub commonly uses `main` as the default branch.

---

## 13. Push the project to GitHub

```powershell
git push -u origin main
```

### Why?

`git push` uploads local commits to GitHub.

The parts of the command mean:

- `origin` — the remote repository
- `main` — the branch being uploaded
- `-u` — connects the local `main` branch to the remote `main` branch

After the first push, future uploads usually require only:

```powershell
git push
```

---

## 14. The normal workflow after making changes

After the project has been connected to GitHub, the usual workflow is:

```powershell
git status
git add .
git commit -m "Describe the changes"
git push
```

### What each command does

```powershell
git status
```

Checks what has changed.

```powershell
git add .
```

Stages the changes for the next commit.

```powershell
git commit -m "Describe the changes"
```

Creates a local snapshot.

```powershell
git push
```

Uploads the commit to GitHub.

---

## Complete Workflow Summary

```text
Create or edit files
        ↓
Save files
        ↓
git status
        ↓
git add .
        ↓
git commit -m "message"
        ↓
git push
        ↓
Changes appear on GitHub
```