from functions import *

def secondary_pallete(colors, fixed_color):
    updated_colors = []
    for color in colors:
        # Remove the '#' symbol
        color = color.lstrip('#')

        # Convert hexadecimal colors to integers
        color_int = int(color, 16)
        fixed_color_int = int(fixed_color, 16)

        # Perform addition
        result_int = color_int + fixed_color_int

        # Ensure the result is within the valid range of 0-FFFFFF
        result_int = min(result_int, 0xFFFFFF)
        result_int = max(result_int, 0)

        # Convert the result back to hexadecimal
        result_hex = '#' + hex(result_int)[2:].zfill(6).upper()

        updated_colors.append(result_hex)

    return updated_colors

# Example usage
fixed_color = '222222'

secondary_color = secondary_pallete(color, fixed_color)
print(secondary_color)

