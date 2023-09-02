sophiashop = ["wig", "blower", "shampoo"]       #displaying items in sohpiashop
petershop = ["ball", "boot", "jersey"]          #displaying items in petershop
sophiashop.pop (2)                              #buying shampoo from sohpiashop
petershop.append ("shampoo")                    #petershop displaying shampoo in his shelf
petershop.pop (2)                               #sohpiashop buying shampoo from petershop
sophiashop.append ("jersey")                    #sophiashop displaying shampoo in her shelf
print(sophiashop)                               #sophiashop displaying new collection of items in her shelf
print(petershop)                                #petershop displaying new collection of items in his shelf


sophiashop = ["wig", "blower", "shampoo"]      #displaying items in sohpiashop
petershop = ["ball", "boot", "jersey"]          #displaying items in petershop
petershop.append (sophiashop[2])                    #petershop displaying shampoo in his shelf
sophiashop.pop (2)                              #buying shampoo from sohpiashop
sophiashop.append (petershop[2])                    #sophiashop displaying shampoo in her shelf
petershop.pop (2)                               #sohpiashop buying shampoo from petershop
print(sophiashop)                               #sophiashop displaying new collection of items in her shelf
print(petershop)                                #petershop displaying new collection of items in his shelf


sophiashop = ["wig", "blower", "shampoo"]       #displaying items in sohpiashop
sophiashop2 = ["wig", "blower", "shampoo"]      #displaying items in sohpiashop
petershop = ["ball", "boot", "jersey"]          #displaying items in petershop
petershop2 = ["ball", "boot", "jersey"]         #displaying items in petershop
sophiashop.pop (2)                              #buying shampoo from sohpiashop
petershop.append (petershop2[2])                    #petershop displaying shampoo in his shelf
petershop.pop (2)                               #sohpiashop buying shampoo from petershop
sophiashop.append (sophiashop2[2])                    #sophiashop displaying shampoo in her shelf
print(sophiashop)                               #sophiashop displaying new collection of items in her shelf
print(petershop)                                #petershop displaying new collection of items in his shelf
