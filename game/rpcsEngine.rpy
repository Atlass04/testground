label firstbluebase:
    $ forces = 45
    $ money = 1200
    $ rep = 100
    $ groundtaken = 30

    $ wolftribe = "undecided"
    $ black = Solid("#000000")  # Create a black image
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
        "Dorms":
            jump dormmenu
        "End the day":
            call bluedayend
#-------------------------------------------------------------------#
#-----------------Dorm menu-----------------------------------------#
#-------------------------------------------------------------------#
label dormmenu:
    menu:
        "Visit Koyo." if koyo == True:
            

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
            hide screen bluemap
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
    if groundtaken >= 20 and wolftribe == "undecided":
        bcom "We have captured the territory around those traitorous beasts of the forest tribe"
        bcom "Are we ready to begin the assault on their little vilage?"
        menu:
            "Yes":
                bcom "Wonderfull"
                bcom "I have taken the liberty and rallied the troops in advance."
                bcom "Where allready to go."
                jump forestassaultblue
            "No":
                bcom "Hmm"
                bcom "Ofcourse, tell me when you're ready to go"

        $ foresttribe = True
    jump forcemenu


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
