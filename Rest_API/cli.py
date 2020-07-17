import asyncio, os, sys

# import ./Sanction as sanction
from Sanction import is_sanctioned

# async def input_loop():
#     yield input("Provide name to verify sanction status:")

# def main_loop():

#     curr = ''
#     while curr.strip() != 'quit':
#         #ask our input here
#         curr = await input_loop()
#         if curr and curr !='quit':
#             cl_input = input_ln[:].lower()# done to avoid modifying OG string
#             if is_sanctioned(name=cl_input)[0]:
#                 print(f'[!]HIT:{input_ln} with percentage {is_sanctioned(name=cl_input)[1]}\n')
#             else:
#                 print(f'No Hit:{input_ln} with percentage {is_sanctioned(name=cl_input)[1]}\n')
#     return


def debug():
    '''Main input loop for verifying if provided argument is sanctioned or not.'''
    
    input_ln =''
    while True and input_ln.lower().strip() != 'quit':

        input_ln = input('\nEnter name to view if sanctioned(\'quit\' to exit shell):').strip()

        if input_ln and input_ln !='quit':
            cl_input = input_ln[:].lower()# done to avoid modifying OG string
            if is_sanctioned(name=cl_input)[0]:
                print(f'[!]HIT:{input_ln} with percentage {is_sanctioned(name=cl_input)[1]}\n')
            else:
                print(f'No Hit:{input_ln} with percentage {is_sanctioned(name=cl_input)[1]}\n')
    return

if __name__ == "__main__":
    # asyncio.run(main_loop())
    debug()