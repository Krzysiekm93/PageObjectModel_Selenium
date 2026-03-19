# Page Object Model with Selenium & Python

This repository contains a test automation framework built with Python and Selenium. It implements the **Page Object Model (POM)** design pattern to enhance test maintenance, improve readability, and reduce code duplication.

## 📂 Project Structure

- **`pages/`** - Contains the Page classes. Each class represents a web page (or a component) and encapsulates its web elements (locators) and interaction methods.
- **`tests/`** - Contains the actual test cases that use the page objects to perform actions and assert outcomes.
- **`utils/`** - Contains helper functions, custom utilities, and WebDriver configuration (e.g., base test classes, browser setup).
- **`test_data/`** - Holds test data files (such as JSON, CSV, or Excel) used to drive data-driven tests.
- **`requirements.txt`** - Lists all the Python dependencies required to run the framework.

## 🚀 Prerequisites

- Python 3.x installed
- A package manager like `pip`
- Supported Web Browsers (e.g., Chrome, Firefox)

## 🛠️ Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Krzysiekm93/PageObjectModel_Selenium.git
   cd PageObjectModel_Selenium
   ```

2. **Create a virtual environment (Recommended):**
   ```bash
   python -m venv venv
   # On macOS/Linux:
   source venv/bin/activate
   # On Windows:
   venv\Scripts\activate
   ```

3. **Install the required dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

## 🧪 Running Tests

Depending on your test runner (e.g., `pytest` or `unittest`), you can typically run the tests from the root directory by executing:

```bash
pytest tests/
```