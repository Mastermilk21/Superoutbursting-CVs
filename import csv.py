import csv

input_file = 'C:\\Users\\eitan\\code repos\\notebook\\pythonProject4\\matched_transients_coords.csv'
output_file = 'matched_transient_coords_no_duplicates.csv'

seen = set()
cleaned_rows = []

with open(input_file, newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        key = (row['name'], row['RA'], row['Dec'])
        if key not in seen:
            seen.add(key)
            cleaned_rows.append(row)

with open(output_file, 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=['name', 'RA', 'Dec'])
    writer.writeheader()
    writer.writerows(cleaned_rows)

print(f"Done! {len(cleaned_rows)} unique rows saved to {output_file}")
