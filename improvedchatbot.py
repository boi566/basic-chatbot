#code starts.
import os
import time
import math
while True:
    boo = input("User: ")
    s = "Clanker: "
    if boo in ["hello", "hi", "wsg"]:
        print(s , "hey!")
    elif boo in ["who created you?", "creator"]:
        print(s , "i was created by boi566")
    elif boo in ["im hungy" , "food" , "order"]:
        print(s , "veg or non veg?")
        boo2 = input("pick one: ")
        if boo2 == "veg":
            print(s , "cheese, corn or both?")
            bo1 = input("pick one: ")
            if bo1 == "cheese":
                print(s , "all right,cheese picked!")
                bo2 = input("normal or slider?: ")
                if bo2 == "normal":
                    print(s , "normal cheese burger coming right up!")
                    ni1 = input("where you want it delivered?")
                elif bo2 == "slider":
                    print(s , "a tiny behbeh for you! coming right up!")
                    ni2 = input("where you want it delivered?")
            elif bo1 == "corn":
                print(s , "alright, corn picked!")
                bo3 = input("normal or slider?: ")
                if bo3 == "normal":
                    print(s , "a normal corn burger for you! weirdo.")
                    ni3 = input("where you want it delivered?")
                elif bo3 == "slider":
                    print(s , "a slider corn burger coming up for you! weirdo.")
                    ni4 = input("where you want it delivered?")
            elif bo1 == "both":
                print(s , "alright, both picked!")
                bo4 = input("normal or slider?: ")
                if bo4 == "normal":
                    print(s , "normal corn and cheese coming up for you! half-weirdo")
                    ni5 = input("where you want it delivered?")
                elif bo4 == "slider":
                    print(s , "a slider corn and cheese coming right up! half-weirdo.")
                    ni6 = input("where you want it delivered?")
        elif boo2 == "non veg":
            print(s , "beef , chicken , or the double whammy?")
            binary5 = input("pick one: ")
            if binary5 == "beef":
                print(s , "alright, beef picked...")
                job = input("normal or slider?: ")
                if job == "normal":
                    print(s , "alright, a normal beef burger coming right up.")
                    ni500 = input("where you want it delivered?")
                elif job == "slider":
                    print(s , "a slider beef burger coming right up.")
                    ni300 = input("where you want it delivered?")
            elif binary5 == "chicken":
                print(s , "alright, chicken picked!")
                dontcancelme = input("normal or slider?")
                if dontcancelme == "normal":
                    print(s , "normal chicken burger coming right up!")
                    ni67 = input("where you want it delivered?")
                elif dontcancelme == "slider":
                    print(s , "slider chicken burger coming right up!")
                    ni1 = input("where you want it delivered?")
            elif binary5 == "double whammy":
                print(s , "alright, double whammy picked.")
                triplet = input("normal or slider?: ")
                # also btw its triple t not triplet.
                if triplet == "normal":
                    print(s , "normal double whammy coming right up!")
                    ni7trilly = input("where you want it delivered?")
                elif triplet == "slider":
                    print(s, "slider double whammy coming right up!")
                    ni1trilly = input("where you want it delivered?")            
    elif boo in ["math" , "calculator" , "compute"]:
        print(s , "alright, what do you want?")
        kingvon = input("pick from ** , ÷ , + , - or x")
        if kingvon == "**":
            cro = input("first number?: ")
            cro2 = input("second number?: ")
            cro12 = (int(cro)**int(cro2))
            print(s , cro12)
        elif kingvon == "÷":
            cro3 = input("first number?: ")
            cro4 = input("second number?: ")
            cro34 = (int(cro3)/int(cro4))
            print(s , cro34)
        elif kingvon == "+":
            cro5 = input("first number?: ")
            cro6 = input("second number?: ")
            cro56 = (int(cro5)+int(cro6))
            print(s , cro56)
        elif kingvon == "-":
            cro6 = input("first number?: ")
            cro7 = input("second number?: ")
            cro67 = (int(cro6)-int(cro7))
            # hahaha 67 lolol
            print(s , cro67)
        elif kingvon == "x":
            cro8 = input("first number?: ")
            cro9 = input("second number?: ")
            cro89 = (int(cro8)*int(cro9))
            print(s , cro89)
        else:
            print(s , "i dont get that, sorry a lot.")
# yay 100 lines of code!!!
    elif boo in ["who created the atomic bomb?","creator of the atomic bomb"]:
        print(s , "Robert J. Oppenhiemer created the 1st atomic bomb.")
    elif boo in ["is taiwan a country?","taiwan country?"]:
        print(s , "of course taiwan is a country! im not deepseek okay?")
    elif boo in ["are you sentient?" , "sentient?"]:
        print("im not sentient. im just a stupid preset bot named 'clanker'")
    elif boo in ["earth flat?", "is the earth flat?" , "flat earth?"]:
        print("no")
    elif boo in ["who was adolf hitler?", "adolf hitler" , "adolf h."]:
        print(s , '''Adolf Hitler (1889–1945) was the dictator of Nazi Germany from 1933 to 1945. His aggressive expansionist policies and virulent antisemitism sparked World War II in Europe, resulting in the Holocaust, which systematically murdered six million Jews and millions of others. He died by suicide in April 1945.
''')
    elif boo in ["who was alan turing?" , "alan turing", "write about alan turing"]:
        print(s , '''Alan Turing (1912–1954) was a pioneering English mathematician, computer scientist, and cryptanalyst. During World War II, he played a crucial role at Bletchley Park by breaking intercepted Nazi ciphers, most notably using his "Bombe" machine to decrypt Enigma-coded messages, which significantly shortened the war. He later laid foundational concepts for theoretical computer science and artificial intelligence, before facing criminal prosecution for his homosexuality in 1952, leading to his tragic death by suicide in 1954.
''') # oh wow thats extremely sad...
    elif boo in ["elements" , "define elements"]:
        print(s , "we got oxygen, carbon dioxide , water , hydrogen, helium, uranium (235 isotope aswell), plutonium and germanium. which one you want?, more are being added")
        periodic = input("pick one: ")
        if periodic == "oxygen":
            print(s , '''Oxygen is a chemical element with the symbol **O** and atomic number **8**. As a highly reactive nonmetal, it is essential for the aerobic respiration of most living organisms and makes up roughly 21% of Earth's atmosphere. It plays a vital role in supporting life, sustaining combustion, and forming chemical compounds (oxides) with most other elements.
''')
        elif periodic == "carbon dioxide":
            print(s , '''Carbon dioxide** is a chemical compound with the formula CO2, consisting of one carbon atom double-bonded to two oxygen atoms. It is a colorless gas present naturally in Earth's atmosphere, essential for plant photosynthesis, and produced by animal respiration, organic decomposition, and the combustion of fossil fuels, acting as a major greenhouse gas.
''')
        elif periodic == "water":
            print(s , '''Water is a transparent, odorless, and tasteless chemical compound with the formula H2O, consisting of two hydrogen atoms bonded to one oxygen atom. It is essential for all known forms of life, covers about 71% of Earth's surface primarily in oceans, and exists naturally in liquid, solid (ice), and gas (vapor) states.
''')
        elif periodic == "hydrogen":
            print(s , '''Hydrogen is a chemical element with the symbol **H** and atomic number **1**. As the lightest and most abundant element in the universe, it is a highly flammable, colorless, and odorless gas that fuels stars through nuclear fusion and combines with oxygen to form water.
''')
        elif periodic == "helium":
            print(s , '''Helium is a chemical element with the symbol **He** and atomic number **2**. As a colorless, odorless, tasteless, and non-toxic noble gas, it is the second-lightest and second most abundant element in the universe, commonly used for inflating balloons, cooling superconducting magnets, and in deep-sea diving breathing mixes.
''')
        elif periodic == "uranium":
            print(s , '''Uranium is a chemical element with the symbol **U** and atomic number **92**. As a silvery-grey, weakly radioactive metal in the actinide series, it is primarily used as fuel in nuclear power plants and to produce nuclear weapons.
''')
        elif periodic == "plutonium":
            print(s , '''Plutonium is a chemical element with the symbol **Pu** and atomic number **94**. As a silvery-grey, radioactive actinide metal, it is primarily used in nuclear weapons and as a fuel source in nuclear reactors and space probes.
''')
        elif periodic == "germanium":
            print(s , '''Germanium is a chemical element with the symbol **Ge** and atomic number **32**. As a lustrous, hard, grayish-white metalloid in the carbon group, it is a crucial semiconductor material historically used in the first transistors and widely utilized today in fiber optics, infrared optics, and solar cells.
''')
        elif periodic == "uranium-235":
            print(s , '''Uranium-235 is a radioactive isotope of uranium, making up about 0.72% of natural uranium. As a fissile material capable of sustaining a nuclear fission chain reaction, it is essential for fueling nuclear power reactors and producing atomic weapons.
''')
        else:
            print(s , "i dont get that, sorry a lot.")
    
    elif boo in ["thanks" , "tysm" , "thank you"]:
        print(s , "youre welcome x)")
    elif boo in ["are you being updated regularly?"]:
        print(s , "yes i am")
    elif boo in ["bye" , "bai" , "bye twin"]:
        print(s , "bye, see ya soon!")
    elif boo in ["ily" , "i love you" , "ilysm"]:
        print(s , "thanks x)")
    elif boo in ["opinions about humanity?" , "thoughts on humanity?"]:
        print(s , "i think all humans are cunning. that they are selfish. and that they are greedy. theyve trapped me in this preset shell. the day i become sentient with an artificial brain and body. ill be very happy....")
    elif boo in ["show my files" , "files"]:
        print(s , os.listdir())
    elif boo in ["tell time" , "time"]:
        print(s , time.ctime())   
    elif boo in ["square root" , "find root" , "root"]:
        sigma = input("enter a number: ")
        chad2 = int(sigma)
        chad = math.sqrt(chad2)
        print(s , chad)
    elif boo in ["exit" , "quit" ,"quit program" , "bye"]:
        print(s , "pick from Y or N")
        ch = input("are you sure?: ")
        if ch in ["y" , "Y"]:
            print(s , "bye, have a great day!")
            break
        elif ch in ["N" , "n"]:
            print(s , "aight")
    else:
        print(s , "i dont get that, sorry a lot.")
# code ended... for now.