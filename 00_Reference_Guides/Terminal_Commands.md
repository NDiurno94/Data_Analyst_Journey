# Terminal Commands

This document contains the most common PowerShell terminal commands used throughout my Data Analysis Journey.

Each command includes:
- Purpose
- Syntax
- Example
- Notes

---

# Navigation

## - pwd

### Purpose
Display the current working directory.

### Syntax

```powershell
pwd
```

### Example

```powershell
pwd
```

### Output

```text
C:\Users\Nicola\Desktop\Data_Analysis_Journey
```

### Notes

One of the first commands to use when opening a terminal to check where you currently are.

---

## - dir

### Purpose

List all files and folders in the current directory.

### Syntax

```powershell
dir
```

### Example

```powershell
dir
```

---

## - ls

### Purpose

Alternative command for listing files and folders.

### Syntax

```powershell
ls
```

### Notes

`ls` and `dir` produce very similar results in PowerShell.

---

## - cd

### Purpose

Move into another directory.

### Syntax

```powershell
cd <folder_name>
```

### Example

```powershell
cd 01_Python
```

---

## - cd ..

### Purpose

Move back one directory.

### Syntax

```powershell
cd ..
```

### Example

```powershell
cd ..
```

---

# Creating Files & Folders

## - mkdir

### Purpose

Create a new directory.

### Syntax

```powershell
mkdir <folder_name>
```

### Example

```powershell
mkdir Day_03
```

---

## - New-Item

### Purpose

Create a new file.

### Syntax

```powershell
New-Item <file_name>
```

### Example

```powershell
New-Item README.md
```

---

## - ni

### Purpose

Short alias for `New-Item`.

### Example

```powershell
ni notes.txt
```

---

# Managing Files

## - ren

### Purpose

Rename a file or folder.

### Syntax

```powershell
ren <old_name> <new_name>
```

### Example

```powershell
ren Day_1 Day_01
```

---

## - Rename-Item

### Purpose

Rename a file or folder.

### Example

```powershell
Rename-Item README.md Notes.md
```

---

## - del

### Purpose

Delete a file.

### Syntax

```powershell
del <file_name>
```

### Example

```powershell
del notes.txt
```

---

## - rmdir

### Purpose

Delete an empty directory.

### Syntax

```powershell
rmdir <folder_name>
```

### Example

```powershell
rmdir OldFolder
```

---

# Terminal

## - cls

### Purpose

Clear the terminal screen.

### Syntax

```powershell
cls
```

---



## - Ctrl + C

### Purpose

Cancel the currently running command.

Useful if a program is taking too long or becomes stuck.

---

# Git Commands

| Command | Purpose |
|----------|---------|
| `git status` | Check repository status |
| `git add .` | Stage all changes |
| `git add <file>` | Stage one file |
| `git commit -m "message"` | Create a commit |
| `git push` | Upload commits to GitHub |
| `git pull` | Download updates |
| `git log` | View commit history |

> Detailed explanations of Git concepts and workflows are available in **Git_and_GitHub.md** and **Git_Workflow_Example**