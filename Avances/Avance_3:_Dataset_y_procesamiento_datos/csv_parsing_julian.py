import csv

CSV_DATA_FILENAME = 'data_read.csv'
CSV_LABELED_DATA_FILENAME = 'training_data.csv'

COMPLIMENT_ROW = 1
QUESTION_ROW   = 2
OTHER_ROW 	   = 3

COMPLIMENT_LABEL = 'elogio'
QUESTION_LABEL 	 = 'pregunta'
OTHER_LABEL 	 = 'otro'

with open(CSV_DATA_FILENAME, newline = '') as csvDataFile:
	with open(CSV_LABELED_DATA_FILENAME,'w') as csvLabeledDataFile:
		csvReader = csv.reader(csvDataFile)
		csvReader.__next__() # skip header line
		for row in csvReader:
			csvLabeledDataFile.write('"' + row[COMPLIMENT_ROW] + '"' + ','
									 + COMPLIMENT_LABEL + '\n')
			csvLabeledDataFile.write('"' + row[QUESTION_ROW] + '"' + ','
									 + QUESTION_LABEL + '\n')
			csvLabeledDataFile.write('"' + row[OTHER_ROW] + '"' + ','
									 + OTHER_LABEL + '\n')
