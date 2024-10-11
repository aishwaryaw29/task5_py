

from utils.userData import removeText
from utils.calDate import custom_date_formatter

def main():

    user_input = input('Enter a string with text and numbers: ')
    result = removeText(user_input)
    print(f'Numerical data: {result}')

    print()
    date_input = input('Enter a date (yyyy-mm-dd or mm-dd-yyyy): ')
    formatted_date = custom_date_formatter(date_input)
    print(f'Formatted date (dd-mm-yyyy): {formatted_date}')


if __name__ == '__main__':
    main()

