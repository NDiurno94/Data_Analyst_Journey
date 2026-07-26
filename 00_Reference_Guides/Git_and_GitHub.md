# Git & GitHub

Git and GitHub are two of the most important tools used by Data Analysts, Business Analysts and Software Developers. They allow you to keep track of changes, organise projects, collaborate with others and maintain a complete history of your work.

Although they are often mentioned together, Git and GitHub are different technologies.

---

# Git vs GitHub

| Git | GitHub |
|------|---------|
| Distributed Version Control System (VCS) | Cloud platform that hosts Git repositories |
| Installed on your computer | Accessed through a web browser or Git client |
| Tracks changes to files | Stores repositories online |
| Works offline | Requires internet connection |
| Creates commits and branches | Enables collaboration and portfolio sharing |

---

# Why Git is important

Git allows you to:

- Track every modification made to a project.
- Restore previous versions if something breaks.
- Work on new features safely.
- Collaborate with multiple developers.
- Maintain a professional project history.

For Data Analysts, Git is commonly used to version:

- Python scripts
- SQL queries
- Jupyter Notebooks
- Documentation
- Dashboards
- Data analysis projects

---

# Repository

A repository is the main project folder tracked by Git.

It contains everything related to a project:

- Source code
- Documentation
- Datasets
- Images
- Project history

Every Git repository contains a hidden folder called `.git`, which stores the complete version history and repository configuration.

---

# Git Workflow

The standard Git workflow is:

Working Directory
↓

Staging Area
↓

Local Repository
↓

Remote Repository (GitHub)

---

## Working Directory

The Working Directory contains the current files you are editing.

Changes made here are **not yet saved** into Git's history.

---

## Staging Area

The Staging Area is a temporary area where you choose which changes will be included in the next commit.

Only staged files become part of the next snapshot.

---

## Commit

A commit is a snapshot of the project at a specific point in time.

Each commit records:

- The changes made
- The author
- The date and time
- A descriptive commit message

Example:

```
Add Day 01 Python exercises
```

✅Good commit message, describe **what changed**, not **what you did**.

```
Stuff
```

❌ Bad, does not describe what changed. 


---

## Remote Repository

A Remote Repository is an online copy of your project hosted on platforms such as GitHub.

It serves as:

- Backup
- Collaboration platform
- Portfolio

---

# Branch

A branch is an independent line of development.

The default branch is usually called **main**.

Branches allow you to develop new features without modifying the stable version of the project.

---

# Merge

Merge combines the changes from one branch into another.

After testing a feature branch, it is merged back into the main branch.

---

# Clone

Downloads an existing Git repository from GitHub onto your computer.

Used when starting work on an existing project.

---

# Push

Uploads local commits to the remote repository.

Changes only appear on GitHub after a successful push.

---

# Pull

Downloads the latest changes from the remote repository and updates your local project.

Always pull before starting work when collaborating with others.

---

# Most Common Git Commands

| Command | Description |
|----------|-------------|
| `git status` | Show repository status |
| `git add .` | Stage all changes |
| `git add <file>` | Stage a specific file |
| `git commit -m "message"` | Create a commit |
| `git push` | Upload commits to GitHub |
| `git pull` | Download latest changes |
| `git clone <url>` | Clone a repository |
| `git log` | Show commit history |
| `git branch` | List branches |
| `git checkout <branch>` | Switch branch |

---

# Best Practices

- Commit frequently.
- Write meaningful commit messages.
- Keep repositories organised.
- Push regularly as a backup.
- Never upload passwords or sensitive data.
- Use `.gitignore` to exclude unnecessary files.

---

# Summary

Git manages version history.

GitHub stores Git repositories online.

Together they provide a reliable workflow for developing, documenting and maintaining professional data analysis projects.