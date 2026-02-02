Beginner Test Lab — Python Bug‑Fixing & Pytest Practice
A hands‑on debugging project designed to simulate real junior‑engineer workflows.
This lab includes intentionally buggy Python functions, a full pytest test suite, and structured bug reports documenting the debugging process.
This project demonstrates:
Running and interpreting pytest test failures
Debugging logic, indexing, and type errors
Writing clear, reproducible bug reports
Fixing code incrementally with test‑driven feedback
Using Git and GitHub to publish a clean, professional project
Project Structure
beginner-test-lab/
│
├── buggy_script.py        # Contains intentionally buggy functions
├── tests/
│   ├── test_buggy_script.py
│   └── __init__.py
│
├── bug-reports/
│   ├── bug-report-01.md
│   ├── bug-report-02.md
│   └── bug-report-03.md
│
└── __init__.py
How to Run the Tests
Install pytest:
pip3 install pytest
Run the test suite:
pytest -v
You’ll see which functions pass, which fail, and why.
Bugs Identified & Fixed
1. `add_numbers`
Issue: Returned incorrect value
Fix: Corrected to a + b
Status: Passing
2. `get_first_item`
Issue: Returned the second item (items[1])
Fix: Updated to items[0]
Status: Passing
3. `format_name`
Issue: Used last.upper instead of last.upper()
Fix: Added parentheses
Status: Passing
4. `divide`
Issue: No zero‑division handling
Note: Current tests do not cover this case
Status: Passing for tested behavior
Why This Project Exists
This lab is designed to show:
How beginners can contribute meaningfully through testing and documentation
How to read error messages and trace failures
How to fix bugs one at a time with confidence
How to publish a clean, reproducible workflow on GitHub
It’s a small project, but it demonstrates real engineering habits.
Future Enhancements
Add divide‑by‑zero tests
Add type‑checking tests
Add more buggy
