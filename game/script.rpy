# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

default Bob = "Bob"
default Lynn = "Lynn"
default Lina = "Lina"
default Eve = "Eve"
default nameOfLawyer = "Lawyer"
default nameOfBob = "Bob"
default nameOfLynn = "Lynn"
default nameOfLina = "Lina"
default nameOfEve = "Eve"
define m = Character("[nameOfBob]", image = "bob")
define t = Character("Me, thinking", image = "bob")
define ev = Character("[nameOfEve]", image = "eve")
define ly = Character("[nameOfLynn]", image="lynn")
define li = Character("[nameOfLina]", image="lina")
define la = Character("[nameOfLawyer]", image="lawyer")
define ol = Character("Old man")
define gl = Character("Boutique Woman")
define gg = Character("Grocerie girl")
define eveboyfriend = Character("[ev]'s boyfriend")
define boss = Character("[ev]'s boss")
define boy2 = Character("Friend")
define boy1 = Character("Friend")
define je = Character("Jenny")
define wi = Character("Winnie")
define fa = Character("Fabienne")
define man = Character("Man")
default GalleryList = []

default hard_indicator = True
default delay_factor = 1.0
default text_color ="#FFF"
default wcolor = "#fff"
default bcolor = "#000"

default WebGenMoney = 500
default Withdraw = 0
default prologue = 1

# The game starts here.

label start:
    call variables

    if prologue == 1:
        call variables from _call_variables
        scene 742e11 with dissolve
        "Do you want to see the Introduction?"
        menu:
            "Yes, show me the beginning of the story again":
                jump pre_story
            "No, I've seen it already":
                jump GAME
    else:
        $ prologue = 1
        jump pre_story   
    
    
    #jump GAME

    
