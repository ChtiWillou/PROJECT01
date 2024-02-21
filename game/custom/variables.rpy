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
        "0700":"EveRoom","0730":"EveRoom","0800":"Bathroom","0830":"Kitchen",
        "0900":"Pool","0930":"EveRoom","1000":"School","1030":"School",
        "1100":"School","1130":"School","1200":"School","1230":"School",
        "1300":"School","1330":"School","1400":"TVRoom","1430":"TVRoom",
        "1500":"TVRoom","1530":"EveRoom","1600":"EveRoom","1630":"EveRoom",
        "1700":"EveRoom","1730":"EveRoom","1800":"EveRoom","1830":"EveRoom",
        "1900":"Diningroom","1930":"Diningroom","2100":"EveRoom","2130":"EveRoom",
        "2100":"EveRoom","2130":"EveRoom","2200":"EveRoom","2230":"EveRoom",
        "2300":"EveRoom","2330":"EveRoom","0000":"EveRoom"
        },
        {
        "0700":"EveRoom","0730":"EveRoom","0800":"Bathroom","0830":"Kitchen",
        "0900":"Pool","0930":"EveRoom","1000":"School","1030":"School",
        "1100":"School","1130":"School","1200":"School","1230":"School",
        "1300":"School","1330":"School","1400":"TVRoom","1430":"TVRoom",
        "1500":"TVRoom","1530":"EveRoom","1600":"EveRoom","1630":"EveRoom",
        "1700":"EveRoom","1730":"EveRoom","1800":"EveRoom","1830":"EveRoom",
        "1900":"Diningroom","1930":"Diningroom","2100":"EveRoom","2130":"EveRoom",
        "2100":"EveRoom","2130":"EveRoom","2200":"EveRoom","2230":"EveRoom",
        "2300":"EveRoom","2330":"EveRoom","0000":"EveRoom"
        })

    $ LynnObj = GirlCharacter("Lynn", 50, 5, 2, 9, 0, "LynnRoom",
        {
        "0700":"LynnRoom","0730":"LynnRoom","0800":"Bathroom","0830":"Kitchen",
        "0900":"Pool","0930":"LynnRoom","1000":"School","1030":"School",
        "1100":"Pool","1130":"Pool","1200":"School","1230":"School",
        "1300":"School","1330":"School","1400":"School","1430":"School",
        "1500":"School","1530":"LynnRoom","1600":"LynnRoom","1630":"LynnRoom",
        "1700":"LynnRoom","1730":"LynnRoom","1800":"LynnRoom","1830":"LynnRoom",
        "1900":"Diningroom","1930":"Diningroom","2100":"LynnRoom","2130":"LynnRoom",
        "2100":"LynnRoom","2130":"LynnRoom","2200":"LynnRoom","2230":"LynnRoom",
        "2300":"LynnRoom","2330":"LynnRoom","0000":"LynnRoom"
        },
        {
        "0700":"LynnRoom","0730":"LynnRoom","0800":"Bathroom","0830":"Kitchen",
        "0900":"Pool","0930":"LynnRoom","1000":"School","1030":"School",
        "1100":"Pool","1130":"Pool","1200":"School","1230":"School",
        "1300":"School","1330":"School","1400":"School","1430":"School",
        "1500":"School","1530":"LynnRoom","1600":"LynnRoom","1630":"LynnRoom",
        "1700":"LynnRoom","1730":"LynnRoom","1800":"LynnRoom","1830":"LynnRoom",
        "1900":"Diningroom","1930":"Diningroom","2100":"LynnRoom","2130":"LynnRoom",
        "2100":"LynnRoom","2130":"LynnRoom","2200":"LynnRoom","2230":"LynnRoom",
        "2300":"LynnRoom","2330":"LynnRoom","0000":"LynnRoom"
        })
    
    $ LinaObj = GirlCharacter("Lina", 50, 5, 2, 10, 0, "LinaRoom",
        {
        "0700":"LinaRoom","0730":"LinaRoom","0800":"Bathroom","0830":"Bathroom",
        "0900":"LinaRoom","0930":"LinaRoom","1000":"School","1030":"School",
        "1100":"TVRomm","1130":"TVRoom","1200":"School","1230":"School",
        "1300":"School","1330":"School","1400":"Pool","1430":"Pool",
        "1500":"School","1530":"LinaRoom","1600":"LinaRoom","1630":"LinaRoom",
        "1700":"LinaRoom","1730":"LinaRoom","1800":"LinaRoom","1830":"LinaRoom",
        "1900":"Diningroom","1930":"Diningroom","2100":"LinaRoom","2130":"LinaRoom",
        "2100":"LinaRoom","2130":"LinaRoom","2200":"LinaRoom","2230":"LinaRoom",
        "2300":"LinaRoom","2330":"LinaRoom","0000":"LinaRoom"
        },
        {
        "0700":"LinaRoom","0730":"LinaRoom","0800":"Bathroom","0830":"Bathroom",
        "0900":"LinaRoom","0930":"LinaRoom","1000":"School","1030":"School",
        "1100":"TVRomm","1130":"TVRoom","1200":"School","1230":"School",
        "1300":"School","1330":"School","1400":"Pool","1430":"Pool",
        "1500":"School","1530":"LinaRoom","1600":"LinaRoom","1630":"LinaRoom",
        "1700":"LinaRoom","1730":"LinaRoom","1800":"LinaRoom","1830":"LinaRoom",
        "1900":"Diningroom","1930":"Diningroom","2100":"LinaRoom","2130":"LinaRoom",
        "2100":"LinaRoom","2130":"LinaRoom","2200":"LinaRoom","2230":"LinaRoom",
        "2300":"LinaRoom","2330":"LinaRoom","0000":"LinaRoom"
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
    default PoolFirstVisit = True
    default FirstSundayPassed = False
    default FirstMondayPassed = False
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