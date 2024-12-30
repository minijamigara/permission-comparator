'''
import pandas as pd

def compare_permissions(file1, file2, output_file):
    """Compare two CSV files and output the differences."""
    df1 = pd.read_csv(file1)
    df2 = pd.read_csv(file2)

    # Compare the DataFrames
    comparison = pd.concat([df1, df2]).drop_duplicates(keep=False)
    comparison.to_csv(output_file, index=False)
'''

import pandas as pd
import json

def flatten_json(json_obj):
    """Flatten nested JSON objects for consistent comparison."""
    flat = {}
    def recurse(curr, parent_key=''):
        if isinstance(curr, dict):
            for k, v in curr.items():
                recurse(v, f"{parent_key}.{k}" if parent_key else k)
        elif isinstance(curr, list):
            for i, v in enumerate(curr):
                recurse(v, f"{parent_key}[{i}]")
        else:
            flat[parent_key] = curr
    recurse(json_obj)
    return flat

def normalize_json_with_flatten(json_str):
    """Normalize JSON-like strings by flattening and sorting keys."""
    try:
        normalized = json.dumps(flatten_json(json.loads(json_str)), sort_keys=True)
        print(f"Normalized JSON: {normalized}")  # Debugging point
        return normalized
    except (TypeError, json.JSONDecodeError):
        stripped_str = str(json_str).strip()
        print(f"Non-JSON string normalized: {stripped_str}")  # Debugging point
        return stripped_str

def preprocess_dataframe(df):
    """Normalize and clean the DataFrame for accurate comparison."""
    df = df.astype(str).fillna("NULL")  # Convert all data to strings and handle NaNs
    print(f"DataFrame before preprocessing:\n{df.head()}")  # Debugging point
    for col in df.columns:
        df[col] = df[col].apply(normalize_json_with_flatten).str.strip().str.lower()  # Normalize JSON and strings
    print(f"DataFrame after preprocessing:\n{df.head()}")  # Debugging point
    return df

def compare_permissions(file1, file2, output_file):
    """Compare two CSV files and output the differences."""
    # Desired column order
    desired_order = ["Role Name", "Employee Actions", "Workflows", "Data Groups"]

    # Load the files
    df1 = pd.read_csv(file1)
    df2 = pd.read_csv(file2)

    print(f"File 1 loaded:\n{df1.head()}")  # Debugging point
    print(f"File 2 loaded:\n{df2.head()}")  # Debugging point

    # Synchronize column structures
    common_columns = list(set(df1.columns) & set(df2.columns))
    print(f"Common columns: {common_columns}")  # Debugging point
    df1 = df1[common_columns]
    df2 = df2[common_columns]

    # Ensure the desired column order is respected
    df1 = df1.reindex(columns=desired_order)
    df2 = df2.reindex(columns=desired_order)

    print(f"File 1 after reordering:\n{df1.head()}")  # Debugging point
    print(f"File 2 after reordering:\n{df2.head()}")  # Debugging point

    # Preprocess both DataFrames
    df1 = preprocess_dataframe(df1)
    df2 = preprocess_dataframe(df2)

    # Sort the DataFrames
    df1 = df1.sort_values(by=desired_order).reset_index(drop=True)
    df2 = df2.sort_values(by=desired_order).reset_index(drop=True)

    print(f"DataFrame 1 after sorting:\n{df1}")  # Debugging point
    print(f"DataFrame 2 after sorting:\n{df2}")  # Debugging point

    # Compare the DataFrames
    differences = pd.concat([df1, df2]).drop_duplicates(keep=False)
    print(f"Row-by-row differences:\n{differences}")  # Debugging point

    # Save the differences to a file with the correct column order
    if not differences.empty:
        differences = differences.reindex(columns=desired_order)  # Ensure correct column order
        differences.to_csv(output_file, index=False)
        print(f"Differences saved to {output_file} in correct column order")
    else:
        print("No differences found.")

# Example usage
# compare_permissions("file1.csv", "file2.csv", "differences.csv"

