import csv

# MAY BE A PROBLEM HERE WITH: ITER is ITER

def open_file(name='sample.csv'):

    try:
        with open(name) as csv_file:
            csv_reader = csv.DictReader(csv_file)

            for row in csv_reader:
                # yield row
                # print({key.strip():value.strip() for key, value in row.items()})
                yield {key.strip():value.strip() for key, value in row.items()}
    except Exception as e:
        print(f"Could not open {name}...")
        print(f"{type(e)}:{e}")

def sanctioned_individuals(name='sample.csv'):

    for dic in open_file(name):
        yield dic['Individuals']

def sanctioned_organizations(name='sample.csv'):

    for dic in open_file(name):
        yield dic['Organizations']

def sanctioned_countries(name='sample.csv'):
    for dic in open_file(name):
        yield dic['Countries']

def parsed_data_params():
    return ('Individuals','Countries','Organizations')