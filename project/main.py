import dataset_parser as parser
import plots
DATASET='../datasets/chronic_kidney_disease_full.arff'
ATTR_LABELS='../datasets/attributes_labeling.csv'

# PARSING DATA

# Load data array
data_array = parser.read_arff_data(DATASET)
# Load attribute information array
attribute_info_array = parser.read_labeling_data(ATTR_LABELS)


# DATA FRAME

# Make Data Frame
data_frame = parser.make_dataframe(data_array, attribute_info_array)


# PLOTTING

# Make a plotly table and display it
#table = plots.get_data_table(data_frame)
#table.show()

#histogram = plots.get_attribute_histogram(data_frame, 'wbcc')
#histogram.show()