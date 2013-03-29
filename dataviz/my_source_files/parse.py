import csv

MY_FILE = "../data/sample_sfpd_incident_all.csv"

def parse(csv_file, delimiter):
    """ Turn a CSV file into a JSON-like object"""
    with open(csv_file) as opened_file:
        csv_data = csv.reader(opened_file, delimiter=delimiter)
        # csv_data is a generator
        fields = csv_data.next()
        parsed_data = [dict(zip(fields, row)) for row in csv_data]
    return parsed_data

def main():
    print parse(MY_FILE, ",")

if __name__ == "__main__":
    main()
