import csv
import json

# Load the spec file
with open('spec.json', 'r') as spec_file:
    spec = json.load(spec_file)

column_names = spec["ColumnNames"]
offsets = list(map(int, spec["Offsets"]))
encoding = spec["FixedWidthEncoding"]
include_header = spec["IncludeHeader"] == "True"


def parse_fixed_width_line(line):
    """Parse a single line of fixed-width data based on the specified offsets."""
    fields = []
    start = 0
    for width in offsets:
        field = line[start:start + width].rstrip()  # Extract the field and strip trailing spaces
        fields.append(field)
        start += width
    return fields


def fixed_width_to_csv(input_filename, output_filename):
    """Convert a fixed-width file to a CSV file."""
    with open(input_filename, 'r', encoding=encoding) as infile, open(output_filename, 'w', newline='',
                                                                      encoding='utf-8') as outfile:
        csv_writer = csv.writer(outfile)
        header_written = False

        # Iterate over each line in the input file
        for line in infile:
            line = line.rstrip()  # Strip trailing newlines or spaces

            # Write header only once
            if include_header and not header_written:
                csv_writer.writerow(column_names)
                header_written = True

            # Only process non-empty lines
            if line:
                fields = parse_fixed_width_line(line)
                csv_writer.writerow(fields)


# Convert the fixed-width file to CSV
fixed_width_to_csv('fixed_width_file.txt', 'output_file.csv')

print("CSV file created successfully.")
