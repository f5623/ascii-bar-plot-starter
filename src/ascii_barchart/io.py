import csv

def load_rows(csv_path):
    rows = []
    with open(csv_path, "r", newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            rows.append((row["type"], float(row["value1"]), float(row["value2"])))
    return rows   