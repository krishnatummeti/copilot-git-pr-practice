# copilot-git-pr-practice

# GitHub Copilot — Git & Pull Request Practice

A small Python calculator project for learning a complete development workflow using GitHub Copilot, VS Code, and the GitHub website.

## Project Structure

```text
calculator.py
test_calculator.py
README.md
```

## Features

- Add two numbers using `add(a, b)`.
- Divide two numbers using `divide(a, b)`.
- Raise `ValueError("Cannot divide by zero")` when the divisor is zero.
- Verify the behaviour with unit tests.

## Run the Tests

From the project folder, run:

```bash
python -m unittest -v
```

If your Python installation uses `python3`, use:

```bash
python3 -m unittest -v
```

The practice session completed with three passing tests:

1. Addition.
2. Division.
3. Division by zero.

## Tools Used

- VS Code for editing files and managing Git changes.
- GitHub Copilot for reviewing code, making focused changes, and suggesting commit messages.
- GitHub website for creating, reviewing, approving, and merging the pull request.

## Workflow Practised

### 1. Create a Feature Branch

Created and switched to:

```text
feature/add-calculator
```

Copilot prompt:

```text
Create and switch to a branch named feature/add-calculator.
Preserve all existing changes.
Do not edit files, commit, or push.
Ask before running commands. Keep your response short.
```

### 2. Add the Calculator and Tests

Created:

- `calculator.py`
- `test_calculator.py`

### 3. Review the Code with Copilot

Attached the two files to Copilot Chat and used:

```text
Review only these two files for bugs and missing tests.
Return at most 3 short findings.
Do not edit files, run commands, commit, or push.
```

### 4. Make a Focused Improvement

Chose explicit division-by-zero handling and requested:

```text
Update only calculator.py and test_calculator.py:
- Make divide(a, 0) raise ValueError("Cannot divide by zero").
- Add one unittest that checks this behavior.
- Keep all existing tests.
Show the diff for review.
Do not run commands, commit, or push.
Keep your explanation short.
```

### 5. Run the Tests

Copilot prompt:

```text
Run python -m unittest -v.
Ask for permission before running it.
Do not edit files, commit, or push.
Report only the test result and any errors.
```

Reported result: three tests passed with no errors.

### 6. Stage and Commit in VS Code

1. Opened Source Control.
2. Inspected the file changes.
3. Staged the intended files using the `+` button.
4. Used Copilot's commit-message generation button.
5. Reviewed the message and committed.

Commit message:

```text
Add calculator functions and corresponding unit tests
```

### 7. Publish the Branch

Used **Publish Branch** in VS Code to upload the committed changes to GitHub.

### 8. Create the Pull Request on GitHub

Created the PR manually on the GitHub website:

- Base branch: `main`
- Compare branch: `feature/add-calculator`

PR title:

```text
Add calculator functions and corresponding unit tests
```

### 9. Review and Approve

Used a second GitHub account to practise the reviewer role.

Review workflow:

1. Open the PR.
2. Select **Files changed**.
3. Inspect the changes.
4. Select **Review changes**.
5. Choose the appropriate review outcome.
6. Submit the review.

The second account simulated a reviewer for this exercise; it was not an independent review by another person.

Copilot feedback and a submitted GitHub review are separate: Copilot can help inspect code, while the reviewer decides what feedback or approval to submit.

### 10. Merge the Pull Request

Approved and merged the PR into `main`.

### 11. Update Local Main After Merging

After merging, switch to `main` in VS Code and pull the latest changes.

Reusable Copilot prompt:

```text
Switch to main and pull its latest changes from origin.
If there are uncommitted changes, stop and tell me.
Ask before running commands.
Do not edit or delete files.
Keep the response short.
```

## Copilot Usage Preferences

- Give Copilot one focused task at a time.
- Provide only relevant files or changes.
- Request short responses.
- Use VS Code buttons for routine Git actions when convenient.
- Review generated code and commit messages.
- Run tests before committing.
- Do not allow automatic commits or pushes unless intended.

## Completed Practice

- [x] Create a feature branch.
- [x] Add calculator functions and unit tests.
- [x] Review the files with Copilot.
- [x] Add explicit division-by-zero handling.
- [x] Run the tests successfully.
- [x] Generate a commit message with Copilot.
- [x] Commit and publish the branch.
- [x] Create a PR manually on GitHub.
- [x] Practise approval using a second account.
- [x] Merge the PR.

## Learning Goal

Understand each step of a small-change development workflow while using Copilot as a helper—not as a replacement for checking code, tests, and review feedback.