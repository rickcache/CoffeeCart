##Coffee Cart Automation Project with Selenium + Pytest

This is an automation testing project for the Coffee Cart web application using Selenium and Pytest.

This includes automated tests for:

Adding multiple products to the cart

Checkout process with form submission

The reporting is implemented using pytest-html and allure, with screenshots captured for failures and logs for tracking each procedure.
## Installation

1. Clone the repository:

```bash
git clone https://github.com/rick/CoffeeCart.git
```
2. Navigate to the project folder:  

```bash
cd CoffeeCart
```
3. Create and activate a virtual environment (optional but recommended):
```bash
python -m venv .venv
.venv\Scripts\activate  # Windows
source .venv/bin/activate  # macOS/Linux

```
4. Install required packages:
```bash
pip install -r requirements.txt
```
5.Run tests:
```bash
pytest -v -s
```
6. Generate HTML report:
```bash
pytest --html=report.html -v -s
```
7. Generate Screenshots
```bash
pytest -v -s --self-contained-html
```
##Features

-Add-To-Cart: Add multiple coffee products to the cart

-Checkout: Fill name, email, accept promotions, and submit order
## Reporting

HTML Report: report.html

Screenshots: Captured automatically for test failures

Logs: test_log.log contains detailed test execution logs
## Notes
This project is primarily for learning, practice, and portfolio showcase purposes.

You can clone and modify it for your own practice projects.

The Coffee Cart website may update periodically, so selectors or test data might need refreshing.
## Author

- [@iamrexx](https://www.github.com/iamrexx)

Key points:

Covers adding multiple products and validating cart

Automated checkout form testing with user input

Detailed logging and reporting for test outcomes