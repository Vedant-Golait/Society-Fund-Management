# User Data Management Application

## Description
This is a Python-based desktop application for managing user data and financial transactions. It provides a graphical user interface (GUI) for performing various operations such as adding new users, viewing user details, managing transactions, and handling capital funds.

## Features
- User Management:
  - Add new users
  - View user details
  - Edit user information
  - Delete user accounts
- Financial Operations:
  - Add or remove funds from user accounts
  - View transaction history
- Capital Fund Management:
  - View and edit capital fund details
  - Track capital fund transactions
- Dashboard:
  - Display recent transactions
  - Show all users

## Requirements
- Python 3.x
- Tkinter library (usually comes pre-installed with Python)

## Installation
1. Ensure you have Python 3.x installed on your system.
2. Clone this repository or download the source code.
3. No additional package installation is required as the application uses standard Python libraries.

## Usage
1. Run the script using Python.
2. The main dashboard will appear, showing recent transactions and providing access to various functions through buttons.
3. Use the buttons to navigate between different features of the application.

## File Structure
- `user_management_app.py`: The main Python script containing the application code.
- `user_data/`: Directory where individual user data files are stored (created automatically).
- `Capital/`: Directory for storing capital fund transaction data.

## Functions
- `UserManagementApp`: Main class handling the application logic and GUI.
- `show_all_users()`: Displays all registered users.
- `view_user()`: Shows detailed information for a selected user.
- `create_new_user_session()`: Interface for adding a new user.
- `add_remove_funds()`: Interface for crediting or debiting user accounts.
- `show_capital_funds()`: Displays and manages capital fund information.

## Data Storage
- User data is stored in individual JSON files within the `user_data` directory.
- Capital fund transactions are stored in a JSON file in the `Capital` directory.

## Notes
- This application is designed for local use and does not include network capabilities or advanced security features.
- Ensure proper backup of the data directories to prevent data loss.

## Contributing
Contributions to improve the application are welcome. Please follow standard coding practices and provide documentation for any new features or changes.

## License
This project is licensed under the [MIT License](LICENSE).

# Support
Email id - vedantgolait04@gmail.com

# Buy me a Book
https://www.buymeacoffee.com/Vedant.Golait
