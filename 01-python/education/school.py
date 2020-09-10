def draw_school(height=0):
    print("        ^")
    print("       / \\")
    print("        - ")
    print("       |O|")
    print("       | |")
    print(" ------   ------")
    print("/                \\")
    print("______SCHOOL______")
    print(" |              |")
    print(" | [ ]      [ ] |")
    
    for i in range(height):
        if (i + 1) % 2 == 0 and i != 0:
            print(" | [ ]      [ ] |")
        else:
            print(" |              |")
        
    print(" |      ___     |")
    print(" |      | |     |")
    print(" |      |_|     |")