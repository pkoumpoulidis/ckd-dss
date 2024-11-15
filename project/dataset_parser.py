import pandas as pd

# Read data from a file and return the contents as a 2-dimensional array
def read_arff_data(data_path):
    data_array = []
    # Open file for reading
    with open(data_path, 'r') as file:
        for row in file:
            # Remove whitespaces
            stripped_line = row.strip()
            # Ignore lines starting with % or @ (comments/metadata)
            if not stripped_line: continue
            if stripped_line.startswith('%'): continue
            if stripped_line.startswith('@'): continue

            # Split each line(row) to columns
            columns = stripped_line.split(',')
            # Check for empty columns
            valid_columns = []
            for column in columns:
                if column != '': valid_columns.append(column)

            data_array.append(valid_columns)

    return data_array

# Read attribute labels a file and return the contents as a 2-dimensional array
def read_labeling_data(labeling_path):
    attribute_labels = []
    # Open file for reading
    with open(labeling_path, 'r') as file:
        for row in file:
            # Remove whitespaces
            stripped_line = row.strip()

            #Split each line(row) to columns
            columns = stripped_line.split(',')
            attribute_labels.append(columns)

    return attribute_labels

def make_dataframe(data_array, attribute_info_array):
    data_frame = pd.DataFrame(data_array, columns= [row[1] for row in attribute_info_array])

    # Assign attributes their data types :
    for label in attribute_info_array:
        abbr = label[1]
        attr_type = label[2]
        # Parse numeric values
        if attr_type == 'Float64' or attr_type == 'Int64':
            data_frame[abbr] = data_frame[abbr].apply(pd.to_numeric, errors='coerce')
            data_frame[abbr] = data_frame[abbr].astype(attr_type)
        # Parse categorical values
        else:
            nominal_values = label[3].split('/')
            data_frame[abbr] = data_frame[abbr].astype(pd.CategoricalDtype(categories=nominal_values, ordered=True))


    # Rename attributes providing full description
    # data_frame = rename_attributes(data_frame, attribute_info_array)

    return data_frame

# Rename attributes providing full description
def rename_attributes(data_frame, attribute_info_array):
    attribute_labels = []
    for label in attribute_info_array:
        attribute_title = f'{label[0]} ({label[1]})'
        attribute_labels.append(attribute_title)

    data_frame.columns = attribute_labels
    return data_frame