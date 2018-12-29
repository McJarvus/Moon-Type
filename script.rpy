# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define a = Character("Alex Jones")
define u = Character("Unknown")
define b = Character("Protaonist-kun")


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.


    # These display lines of dialogue.
    "I knew from the moment I was born - I was an InfoWarrior." 
    u "Hey kid!"
    "His voice broke through the silence of the room. His smile - those briliantly radient teeth - guided my eyes upward."
    "He stared right into my soul."
    "It was him...."
    "Alex. Fucking. Jones."
    a "You ready to take on those Globaist scumbags and save the world?"
    "His hand reached out for mine; glently, but expactantly, he held his stance and awaited my response."
    "He was testing my conviction. Testing my devotion to him and to InfoWars as a whole."
    "This time - I would not let him down."
        menu:
            "Take his hand - ACCEPT FATE"
            jump startFATE
            "Backaway - DENY FATE"
            jump firstdeath
    label firstdeath
    b "I-I..."
    "The words get caught in my throat. Tears well up from my eyes. My very SOUL cries out from my betrayal."
    "I can't beleive that I'm doing this..."
    b "I'm sorry Alex. I can't."
    "I turn away to hid my shame - to protect Alex from the cutting words that I just uttered from my SUBHUMAN mouth-hole."
    "My feet carry me away. Each step farther from the greaest of all InfoWarriors."
    a "That's a damn shame, kid."
    "His hand finally drops back to his side. His eyes are stern...."
    "At once, Alex's immeasureable disappointment and undying dedication to protecting earth break his pensiveness, he speaks:"
    a "You won't get a second chance."
    b "I know."
    a "You know I can't protect you now."
    b "I know..."
    a "And you're okay with that?"
    "His kind words pleaded me to come back."
    "But I have already made up my mind." 
    b "I am."
    "And with those words, I turn back to face Alex one last time."
    "But he's gone."
    "Spirited away like all great heros are. completely lost to me - but not to the world." 
    b "Goodbye, Alex." 
    "I'm not sure if those words will ever reach him. Hell, I'm not even sure he would even dare to listen to a scumbag like me anymore."
    "Reguardless, I walk away from here - wherever here is - certian of my fate."
    "The globalists will have my head on a pike. They will rob the world of another truthseeker. and continue ravaging the innocent."
    "I could have stopped them. WE could have stopped them."
    "But I just wan't cut out for it... My resovle was weak - already corrupted by FAKENEWS and false promises." 
    "I gave up on the InfoWar..."
    "And Alex gave up on me."
    
    label startFATE
    "I reach out for his meaty, vampire-slaying hands."
    "He accepts me unconditionally. For once in my life, I have purpose - a reason to live."
    a "Let's go, kid. We've gotta job to do, and no one but us is gonna stop those pigs from ruining our country!"
    

    # This ends the game.

    return
