def number_to_words(number):
    digit_map = {
        '0': 'Zero', '1': 'One', '2': 'Two', '3': 'Three', '4': 'Four',
        '5': 'Five', '6': 'Six', '7': 'Seven', '8': 'Eight', '9': 'Nine'
    }
    
    return ' '.join(digit_map[digit] for digit in str(number))
print(number_to_words(125))  
