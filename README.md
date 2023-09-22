# IDS706 Mini Project 4
## Requirements

- Set up a GitHub Actions workflow.
- Test across at least 3 different Python versions.

## GitHub Actions Workflow

The GitHub Actions workflow is configured to run on every push and pull request to the `main` branch. It tests the code across three different Python versions: 3.8, 3.x (latest stable release), and 3.11, on both Ubuntu and Windows.

### Workflow Steps

1. **Checkout Code**: Checks out the repository code.
2. **Set up Python**: Sets up the specified Python version.
3. **Cache Python Packages**: Caches Python packages for faster workflow runs.
4. **Install Packages**: Installs the required packages specified in the `Makefile`.
5. **List Installed Packages**: Lists all installed Python packages.
6. **Lint**: Runs linting using the commands specified in the `Makefile`.
7. **Test**: Runs the tests using `pytest`.
8. **Format**: Formats the code using the commands specified in the `Makefile`.

