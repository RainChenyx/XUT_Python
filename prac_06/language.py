"""
Which returns True/False if the programming language is dynamically typed or not.
This file is using the ProgrammingLanguage class.
"""

from programming_language import ProgrammingLanguage


def main():
    ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
    python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
    visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)

    print(ruby)
    print(visual_basic)
    print(python)
    programming_list = [ruby, python, visual_basic]
    for i in range(len(programming_list)):
        if programming_list[i].is_dynamic():
            print("The dynamically typed languages are:", programming_list[i])
    return 0


main()
