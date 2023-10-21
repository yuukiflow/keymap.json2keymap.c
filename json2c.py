import json
import argparse
import re

def generate_c_code(json_file_path, new_layer_names):
    with open(json_file_path, 'r') as json_file:
        config = json.load(json_file)

    # Extract the part of the existing code after the keymaps declaration
    c_code = ""
    
    # Generate the new keymaps section using the JSON data
    for i, layer_name in enumerate(new_layer_names):
        if i < len(config["layers"]):
            c_code += f'  [{layer_name}] = LAYOUT('
            for key in config["layers"][i]:
                c_code += f'{key}, '
            c_code = c_code[:-2]  # Remove the trailing comma and space
            c_code += '),\n'

    return c_code

def replace_keymaps_in_c_file(c_file_path, new_keymaps_content):
    # Read the existing C file
    with open(c_file_path, 'r') as file:
        file_contents = file.read()

    # Define a regular expression pattern for matching the keymaps section
    keymaps_pattern = re.compile(r"(const uint16_t PROGMEM keymaps\[\]\[MATRIX_ROWS\]\[MATRIX_COLS\] = {)(.*?)(};)", re.DOTALL)

    # Search for the keymaps section in the file
    match = keymaps_pattern.search(file_contents)

    if match:
        # Replace only what's inside the {} with the new content
        updated_contents = file_contents.replace(match.group(2), '\n' + new_keymaps_content)

        # Write the updated contents back to the file
        with open(c_file_path, 'w') as file:
            file.write(updated_contents)
        print("Keymaps section content replaced successfully.")
    else:
        print("Keymaps section not found in the file.")


# Exam
def main():
    parser = argparse.ArgumentParser(description="Convert JSON file to keymap.c file")
    parser.add_argument("json_file", help="Path to the JSON file")
    parser.add_argument("c_file", help="Path to the output C file")
    parser.add_argument("--new_layers", nargs='+', help="New layer names", required=True)

    args = parser.parse_args()

    # Generate the new C code, replacing the keymaps section
    c_code = generate_c_code(args.json_file, args.new_layers)
    print(c_code)
    # Save the resulting code back to the file
    replace_keymaps_in_c_file(args.c_file, c_code)

    print(f"C code generated and saved to {args.c_file}")

if __name__ == "__main__":
    main()
