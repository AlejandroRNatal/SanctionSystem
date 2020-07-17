import asyncio, os, sys

# import ./Sanction as sanction
from Sanction import is_sanctioned
import sanctioned_data_parser

from sanctioned_data_parser import open_file


def row_to_list(row):
    return [row['Individuals'],row[' Countries'], row[' Organizations']]


def debug(db_name="sample.csv"):
    '''Main input loop for verifying if provided argument is sanctioned or not.'''
    import os.path

    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(BASE_DIR, db_name)

    names = []

    for row in open_file(db_path):

        for a in row_to_list(row):

            names.append(a)

    input_ln =''
    while True and input_ln.lower().strip() != 'quit':

        input_ln = input('\nEnter name to view if sanctioned(\'quit\' to exit shell):').strip()

        if input_ln and input_ln !='quit':
            cl_input = input_ln[:].lower()# done to avoid modifying OG string
            if is_sanctioned(name=cl_input, sanctioned_names=names)[0]:
                print(f'[!]HIT:{input_ln} with percentage {is_sanctioned(sanctioned_names=names, name=cl_input)[1]}\n')
            else:
                print(f'No Hit:{input_ln} with percentage {is_sanctioned(sanctioned_names=names, name=cl_input)[1]}\n')
    return

if __name__ == "__main__":
    # asyncio.run(main_loop())
    debug()