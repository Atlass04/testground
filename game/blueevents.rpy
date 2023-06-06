#-------------------------------------------------------------------#
#-----------------Start of foresttribe------------------------------#
#-------------------------------------------------------------------#

label forestassaultblue:
    scene forestpath
    "As you step into the dense forest, a shiver runs down your spine."
    "The air feels heavy with an enigmatic presence, the silence is broken only by the rustling of leaves and the marching of your men."
    "The towering trees rise high above you and block out the light almost completely."
    "The lightlevel is more similar to a fullmoon night, and you're finding it quite hard to navigate."

    "After walking for what must be an hour, you start to see small wooden masks hanging from the trees what loosley resemblimg a line, marking some ancient border."
    "The masks resembles the shape of wolf skulls, and small carvings of unowkn meanings have been inscribed upon them."
    bcom "We've arrived, sir. This is where the old border between our house and the forest tribe once was."
    "after walking for some time you notice that the masks appears with shorter frequently the further down the path you go, and soon they hang down from almost every branch."
    "You walk in silence for some time, coming closer to the camps location."
    "Then all of a sudden one of your soldiers gets pulled into the forest, without even having the time to make a sound."
    "Only the rustling of bushes can be heard or seen, and momentarily, the silhouette of a man."
    "Seconds pass as you and your soldiers fixate on the bush where he met his end until the silence is broken."
    bsol "CONTACT RIGHT!"
    "Spears and arrows start flying from all directions with deadly accuracy."
    "Soldier after soldier falls to the ground, all with large bolts sticking out of them."
    "They've formed a primitive deffensive circle of shields around you, only moments later."
    bcom "Orders sir!"
    mc "How far until the opening?!"
    bcom "It isn't far ahead now!"
    bcom "Should we keep going?"
    menu:
        "Push forward to the camp":
            $ floatvar = 1
            mc "This ambush is a slaughter!{w=2.0} We won't have a chanse fghting here!"
            bcom "KEEP MOVING FORWARD!"
            "You slowly press forward, paying in blood for every step as more men groans when hit."
            "An arrow wissles past you, only inches from hitting your head. Moments later one manages to hit you in your left shoulder."
            "A guttural crunching sound comes from your shoulder as the bolt burrows deep into your arm."
            "A surge of pain courses through you, and you almost fade out of consciousness."
            "Even after how painful it is you unsheath your dagger, and sever the arrow by it's shaft."
            "Another wave pain hits you, but at least you regain some semblance of mobility in your broken arm."
            "Suddenly, the never ending barrage of arrows stops as the path opens up to a clearing a few meters ahead."
            bcom "We're here!"

        "Defeat the ambush":
            $ floatvar = 0
            mc "Hold your ground! Fight back!"
            "Your men fiercely engage the enemy, but they're severely lacking the knowledge of fighting in thick forests."
            "You're slowly getting pushed into a small, deffensive circle."
            "The barrage of arrows, rocks and bolts is never ending, and the situation has fallen out of your favour."
            "As you push forward, you realize the cost of this battle is greater than anticipated."
            bcom "We're losing too many! We need to regroup!"
            mc "Keep going forward! We can't afford to retreat!"
            "The fighting continues, and you slowly advance torwards the clearing."
            "Finally, you manage to break through the ambush and reach the clearing ahead, but the battle is a compleete dissaster."


    scene forestlake
    "The thick canopy above you disappears as you run to the clearing, revealing what must be hundreds of tents surrounding a lake."
    "The lake is large, and is surrounded by a rocky beach."
    "Trees circle around the area, and almost forms a wall of wood, with only small openings large enough to fit a few persons."
    unowkn "HALT!"
    "The voice belongs to an old man, most likely the town elder."
    "He has a rugged scarred face, showing his countless victories."
    "Though it is clear that the years has gotten to him, and he's surrounded by a dozen warriors all snarling at you."
    wolfeld "You have no right to step into this forest."
    wolfeld "It would be wise of you to turn around and leave while you have the chance."
    #house name
    mc "This entire forest rightfully belongs to the House of the Burning Wyvern."
    mc "And we're here to reclaim it. It's up to you to decide how you'll be a part of it."
    wolfeld "You expect us to just lay down our arms and bow to your kind again?"
    wolfeld "You couldn't deffend this territory once, what's different now? We're better of defending our on our own."
    menu:
        "Give them the forest":
            mc "The relations betweem my House and the forest clan has alway been unstable."
            mc "But those times could be over if we want it to."
            mc "I suggest you join us as allies."
            wolfeld "Oh?"
            wolfeld "And what do we recieve out of it?"
            mc "My house doesn't need the forest, as long as we get some of the leather spoils."
            mc "I would give my houses part of the forest to you."
            wolfeld "And what's our part of the deal?"
            mc "A tribute to ensure your loyalty, ofcourse."
            "The wolfman visibly tenses up."
            wolfeld "What?"
            mc "Your firstborn will join my house."
            "The wolves start snarling intensely, and a fight seems imminent."
            wolfeld "Unacc-{w=0.4}{nw}"
            unowkn "I accept."
            "A young halfwolf has approached the party, and now stands between you and the elder."
            "She is a bit on the shorter side and is quite slim."
            "Her hair is an ashen silver, and cut just below the ears."
            koyo "For the sake of my tribe I accept your demands."
            wolfeld "But Koyo..."
            koyo "No, it's for the best of the tribe, so I'll go."
            wolfeld ".{w=0.5}.{w=0.5}."
            wolfeld "Fine, the forest tribe accepts the alliance"
            "A heavy silence has fallen over the wolfmen."
            mc "Then it's decided, this will benefit both of us greatly."
            $ koyo == True
            $ wolftribe == "ally"


        "Make your forces attack":
            if floatvar == 1:
                "Their warriors appear to be mostly trained in archery, and now that you're out of the thick forest the advantage is on your side."
                mc "attack!"
                "You almost throw yourself at the halfwolves, and your soldiers are quick to follow suit."
                "Your sudden attack has taken the the elder and his men ofguard."
                "The fighting is over in mere moments, and wolfblood paints the ground red."
                wolfeld "..."
                wolfeld "It would appear that you have us beaten."
                wolfeld "So what now?"
                menu:
                    "Forgive their transgressions":
                        mc "I'll forgive your transgressions, but I wont be so mercyfull next time."
                        mc "You'll join us as allies, and I will donate the rest of the forest to your tribe."
                        wolfeld "I... Thank you for-{w=0.4}{nw}"
                        mc "And I'll take your firstborn to ensure your commpliance."
                        wolfeld "I'm not in a possition to bargain, but please."
                        unowkn "It's okay dad"
                        "A young halfwolf has approached the party, and now stands between you and the elder."
                        "She is a bit on the shorter side and is quite slim."
                        "Her har is a ashen silver, and cut just below the ears."
                        unowkn "I am koyo, firstborn of the forest tribe."
                        koyo "For the sake of my tribe I accept your demands."
                        wolfeld "..."
                        mc "Well then, that would be all for now."
                        $ koyo = True
                        $ wolftribe == "ally"

                    "Enslave the wolfclan":
                        mc "You should have taken the deal."
                        mc "Round up the these halfbreeds."
                        bcom "Yes sir!"
                        "Soon all the halfwolves have been rounded up, and you appear to have their undivided atention,"
                        mc "I came here with the goal to form an allience, but you slaughter my men."
                        mc "This is unnaceptable."
                        "Your commander unsheaths his sword and steps forward."
                        bcom "Bring me the elder!"
                        "Several soldiers walk into the crowd, and drags him to the commander."
                        mc "There will be som changes here from now on, starting the leadership."
                        "Your commander lifts his sword, ready to strike down, as the halfwolf reflexivly recoils."
                        "Cries and shreaks come from the crowd, but one woman jumps out of the crowd to get instantly pushed to the ground by your men."
                        "She is a bit on the shorter side and is quite slim, and her hair is a ashen silver, and cut just below the ears."
                        unowkn "Stop!"
                        "Your commnder gives you a questioning look."
                        unowkn "Just stop!"
                        mc "And who might you be? His daughter i take it?"
                        koyo "Yes, my name is Koyo but please, just dont hurt him.{w=1.0} You've proven your point, and killing him wont change it."
                        Koyo "Please! I-I'll come with you!{w=0.3} As a hostage!"
                        mc "Fine, we'l be leaving then."
                        $ koyo = True
                        $ wolftribe == "enslaved"
            else:
                mc "attack!"
                "You almost throw yourself at the halfwolves, but the same cant be said for your men."
                "They are in no shape to fight since their latest skirmish, and are quickly overrun."
                wolfeld "It would appear that you have bitten down on more than you can chew."
                mc "Damn you!"
                wolfeld "I think we'il kill your troops and send you two home."
                wolfeld "Hopefully that'll keep you from atempting this again for a while."
                "When he's done talking you first hear flesh being cut open and your men hit the ground, all bleeding from their throat."
                "Suddendly you feel a sharp pain in the backk of your head and everything goes black."
                $ koyo == False
                $ wolftribe == "Free"

    bcom "We're going back, boys!"
    bsol "Yes sir!"

    show black with dissolve  # Show the black image with dissolve effect
    pause 1.0  # Pause for one second
    hide black with dissolve  # Hide the black image with dissolve effect

    scene forestpath
    "The journey back takes longer, the fighting has taken a heavy toll on your party."
    "Some soldiers are carried on stretchers, and many still wounded by arrows."
    "The mood however is rather cheerfull. The forest tribe is once again allied to your house."
    "Your camp soon lies ahead of you, and workers come running to help with the wounded."
    jump bluehub

#-----------------End of foresttribe--------------------------------#
#-------------------------------------------------------------------#
#-----------------
