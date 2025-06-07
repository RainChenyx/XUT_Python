"""
Based on the state name example program above, create a program that allows you to
look up hexadecimal colour codes like those at https://www.color-hex.com/color-names.html
"""

ALL_CAPS = {"Absolute Zero": "#0048ba", "Acid Green": "#b0bf1a", "AliceBlue": "#f0f8ff", "Alizarin crimson": "#e32636",
            "Amaranth": "#e52b50", "Amber": "#ffbf00", "Amethyst": "#9966cc", "AntiqueWhite": "#faebd7",
            "AntiqueWhite1": "#ffefdb", "AntiqueWhite2": "#eedfcc", "AntiqueWhite3": "#cdc0b0"}


def main():
    print(ALL_CAPS.items())
    name = input("Please enter a color name: ").strip()
    while name != "":
        if name in ALL_CAPS:
            code_color = ALL_CAPS[name]
            print(code_color)
        else:
            print("The name is not in AAL_CAPS")
        print(ALL_CAPS.items())
        name = input("Please enter a color name: ").strip()


main()
