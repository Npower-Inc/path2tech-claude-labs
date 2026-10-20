# Claude Labs

Hands-on exercises for the Path2Tech Claude course. In each lab you use **Claude as your coding partner**: you write a prompt, get Python code back, run it, and check whether it does what you need. You don't need to know how to code before you start.

## What You Need

- A free [claude.ai](https://claude.ai) account
- A free [Replit](https://replit.com) account (all code runs here, so you don't need to install anything on your computer)
- A way to open `.docx` files: Microsoft Word, Google Docs (upload the file to Google Drive), or the free Word at [office.com](https://www.office.com)

## Getting Started

1. **Download the labs.** On this repository's main page, click the green **Code** button, then **Download ZIP**, and unzip it on your computer. To grab a single file instead, click it and use the **Download raw file** button.
2. **Open the folder for your lab** (see [Labs at a Glance](#labs-at-a-glance)).
3. **Open `GETTING_STARTED.txt`.** It walks you through setting up your Replit project and uploading the right starter files for that lab.
4. **Read `Lab Instructions.docx` all the way through.** It explains the lab itself, every step, and what you hand in.

> **Tip:** Before you start a debugging or "break it" lab, paste your working code into a Claude chat as a backup.

## Labs at a Glance

Each lesson has two labs that practice the same skill on different scenarios.

| Lesson | Skill | Lab | Starter Files |
|---|---|---|---|
| In class | Your first program with Claude | [Build a Calculator (group activity)](exercises/in_class/) | None (handout only) |
| 1 | Prompting for code | [01_01 – Customer Feedback Tagger](exercises/lab_01_01/) | `customer_feedback.csv` |
| | | [01_02 – Timesheet Cleaner](exercises/lab_01_02/) | `timesheet.csv` |
| 2 | Debugging | [02_01 – Text Adventure Game](exercises/lab_02_01/) | `adventure_game.py`, `rooms.csv` |
| | | [02_02 – Text Analyzer](exercises/lab_02_02/) | `text_analyzer.py`, `sample_text.txt` |
| 3 | Automating file tasks | [03_01 – Meridian Apartments Maintenance Pipeline](exercises/lab_03_01/) | `lab3_starter_data.zip` |
| | | [03_02 – Bright Path Vet File Renaming](exercises/lab_03_02/) | `lab03_02_starter_data.zip` |
| 4 | Breaking a problem into steps | [04_01 – Grade Report Pipeline](exercises/lab_04_01/) | `grades.csv` |
| | | [04_02 – Fitness Log Pipeline](exercises/lab_04_02/) | `workout_log.csv` |
| 5 | Error handling & validation | [05_01 – TripSplit](exercises/lab_05_01/) | `tripsplit.py` |
| | | [05_02 – FocusPlanner](exercises/lab_05_02/) | `focusplanner.py` |
| 6 | Documenting code | [06_01 – Budget Tracker](exercises/lab_06_01/) | `main.py` |
| | | [06_02 – Habit Tracker](exercises/lab_06_02/) | `main.py`, `habits.csv` |

## Working in Replit: The Basics

Each lab's `GETTING_STARTED.txt` has the full steps. These rules apply to every lab:

- **Start from the Python template** and use claude.ai for help, not Replit's built-in AI Agent.
- **Upload data files next to `main.py`**, not inside another folder. The code finds files by name.
- **Starter code goes into `main.py`.** The green **Run** button runs `main.py`, so paste a lab's starter script (for example `tripsplit.py`) into it.
- **Scripts with other names (Lessons 3 and 4) run from the Shell.** Type `python script_name.py` in the **Shell** tab.
- **The starter data is messy on purpose.** Don't fix it by hand; cleaning it up with Python and Claude is part of the lab.

## Lab Descriptions

### In-Class Activity: Build a Calculator with Claude
A 30-minute activity for groups of three. Each person takes a role (Prompter, Coder, or Tester/Recorder). Your group plans, builds, and tests a Python calculator with Claude, then adds one extra feature. The handout is available as `.pdf` and `.docx`.

### Lesson 1: Prompting Claude for Code
Use the **Inputs / Outputs / Business Context** framework to write prompts that turn messy data into a useful report. You write a first prompt, improve it, and compare the results.
- **01_01 Customer Feedback Tagger:** Clean customer feedback and sort each comment as Positive, Negative, or Needs Follow-Up.
- **01_02 Timesheet Cleaner:** Clean employee shift data and add up the hours each employee worked for payroll.

### Lesson 2: Debugging with Claude
Practice the **Break → Read → Ask → Fix → Verify** loop. You start with a working program, break it on purpose in five specific ways, and use Claude to find and fix each problem.
- **02_01 Text Adventure Game:** A room-exploring game. Its rooms are stored in a CSV file, so one of the bugs is in the data, not the code.
- **02_02 Text Analyzer:** A program that reports word and sentence statistics. This lab introduces two new error types.

### Lesson 3: Automating File Tasks
Write prompts for scripts that rename files, clean CSV data, and pull structured information out of messy text. The starter data comes as a zip file: upload it and unzip it in Replit's Shell, or upload the unzipped folder instead.
- **03_01 Meridian Apartments:** Build three scripts for a property management company: rename tenant photos, clean a maintenance request log, and sort tenant complaints by category and urgency. Then explain how you would connect the three scripts.
- **03_02 Bright Path Veterinary Clinic:** A harder renaming lab. You'll build names from several fields, reformat dates, sort files into subfolders, and handle problems in the mapping file.

### Lesson 4: Breaking a Problem into Steps
Plan before you prompt. Use the 4-step decomposition framework (end goal → actions → data flow → order), then build a pipeline of four small scripts, each from its own prompt: **read → clean → calculate → summarize**. Each script reads the file the previous one created.
- **04_01 Grade Report:** Turn messy student test scores into a class report.
- **04_02 Fitness Log:** Turn a messy workout log into a summary by exercise type.

### Lesson 5: Error Handling & Validation
Each starter script works perfectly as long as the user types exactly what it expects. First you try to break it. Then you prompt Claude to add **validation**, **error handling**, and **logging**, and you test the new version against your list of bad inputs.
- **05_01 TripSplit:** Splits a bill and tip among friends.
- **05_02 FocusPlanner:** Plans study sessions with work and break blocks, Pomodoro-style.

### Lesson 6: Documenting Code
Take a working script that has no documentation and use Claude to add **docstrings**, write a **README**, and write a **plain-English summary** for readers who don't code.
- **06_01 Budget Tracker:** Tracks spending by category and flags categories that go over budget.
- **06_02 Habit Tracker:** Reads habit data from a CSV file and reports how often each habit was completed.

## Repository Layout

```
exercises/
├── in_class/
│   ├── GETTING_STARTED.txt          How to get ready for the activity
│   └── Claude_Calculator_Group_Activity (.pdf / .docx)
├── lab_01_01/
│   ├── GETTING_STARTED.txt          Start here: Replit setup and uploads
│   ├── Lab Instructions.docx        The full lab, step by step
│   └── customer_feedback.csv        Starter files for this lab
├── ...                              Every lab folder follows the same pattern
└── lab_06_02/
```
