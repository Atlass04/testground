label firstbluebase:
    $ forces = 45
    $ money = 1200
    $ rep = 100
    $ groundtaken = 30

    $ foresttribe = False

    $ forcechange = 0
    $ moneychange = 0
    $ repchange = 0
    $ recapturedaily = False

    $ floatvar = 0
    jump bluehub
label bluehub:
    menu:
        "Survey your forces":
            "You summon your commander"
            jump bluewarevents
        "End the day":
            call bluedayend

#-------------------------------------------------------------------#
#-----------------Military acts-------------------------------------#
#-------------------------------------------------------------------#
label forcemenu:
    show screen bluemap
    menu:
        "Recapture territory":
            if forces + forcechange > 14:
                if recapturedaily == False:
                    $ forcechange -= 15
                    $ recapturedaily = True
                    bcom "Ofcourse, I'll plan for an assault to recapture our territory."

                else:
                    bcom "We're allready preparing an attack for today"

            else:
                bcom "Our forces are too weakend to attack anny territory and still deffend your borders"

        "Hire soldiers (cost 400)":
            if money + moneychange > 399:
                $ moneychange -= 400
                bcom "Ofcourse, I'll arange the recruitment immediately"

            else:
                bcom "We don't have the funds for that at the moment"

        "Donate forces":
            if forces + forcechange > 99:
                $ forcechange -= 100
                bcom "Ofcourse, well send some men to the royal army"

            else:
                bcom "Sadly we dont have any forces to spare."

        "Return":
            "You dismiss your commander"
            jump bluehub
    jump forcemenu
#-----------------------
#------map screen-------
screen bluemap:
    if groundtaken > 39:
        add "bluemap40per.png" xalign 1.0 yalign 0.0
    elif groundtaken > 29:
        add "bluemap30per.png" xalign 1.0 yalign 0.0
    elif groundtaken > 19:
        add "bluemap20per.png" xalign 1.0 yalign 0.0
    elif groundtaken > 9:
        add "bluemap10per.png" xalign 1.0 yalign 0.0
    else:
        add "bluemap0per.png" xalign 1.0 yalign 0.0

#-----------------------
#------war events-------
label bluewarevents:
    #Forest tribe recapture
    if groundtaken >= 20 and foresttribe == False:
        bcom "We have captured the territory around those traitorous beasts of the forest tribe"
        bcom "Are we ready to begin the assault on their little vilage?"
        menu:
            "Yes":
                bcom "Wonderfull"
                bcom "I have taken the liberty and rallied the troops in advance."
                bcom "Where allready to go."
            "No":
                bcom "Hmm"
                bcom "Ofcourse, tell me when you're ready to go"

        $ foresttribe = True
    jump forcemenu

label forestassaultblue:
    "As you step into the dense forest, a shiver runs down your spine."
    "The air feels heavy with an enigmatic presence, and the silence is broken only by the rustling of leaves and the marching of you men."
    "The towering trees rises high above you, and cuts the light out almost completely."

    "After walking for an hour you see small wooden masks hanging from the trees in a line."
    bcom "We've arrived sir, this is the border to their part of the forest."
    "The masks appears more often the further down the path you go, and soon they hang from every branch."
    "A soldier sudendly screams as he is ripped from his horse, and dissapears into the forest."
    "Only russling of the bush can be seen, and momentarely the gestalt of somethink the size of a man."
    "Seconds go by where you look at the bush where he met his end until the silence is broken."
    bsol "CONTACT RIGHT!"
    "spears and arrows start flying from all dirrections, and your men has formed an deffensive circle arround you."
    bcom "THEIR CAMP SHOULDN'T BE FAR AHEAD!"
    bcom "SHOULD WE KEEP GOING?"
    menu:
        "Push forward to the camp":
            $ floatvar += 1
            mc "Well we cant stay here!"
            bcom "KEEP MOVING FORWARD!"
            "You push fowrard, paying in blood for every step taken."
            "One arrow manages to hit you, burrowing deeply into your arm."
            "It sends an explotion of pain through you, and you almost blank out."
            "With your dagger you cut the arrow by the shaft, leaving the bolt stuck but affording you some mobility."
            "Then the barrage suddenly stops as the path opens up to a clearing meters infront of you"
            bcom "We're here"


        "Deffeat the ambush":
            $ floatvar -= 1

    "The thick cannopy above you dissapears as you step into the clearing, and you see what must be hundreds of tents surrounding a lake."
    unowkn "HALT"
    "The voice belongsto an old man, most likely the town elder, surrounded by a dozzen warriors snarling at you."
    wolfeld "You have no righs to step into this forest."
    #house name
    mc "This entire forest is on land rightfully owned by the house of the burning vyvern."
    mc "And we're here to take it back, it's for you to decide how you'll be part of it."
    wolfeld "You expect us to just lay down our arms and bow to your kind again?"
    menu:
        "Give them the forest":
            mc "Your tribe has allways been loyal subject to the burning vyvern house."
            mc "Those times died with the house."
            mc "I sugest you join us as alies, and the forest is yours."
            wolfeld "Oh?"
            wolfeld "And whats the catch?"
            mc "A tribute to ensure your loyalty, and the forest it yours"
            "The wolfman tenses up noticibly."
            wolfeld "What?"

        "Make your forces attack":



#-------------------------------------------------------------------#
#-----------------End of day calcs----------------------------------#
#-------------------------------------------------------------------#
screen bluestats:
    modal True
    add "brownbox.png" xalign 0.5 yalign 0.1
    vbox:
        xalign 0.47 yalign 0.14
        text "Forces: [forces]" color "#000000"
        text "Funds: [money]" color "#000000"
        text "Rep: [rep]" color "#000000"
        text "Area taken: [groundtaken]" color "#000000"

    vbox:
        xalign 0.57 yalign 0.14
        text "[forcechange]" color "#000000"
        text "[moneychange]" color "#000000"
        text "[repchange]" color "#000000"
        if recapturedaily == True:
            text "+1" color "#000000"
        else:
            text "0" color "#000000"


    imagebutton:
        idle "redOK.png"
        action Hide("bluestats")
        xalign 0.5 yalign 0.42

label bluedayend:
    $ floatvar = groundtaken*25
    $ moneychange += floatvar
    "The tax of your land added up to [floatvar]"

    show screen bluestats
    pause 0.1


    #add day stats
    $ money += moneychange
    $ forces += forcechange
    $ rep += repchange
    if recapturedaily == True:
        $ groundtaken += 1
    #Reset day stats
    $ recapturedaily = False
    $ repchange = 0
    $ forcechange = 0
    $ moneychange = 0
    "Dayend"
    jump bluehub
