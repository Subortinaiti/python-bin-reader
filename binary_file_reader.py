filename = input("Write the name of the file to open > ")
linelength = 32
invalid_placeholder = "*"



def print_formatted(hex_buffer, ascii_str):
    halves = split_string_in_half(ascii_str)
    print(halves[0] + " | " + hex_buffer + " | " + halves[1])



def split_string_in_half(input_string):
    middle = len(input_string) // 2
    

    first_half = input_string[:middle]
    second_half = input_string[middle:]
    

    return (first_half, second_half)

try:
    with open(filename, 'rb') as file:
        byte = file.read(1)
        count = 0
        hex_buffer = ""
        ascii_buffer = ""

        while byte:
            byte_hex = byte.hex()
            hex_buffer += f"{byte_hex} "
            count += 1

            if count == linelength:
                ascii_str = "".join([char if 32 <= ord(char) <= 126 else invalid_placeholder for char in ascii_buffer])

                print_formatted(hex_buffer, ascii_str)
                ascii_buffer = ""
                hex_buffer = ""
                count = 0
            else:
                ascii_char = byte.decode('ascii', errors='replace')
                ascii_buffer += ascii_char

            byte = file.read(1)

        if ascii_buffer:
            ascii_str = "".join([char if 32 <= ord(char) <= 126 else invalid_placeholder for char in ascii_buffer])

            print_formatted(hex_buffer, ascii_str)

except FileNotFoundError:
    print(f"File '{filename}' not found.")
except Exception as e:
    print(f"An error occurred: {e}")

input()
