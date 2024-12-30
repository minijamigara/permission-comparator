import csv

def save_to_csv(data, file_path):
    """Save a list of dictionaries to a CSV file."""
    if not data:
        return

    keys = data[0].keys()
    with open(file_path, "w", newline="", encoding="utf-8") as output_file:
        dict_writer = csv.DictWriter(output_file, fieldnames=keys)
        dict_writer.writeheader()
        dict_writer.writerows(data)
