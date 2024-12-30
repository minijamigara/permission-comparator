# performance-comparator

## Description

Permissions Comparator is a Python-based tool designed to extract, compare, and analyze user role permissions across two instances. The tool generates structured CSV files for each instance and identifies differences in permissions, including the source of the differences.

## Features

Extract permissions from two instances using API endpoints.

Normalize and preprocess data for accurate comparison.

Compare CSV files to identify differences (Instance 1 or Instance 2).

Generate outputs in a consistent format with the correct column order.

## Technologies Used

Python

Pandas

Requests

Prerequisites

Python 3.x

Pip (for managing dependencies)

## Installation

1. **Clone the repository:**

   ```bash
   git clone <repository-url>

2. Navigate to the project directory:

    ```bash
    cd permissions-comparator

3. Install dependencies:

    ```bash
    pip install -r requirements.txt

4. Configuration

    Set up the config.json file with the required instance details:

        {
          "instance_1": {
            "base_url": "https://instance1-url", 
            "client_id": "your_client_id", 
            "client_secret": "your_client_secret", 
            "username": "your_username",
            "password": "your_password" 
          }, 
          "instance_2": { 
            "base_url": "https://instance2-url", 
            "client_id": "your_client_id", 
            "client_secret": "your_client_secret", 
            "username": "your_username", 
            "password": "your_password" 
          }
        }

5. Adjust the desired_order of columns in the comparison output (if needed):

    desired_order = ["Role Name", "Employee Actions", "Workflows", "Data Groups"]

6. Usage

   **Run the application:**

    ```bash
    python src/main.py

7. Outputs generated:

      instance_1.csv: Permissions data for Instance 1.
      
      instance_2.csv: Permissions data for Instance 2.
      
      comparison_result.csv: Differences between the two instances, including a source column.

## Folder Structure ##

permissions-comparator / <br> 
src/ <br>
├── main.py <br>
│   ├── auth.py <br>
│   ├── extractor.py <br>
│   ├── comparator.py <br>
├── config.json <br>
├── requirements.txt <br>
├── README.md <br>

**Known Issues**

  1. Ensure that the API credentials and instance URLs are correct in the config.json file.
  
  2. Differences are identified row-by-row, so changes in the order of rows may appear as differences.

## Contributing ##

- Contributions are welcome! Please follow these steps:

- Fork the repository.

- Create a new branch for your feature or bug fix:

- git checkout -b feature-or-bugfix-name

- Commit your changes:

    -- git commit -m "Description of changes"

    -- Push to your fork:

    -- git push origin feature-or-bugfix-name

    -- Submit a pull request.

**Contact**

  For issues or feature requests, please open an issue in the repository or contact the maintainer at [minija@orangehrm.com].
