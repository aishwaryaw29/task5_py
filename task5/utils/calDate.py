

import re

def custom_date_formatter(date_string):

    if re.match(r'^\d{4}-\d{2}-\d{2}$', date_string):
        date_parts = date_string.split('-')
        return date_parts[2] + '-' + date_parts[1] + '-' + date_parts[0]
                
    elif re.match(r'^\d{2}-\d{2}-\d{4}$', date_string):
        date_parts = date_string.split('-')
        return date_parts[1] + '-' + date_parts[0] + '-' + date_parts[2]
                
    else:
        return 'Inavalid date format. Please use (yyyy-mm-dd or mm-dd-yyyy) format only.'
    









