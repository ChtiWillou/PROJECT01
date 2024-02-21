label GAME:        
    show screen Header()
    scene home_bg with dissolve     

    # Here we enter an 'infinite loop' to play the game
    while PlayGame:
        # each event should come back to this label:
        label GAMECONTINUE: 
            hide screen QuickStats  
            show screen Header()
            show screen LocationsSubMenu()         
            # Reset the BlockToCall in case of event triggering
            $ BlockToCall = ""
            $ LinaObj.GetLocation(Date)
            $ LynnObj.GetLocation(Date)
            $ EveObj.GetLocation(Date)
            $ lysh = LynnObj.DefShyLvl()                  

            # Code to parse EVENTS array and eventually call a block if an event is triggered
            python:
                for q in EVENTS:
                    if q.EventCheck(Date):
                        BlockToCall = q.Block
            
            if BlockToCall <> "":
                call expression BlockToCall
            elif curLocForEvent <> "":                
                call expression curLocForEvent
            
            # This pauses the game until a new action like changing room or advancing time
            window hide
            $ renpy.pause(hard=True)
    
    return

label addingallery(pic):
    show screen flash_black with flash_effect
    hide flash_black
    if pic not in GalleryList:
        $ GalleryList.append(pic)
    return

label splashscreen:

    $ quick_menu = True
    scene black with Dissolve (2.0)
    hide text with dissolve
    show text "{color=[text_color]}Bob Bobson and Ce La Vie Group proudly presents...{/color}" with dissolve
    $ rfr_pause(2, hard = True)
    show text "{size=100}{color=[text_color]}My Early Life{/color}{/size}" with dissolve
    $ rfr_pause(2, hard = True)
    show text "{color=[text_color]}THE CONTENT FROM OR THROUGH THIS GAME ARE PROVIDED “AS-IS,” “AS AVAILABLE,” AND ALL WARRANTIES, EXPRESSED OR IMPLIED, ARE DISCLAIMED (INCLUDING BUT NOT LIMITED TO THE DISCLAIMER OF ANY IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE). IT MAY CONTAIN BUGS, ERRORS, PROBLEMS OR OTHER LIMITATIONS. THE OWNER OF THIS GAME ASSUMES NO LIABILITY OR RESPONSIBILITY FOR ANY ERRORS OR OMISSIONS. WARNING. This game contains sexually oriented adult material intended for individuals 18 years of age or older. If you are not yet 18, if adult material offends you, or if you are accessing this game from any country or locale where adult material is prohibited by law, PLEASE LEAVE NOW! SEXUAL ACTIVITY IN THIS GAME IS A FANTASY, IT ISN'T REALITY, THIS GAME IS NOT ADVOCATING THAT YOU REENACT ANYTHING FROM ITS CONTENT. ALL CHARACTERS PORTRAYED IN THIS GAME ARE AT LEAST 18 YEARS OLD. If you understand and accept these terms, you may ENTER.{/color}" with dissolve
    $ rfr_pause(5, hard = True)
    show text "{color=[text_color]}The story is about our hero's early life. {/color}" with dissolve
    $ rfr_pause(4, hard = True)
    show text "{color=[text_color]}This is a beta version. Bugs, spelling errors etc may occur{/color}" with dissolve
    $ rfr_pause(4, hard = True)
    show text "{color=[text_color]}A very special thanks to my alpha test dream team - Lukumo, WhiteWolf, Hellster, squid44,  and Burg. You're doing a fantastic job.{/color}" with dissolve
    $ rfr_pause(4, hard = True)
    show text "{color=[text_color]}A very special thanks to Lukumo for the WT, Whitewolf for taking care of my Discord channel and Chtwillou and Lewis as my partner on this game{/color}" with dissolve
    $ rfr_pause(4, hard = True)
    show text "{color=[text_color]}(c) 2019 - 2024 Ce La Vie Group, All Rights Reserved{/color}" with dissolve
    $ rfr_pause(2, hard = True)
    hide text with dissolve
    menu:
        "{color=[text_color]}I am 18 years old or above {/color}":
            jump agecheck
        "{color=[text_color]}I am below 18 years old{/color}":
            jump agecheck1

label agecheck:
    show text "{size=100}{color=[text_color]} This game is for personal use only {/color}{/size}" with dissolve
    $ rfr_pause(2, hard = True)
    show text "{size=100}{color=[text_color]} Any copy or link to all or any part of this game is strictly prohibited {/color}{/size}" with dissolve
    $ rfr_pause(3, hard = True)
    scene black with dissolve
    hide text
    $ rfr_pause(1, hard = True)
    return

label agecheck1:
    "{color=[text_color]}YOU CAN'T PLAY IF YOU'RE YOUNGER THAN 18{/color}"
    $ renpy.quit()

label gamequit:
    scene intro_backe11 with dissolve
    show text "{size=50}{color=#000} Thank you for playing 'My Early Life'{/color}{/size}" with dissolve
    pause 1
    show text "{size=50}{color=#000}  Please click the Patreon mark to visit my site{/color}{/size}" with dissolve
    show screen custom
    pause 1
    jump end

label quit:
    scene intro_backe11
    show screen custom
    call info from _call_info
    jump end

label info:
    show text "{size=50}{color=#000} Thank you for playing 'My Early Life'{/color}{/size}"
    pause 1
    show text "{size=50}{color=#000}  Please click the logos to visit my sites{/color}{/size}"
    pause 1
    return

label GAMEOVER:
    show text "{size=50}{color=#fff} You've failed in earning enough money...{/color}{/size}"
    pause 1
    show text "{size=50}{color=#fff} This game is over... Try harder next time...{/color}{/size}"
    pause 1
    $ MainMenu(confirm=False)()

label end:
    return

init -501 python:
    def _pause (pdelay = 1.0, hard = False):
        renpy.pause ((pdelay * delay_factor), hard = (hard and hard_indicator))

label withdraw():
    if WebGenMoney > 0:
        label ReqWithdraw:
            $ Withdraw = renpy.input("How much do you want to withdraw? (between 1 and [WebGenMoney])")
            if Withdraw.isdigit():
                $ Withdraw = int(Withdraw)
            else:
                "Wrong request..."
                jump ReqWithdraw
        
        if Withdraw > WebGenMoney:
            "You can only withdraw [WebGenMoney]$. They will be added to your account"
            $ BobObj.Money += WebGenMoney
            $ WebGenMoney = 0
        else:
            $ BobObj.Money += Withdraw
            $ WebGenMoney -= Withdraw
            "$[Withdraw] have been added to your account"

        $ BobObj.Money = round(BobObj.Money)
    else:
        "Sorry, you have nothing to withdraw..."   
    return

label Diningroom:
    #hide screen QuickStats
    $ curLoc = "Dining room"
    $ curLocForEvent = "Diningroom"

    if DiningRoomFirstVisit:
        $ DiningRoomFirstVisit = False    
        scene diningroom_bg with dissolve
        m "This is our dining room"        
    else:
        scene diningroom_bg with dissolve     
    
    $ LinaObj.GetLocation(Date)
    $ LynnObj.GetLocation(Date)
    $ EveObj.GetLocation(Date)
    #show screen Header()
    #show screen LocationsSubMenu()

    return

label Bathroom:
    $ curLoc = "Bathroom"
    $ curLocForEvent = "Bathroom"

    if BathroomFirstVisit:
        $ BathroomFirstVisit = False       
        scene bathroome11 with dissolve
        m "This is our bathroom"
    else:
        scene bathroome11 with dissolve     

    return

label Kitchen:
    $ curLoc = "Kitchen"
    $ curLocForEvent = "Kitchen"

    if KitchenFirstVisit:  
        $ KitchenFirstVisit = False     
        scene kitchene11 with dissolve
        m "This is our kitchen"
    else:
        scene kitchene11 with dissolve    

    return

label BobRoom:
    $ curLoc = "Bob's Room"
    $ curLocForEvent = "BobRoom"
    scene bobroom_bg with dissolve

    if BobRoomFirstVisit: 
        $ BobRoomFirstVisit = False
        m "This is my bedroom"
        
    else:
        if FirstSundayPassed:
            if Date.Hours == 6 and Date.Minutes == 50:
                hide screen Header
                hide screen BobRoomIcons
                $ StudyLeft = 15 - BobStudyHours
                if StudyLeft > 0:
                    "You still need to study [StudyLeft] hours before Sunday - 20:00. Otherwise, the game will end for you! Click the tool icon in the upper right corner to study"
                else:
                    "You've studied enough this week. Congratulations!"
                    if CurrentEpisode == 1:
                        $ EVENTS[27].SetDone()

                $ Date.Hours = 7
                $ Date.Minutes = 0
                show screen BobRoomIcons()
                jump GAMECONTINUE    

    show screen BobRoomIcons()

    return

label LinaRoom:
    $ curLoc = "[nameOfLina]'s Bedroom"
    $ curLocForEvent = "LinaRoom"

    if LinaRoomFirstVisit:  
        $ LinaRoomFirstVisit = False   
        scene linaroom_bg with dissolve
        m "This is Lina's bedroom"
    else:
        scene linaroom_bg with dissolve
       

    
    return

label LynnRoom:
    $ curLoc = "Lynn's Room"
    $ curLocForEvent = "LynnRoom"

    if LynnRoomFirstVisit:    
        $ LynnRoomFirstVisit = False 
        scene lynnroom_bg with dissolve
        m "This is Lynn's bedroom"
    else:
        #scene expression "1614sh[lysh]" with dissolve
        scene lynnroom_bg with dissolve

    return

label EveRoom:
    $ curLoc = "Eve's Room"
    $ curLocForEvent = "EveRoom"

    if EveRoomFirstVisit:  
        $ EveRoomFirstVisit = False 
        scene everoom_bg with dissolve
        m "This is Eve's bedroom"
    else:
        scene everoom_bg with dissolve
           
    return

label LivingRoom:
    $ curLoc = "Living Room"
    $ curLocForEvent = "LivingRoom"

    if TVRoomFirstVisit:  
        $ TVRoomFirstVisit = False     
        scene tvroom_bg with dissolve
        m "This is the TV room"
    else:
        scene tvroom_bg with dissolve     
    
    return

label Pool:
    $ curLoc = "Pool"
    $ curLocForEvent = "Pool"

    if PoolFirstVisit:  
        
        $ PoolFirstVisit = False     
        scene pool_bg with dissolve
        m "This is our pool"
    else:
        scene pool_bg with dissolve     
    
    return

# Label called when we want to add an hour
label add1hour:
    $ Date.AddHours(1)
    return

# Label called when we want to add two hours
label add2hours:
    $ Date.AddHours(2)
    return  

# Label called when we want to 30 minutes
label add30min:
    $ Date.AddMinutes(30)
    return

# Label called when we want to advance one day
# We'll jump on the day after at 07:00AM on WorkingDays and 09:00AM on Weekend
label changeDay:    
    if Date.Hours >= 0 and Date.Hours <= 2:
        if Date.WeekdaysList[Date.DayInWeek] in WeekendTuple:
            $ Date.Hours = 9
            $ Date.Minutes = 0
        else:
            $ Date.Hours = 7
            $ Date.Minutes = 0
    else:
        $ Date.AddHours(24)
        if Date.WeekdaysList[Date.DayInWeek] in WeekendTuple:
            $ Date.Hours = 9
            $ Date.Minutes = 0
        else:
            $ Date.Hours = 7
            $ Date.Minutes = 0
    return

# Label called when we want to read about yoga
label ReadYoga:
    $ Reading("Yoga")
    call add1hour
    return

# Label called when we want to read about hacking
label ReadHack:
    $ Reading("Hack")
    call add1hour
    return

# Label called when we want to read about photo
label ReadPhoto:
    $ Reading("Photo")
    call add1hour
    return

# Label called when we want to study
label Study:
    $ Study()
    call add1hour
    return

# Label called when we want to study
label Sport:
    $ Sport()
    call add1hour
    return
    