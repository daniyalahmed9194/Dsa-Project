import math
def clean_numeric_value(value, column):
    # Remove 'Rs.' and commas, and convert the string to a float
    if(column==1):
        try:
            # Strip the currency symbol and commas, then convert to float
            cleaned_value = float(value.replace('Rs.', '').replace(',', '').strip())
        except ValueError:
            # Handle the case where the value cannot be converted (optional)
            cleaned_value = 0.0  # Default value for invalid entries
        return cleaned_value
    elif (column==2):
        try:
            cleaned_value = int(value*10)
        except ValueError:
            cleaned_value = 0
        return cleaned_value
    elif (column==3):
        try:
            if (value=='No discount'):
                cleaned_value = 0
            else:
                cleaned_value = float(value.replace('%', '').replace('Off', '').strip())
        except ValueError:
            cleaned_value = 0.0  # Default value for invalid entries
        return cleaned_value
    elif (column==5):
        cleaned_value = value.replace('sold', '').strip()
    
        try:
            # Check if it ends with 'K' for thousands
            if cleaned_value.endswith('K'):
                # Convert to float and multiply by 1000
                cleaned_value = float(cleaned_value[:-1]) * 1000  
            else:
                # Convert directly to float
                cleaned_value = float(cleaned_value)
        except ValueError:
            # Handle cases where conversion fails
            cleaned_value = 0.0
        cleaned_value = math.floor(cleaned_value)
        return cleaned_value
    else:
        return value