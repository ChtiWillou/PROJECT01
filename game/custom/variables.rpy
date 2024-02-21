label variables:
    $ PlayGame = True
    $ BlockToCall = ""
    $ EVENTS = []
    $ Events_Counter = 0
    $ MonthsTuple = ("January","February","March","April","May","June","July","August","September","October","November","December")
    $ FullWeekTuple = ("Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday")
    $ WorkingDaysTuple = ("Monday","Tuesday","Wednesday","Thursday","Friday")
    $ WeekendTuple = ("Saturday","Sunday")
    $ DaysPerMonthTuple = (31,28,31,30,31,30,31,31,30,31,30,31)

    $ Date = Calendar(10, 0, 5, 5, MonthsTuple, 5, FullWeekTuple, DaysPerMonthTuple)
      
    $ BobObj = MainCharacter("Bob", 200, 0, 0, 0, 0, 0, "BobRoom")
    
    $ EveObj = GirlCharacter("Eve", 50, 5, 1, 8, 0, "EveRoom",
        {
        "0700":"LisaRoom","0730":"LisaRoom","0800":"Bathroom","0830":"Bathroom",
        "0900":"LisaRoom","0930":"LisaRoom","1000":"School","1030":"School",
        "1100":"School","1130":"School","1200":"School","1230":"School",
        "1300":"School","1330":"School","1400":"School","1430":"School",
        "1500":"School","1530":"LisaRoom","1600":"LisaRoom","1630":"LisaRoom",
        "1700":"LisaRoom","1730":"LisaRoom","1800":"LisaRoom","1830":"LisaRoom",
        "1900":"Diningroom","1930":"Diningroom","2100":"LisaRoom","2130":"LisaRoom",
        "2100":"LisaRoom","2130":"LisaRoom","2200":"LisaRoom","2230":"LisaRoom",
        "2300":"LisaRoom","2330":"LisaRoom","0000":"LisaRoom"
        },
        {
        "0700":"LisaRoom","0730":"LisaRoom","0800":"Bathroom","0830":"Bathroom",
        "0900":"LisaRoom","0930":"LisaRoom","1000":"LisaRoom","1030":"LisaRoom",
        "1100":"Boutique","1130":"Boutique","1200":"Lingerie","1230":"Lingerie",
        "1300":"Jewelry","1330":"Jewelry","1400":"Café","1430":"Café",
        "1500":"LisaRoom","1530":"LisaRoom","1600":"LisaRoom","1630":"LisaRoom",
        "1700":"LisaRoom","1730":"LisaRoom","1800":"LisaRoom","1830":"LisaRoom",
        "1900":"Diningroom","1930":"Diningroom","2000":"LisaRoom","2030":"LisaRoom",
        "2100":"TVRoom","2130":"TVRoom","2200":"LisaRoom","2230":"LisaRoom",
        "2300":"LisaRoom","2330":"LisaRoom","0000":"LisaRoom"
        })

    $ LynnObj = GirlCharacter("Lynn", 50, 5, 2, 9, 0, "LynnRoom",
        {
        "0700":"LisaRoom","0730":"LisaRoom","0800":"Bathroom","0830":"Bathroom",
        "0900":"LisaRoom","0930":"LisaRoom","1000":"School","1030":"School",
        "1100":"School","1130":"School","1200":"School","1230":"School",
        "1300":"School","1330":"School","1400":"School","1430":"School",
        "1500":"School","1530":"LisaRoom","1600":"LisaRoom","1630":"LisaRoom",
        "1700":"LisaRoom","1730":"LisaRoom","1800":"LisaRoom","1830":"LisaRoom",
        "1900":"Diningroom","1930":"Diningroom","2100":"LisaRoom","2130":"LisaRoom",
        "2100":"LisaRoom","2130":"LisaRoom","2200":"LisaRoom","2230":"LisaRoom",
        "2300":"LisaRoom","2330":"LisaRoom","0000":"LisaRoom"
        },
        {
        "0700":"LisaRoom","0730":"LisaRoom","0800":"Bathroom","0830":"Bathroom",
        "0900":"LisaRoom","0930":"LisaRoom","1000":"LisaRoom","1030":"LisaRoom",
        "1100":"Boutique","1130":"Boutique","1200":"Lingerie","1230":"Lingerie",
        "1300":"Jewelry","1330":"Jewelry","1400":"Café","1430":"Café",
        "1500":"LisaRoom","1530":"LisaRoom","1600":"LisaRoom","1630":"LisaRoom",
        "1700":"LisaRoom","1730":"LisaRoom","1800":"LisaRoom","1830":"LisaRoom",
        "1900":"Diningroom","1930":"Diningroom","2000":"LisaRoom","2030":"LisaRoom",
        "2100":"TVRoom","2130":"TVRoom","2200":"LisaRoom","2230":"LisaRoom",
        "2300":"LisaRoom","2330":"LisaRoom","0000":"LisaRoom"
        })
    
    $ LinaObj = GirlCharacter("Lina", 50, 5, 2, 10, 0, "LinaRoom",
        {
        "0700":"LisaRoom","0730":"LisaRoom","0800":"Bathroom","0830":"Bathroom",
        "0900":"LisaRoom","0930":"LisaRoom","1000":"School","1030":"School",
        "1100":"School","1130":"School","1200":"School","1230":"School",
        "1300":"School","1330":"School","1400":"School","1430":"School",
        "1500":"School","1530":"LisaRoom","1600":"LisaRoom","1630":"LisaRoom",
        "1700":"LisaRoom","1730":"LisaRoom","1800":"LisaRoom","1830":"LisaRoom",
        "1900":"Diningroom","1930":"Diningroom","2100":"LisaRoom","2130":"LisaRoom",
        "2100":"LisaRoom","2130":"LisaRoom","2200":"LisaRoom","2230":"LisaRoom",
        "2300":"LisaRoom","2330":"LisaRoom","0000":"LisaRoom"
        },
        {
        "0700":"LisaRoom","0730":"LisaRoom","0800":"Bathroom","0830":"Bathroom",
        "0900":"LisaRoom","0930":"LisaRoom","1000":"LisaRoom","1030":"LisaRoom",
        "1100":"Boutique","1130":"Boutique","1200":"Lingerie","1230":"Lingerie",
        "1300":"Jewelry","1330":"Jewelry","1400":"Café","1430":"Café",
        "1500":"LisaRoom","1530":"LisaRoom","1600":"LisaRoom","1630":"LisaRoom",
        "1700":"LisaRoom","1730":"LisaRoom","1800":"LisaRoom","1830":"LisaRoom",
        "1900":"Diningroom","1930":"Diningroom","2000":"LisaRoom","2030":"LisaRoom",
        "2100":"TVRoom","2130":"TVRoom","2200":"LisaRoom","2230":"LisaRoom",
        "2300":"LisaRoom","2330":"LisaRoom","0000":"LisaRoom"
        })

    default curLoc = ""
    default curLocForEvent = ""
    default DiningRoomFirstVisit = True
    default BathroomFirstVisit = True
    default KitchenFirstVisit = True
    default TVRoomFirstVisit = True
    default BobRoomFirstVisit = True
    default LinaRoomFirstVisit = True
    default LynnRoomFirstVisit = True
    default EveRoomFirstVisit = True
    default JacuzziFirstVisit = True
    default NbHackReadHoursForSkill = 5
    default NbYogaReadHoursForSkill = 5
    default NbPhotoReadHoursForSkill = 5
    default NbSportHoursForSkill = 5
    default NbStudyHoursForSkill = 10
    default NbHackRead = 0
    default NbYogaRead = 0
    default NbPhotoRead = 0
    default NbStudyHours = 0
    default NbSportHours = 0

    return