# CLAUDE.md - AI Assistant Guide for GAIH Student Repository

This document provides comprehensive guidance for AI assistants working with this Global AI Hub (GAIH) student repository.

## Repository Overview

**Purpose:** This is a student submission repository for Global AI Hub courses, containing Python homework assignments and final projects.

**Repository Type:** Educational / Student Portfolio
**Primary Language:** Python
**Course Date:** 08.03.2021
**Student:** Mustafa Üstünsöz

## Repository Structure

```
gaih-students-repo-example/
├── README.md                    # Student information and project overview
├── CLAUDE.md                    # This file - AI assistant guide
├── homework_1.py                # Root-level homework (legacy location)
├── Homeworks/                   # Organized homework directory
│   ├── HW1.py                  # Homework assignment 1
│   ├── HW2.py                  # Homework assignment 2
│   ├── HW3.py                  # Homework assignment 3
│   └── sample.py               # Sample/template file
├── Final Project/               # Final project directory
│   └── Final_Project.py        # Main final project file
└── img/                         # Images and certificates
    ├── newlogo.png             # GAIH logo
    ├── logo.png                # Alternative logo
    └── TopLearnerCertificate.png  # Student certificate
```

## File Organization Conventions

### Homework Files
- **Location:** All homework should be in the `Homeworks/` directory
- **Naming Convention:** `HW[number].py` (e.g., HW1.py, HW2.py, HW3.py)
- **Format:** Python files (.py) or Jupyter notebooks (.ipynb)
- **Structure:**
  ```python
  #Explain your work

  #Question 1
  # Solution code here

  #Question 2
  # Solution code here
  ```

### Final Project Files
- **Location:** `Final Project/` directory
- **Main File:** `Final_Project.py`
- **Dependencies:** May include CSV files or data files (e.g., project.csv)
- **Common Imports:** pandas, numpy, matplotlib, sklearn (typical for data science projects)

### Documentation Files
- **README.md:** Contains student information, project description, requirements, and certification
- **Required Formats:** .py or .ipynb files only (NOT .txt files)

## Development Workflow

### 1. Adding New Homework
When creating or modifying homework:
1. Place files in the `Homeworks/` directory
2. Follow the naming convention: `HW[number].py`
3. Include comments explaining the work
4. Add question numbers as comments
5. Ensure code is runnable (no syntax errors)

### 2. Working on Final Projects
For final project work:
1. Keep all project files in the `Final Project/` directory
2. Update README.md with project description
3. List all required libraries in the Requirements section
4. Include data files in the same directory as the main script
5. Use relative paths for data loading (e.g., `pd.read_csv("project.csv")`)

### 3. Documentation Updates
When updating the README:
1. Keep student information current (Name, Surname, Email)
2. Update Course Date if applicable
3. Provide clear project descriptions
4. List all Python library requirements
5. Maintain image references for logos and certificates

## Key Conventions for AI Assistants

### Code Quality Standards
1. **Runnable Code:** All Python files must be syntactically correct and executable
2. **Comments:** Include explanatory comments, especially for homework questions
3. **No Text Files:** Never submit homework as .txt files - only .py or .ipynb
4. **Import Statements:** Place all imports at the top of files
5. **Code Style:** Follow standard Python conventions (PEP 8)

### Common Code Patterns
- **List Operations:** Common in homework (sorting, merging, comprehensions)
- **Data Analysis:** Final projects typically use pandas DataFrames
- **Iteration:** Homework often involves loops and range operations

### File Handling
- **Read Before Edit:** Always read existing files before modifying
- **Preserve Structure:** Maintain the established directory structure
- **Relative Paths:** Use relative paths for data files within the project
- **Space in Paths:** Note that "Final Project" has a space - quote paths when needed

### Git Operations
- **Branch Naming:** Follow the pattern `claude/[description]-[session-id]`
- **Commit Messages:** Use clear, descriptive messages
  - Good: "Add homework 4 solution for loops and functions"
  - Bad: "Update file"
- **Push Behavior:** Always use `git push -u origin <branch-name>`

## Common Tasks and Guidance

### Task: Add New Homework Assignment
```bash
# 1. Create file in Homeworks directory
# 2. Name it appropriately (e.g., HW4.py)
# 3. Include structure with comments
# 4. Test that code runs without errors
```

### Task: Update Final Project
```bash
# 1. Read existing Final_Project.py
# 2. Make incremental changes
# 3. Ensure data file paths are correct
# 4. Update README.md with new requirements if needed
```

### Task: Fix Code Errors
```python
# 1. Read the file to understand context
# 2. Identify syntax or runtime errors
# 3. Fix while preserving original intent
# 4. Test that fixes don't break other parts
```

## Important Considerations

### When Working with This Repository:
1. **Student Work:** This contains student submissions - maintain academic integrity
2. **Educational Context:** Code may be learning exercises, not production quality
3. **Template Nature:** This is an example repository structure for students to fork/copy
4. **Incremental Progress:** Homework files show learning progression

### What NOT to Do:
1. Don't over-engineer simple homework solutions
2. Don't add complex dependencies without justification
3. Don't modify the overall repository structure
4. Don't remove comments or explanatory text
5. Don't create .txt files for code submissions

### What TO Do:
1. Maintain the simple, educational nature of the code
2. Add helpful comments for learning purposes
3. Ensure all code is runnable and tested
4. Follow the established naming conventions
5. Keep the structure clean and organized

## Python Environment Notes

### Common Libraries Used:
- **pandas:** Data manipulation and analysis
- **numpy:** Numerical computations
- **matplotlib/seaborn:** Data visualization
- **scikit-learn:** Machine learning (for advanced projects)

### Setup Recommendations:
```bash
# Typical environment setup for this repository
pip install pandas numpy matplotlib jupyter
```

## Quick Reference

### Directory Navigation:
```bash
/home/user/gaih-students-repo-example/              # Root
/home/user/gaih-students-repo-example/Homeworks/    # Homework files
/home/user/gaih-students-repo-example/Final Project/ # Final project (note space!)
```

### File Patterns:
- Homework: `Homeworks/HW*.py`
- Python files: `**/*.py`
- Notebooks: `**/*.ipynb`
- Images: `img/*.png`

## Troubleshooting

### Common Issues:

**Issue:** Code with undefined variables (e.g., `for x in range(a):` without defining `a`)
**Solution:** This may be a template/incomplete homework. Ask before adding test values.

**Issue:** Missing data files (e.g., project.csv not found)
**Solution:** Check if it should exist. May need to be created or is not committed to repo.

**Issue:** Import errors
**Solution:** Add missing library to README.md requirements section.

## Version Control Best Practices

1. **Commit Granularity:** One homework per commit, or logical chunks of final project work
2. **Branch Strategy:** Feature branches for each major addition
3. **Review Changes:** Always check git diff before committing
4. **Clean History:** Avoid committing work-in-progress or broken code

## Additional Resources

- **GAIH Website:** Global AI Hub program information
- **Python Documentation:** https://docs.python.org/3/
- **Pandas Documentation:** https://pandas.pydata.org/docs/
- **PEP 8 Style Guide:** https://pep8.org/

---

**Last Updated:** 2026-01-05
**Repository Status:** Active student portfolio/template
**Maintenance:** Update this file when repository structure or conventions change
