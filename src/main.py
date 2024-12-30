import json
from auth import get_bearer_token
from extractor import extract_permissions
from comparer import compare_permissions

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

def load_config(config_file):
    """Load configuration from file."""
    with open(config_file, "r") as file:
        return json.load(file)

def main():
    # Load configuration
    config = load_config("config/config.json")

    # Process each instance
    instance_files = []
    for instance in config["instances"]:
        print(f"Processing {instance['name']}...")
        
        # Step 1: Get token
        token = get_bearer_token(
            instance["base_url"],
            instance["client_id"],
            instance["client_secret"],
            instance["grant_type"],
            instance["username"],
            instance["password"]
        )

        # Step 2: Extract permissions
        output_file = f"data/{instance['name'].replace(' ', '_')}_permissions.csv"
        extract_permissions(instance["base_url"], token, output_file)
        instance_files.append(output_file)

    # Step 3: Compare permissions
    if len(instance_files) == 2:
        compare_permissions(instance_files[0], instance_files[1], "data/comparison_result.csv")
        print("Comparison completed. Check data/comparison_result.csv for results.")
    else:
        print("Comparison requires exactly 2 instances.")

if __name__ == "__main__":
    main()
