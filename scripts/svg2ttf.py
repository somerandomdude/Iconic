#!/usr/bin/env python

import fontforge

letters = [
	["!", "home"],
	['"', "left_quote"],
	["#", "arrow_up_alt1"],
	["$", "arrow_right_alt1"],
	["%", "arrow_down_alt1"],
	["&", "move_horizontal_alt2"],
	["'", "left_quote_alt"],
	["(", "move_alt2"],
	[")", "cursor"],
	["*", "move_vertical_alt2"],
	["+", "plus"],
	[",", "headphones"],
	["-", "minus"],
	[".", "read_more"],
	["/", "link"],
	["0", "lightbulb"],
	["1", "new_window"],
	["2", "dial"],
	["3", "arrow_up"],
	["4", "arrow_right"],
	["5", "arrow_down"],
	["6", "arrow_left"],
	["7", "move_horizontal"],
	["8", "move_vertical"],
	["9", "move"],
	[":", "fullscreen"],
	[";", "fullscreen_exit"],
	["<", "equalizer"],
	["=", "plus_alt"],
	[">", "article"],
	["?", "image"],
	["@", "at"],
	["A", "calendar"],
	["E", "book_alt"],
	["J", "chat_alt_stroke"],
	["L", "lock_stroke"],
	["M", "mail"],
	["P", "pen"],
	["Q", "comment_alt2_stroke"],
	["V", "volume_mute"],
	["W", "cog"],
	["X", "x_alt"],
	["Y", "check_alt"],
	["Z", "beaker_alt"],
	["[", "spin"],
	["\\", "map_pin_stroke"],
	["]", "moon_stroke"],
	["^", "arrow_left_alt1"],
	["_", "minus_alt"],
	["`", "denied"],
	["a", "calendar_alt_stroke"],
	["b", "bolt"],
	["c", "clock"],
	["d", "document_stroke"],
	["e", "book"],
	["f", "magnifying_glass_alt"],
	["g", "tag_stroke"],
	["h", "heart_stroke"],
	["i", "info"],
	["j", "chat"],
	["k", "key_stroke"],
	["l", "unlock_stroke"],
	["m", "mail_alt"],
	["n", "iphone"],
	["o", "box"],
	["p", "pen_alt_stroke"],
	["q", "comment_stroke"],
	["r", "rss"],
	["s", "star"],
	["t", "trash_stroke"],
	["u", "user"],
	["v", "volume"],
	["w", "cog_alt"],
	["x", "x"],
	["y", "check"],
	["z", "beaker"],
	["{", "spin_alt"],
	["|", "pin"],
	["}", "sun"],
	["~", "eyedropper"]
]

font = fontforge.open('blank.sfd')

for letter_config in letters:
	char = letter_config[0]
	file_name = letter_config[1]

	c = font.createChar(ord(char))

	c.importOutlines('../vector/' + file_name + '.svg')

	c.left_side_bearing = 15
	c.right_side_bearing = 15

font.generate('iconic_stroke.ttf')
