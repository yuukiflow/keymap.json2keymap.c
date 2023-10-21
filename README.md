***SIMPLE QMK Configurator converter from JSON to C keymap file***

I built this simple tool to convert json file from QMK online configurator and write it to my keymap.c as I use OLED and other functions that are not working with JSON keymaps.
You need to specify your layer names in the command, it will write them in the order of the JSON file.

**USAGE**

1. Clone this repository to your local machine.

2. Open a terminal and navigate to the directory where the `json2c.py` script is located.

3. Run the script with the following command:
```bash
python json2c.py <JSON_FILE> <keymap.c> --new_layer <layer1, layer2, ...>
```
