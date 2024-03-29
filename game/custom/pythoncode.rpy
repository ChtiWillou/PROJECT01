init python:
    def rfr_pause (pdelay = 1.0, hard = False):
        renpy.pause ((pdelay * delay_factor), hard = (hard and hard_indicator))
    
    def Reading(topic):
        global NbHackRead
        global NbYogaRead
        global NbPhotoRead
        global NbHackReadHoursForSkill
        global NbYogaReadHoursForSkill
        global NbPhotoReadHoursForSkill
        global BobObj
        
        if topic == "Hack":
            NbHackRead += 1
            if NbHackRead == NbHackReadHoursForSkill:
                NbHackRead = 0
                if BobObj.HackingSkills < 10:   
                    BobObj.IncreaseHackingSkills(1)              
        elif topic == "Yoga":
            NbYogaRead += 1
            if NbYogaRead == NbYogaReadHoursForSkill:
                NbYogaRead = 0
                if BobObj.YogaSkills < 10:   
                    BobObj.IncreaseYogaSkills(1)
        elif topic == "Photo":
            NbPhotoRead += 1
            if NbPhotoRead == NbPhotoReadHoursForSkill:
                NbPhotoRead = 0
                if BobObj.PhotoSkills < 10:   
                    BobObj.IncreasePhotoSkills(1)        
        return
    
    def Study():
        global NbStudyHours
        global NbStudyHoursForSkill
        global BobObj

        NbStudyHours += 1
        if NbStudyHours == NbStudyHoursForSkill:
            NbStudyHours = 0
            if BobObj.Intel < 10:   
                BobObj.IncreaseIntel(1)
    
    def Sport():
        global NbSportHours
        global NbSportHoursForSkill
        global BobObj
        
        NbSportHours += 1
        if NbSportHours == NbSportHoursForSkill:
            NbSportHours = 0
            if BobObj.Strength < 10:   
                BobObj.IncreaseStrength(1)