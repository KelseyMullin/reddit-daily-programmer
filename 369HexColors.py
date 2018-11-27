#Challenge from https://www.reddit.com/r/dailyprogrammer/comments/a0lhxx/20181126_challenge_369_easy_hex_colors/

def hex_color(red, green, blue):
    color = "#"
    color = color + pad_color(red)
    color = color + pad_color(green)
    color = color + pad_color(blue)
    return color


def pad_color(color):
    hex_color = dec_to_hex(color)
    if len(hex_color) == 1:
        return "0" + hex_color
    else:
        return hex_color


def dec_to_hex(dec):
    hex = ""
    if dec == 0:
        hex = "0"
    while dec > 0:
        temp = dec % 16
        if temp > 9:
            temp = 55 + temp
            temp = chr(temp)
        hex = str(temp) + hex
        dec = dec // 16
    return hex


print(hex_color(127, 255, 212))
print(hex_color(255, 99, 71))
print(hex_color(184, 134, 11))
print(hex_color(189, 183, 107))
print(hex_color(0, 0, 205))