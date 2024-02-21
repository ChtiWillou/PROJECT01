##########################################Custom Screens#########################
screen custom():
    vbox xalign 1.0 yalign 0.3:
        imagebutton auto "gui/exit_%s.png" action OpenURL("https://www.patreon.com/celaviegroup")
        vbox xalign 0.0 yalign 0.5:
            imagebutton auto "gui/subs_%s.png" action OpenURL("https://subscribestar.adult/celaviegroup")

screen BobRoomIcons():
    frame:
        background None
        xalign 0.90 yalign 0.0
        hbox:
            if (Date.Hours >= 6 and Date.Hours <= 23):
                imagebutton:
                    idle "comp_icon_idle"
                    hover "comp_icon_hover"
                    hovered Show("disp_info",None,info="Go on computer")#, Hide("LocationsSubMenu")
                    unhovered Hide("disp_info")
                    action Hide("Picture_exchange"), Hide("disp_info"), Hide("ActionsSubMenu")#, Call("selling_pictures")
                if BobObj.Intel < 10:
                    imagebutton:
                        idle "study_icon_idle"
                        hover "study_icon_hover"
                        hovered Show("disp_info",None,info="Study 1 hour")#, Hide("LocationsSubMenu")
                        unhovered Hide("disp_info")
                        action Hide("disp_info"), Hide("ActionsSubMenu"), Call("Study")
                if BobObj.Strength < 10:        
                    imagebutton:
                        idle "sport_icon_idle"
                        hover "sport_icon_hover"
                        hovered Show("disp_info",None,info="Sport 1 hour")#, Hide("LocationsSubMenu")
                        unhovered Hide("disp_info")
                        action Hide("disp_info"), Hide("ActionsSubMenu"), Call("Sport")
                if BobObj.HackingSkills < 10:
                    imagebutton:
                        idle "hack_icon_idle"
                        hover "hack_icon_hover"
                        hovered Show("disp_info",None,info="Read about Hacking")#, Hide("LocationsSubMenu")
                        unhovered Hide("disp_info")
                        action Hide("disp_info"), Hide("ActionsSubMenu"), Call("ReadHack")
                if BobObj.YogaSkills < 10:
                    imagebutton:
                        idle "yoga_icon_idle"
                        hover "yoga_icon_hover"
                        hovered Show("disp_info",None,info="Read about Yoga")#, Hide("LocationsSubMenu")
                        unhovered Hide("disp_info")
                        action Hide("disp_info"), Hide("ActionsSubMenu"), Call("ReadYoga")
                if BobObj.PhotoSkills < 10:
                    imagebutton:
                        idle "photo_icon_idle"
                        hover "photo_icon_hover"
                        hovered Show("disp_info",None,info="Read about Photography")#, Hide("LocationsSubMenu")
                        unhovered Hide("disp_info")
                        action Hide("disp_info"), Hide("ActionsSubMenu"), Call("ReadPhoto")                                         
                imagebutton:
                        idle "money_icon_idle"
                        hover "money_icon_hover"
                        hovered Show("disp_info",None,info="Withdraw")#, Hide("LocationsSubMenu")
                        unhovered Hide("disp_info")
                        action Hide("disp_info"), Hide("ActionsSubMenu"), Call("withdraw")

screen Header():
    frame:
        background "#00000060"
        xalign 0.0 yalign 0.0
        xsize 1920 ysize 50
        padding 0,0
        margin 0,0        

        frame:
            background None
            xalign 0.0 yalign 0.0
            hbox:
                imagebutton:
                    idle "user_icon_idle"
                    hover "user_icon_hover"
                    hovered Show("disp_info",None,info="Show Stats"), Hide("TimeSubMenu")#, Hide("LocationsSubMenu")#, Show("QuickStats")
                    unhovered Hide("disp_info")#, Hide("QuickStats")
                    action Hide("disp_info"), ToggleScreen("QuickStats")
                
                if (Date.Hours >= 6 and Date.Hours <= 23):         #(Date.Hours >= 0 and Date.Hours <= 1) or        
                    imagebutton:
                        idle "time_icon_idle"
                        hover "time_icon_hover"
                        #hovered Show("disp_info",None,info="Add time")#, Hide("LocationsSubMenu")
                        #unhovered Hide("disp_info")
                        #action Hide("disp_info"), ToggleScreen("TimeSubMenu")
                        hovered Show("disp_info",None,info="Add 1 hour")
                        unhovered Hide("disp_info")
                        action Hide("disp_info"), Call("add1hour")#Hide("TimeSubMenu"), 
                else:
                    imagebutton:
                        idle "empty"
                if (Date.Hours >= 6 and Date.Hours <= 23):
                    imagebutton:  
                        idle "nextday_icon_idle"
                        hover "nextday_icon_hover"
                        hovered Show("disp_info",None,info="Go to next day"), Hide("TimeSubMenu")#, Hide("LocationsSubMenu")
                        unhovered Hide("disp_info")
                        action Hide("disp_info"), Call("changeDay")
                else:
                    imagebutton:  
                        idle "sleep_icon_idle"
                        hover "sleep_icon_hover"
                        hovered Show("disp_info",None,info="Go to next day"), Hide("TimeSubMenu"), Hide("LocationsSubMenu")
                        unhovered Hide("disp_info")
                        action Hide("disp_info"), Call("changeDay")
        frame:
            background None
            xalign 0.2 yalign 0.0
            ysize 50
            padding 0,0
            margin 0,0
            textbutton "{size=25}[Date.Output]{/size}" text_color "#ffffff" yalign 0.5

        #frame:
        #    background None
        #    xalign 1.0 yalign 0.0
        #   
        #    hbox:            
                
screen disp_info(info):
    frame:        
        background None        
        ysize 50
        padding 0,0
        margin 0,0
        xalign 0.5 yalign 0.0
        text "[info]" yalign 0.5

screen LocationsSubMenu():
    frame:
        background None # "#00000060"
        xalign 1.0 ypos 60
        xsize 85 ysize 1000
        padding 5,0
        margin 0,0
        vbox:
            xalign 1.0
            imagebutton:
                idle "bedroom_icon_idle"
                hover "bedroom_icon_hover"
                hovered Show("disp_info",None,info="Move to Bob's Room")
                unhovered Hide("disp_info")
                action Hide("disp_info"), Show("BobRoomIcons"), SetVariable("curLocForEvent","BobRoom"), Jump("GAMECONTINUE")               
            
            #imagebutton:
            #    xalign 1.0
            #    idle "bedroom_icon_idle"
            #    hover "bedroom_icon_hover"
            #    hovered Show("disp_info",None,info="Move to Bob's Room")
            #    unhovered Hide("disp_info")
            #    action Hide("LocationsSubMenu"), Hide("disp_info"), Show("BobRoomIcons"), SetVariable("curLocForEvent","BobRoom"), Jump("GAMECONTINUE")
            imagebutton:
                xalign 1.0
                idle "bedroom2_icon_idle"
                hover "bedroom2_icon_hover"
                hovered Show("disp_info",None,info="Move to Lina's Room")
                unhovered Hide("disp_info")
                action Hide("BobRoomIcons"), Hide("disp_info"), SetVariable("curLocForEvent","LinaRoom"), Jump("GAMECONTINUE")
            imagebutton:
                xalign 1.0
                idle "bedroom2_icon_idle"
                hover "bedroom2_icon_hover"
                hovered Show("disp_info",None,info="Move to Lynn's Room")
                unhovered Hide("disp_info")
                action Hide("BobRoomIcons"), Hide("disp_info"), SetVariable("curLocForEvent","LynnRoom"), Jump("GAMECONTINUE")
            imagebutton:
                xalign 1.0
                idle "bedroom2_icon_idle"
                hover "bedroom2_icon_hover"
                hovered Show("disp_info",None,info="Move to Eve's Room")
                unhovered Hide("disp_info")
                action Hide("BobRoomIcons"), Hide("disp_info"), SetVariable("curLocForEvent","EveRoom"), Jump("GAMECONTINUE")
            imagebutton:
                xalign 1.0
                idle "kitchen_icon_idle"
                hover "kitchen_icon_hover"
                hovered Show("disp_info",None,info="Move to Kitchen")
                unhovered Hide("disp_info")
                action Hide("BobRoomIcons"), Hide("disp_info"), SetVariable("curLocForEvent","Kitchen"), Jump("GAMECONTINUE")
            imagebutton:
                xalign 1.0
                idle "tv_icon_idle"
                hover "tv_icon_hover"
                hovered Show("disp_info",None,info="Move to Living Room")
                unhovered Hide("disp_info")
                action Hide("BobRoomIcons"), Hide("disp_info"), SetVariable("curLocForEvent","LivingRoom"), Jump("GAMECONTINUE")
            imagebutton:
                xalign 1.0
                idle "bath_icon_idle"
                hover "bath_icon_hover"
                hovered Show("disp_info",None,info="Move to Bathroom")
                unhovered Hide("disp_info")
                action Hide("BobRoomIcons"), Hide("disp_info"), SetVariable("curLocForEvent","Bathroom"), Jump("GAMECONTINUE")
            imagebutton:
                xalign 1.0
                idle "jacuzzi_icon_idle"
                hover "jacuzzi_icon_hover"
                hovered Show("disp_info",None,info="Move to Pool")
                unhovered Hide("disp_info")
                action Hide("BobRoomIcons"), Hide("disp_info"), SetVariable("curLocForEvent","Pool"), Jump("GAMECONTINUE")
    
    frame:
        background None
        if LynnObj.Location <> "":          
            if LynnObj.Location == "BobRoom":
                imagebutton idle "small_lynn" xpos 1875 ypos 45 at reduce_navgirl_icons
            if LynnObj.Location == "LinaRoom":
                imagebutton idle "small_lynn" xpos 1875 ypos 115 at reduce_navgirl_icons
            if LynnObj.Location == "LynnRoom":
                imagebutton idle "small_lynn" xpos 1875 ypos 185 at reduce_navgirl_icons
            if LynnObj.Location == "EveRoom":
                imagebutton idle "small_lynn" xpos 1875 ypos 255 at reduce_navgirl_icons
            if LynnObj.Location == "Kitchen":
                imagebutton idle "small_lynn" xpos 1875 ypos 325 at reduce_navgirl_icons
            if LynnObj.Location == "TVRoom":
                imagebutton idle "small_lynn" xpos 1875 ypos 395 at reduce_navgirl_icons
            if LynnObj.Location == "Bathroom":
                imagebutton idle "small_lynn" xpos 1875 ypos 465 at reduce_navgirl_icons
            if LynnObj.Location == "Pool":
                imagebutton idle "small_lynn" xpos 1875 ypos 535 at reduce_navgirl_icons

        if LinaObj.Location <> "":          
            if LinaObj.Location == "BobRoom":
                imagebutton idle "small_lina" xpos 1835 ypos 45 at reduce_navgirl_icons
            if LinaObj.Location == "LinaRoom":
                imagebutton idle "small_lina" xpos 1835 ypos 115 at reduce_navgirl_icons
            if LinaObj.Location == "LynnRoom":
                imagebutton idle "small_lina" xpos 1835 ypos 185 at reduce_navgirl_icons
            if LinaObj.Location == "EveRoom":
                imagebutton idle "small_lina" xpos 1835 ypos 255 at reduce_navgirl_icons
            if LinaObj.Location == "Kitchen":
                imagebutton idle "small_lina" xpos 1835 ypos 325 at reduce_navgirl_icons
            if LinaObj.Location == "TVRoom":
                imagebutton idle "small_lina" xpos 1835 ypos 395 at reduce_navgirl_icons
            if LinaObj.Location == "Bathroom":
                imagebutton idle "small_lina" xpos 1835 ypos 465 at reduce_navgirl_icons
            if LinaObj.Location == "Pool":
                imagebutton idle "small_lina" xpos 1835 ypos 535 at reduce_navgirl_icons

        if EveObj.Location <> "":          
            if EveObj.Location == "BobRoom":
                imagebutton idle "small_eve" xpos 1855 ypos 80 at reduce_navgirl_icons
            if EveObj.Location == "LinaRoom":
                imagebutton idle "small_eve" xpos 1855 ypos 150 at reduce_navgirl_icons
            if EveObj.Location == "LynnRoom":
                imagebutton idle "small_eve" xpos 1855 ypos 220 at reduce_navgirl_icons
            if EveObj.Location == "EveRoom":
                imagebutton idle "small_eve" xpos 1855 ypos 290 at reduce_navgirl_icons
            if EveObj.Location == "Kitchen":
                imagebutton idle "small_eve" xpos 1855 ypos 360 at reduce_navgirl_icons
            if EveObj.Location == "TVRoom":
                imagebutton idle "small_eve" xpos 1855 ypos 430 at reduce_navgirl_icons
            if EveObj.Location == "Bathroom":
                imagebutton idle "small_eve" xpos 1855 ypos 500 at reduce_navgirl_icons
            if EveObj.Location == "Pool":
                imagebutton idle "small_eve" xpos 1855 ypos 570 at reduce_navgirl_icons

screen StatsSubMenu():
    frame:
        background "#00000060"
        xpos 0 ypos 80
        xsize 100 ysize 70
        padding 0,0
        margin 0,0
        vbox:
            textbutton "Bob":
                hovered Show("disp_info",None,info="Bob's Stats")
                unhovered Hide("disp_info")
                action Hide("StatsSubMenu"), Hide("disp_info")
            textbutton "Girl":
                hovered Show("disp_info",None,info="Girl's Stats")
                unhovered Hide("disp_info")
                action Hide("StatsSubMenu"), Hide("disp_info")              

screen TimeSubMenu():
    frame:
        background "#00000060"
        xpos 80 ypos 80
        xsize 180 ysize 110
        padding 0,0
        margin 0,0
        vbox:
            textbutton "Add 30 minutes":
                hovered Show("disp_info",None,info="Add 30 minutes")
                unhovered Hide("disp_info")
                action Hide("TimeSubMenu"), Hide("disp_info"), Call("add30min")
            textbutton "Add 1 hour":
                hovered Show("disp_info",None,info="Add 1 hour")
                unhovered Hide("disp_info")
                action Hide("TimeSubMenu"), Hide("disp_info"), Call("add1hour")
            textbutton "Add 2 hours":
                hovered Show("disp_info",None,info="Add 2 hours")
                unhovered Hide("disp_info")
                action Hide("TimeSubMenu"), Hide("disp_info"), Call("add2hours")

screen QuickStats():
    #modal True
    frame:
        background 'gui/frame_stats.png'
        xalign 0.5 ypos 80
        xsize 1210 ysize 920
        padding 0,0
        margin 0,0
        #vbox:
        #Display Bob's Stats
        frame:
            background 'gui/frame_stats_title.png'           
            xpos 10 ypos 10
            xsize 1190 ysize 80
            padding 0,0
            margin 0,0
            vbox:
                xalign 0.5
                textbutton "{size=20}{color=[wcolor]}{b}[BobObj.Name]'s quick stats{/b}{/color}{/size}"
                textbutton "{size=15}{color=[wcolor]}You have [BobObj.Money] ${/color}{/size}"
        
        frame:
            background "#e0e0e052"
            xpos 10 ypos 100
            xsize 390 ysize 200
            padding 0,0
            margin 0,0
            vbox:
                xalign 0.5 
                $ sp = NbSportHoursForSkill - NbSportHours
                textbutton "{size=17}{color=[wcolor]}{b}Your Strength is [BobObj.Strength] / 10{/b}{/color}{/size}" xalign 0.5 
                if BobObj.Strength < 10:
                    textbutton "{size=15}{color=[wcolor]}Do sport for [sp]h to improve{/color}{/size}" xalign 0.5
                else:
                    textbutton "{size=15}{color=[wcolor]}You're at the maximum of Strength{/color}{/size}" xalign 0.5
                                
                bar value StaticValue(BobObj.Strength, 10) xpos 5 xsize 310 ysize 15
                bar value StaticValue(NbSportHours, NbSportHoursForSkill) xpos 5 xsize 310 ysize 15 style "graybar"
                
                $ st = NbStudyHoursForSkill - NbStudyHours
                textbutton "{size=17}{color=[wcolor]}{b}Your Intel is [BobObj.Intel] / 10{/b}{/color}{/size}" xalign 0.5 
                if BobObj.Intel < 10:
                    textbutton "{size=15}{color=[wcolor]}Study [st]h to improve{/color}{/size}" xalign 0.5
                else:
                    textbutton "{size=15}{color=[wcolor]}You're at the maximum of Intel{/color}{/size}" xalign 0.5
                
                bar value StaticValue(BobObj.Intel, 10) xpos 5 xsize 310 ysize 15
                bar value StaticValue(NbStudyHours, NbStudyHoursForSkill) xpos 5 xsize 310 ysize 15 style "graybar"
        frame:
            background "#e0e0e052"
            xpos 410 ypos 100
            xsize 390 ysize 200
            padding 0,0
            margin 0,0    
            vbox:
                xalign 0.5 
                $ yo = NbYogaReadHoursForSkill - NbYogaRead
                textbutton "{size=17}{color=[wcolor]}{b}Your Yoga Skills are [BobObj.YogaSkills] / 10{/b}{/color}{/size}" xalign 0.5 
                if BobObj.YogaSkills < 10:
                    textbutton "{size=15}{color=[wcolor]}Read about Yoga [yo]h to improve{/color}{/size}" xalign 0.5
                else:
                    textbutton "{size=15}{color=[wcolor]}You're at the maximum of Yoga skills{/color}{/size}" xalign 0.5
                
                bar value StaticValue(BobObj.YogaSkills, 10) xpos 5 xsize 310 ysize 15
                bar value StaticValue(NbYogaRead, NbYogaReadHoursForSkill) xpos 5 xsize 310 ysize 15 style "graybar"
                
                $ ha = NbHackReadHoursForSkill - NbHackRead
                textbutton "{size=17}{color=[wcolor]}{b}Your Hacking Skills are [BobObj.HackingSkills] / 10{/b}{/color}{/size}" xalign 0.5 
                if BobObj.HackingSkills < 10:
                    textbutton "{size=15}{color=[wcolor]}Read about Hacking [ha]h to improve{/color}{/size}" xalign 0.5 
                else:
                    textbutton "{size=15}{color=[wcolor]}You're at the maximum of Hacking skills{/color}{/size}" xalign 0.5

                bar value StaticValue(BobObj.HackingSkills, 10) xpos 5 xsize 310 ysize 15 
                bar value StaticValue(NbHackRead, NbHackReadHoursForSkill) xpos 5 xsize 310 ysize 15 style "graybar"
        frame:
            background "#e0e0e052"
            xpos 810 ypos 100
            xsize 390 ysize 200
            padding 0,0
            margin 0,0   
            vbox:
                xalign 0.5 
                $ ph = NbPhotoReadHoursForSkill - NbPhotoRead
                textbutton "{size=17}{color=[wcolor]}{b}Your Photography Skills are [BobObj.PhotoSkills] / 10{/b}{/color}{/size}" xalign 0.5 
                if BobObj.PhotoSkills < 10:
                    textbutton "{size=15}{color=[wcolor]}Read about Photography [ph]h to improve{/color}{/size}" xalign 0.5
                else:
                    textbutton "{size=15}{color=[wcolor]}You're at the maximum of Photography skills{/color}{/size}" xalign 0.5
                                
                bar value StaticValue(BobObj.PhotoSkills, 10) xpos 5 xsize 310 ysize 15
                bar value StaticValue(NbPhotoRead, NbPhotoReadHoursForSkill) xpos 5 xsize 310 ysize 15 style "graybar"

        #Other Character 1
        frame:
            background "#98ddf8a2"
            xpos 10 ypos 320
            xsize 1190 ysize 50
            padding 0,0
            margin 0,0
            vbox:
                #Display Lisa's Stats
                xalign 0.5
                textbutton "{size=20}{color=[wcolor]}{b}[EveObj.Name]'s quick stats{/b}{/color}{/size}"
                
                
        frame:
            background "#e0e0e052"
            xpos 10 ypos 380
            xsize 590 ysize 110
            padding 0,0
            margin 0,0            
            vbox: 
                xalign 0.5               
                textbutton "{size=15}{color=[wcolor]}Her mood is [EveObj.Mood] / 10{/color}{/size}" xalign 0.5
                if EveObj.Mood >= 8:
                    bar value StaticValue(EveObj.Mood, 10) xpos 5 xsize 310 ysize 15 style "greenbar"
                elif EveObj.Mood <= 3:
                    bar value StaticValue(EveObj.Mood, 10) xpos 5 xsize 310 ysize 15 style "redbar"
                else:
                    bar value StaticValue(EveObj.Mood, 10) xpos 5 xsize 310 ysize 15
                
                textbutton "{size=15}{color=[wcolor]}Her feelings are [EveObj.Feelings] / 10{/color}{/size}" xalign 0.5
                if EveObj.Feelings >= 8:
                    bar value StaticValue(EveObj.Feelings, 10) xpos 5 xsize 310 ysize 15 style "greenbar"
                elif EveObj.Feelings <= 3:
                    bar value StaticValue(EveObj.Feelings, 10) xpos 5 xsize 310 ysize 15 style "redbar"
                else:
                    bar value StaticValue(EveObj.Feelings, 10) xpos 5 xsize 310 ysize 15
        
        frame:
            background "#e0e0e052"
            xpos 610 ypos 380
            xsize 590 ysize 110
            padding 0,0
            margin 0,0   
            vbox:
                xalign 0.5 
                textbutton "{size=15}{color=[wcolor]}Her shyness is [EveObj.Shyness] / 10{/color}{/size}" xalign 0.5
                if EveObj.Shyness >= 8:
                    bar value StaticValue(EveObj.Shyness, 10) xpos 5 xsize 310 ysize 15 style "redbar"
                elif EveObj.Shyness <= 3:
                    bar value StaticValue(EveObj.Shyness, 10) xpos 5 xsize 310 ysize 15 style "greenbar"
                else:
                    bar value StaticValue(EveObj.Shyness, 10) xpos 5 xsize 310 ysize 15
                
                textbutton "{size=15}{color=[wcolor]}Her arousal is [EveObj.Arousal] / 10{/color}{/size}" xalign 0.5
                if EveObj.Arousal >= 8:
                    bar value StaticValue(EveObj.Arousal, 10) xpos 5 xsize 310 ysize 15 style "greenbar"
                elif EveObj.Arousal <= 3:
                    bar value StaticValue(EveObj.Arousal, 10) xpos 5 xsize 310 ysize 15 style "redbar"
                else:
                    bar value StaticValue(EveObj.Arousal, 10) xpos 5 xsize 310 ysize 15
        
        #Other Character 2
        frame:
            background "#98ddf8a2"
            xpos 10 ypos 510
            xsize 1190 ysize 50
            padding 0,0
            margin 0,0
            vbox:
                #Display Lisa's Stats
                xalign 0.5
                textbutton "{size=20}{color=[wcolor]}{b}[LynnObj.Name]'s quick stats{/b}{/color}{/size}"
                
                
        frame:
            background "#e0e0e052"
            xpos 10 ypos 570
            xsize 590 ysize 110
            padding 0,0
            margin 0,0   
            vbox: 
                xalign 0.5               
                textbutton "{size=15}{color=[wcolor]}Her mood is [LynnObj.Mood] / 10{/color}{/size}" xalign 0.5
                if LynnObj.Mood >= 8:
                    bar value StaticValue(LynnObj.Mood, 10) xpos 5 xsize 310 ysize 15 style "greenbar"
                elif LynnObj.Mood <= 3:
                    bar value StaticValue(LynnObj.Mood, 10) xpos 5 xsize 310 ysize 15 style "redbar"
                else:
                    bar value StaticValue(LynnObj.Mood, 10) xpos 5 xsize 310 ysize 15
                
                textbutton "{size=15}{color=[wcolor]}Her feelings are [LynnObj.Feelings] / 10{/color}{/size}" xalign 0.5
                if LynnObj.Feelings >= 8:
                    bar value StaticValue(LynnObj.Feelings, 10) xpos 5 xsize 310 ysize 15 style "greenbar"
                elif LynnObj.Feelings <= 3:
                    bar value StaticValue(LynnObj.Feelings, 10) xpos 5 xsize 310 ysize 15 style "redbar"
                else:
                    bar value StaticValue(LynnObj.Feelings, 10) xpos 5 xsize 310 ysize 15 
        
        frame:
            background "#e0e0e052"
            xpos 610 ypos 570
            xsize 590 ysize 110
            padding 0,0
            margin 0,0   
            vbox:
                xalign 0.5 
                textbutton "{size=15}{color=[wcolor]}Her shyness is [LynnObj.Shyness] / 10{/color}{/size}" xalign 0.5
                if LynnObj.Shyness >= 8:
                    bar value StaticValue(LynnObj.Shyness, 10) xpos 5 xsize 310 ysize 15 style "redbar"
                elif LynnObj.Shyness <= 3:
                    bar value StaticValue(LynnObj.Shyness, 10) xpos 5 xsize 310 ysize 15 style "greenbar"
                else:
                    bar value StaticValue(LynnObj.Shyness, 10) xpos 5 xsize 310 ysize 15
                
                textbutton "{size=15}{color=[wcolor]}Her arousal is [LynnObj.Arousal] / 10{/color}{/size}" xalign 0.5
                if LynnObj.Arousal >= 8:
                    bar value StaticValue(LynnObj.Arousal, 10) xpos 5 xsize 310 ysize 15 style "greenbar"
                elif LynnObj.Arousal <= 3:
                    bar value StaticValue(LynnObj.Arousal, 10) xpos 5 xsize 310 ysize 15 style "redbar"
                else:
                    bar value StaticValue(LynnObj.Arousal, 10) xpos 5 xsize 310 ysize 15

        #Other Character 3
        frame:
            background "#98ddf8a2"
            xpos 10 ypos 700
            xsize 1190 ysize 50
            padding 0,0
            margin 0,0
            vbox:
                #Display Lisa's Stats
                xalign 0.5
                textbutton "{size=20}{color=[wcolor]}{b}[LinaObj.Name]'s quick stats{/b}{/color}{/size}"
                
                
        frame:
            background "#e0e0e052"
            xpos 10 ypos 760
            xsize 590 ysize 110
            padding 0,0
            margin 0,0   
            vbox: 
                xalign 0.5               
                textbutton "{size=15}{color=[wcolor]}Her mood is [LinaObj.Mood] / 10{/color}{/size}" xalign 0.5
                if LinaObj.Mood >= 8:
                    bar value StaticValue(LinaObj.Mood, 10) xpos 5 xsize 310 ysize 15 style "greenbar"
                elif LinaObj.Mood <= 3:
                    bar value StaticValue(LinaObj.Mood, 10) xpos 5 xsize 310 ysize 15 style "redbar"
                else:
                    bar value StaticValue(LinaObj.Mood, 10) xpos 5 xsize 310 ysize 15
                
                textbutton "{size=15}{color=[wcolor]}Her feelings are [LinaObj.Feelings] / 10{/color}{/size}" xalign 0.5
                if LinaObj.Feelings >= 8:
                    bar value StaticValue(LinaObj.Feelings, 10) xpos 5 xsize 310 ysize 15 style "greenbar"
                elif LinaObj.Feelings <= 3:
                    bar value StaticValue(LinaObj.Feelings, 10) xpos 5 xsize 310 ysize 15 style "redbar"
                else:
                    bar value StaticValue(LinaObj.Feelings, 10) xpos 5 xsize 310 ysize 15
        
        frame:
            background "#e0e0e052"
            xpos 610 ypos 760
            xsize 590 ysize 110
            padding 0,0
            margin 0,0   
            vbox:
                xalign 0.5 
                textbutton "{size=15}{color=[wcolor]}Her shyness is [LinaObj.Shyness] / 10{/color}{/size}" xalign 0.5
                if LinaObj.Shyness >= 8:
                    bar value StaticValue(LinaObj.Shyness, 10) xpos 5 xsize 310 ysize 15 style "redbar"
                elif LinaObj.Shyness <= 3:
                    bar value StaticValue(LinaObj.Shyness, 10) xpos 5 xsize 310 ysize 15 style "greenbar"
                else:
                    bar value StaticValue(LinaObj.Shyness, 10) xpos 5 xsize 310 ysize 15
                
                textbutton "{size=15}{color=[wcolor]}Her arousal is [LinaObj.Arousal] / 10{/color}{/size}" xalign 0.5
                if LinaObj.Arousal >= 8:
                    bar value StaticValue(LinaObj.Arousal, 10) xpos 5 xsize 310 ysize 15 style "greenbar"
                elif LinaObj.Arousal <= 3:
                    bar value StaticValue(LinaObj.Arousal, 10) xpos 5 xsize 310 ysize 15 style "redbar"
                else:
                    bar value StaticValue(LinaObj.Arousal, 10) xpos 5 xsize 310 ysize 15