# 🎭 Playwright & Python End-to-End Automation Framework

An End-to-End (E2E) Test Automation Framework built with Python, Playwright and Pytest. Designed using practices to deliver fast, reliable, and isolated test execution for modern web applications.

## 📋 Key Architectural Highlights

* **Page Object Model (POM):** Strict separation between page elements/interactions and test scripts for maximum maintainability.

* **AAA Pattern:** All tests strictly adhere to the **Arrange-Act-Assert** structure for clarity and readability.

* **Network Interception & API Mocking:** Simulates edge-case backend behavior and server errors (e.g., HTTP 500) through Playwright's native routing capabilities without external mocks.

* **Automated CI/CD Pipeline:** Fully integrated GitHub Actions workflow running headless tests on every push and pull request.

* **Automatic Retries:** Configured flaky test resilience using `pytest-rerunfailures` for unstable environment handling.

## 📁 Repository Structure

```
.
├── .github/
│   └── workflows/
│       └── playwright.yml         # GitHub Actions CI/CD pipeline configuration
├── pages/                         # Page Object Model (POM) components
│   ├── base_page.py               # Base page with encapsulated generic actions
│   ├── login_page.py              # Authentication page locators & user actions
│   ├── inventory_page.py          # Post-authentication UI components
│   ├── cart_page.py               # Shopping cart management
│   └── checkout_page.py           # Shipping details & order completion flow
├── tests/                         # Test suites categorized by functionality
│   ├── test_auth.py               # Positive and negative authentication tests
│   ├── test_inventory.py          # Inventory UI & data validation
│   ├── test_checkout.py           # Full E2E checkout journey (Login -> Order Complete)
│   └── test_api_mocking.py        # Intercepted network edge cases
├── .gitignore                     # Git exclusion patterns
├── conftest.py                    # Global fixtures (browser context, page setup)
├── pytest.ini                     # Global Pytest settings, markers and timeouts
├── requirements.txt               # Python package dependencies
└── README.md                      # Project documentation

```

## ⚙️ Getting Started

### Prerequisites

Ensure you have the following installed locally:

* Python 3.11+

* pip (Python Package Installer)

* Git

### Installation

1. Clone the repository:

   ```
   git clone https://github.com/your-username/playwright-python-portfolio.git
   cd playwright-python-portfolio
   
   
   ```

2. Create and activate a virtual environment:

   ```
   # On macOS/Linux:
   python3 -m venv venv
   source venv/bin/activate
   
   # On Windows:
   python -m venv venv
   .\venv\Scripts\activate
   
   
   ```

3. Install dependencies:

   ```
   pip install -r requirements.txt
   
   
   ```

4. Install Playwright browsers and system dependencies:

   ```
   playwright install
   
   
   ```

## 🚀 Running Tests

### Standard Execution

Run the full test suite in headless mode:

```
pytest


```

### Run Tests in Headed Mode (Visual Inspection)

```
pytest --headed


```

### Parallel Execution

Run tests in parallel across all available CPU cores using `pytest-xdist`:

```
pytest -n auto


```

### Targeted Execution

```
# Run only checkout tests
pytest tests/test_checkout.py

# Run API mocking tests
pytest tests/test_api_mocking.py


```

## 🔄 CI/CD Pipeline Workflow

The repository includes a GitHub Actions pipeline (`.github/workflows/playwright.yml`) configured with:

1. Automated Triggers: Executes automatically on push and pull_request to main / master branches.

2. Environment Setup: Spins up an Ubuntu worker, installs Python dependencies, and provisions system-level browser requirements using `playwright install --with-deps`.

3. Execution: Automatically runs all Pytest suites in headless mode on a clean container.

## 🛠️ Key Engineering Decisions

| Feature | Solution | Impact | 
 | ----- | ----- | ----- | 
| Maintainability | Page Object Model (POM) encapsulation | Reduced code duplication and centralized locator updates. | 
| Flaky Test Reduction | Auto-retrying web assertions (`expect`) | Replaced hardcoded `time.sleep` calls with event-driven dynamic polling. | 
| Resilience Testing | Native page.route network interception | Allowed simulating backend failures (HTTP 500) without changing server state. | 
| CI Automation | Isolated GitHub Actions Linux runner | Guaranteed consistent test execution across independent environments. | 

## 📄 License

Distributed under the MIT License. See `LICENSE` for more information.