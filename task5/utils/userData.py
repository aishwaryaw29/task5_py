

def removeText(input_string):
    try:
        result = ''.join([char for char in input_string if char.isdigit()])
        
        return result
    
    except:
        return print(f'An error occurred.')


