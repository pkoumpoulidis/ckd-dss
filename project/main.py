import dataset_parser as parser

DATASET='../datasets/chronic_kidney_disease_full.arff'
ATTR_LABELS='../datasets/attributes_labeling.csv'

# Load data array
data_array = parser.read_arff_data(DATASET)
# Load attribute information array
attribute_info_array = parser.read_labeling_data(ATTR_LABELS)
# Make Data Frame
data_frame = parser.make_dataframe(data_array, attribute_info_array)