import json
import random
import string

# Load the spec file
with open('spec.json', 'r') as spec_file:
    spec = json.load(spec_file)

column_names = spec["ColumnNames"]
offsets = list(map(int, spec["Offsets"]))
encoding = spec["FixedWidthEncoding"]
include_header = spec["IncludeHeader"] == "True"


def generate_random_string(length):
    """Generate a random string of a given length, truncated or padded with spaces if needed."""
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))[:length].ljust(length)


def generate_sample_data(num_rows):
    """Generate sample data based on the given offsets."""
    data = []
    for _ in range(num_rows):
        row = [generate_random_string(width) for width in offsets]
        data.append(row)
    return data


def format_row(row):
    """Format a row into fixed-width string based on the offsets."""
    return "".join(field[:width].ljust(width) for field, width in zip(row, offsets))


def write_fixed_width_file(filename, sample_data):
    """Write sample data to a fixed-width file with the specified encoding."""
    with open(filename, 'w', encoding=encoding) as file:
        if include_header:
            header = format_row(column_names)
            file.write(header + '\n')

        for data_row in sample_data:
            formatted_row = format_row(data_row)
            file.write(formatted_row + '\n')


# Generate sample data with 5 rows
sample_data = generate_sample_data(5)

# Write the sample data to the fixed-width file
write_fixed_width_file('fixed_width_file.txt', sample_data)

print("Fixed-width file with sample data created successfully.")
