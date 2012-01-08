#!/usr/bin/env python

import fontforge

letters = [
	[0x0023,"hash"],
	[0x003F,"question_mark"],
	[0x0040,"at"],
	[0x00b6, "pilcrow"],
	[0x2139, "info"],
	[0x2190, "arrow_left"],
	[0x2191, "arrow_up"],
	[0x2192, "arrow_right"],
	[0x2193, "arrow_down"],
	[0x2302, "home"],
	[0x2600, "sun_stroke"],
	[0x2601, "cloud"],
	[0x2602, "umbrella"],
	[0x2605, "star"],
	[0x263e, "moon_stroke"],
	[0x2764, "heart_stroke"],
	[0x2699, "cog"],
	[0x26a1, "bolt"],
	[0x26bf, "key_stroke"],
	[0x26c6, "rain"],
	[0x26d4, "denied"],
	[0x2709, "mail"],
	[0x270e, "pen"],
	[0x2717, "check"],
	[0x2718, "check_alt"],
	[0x2713, "x"],
	[0x2714, "x_alt"],
	[0x275d, "left_quote"],
	[0x275e, "right_quote"],
	[0x2795, "plus"],
	[0x2796, "minus"],
	[0x2935, "curved_arrow"],
	# webkit doesn't seem to support Unicode ranges above 0xffff
	#[0x1f3a4, "mic"],
	#[0x1f3a5, "movie"],
	#[0x1f3a7, "headphones"],
	#[0x1f464, "user"],
	#[0x1f4a1, "lightbulb"],
	#[0x1f4bf, "cd"],
	#[0x1f4c1, "folder_stroke"],
	#[0x1f4c4, "document_stroke"],
	#[0x1f4cc, "pin"],
	#[0x1f4cd, "map_pin_stroke"],
	#[0x1f4d5, "book"],
	#[0x1f4d6, "book_alt2"],
	#[0x1f4e6, "box"],
	#[0x1f4c5, "calendar_alt_stroke"],
	#[0x1f4ac, "comment_stroke"],
	#[0x1f4f1, "iphone"],
	#[0x1f4f6, "bars"],
	#[0x1f4f7, "camera"],
	#[0x1f507, "volume_mute"],
	#[0x1f508, "volume"],
	#[0x1f50b, "battery_full"],
	#[0x1f50e, "magnifying_glass"],
	#[0x1f512, "lock_stroke"],
	#[0x1f513, "unlock_stroke"],
	#[0x1f517, "link"],
	#[0x1f527, "wrench"],
	#[0x1f550, "clock"],
	[0xe000, "document_alt_stroke"],
	[0xe001, "calendar"],
	[0xe002, "map_pin_alt"],
	[0xe003, "comment_alt1_stroke"],
	[0xe004, "comment_alt2_stroke"],
	[0xe005, "pen_alt_stroke"],
	[0xe006, "pen_alt2"],
	[0xe007, "chat_alt_stroke"],
	[0xe008, "plus_alt"],
	[0xe009, "minus_alt"],
	[0xe00a, "bars_alt"],
	[0xe00b, "book_alt"],
	[0xe00c, "aperture_alt"],
	[0xe010, "beaker_alt"],
	[0xe011, "left_quote_alt"],
	[0xe012, "right_quote_alt"],
	[0xe013, "arrow_left_alt1"],
	[0xe014, "arrow_up_alt1"],
	[0xe015, "arrow_right_alt1"],
	[0xe016, "arrow_down_alt1"],
	[0xe017, "arrow_left_alt2"],
	[0xe018, "arrow_up_alt2"],
	[0xe019, "arrow_right_alt2"],
	[0xe01a, "arrow_down_alt2"],
	[0xe01b, "brush"],
	[0xe01c, "brush_alt"],
	[0xe01e, "eyedropper"],
	[0xe01f, "layers"],
	[0xe020, "layers_alt"],
	[0xe021, "compass"],
	[0xe022, "award_stroke"],
	[0xe023, "beaker"],
	[0xe024, "steering_wheel"],
	[0xe025, "eye"],
	[0xe026, "aperture"],
	[0xe027, "image"],
	[0xe028, "chart"],
	[0xe029, "chart_alt"],
	[0xe02a, "target"],
	[0xe02b, "tag_stroke"],
	[0xe02c, "rss"],
	[0xe02d, "rss_alt"],
	[0xe02e, "share"],
	[0xe02f, "undo"],
	[0xe030, "reload"],
	[0xe031, "reload_alt"],
	[0xe032, "loop_alt1"],
	[0xe033, "loop_alt2"],
	[0xe034, "loop_alt3"],
	[0xe035, "loop_alt4"],
	[0xe036, "spin"],
	[0xe037, "spin_alt"],
	[0xe038, "move_horizontal"],
	[0xe039, "move_horizontal_alt1"],
	[0xe03a, "move_horizontal_alt2"],
	[0xe03b, "move_vertical"],
	[0xe03c, "move_vertical_alt1"],
	[0xe03d, "move_vertical_alt2"],
	[0xe03e, "move"],
	[0xe03f, "move_alt1"],
	[0xe040, "move_alt2"],
	[0xe041, "transfer"],
	[0xe042, "download"],
	[0xe043, "upload"],
	[0xe044, "cloud_download"],
	[0xe045, "cloud_upload"],
	[0xe046, "fork"],
	[0xe047, "play"],
	[0xe048, "play_alt"],
	[0xe049, "pause"],
	[0xe04a, "stop"],
	[0xe04b, "eject"],
	[0xe04c, "first"],
	[0xe04d, "last"],
	[0xe04e, "fullscreen"],
	[0xe04f, "fullscreen_alt"],
	[0xe050, "fullscreen_exit"],
	[0xe051, "fullscreen_exit_alt"],
	[0xe052, "equalizer"],
	[0xe053, "article"],
	[0xe054, "read_more"],
	[0xe055, "list"],
	[0xe056, "list_nested"],
	[0xe057, "cursor"],
	[0xe058, "dial"],
	[0xe059, "new_window"],
	[0xe05a, "trash_stroke"],
	[0xe05b, "battery_half"],
	[0xe05c, "battery_empty"],
	[0xe05d, "battery_charging"],
	[0xe05e, "chat"],
	
	#temporary unicode values until Webkit fixes support
	[0xe05f, "mic"],
	[0xe060, "movie"],
	[0xe061, "headphones"],
	[0xe062, "user"],
	[0xe063, "lightbulb"],
	[0xe064, "cd"],
	[0xe065, "folder_stroke"],
	[0xe066, "document_stroke"],
	[0xe067, "pin"],
	[0xe068, "map_pin_stroke"],
	[0xe069, "book"],
	[0xe06a, "book_alt2"],
	[0xe06b, "box"],
	[0xe06c, "calendar_alt_stroke"],
	[0xe06d, "comment_stroke"],
	[0xe06e, "iphone"],
	[0xe06f, "bars"],
	[0xe070, "camera"],
	[0xe071, "volume_mute"],
	[0xe072, "volume"],
	[0xe073, "battery_full"],
	[0xe074, "magnifying_glass"],
	[0xe075, "lock_stroke"],
	[0xe076, "unlock_stroke"],
	[0xe077, "link"],
	[0xe078, "wrench"],
	[0xe079, "clock"],
]

font_stroke = fontforge.open('blank_stroke.sfd')

for letter_config in letters:
	char = letter_config[0]
	file_name = letter_config[1]

	c = font_stroke.createChar(char)

	c.importOutlines('../../vector/' + file_name + '.svg')

	c.left_side_bearing = 15
	c.right_side_bearing = 15

#font files

font_stroke.generate('iconic_stroke.svg')
font_stroke.generate('iconic_stroke.ttf')
font_stroke.generate('iconic_stroke.eot')
font_stroke.generate('iconic_stroke.otf')

#css file

theString="@font-face { font-family: 'IconicStroke'; src: url('iconic_stroke.eot'); src: url('iconic_stroke.eot?#iefix') format('embedded-opentype'), url('iconic_stroke.ttf') format('truetype'), url('iconic_stroke.svg#iconic') format('svg'); font-weight: normal; font-style: normal; }"
theString+=".iconic { display:inline-block; font-family: 'IconicStroke'; }"
for letter_config in letters:
	theHex = int(letter_config[0])
	theHex = hex(theHex)
	theString += "." + letter_config[1] + ":before {content:'\\" + theHex[2:] + "';}"

f = open("iconic_stroke.css", 'w')
f.write(theString)
f.close()

#html file
theString="<html><head><title>Iconic Font-embedding demo</title><link rel='stylesheet' href='iconic_stroke.css' type='text/css' media='screen' /><style> body {font-family:'Helvetica', arial, sans-serif;} span { font-size:36px; }</style><body>"
theString += "<table><tr><th>Name</th><th>Iconic Icon</th><th>Unicode Icon</th><th>Hexidecimal Code</th>"
for letter_config in letters:
	theHex = int(letter_config[0])
	theHex = hex(theHex)
	theString += "<tr><td>" + letter_config[1] + "</td><td><span class='iconic " + letter_config[1] + "'></span></td><td><span class='" + letter_config[1] + "'></span></td><td>" + theHex + "</td></tr>" 

theString += "</table></body></html>"
	
f = open("iconic_stroke_demo.html", 'w')
f.write(theString)
f.close()