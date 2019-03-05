# Function that contains a list of modifier keys (shift, ctrl, del, etc).
def modificators_key():
	modificators_key = ["Shift_L", "Shift_R", "Control_L", "Control_R", "Caps_Lock", "Alt_L",
		"Alt_R", "Super_L", "Super_R", "Meta_L", "Meta_R", "Escape", "Print", "Delete", "Home",
		"End", "Page_Up", "Next", "BackSpace", "Num_Lock", "Tab", "P_", "P_Home", "Up", "Left",
		"Begin", "Right", "P_End", "Down", "[65027]", "Insert", "[269025043]", "[269025042]"]
	return modificators_key


# Function that contains a dictionary of special characters.
def characters():
	characters = {"P_Divide": "/", "Divide": "/", "P_Multiply": "*", "Multiply": "*",
		"P_Subtract": "-", "Subtract": "-", "P_Add": "+", "Add": "+", "plus": "+", "P_Enter": "\n",
		"Enter": "\n", "braceright": "}", "braceleft": "{", "ntilde": "ñ", "minus": "-",
		"quotedbl": '"', "numbersign": "#", "dollar": "$", "percent": "%", "ampersand": "&",
		"slash": "/", "parenleft": "(", "parenright": ")", "equal": "=", "questionup": "?",
		"semicolon": ";", "colon": ":", "underscore": "_", "[65105][65105]": "´", "[65105]a": "á",
		"[65105]A": "Á", "[65105]e": "é", "[65105]E": "É", "[65105]i": "í", "[65105]I": "Í",
		"[65105]o": "ó", "[65105]O": "Ó", "[65105]u": "ú", "[65105]U": "Ú", "space": " ",
		"exclam": "!", "comma": ",", "Return": "\r", "period": ".", "bar": "|", "apostrophe": "'",
		"questiondown": "¿|"}

	return characters


# Function that contains a list of special characters.
def characters_list():
	characters_list = ["P_Divide", "Divide", "P_Multiply", "Multiply", "P_Subtract",
		"Subtract", "P_Add", "Add", "plus", "P_Enter", "Enter", "braceright", "braceleft", "ntilde",
		"minus", "quotedbl", "numbersign", "dollar", "percent", "ampersand", "slash", "parenleft",
		"parenright", "equal", "questionup", "semicolon", "colon", "underscore", "[65105][65105]",
		"[65105]a", "[65105]A", "[65105]e", "[65105]E", "[65105]i", "[65105]I", "[65105]o",
		"[65105]O", "[65105]u", "[65105]U", "space", "exclam", "comma", "Return", "period", "bar",
		"apostrophe", "questiondown"]

	return characters_list
