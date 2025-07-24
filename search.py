import csv
" finds name, RA, Dec from a CSV file."
# Your list of transient names without the "AT" prefix
names = [
    "2018gum", "2018jms", "2018jro", "2018kjp", "2019aih", "2019bfd", "2019cjz",
    "2019bqk", "2019box", "2019dtv", "2019cow", "2019gac", "2019hlb", "2019gdy",
    "2019kli", "2019krj", "2019njr", "2019pzj", "2019nzq", "2019osp", "2019nwu",
    "2019tat", "2019slj", "2019ulv", "2019uwj", "2019zsi", "2020gbb", "2020ilw",
    "2020liy", "2020qit", "2020rtt", "2020aacy", "2021zf", "2021djx", "2021kei",
    "2021ife", "2021qut", "2021stc", "2021soz", "2021ageo", "2022eg", "2022pix",
    "2022vyq", "2023rt", "2023ekc", "2023dvq", "2023iwl", "2023xnf", "2023zyb",
    "2024mu", "2024re", "2024cco", "2024ggu", "2024nsz", "2024rwq", "2024agoe"
]

# Prepend "AT" to each name to get the full transient name
full_names = [f"AT{name}" for name in names]

input_filename = r'c:\Users\eitan\Downloads\count_transients.txt'
output_filename = 'matched_transients_coords.csv'

results = []

with open(input_filename, "r", encoding="utf-8") as file:
    for line in file:
        parts = line.strip().split()
        # Check that line has at least 8 columns (adjust if needed)
        if len(parts) < 8:
            continue
        ra = parts[1]
        dec = parts[2]
        name_in_line = parts[7]
        if name_in_line in names:
            results.append({"name": name_in_line, "RA": ra, "Dec": dec})

# Write all matches to CSV
with open(output_filename, "w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=["name", "RA", "Dec"])
    writer.writeheader()
    writer.writerows(results)

print(f"✅ Done! Saved {len(results)} entries to {output_filename}")
