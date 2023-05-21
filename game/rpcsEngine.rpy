label bluehub:
    menu:
        "Survey your forces":
            "You summon your commander"
            jump forcemenu
        "End the day":
            call bluedayend


label forcemenu:
    menu:
        "Recapture territory":
            if forces > 14:
                bcom "Ofcourse, I'll plan for an assault to recapture our territory."

            else:
                bcom "Our forces are too weakend to attack anny territory and still deffend your borders"
                jump forcemenu

        "Hire soldiers":

        "Donate forces":

        "Return":
            "You dismiss your commander"
            jump bluehub

screen bluestats:
    modal True
    add "brownbox.png" xalign 0.5 yalign 0.1
    vbox:
        xalign 0.43 yalign 0.14
        text "Test" color "#000000"
        text "Test1" color "#000000"
        text "Test2" color "#000000"
    imagebutton:
        idle "redOK.png"
        action Return()
        xalign 0.5 yalign 0.42

label bluedayend:
    show screen bluestats
    pause
