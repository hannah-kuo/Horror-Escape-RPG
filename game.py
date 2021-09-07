"""
Name: Kelly Olsson & Hannah Kuo
Student number: A01030513 & A01068509
Date: April 25, 2021
"""


import doctest
import random
import sys
import itertools
from prettytable import PrettyTable


def GAME_TITLE():
    """
    Return title screen art for the game opening.

    :return: title screen art
    """
    return r"""
 ██░ ██ ▒█████  ██▀███  ██▀███  ▒█████  ██▀███      ███▄ ▄███▓▒█████  ██▒   █▓██▓█████
▓██░ ██▒██▒  ██▓██ ▒ ██▓██ ▒ ██▒██▒  ██▓██ ▒ ██▒   ▓██▒▀█▀ ██▒██▒  ██▓██░   █▓██▓█   ▀
▒██▀▀██▒██░  ██▓██ ░▄█ ▓██ ░▄█ ▒██░  ██▓██ ░▄█ ▒   ▓██    ▓██▒██░  ██▒▓██  █▒▒██▒███
░▓█ ░██▒██   ██▒██▀▀█▄ ▒██▀▀█▄ ▒██   ██▒██▀▀█▄     ▒██    ▒██▒██   ██░ ▒██ █░░██▒▓█  ▄
░▓█▒░██░ ████▓▒░██▓ ▒██░██▓ ▒██░ ████▓▒░██▓ ▒██▒   ▒██▒   ░██░ ████▓▒░  ▒▀█░ ░██░▒████▒
 ▒ ░░▒░░ ▒░▒░▒░░ ▒▓ ░▒▓░ ▒▓ ░▒▓░ ▒░▒░▒░░ ▒▓ ░▒▓░   ░ ▒░   ░  ░ ▒░▒░▒░   ░ ▐░ ░▓ ░░ ▒░ ░
 ▒ ░▒░ ░ ░ ▒ ▒░  ░▒ ░ ▒░ ░▒ ░ ▒░ ░ ▒ ▒░  ░▒ ░ ▒░   ░  ░      ░ ░ ▒ ▒░   ░ ░░  ▒ ░░ ░  ░
 ░  ░░ ░ ░ ░ ▒   ░░   ░  ░░   ░░ ░ ░ ▒   ░░   ░    ░      ░  ░ ░ ░ ▒      ░░  ▒ ░  ░
 ░  ░  ░   ░ ░    ░       ░        ░ ░    ░               ░      ░ ░       ░  ░    ░  ░
               ▓█████  ██████ ▄████▄  ▄▄▄      ██▓███ ▓█████              ░
               ▓█   ▀▒██    ▒▒██▀ ▀█ ▒████▄   ▓██░  ██▓█   ▀
               ▒███  ░ ▓██▄  ▒▓█    ▄▒██  ▀█▄ ▓██░ ██▓▒███
               ▒▓█  ▄  ▒   ██▒▓▓▄ ▄██░██▄▄▄▄██▒██▄█▓▒ ▒▓█  ▄
               ░▒████▒██████▒▒ ▓███▀ ░▓█   ▓██▒██▒ ░  ░▒████▒
               ░░ ▒░ ▒ ▒▓▒ ▒ ░ ░▒ ▒  ░▒▒   ▓▒█▒▓▒░ ░  ░░ ▒░ ░
                ░ ░  ░ ░▒  ░ ░ ░  ▒    ▒   ▒▒ ░▒ ░     ░ ░  ░
                  ░  ░  ░  ░ ░         ░   ▒  ░░         ░
                  ░  ░     ░ ░ ░           ░  ░          ░  ░
                             ░
"""


def SUBURBAN_NEIGHBORHOOD_IMAGE():
    """
    Return level one area art for the level one map.

    :return: level one area art
    """
    return r"""________.   ._____________________________.
(///(////\  ///(///(///(///(///(///(///(////\
///(///(  \///(///(///(///(///(///(///(///(  \
//(///(   ///(///(///(///(///(///(///(///(   |
/(///(  .///(///(///(///(///(///(///(///(  . |
    | .' |  ___    ___    ___   _____  | .'| |
    | |.'| |_|_|  |_|_|  |_|_| |__|__| | |.' |
    | '  | |_|_|  |_|_|  |_|_| |__|__| | ' . ||'--:|
__  |  .'|    __   _____    _ %%%____  | .'| |  .|
__| | |.'|   |  | |__|__|  |_%%%%%___| ||.' .'.|   .'         .'
__| | '.'|   | .| |__|__|  |%%%:%%___| |' .'.|   .'         .'
____|.'  |___|__|___________%%::%______|.'.|   .'         .'
       .|   '-=-.'            :'       .|    .'         .'
     .|   '   .               :      .|    .'         .'
   .|   '   .                       .|   .'         .'
  |'--'|==||'--'|'--'|'--'|'--'|'-'|   .'         .'
===jim================================'         .'
.    ...   ...   ...   ...   ...              .'
================================.
                              .'         .'
                            .'         .'"""


def GRAVEYARD_IMAGE():
    """
    Return level two area art for the level two map.

    :return: level two area art
    """
    return r"""
                  _  /)
                 mo / )
                 |/)\)
                  /\_
                  \__|=
                 (    )
                 __)(__
________+_______/      \_______+__________
- --_ _-| _               _    |---_   - -
  __--  |/_|) \ |\||\| /||_|  /|-_-- __
_ --_ - |\/|\/-\| ||/|/ ||_|// |   -_  -
_-- -   |_____ __________ _____|_ --  _
-_-- __  || | | | {|    /| | || __---  -_
 --__-   || | | | {|   /|| | ||--        -
         || | | | {|  /||| | ||__--
 __-- -__|| | | | {| |}||| | ||--   __--
         ||_|_|_|_{| |}|||_|_||  -__
 --__-  -|| | | | {& |}||/ | ||---   __--
         || | | | {| |}|/| | ||-__
--   __--|| | | | {| |}/|| | ||__-- -__
  --     || | | | {| &}||| | ||   __
---   __-|| | | | {| |}||| | ||_---__-  --
 -  -_   || | | | {| |}||| | || --
 __ejm 97|| | | | {| |}||| | ||_--__-   _---
_________||_|_|_|_{| |}|||_|_||______________
                     |}|/
                     |}/
                     |/
"""


def CIRCUS_IMAGE():
    """
    Return level three area art for the level three map.

    :return: level three area art
    """
    return r"""⣼⡟⠋⣀⣼⣾⣶⣶⣦⣤⣤⣴⣶⣶⣶⣾⣿⣿⣿⣿⣿⣿⣿⣿⣶⣤⡘⢹⠄
⡟⠄⢰⣿⣿⣿⣿⣿⣿⣿⠈⠈⣿⣿⣿⣿⡋⠉⣻⣿⣿⣿⣿⣿⣿⣿⡄⠘⣇
⠁⠄⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⢵⣽⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⠄⢹
⠄⢀⣾⣿⣿⣿⣿⣿⣿⣿⡿⠋⣿⣿⣿⣿⣿⠉⠻⠿⣿⣿⣿⣿⣿⣿⣿⣇⠄
⠄⢰⣿⣿⡿⠿⠟⠋⠉⠄⠄⠈⣿⣿⣿⣿⡏⢀⣤⣤⣄⣀⣀⣀⡈⠉⢻⣿⠄
⡄⢸⣯⣥⡴⠒⢊⡁ ⭕ ⢸⣿⣿⣿⣿⣦⠈⠁ ⭕ ⣆⠈⣁⣈⣿⣿⡴
⣿⢸⣿⣿⣿⣿⣶⣶⣿⣶⣡⣼⣿⣿⣿⣿⣿⢿⣆⣤⣾⣬⣭⣵⣶⣿⣿⣿⣿
⠄⢻⡟⣩⣾⣿⣿⣿⠏⠿⡿⢿⡿⠿⠯⠎⠉⠙⠻⣿⣿⣿⡿⢖⣀⣀⠄⣼⠄
⢀⠘⣷⣿⢿⣿⣿⣿⡀⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⢸⣿⠿⠟⠋⠁⣴⣿⠏⠄
⠄⠄⠘⣿⣷⣌⠙⠻⢿⣷⣶⣤⣤⣤⣀⣠⡤⠞⡋⡍⠄⠂⠄⠄⣼⣿⠃⠄⠄
⠄⠄⠄⠄⢸⣿⣦⠄⠘⣿⡁⣾⣹⡍⣁⠐⡆⡇⠁⡌⠄⠄⠄⣰⣿⠇⠄⠄⠄
⠄⠄⠄⠄⠄⢹⣿⣷⡘⢻⣧⣇⡟⢿⢿⠄⢷⢸⡧⠁⠄⠄⢰⣿⣿⠏⠄⠄⠄
⠄⠄⠄⠄⠄⠈⣿⣿⣷⡹⢹⠸⢣⢈⠘⡇⠘⠈⠄⠁⠄⠄⣼⣿⣿⠃⣰⠄⠄
⠄⠄⠄⠄⠄⣷⠘⣿⣿⣷⡀⠄⠸⢿⣿⡏⣾⠓⠃⠄⠄⢀⡟⣿⠏⣰⣿⣷⠄
⠄⠄⣠⣿⣿⣿⣷⠙⣿⣿⣷⡀⠄⠈⠄⠄⠄⠄⠄⠄⣠⡞⣼⡿⢀⣿⣿⣿⣷
⠄⣼⣿⣿⣿⣿⣿⣷⠈⠿⣝⣿⣿⣦⣤⣭⣥⣤⣤⣶⣾⠿⠋⢀⣼⣿⣿"""


def AUTOHEAL_HP():
    """
    Return constant representing the HP gain for each heal.

    :return: constant representing the HP gain for each heal
    """
    return 4


def LEVEL_ONE_STATS():
    """
    Return basic level one player stats for all classes.

    :return: level one player stats
    """
    level_one_stats = {"player_hp": 30, "player_level": 1, "max_player_hp": 30,
                       "light_damage": 6, "medium_damage": 10, "heavy_damage": 15}
    return level_one_stats


def LEVEL_TWO_STATS():
    """
    Return basic level two player stats for all classes.

    :return: level two player stats
    """
    level_two_stats = {"player_level": 2, "light_damage": 16, "medium_damage": 20, "heavy_damage": 25}
    return level_two_stats


def LEVEL_THREE_STATS():
    """
    Return basic level three player stats for all classes.

    :return: level three player stats
    """
    level_three_stats = {"player_level": 3, "light_damage": 26, "medium_damage": 30, "heavy_damage": 35}
    return level_three_stats


def ATTACK_STATS():
    """
    Return basic base attack hit chance percentiles.

    :return: basic base attack hit chance percentile
    """
    attack_stats = {"heavy_attack_hit_chance": 4, "heavy_attack_critical_hit_chance": 8, "medium_attack_hit_chance": 7,
                    "light_attack_hit_chance": 10, "light_attack_critical_hit_chance": 8}
    return attack_stats


def BOARD_WIDTH():
    """
    Return the board width.

    :return: the board width
    """
    return 25


def BOARD_HEIGHT():
    """
    Return the board height.

    :return: the board height
    """
    return 25


def INITIAL_X_COORDINATE():
    """
    Return the starting player x-coordinate.

    :return: the starting player x-coordinate
    """
    return 0


def INITIAL_Y_COORDINATE():
    """
    Return the starting player y-coordinate.

    :return: the starting player y-coordinate
    """
    return 0


def INITIAL_EXPERIENCE_POINT():
    """
    Return the starting player experience points.

    :return: the starting player experience points
    """
    return 0


def EXPERIENCE_POINT_GAINS():
    """
    Return constant representing the number of experience points gained from defeating an enemy.

    :return: number of experience points gained from defeating an enemy
    """
    return 100


def LEVEL_TWO_XP_THRESHOLD():
    """
    Return constant representing the number of experience points needed to reach level two.

    :return: number of experience points needed to reach level two
    """
    return 300


def LEVEL_THREE_XP_THRESHOLD():
    """
    Return constant representing the number of experience points needed to reach level three.

    :return: number of experience points needed to reach level three
    """
    return 800


def LEVEL_UP_HP_INCREASE():
    """
    Return constant representing the number of health points gained from leveling up.

    :return: number of health points gained from leveling up
    """
    return 10


def LEVEL_1_ENEMIES_HP():
    """
    Return constant representing the health points of enemies at level one.

    :return: number representing health points of enemies at level one
    """
    return 15


def LEVEL_2_ENEMIES_HP():
    """
    Return constant representing the health points of enemies at level two.

    :return: number representing health points of enemies at level two
    """
    return 20


def LEVEL_3_ENEMIES_HP():
    """
    Return constant representing the health points of enemies at level three.

    :return: number representing health points of enemies at level three
    """
    return 25


def LEVEL_1_ENEMY_NAMES():
    """
    Return names of enemies encountered in the level one map area.

    :return: dictionary of names of enemies encountered in the level one map area
    """
    return {1: "Norman Bates", 2: "Freddy", 3: "Jason", 4: "The Marshmallow Man", 5: "Carrie", 6: "Dracula"}


def LEVEL_1_ENEMY_DESCRIPTIONS():
    """
    Return descriptions of enemies encountered in the level one map area.

    :return: dictionary of descriptions of enemies encountered in the level one map area
    """
    return {1: "You stumble across a hotel. There is a dark figure stuffing something into the trunk of a car...could "
               "it be a body? Norman Bates isn't happy to see you...\"Mother\" isn't happy to see you...", 2: "You "
               "find yourself incredibly sleepy. Time for a nap...you see a man wearing a fedora with the name "
               "\"Fred Krueger\" on the side. He lunges toward you.", 3: "You wander a little further and see a lake. "
               "You see a decrepit figure shambling towards you from the trees, a machete in his hand, and a mask "
               "over his face. Is this Jason Vorhees, looking for another victim? He attacks you.", 4: "There's "
               "something weird...in the neighborhood...who you gonna call...(too bad, the ghostbusters are nowhere to"
               " be found and it's up to you to take care of the latest incarnation of Marshamllow Man!)", 5: "You see "
               "a gym burning. A lone figure in a blood-soaked dress emerges from the blaze, her arms held away from "
               "her sides, her eyes wide. She looks toward you and flames begin to burn.", 6: "You notice an"
               " old house...almost castle-like. You really can't stand all these new yuppies moving into town. "
               "Suddenly, a pale-faced man emerges from the front door. He laughs like his diaphragm only moves in "
               "short bursts.\nHe extends his hand towards you, his eyes widen, and he begins to advance, his "
               "unnaturally long white front teeth bared. Really...what can you expect from out-of-towners?"}


def LEVEL_2_ENEMY_NAMES():
    """
    Return names of enemies encountered in the level two map area.

    :return: dictionary of names of enemies encountered in the level two map area
    """
    return {1: "Frankenstein's Monster", 2: "Sadako", 3: "Kayako", 4: "The Woman in Black", 5: "The Witch Ghost",
            6: "Annabelle"}


def LEVEL_2_ENEMY_DESCRIPTIONS():
    """
    Return descriptions of enemies encountered in the level two map area.

    :return: dictionary of descriptions of enemies encountered in the level two map area
    """
    return {1: "You see a figure kneeling among the tombstones. He is crying. You notice that his flesh is grey and "
               "mottled. His hair is patchy and stringy. He turns toward you and whispers, \n\"Humans...I can't forgive"
               " you...your arrogant race has damned me!!\". He lunges at you screaming, muscled arms outstretched.",
               2: "How odd...you find an old-looking well between a circle of tombstones. As you approach, you freeze "
               "when you see a rotting pale hand rise from the depths and clutch the cusp of the well. \nA figure "
               "slowly climbs out, her movements spider-like. She moves with unnatural speed toward you. You are "
               "nearly in her grasp.", 3: "You notice an old hut. \"Probably the graveyard keeper's shed\", you think"
               " to yourself. You wander inside, it's bigger than you thought. It appears to have Japanese-style "
               "sliding doors. \nYour blood runs cold when you see one slowly sliding open, a pale hand, gripping its "
               "frame. You hear a low, grating grumble, the sound of air escaping the throat of a vengeful, dying woman"
               " \nfor the last time. She lunges toward you, her black mouth agape and her long hair swinging in her "
               "face.", 4: "You come across a stately old mansion, hidden by the mists and the dark. You curiously "
               "wander inside. Suddenly, a loud pounding echoes...echoes. \nThere's a whoosh of wind as a "
               "black-laced spirit of a woman flies into you shrieking.", 5: "You wander farther into the graveyard. "
               "You come across an old tree. Is that a length of rope swinging from a tall branch? You think there "
               "might be someone attached to it, \nwhen suddenly, they are upon you, with a blood-curdling shriek.",
               6: "You hear a childish giggle, like the laugh of a little girl. You think you see a glimpse of a white"
               " dress vanish around a tombstone. You approach, but nothing is there. \nSuddenly, you feel the scrape "
               "of claws across your back - she has found you."}


def LEVEL_3_ENEMY_NAMES():
    """
    Return names of enemies encountered in the level three map area.

    :return: dictionary of names of enemies encountered in the level three map area
    """
    return {1: "Imhotep", 2: "The Predator", 3: "Dr. Heiter", 4: "Hannibal", 5: "Pennywise", 6: "Chucky"}


def LEVEL_3_ENEMY_DESCRIPTIONS():
    """
    Return descriptions of enemies encountered in the level three map area.

    :return: dictionary of descriptions of enemies encountered in the level three map area
    """
    return {1: "As you peruse the big top, you feel a hint of warmth, a sandy wind. You see a dark figure materialize"
               " from the shadows. \nHe is barely covered by dirty funeral wrappings, and gaping holes cover his body "
               "where flesh ought to be. \nHe snarls at you before unseen forces begin to wrap around you. The undead"
               " Egyptian lives.", 2: "You notice a figure in the crowd whose face looks...strange. It separates you"
               " from the crowd, and before you know it, \nan insectile face is revealed to the light, and the"
               " Predator is ready to take you down as his right of passage.", 3: "You see a strange sign on the wall, "
               "\"The Human Centipede\". There is a dirty curtain draped below it, where surely something twisted "
               "lurks. \nJust as you're deciding it would be better not to find out what that attraction is, you notice"
               " a gaunt man in a sterile white coat advancing\ntoward you purposely, an ominous and eager gleam in his"
               " eyes.", 4: "You survey a tightrope show from the dark bleachers. You see the tightrope walker falter, "
               "you cannot be sure, but sweat seems to drip down their face.\n\"Beautiful\", someone sighs behind you "
               "in the dark. \"That beautiful face at the moment when death can be a reality, absolutely glorious...\","
               "\nthe voice continues. Just then, the tightrope walker makes it across, and the lights in the "
               "bleachers flare. You turn to look behind you,\nand the man is there. An unblinking man. He looks "
               "excited...and hungry. You desperately look around the bleachers for anyone at all, but as you scan,\n"
               "the lights shut off.", 5: "The clowns come onto the stage. They begin to dance and giggle. But one of "
               "them is still, staring into the dark. At you. His gaze doesn't waver.\nYou begin to sidle along the "
               "seats nervously toward what you think is the exit, but when you swing your gaze back to that clown,\n"
               "he is gone. Suddenly, something grabs you in the dark!", 6: "You feel your stomach grumble and decide "
               "to grab a snack. As you make your way to the cotton candy machine, you hear a giggle and something\n"
               "small brushes by you. But when you look down, no one is there. When you make it to the counter, there "
               "is a doll propped up by the machine.\nYou feel yourself freeze in shock as you watch the doll's head "
               "swivel, and its beady eyes lock onto yours."}


def BOSS_INFORMATION():
    """
    Return dictionary containing boss information.

    :return: dictionary containing boss information
    """
    return {"x_coordinate": 12, "y_coordinate": 24, "boss_name": "THE QUEEN XENOMORPH", "description": "You think you "
            "see a tail flick in the shadows. You come closer into a room whose oscillating fan cuts the light in "
            "fractional slices,\ncausing a strobe light effect. Is it your imagination, or is there a giant reptilian "
            "creature extending her dripping maw towards you?\nSuddenly, she rears up, the queen of the Xenomorphs. "
            "You back slowly into the P-5000 mecha suit conveniently behind you and prepare for battle.\nBeware, this "
            "will be a combat to the death.\n", "enemy_hp": 120, "enemy_damage": 30, "enemy_damage_minimum": 10}


def VICTORY_IMAGE():
    """
    Return r string containing victory image.

    :return: r string containing victory image
    """
    return r"""                                                                          / /
                                                                        | | |  /
                                                                         \|_|_/
                                                                       ,--/.__/--'
                                       _.-/   _   \-._                    .'|
                                     .'::(_,-' `-._)::`.                  |:|
                                    (:::::::::::::::::::)                .':|
                                     \_:::;;;::::;;;:::/    /            |::|
                             \        ,---'..\::/..`-.'    /             |::|
                              \       \_;:....|'...:_ )   /             .'=||
                               \.       )---. )_.--< (   /'             ||=||
                                \\     //|:: /--\:::\\\ //             _||= |
                                 \\   ||::\:|----|:/:||/--.______,--==' \ - /
                          -._     \`.  \\:|:|-- -|:\:/-.,,\\  .----'//'_.`-'
                      \.     `-.   \ \ _|:|:|-- -|::||::\,,||-'////---' |/'
                       \\       `._)\ / |\/:|-/|--\:/|. :\_,'---'       /
                        \\_      /,,\/:.'\\/-.'`-.-//  \ |
                        /`\-    //,,,' |-.\-'\--/|-/ ./| |             /
                         /||-   ||, /| |\. |.-==-.| . /| |            | /
                 __  |    /||-  ||,,\- | .  \;;;;/ .  .':/         _,-=/-'
                /  \//    /||-  ' `,-|::\ . \,..,/   /: /         /.-'
                ,--||      /||-/.-.'  \  `._ `--' _.' .'|        //
                .--||`.    /||//\ '   |-'.___`___' _,'|//       /;
                  /\| \     ///\ /     \\_`-.`--`-'_==|'       /;'
                 / |'\ \.   //\ /       \_\__)\`==-_'_|       / /
                  .'  \.=`./|\ /          \`-- \--._/_/------( /
                       \.=| `_/|-          |\`-| -/| `--------'
                        \\` ./|-/-         |\`-| |-|     ________
                         `--\ |=|'        _|\`-| |-|----'.-._ ..\`-.
                             -|-|-     .-':`-;-| |./.-.-( | ||..|=-\\
                             `'= /'   / ,--.:|-| ||_|_|_|_|-'__ .`-._)
                              /|-|- .' /\ \ \|-` \\ ____,---'  `-. ..|
                               /\=\/..'\ \_>-'`-\ \'              \ .|
                               `,-':/\`.>' |\/ \/\ \              `- |
                               //::/\ \/_/|-' \/| \ `.            / ||
                              / (:|\ \/) \ \|.'-'  `-\\          |;:|\_
                             || |:`-/:.'-|-' \|       \\          `;_\-`-._
                             \\=/:_/::/\| \|          |\\            `-._ =`-._
                              \_)' |:|                | //               `--.__`-.
                                   |:|                                         )\|
                                   /;/                                         / (\_
                                  / /                                         |\\;;_`-.
                                _/ /                                          ' `---\.-\
                              /:::/
                             //;;'
                            `-'"""


def LEVEL_1_ENEMY_DAMAGE():
    """
    Return integer representing the damage dealt by Level One enemies.

    :return: integer representing the damage dealt by Level One enemies
    """
    return 10


def LEVEL_2_ENEMY_DAMAGE():
    """
    Return integer representing the damage dealt by Level Two enemies.

    :return: integer representing the damage dealt by Level Two enemies
    """
    return 15


def LEVEL_3_ENEMY_DAMAGE():
    """
    Return integer representing the damage dealt by Level Three enemies.

    :return: integer representing the damage dealt by Level Three enemies
    """
    return 20


def SHRIEKING_STUMBLER_DESCRIPTION():
    """
    Return description of player class "Shrieking Stumbler".

    :return: string containing description of player class "Shrieking Stumbler"
    """
    return f"\n\n{TextColors.PURPLE}CLASS: SHRIEKING STUMBLER\n\n{TextColors.YELLOW}The {TextColors.PURPLE}SHRIEKING " \
           f"STUMBLER {TextColors.YELLOW}is great at screaming and yelling and falling, but still manages to " \
           f"survive. They are also very good at picking up items they find\nfrom the ample time they spend on the " \
           f"ground.\n\n{TextColors.BLUE}SUBCLASS: DAY TRIPPER\n{TextColors.RED}SPECIAL ATTACK: STICK STAB\n" \
           f"{TextColors.CYAN}CLASS BENEFIT: ONE EXTRA CHANCE TO ATTACK ON MISSED ATTACK{TextColors.ENDC}\n\n"


def SCHOOL_JOCK_DESCRIPTION():
    """
    Return description of player class "School Jock".

    :return: string containing description of player class "School Jock"
    """
    return f"\n\n{TextColors.PURPLE}CLASS: SCHOOL JOCK\n\n{TextColors.YELLOW}The {TextColors.PURPLE}SCHOOL JOCK " \
           f"{TextColors.YELLOW}is tough to defeat. After long hours of extracurricular sports-ing, taking down a " \
           f"ghost or a killer hardly makes them break a sweat.\n\n{TextColors.BLUE}SUBCLASS: FRESHMAN\n" \
           f"{TextColors.RED}SPECIAL ATTACK: HOCKEY STICK SWING\n{TextColors.CYAN}CLASS BENEFIT: +10 HP" \
           f"{TextColors.ENDC}\n\n"


def COMPUTER_NERD_DESCRIPTION():
    """
    Return description of player class "Computer Nerd".

    :return: string containing description of player class "Computer Nerd"
    """
    return f"\n\n{TextColors.PURPLE}CLASS: COMPUTER NERD\n\n{TextColors.YELLOW}The {TextColors.PURPLE}COMPUTER NERD " \
           f"{TextColors.YELLOW}knows that a strategic plan wins the day. With their know-how and Googling skills, " \
           f"enemies are just another bug to squash.\n\n{TextColors.BLUE}SUBCLASS: n00b\n{TextColors.RED}SPECIAL " \
           f"ATTACK: MECHANICAL KEYBOARD CLICKING\n{TextColors.CYAN}CLASS BENEFIT: LIGHT ATTACK - 100% CHANCE OF " \
           f"CRITICAL HIT CHANCE{TextColors.ENDC}\n\n"


def THE_NATURAL_DESCRIPTION():
    """
    Return description of player class "The Natural".

    :return: string containing description of player class "The Natural"
    """
    return f"\n\n{TextColors.PURPLE}CLASS: THE NATURAL\n\n{TextColors.YELLOW}The {TextColors.PURPLE}THE NATURAL " \
           f"{TextColors.YELLOW}was just another person in the crowd until they felt the rush of their first fight. " \
           f"It's now unclear who the real killer is.\n\n{TextColors.BLUE}SUBCLASS: DAYDREAMER\n{TextColors.RED}" \
           f"SPECIAL ATTACK: LUCKY STRIKE\n{TextColors.CYAN}CLASS BENEFIT: HEAVY ATTACK - 60% CHANCE OF CRITICAL " \
           f"HIT CHANCE{TextColors.ENDC}\n\n"


def PLAYER_CLASS_SHRIEKING_STUMBLER():
    """
    Return dictionary containing specific class information for the player class "Shrieking Stumbler".

    :return: dictionary containing specific class information for the player class "Shrieking Stumbler"
    """
    shrieking_stumbler = {"player_class": "SHRIEKING STUMBLER", "re-rolls": 1, "special_attack": "STICK STAB",
                          "class_level": "DAY TRIPPER"}
    return shrieking_stumbler


def PLAYER_CLASS_SHRIEKING_STUMBLER_LEVEL_2():
    """
    Return dictionary containing specific class information for level 2 of player class "Shrieking Stumbler".

    :return: dictionary containing specific class information for level 2 of player class "Shrieking Stumbler"
    """
    shrieking_stumbler = {"special_attack": "LEAF MIRAGE", "class_level": "FORAGER"}
    return shrieking_stumbler


def PLAYER_CLASS_SHRIEKING_STUMBLER_LEVEL_3():
    """
    Return dictionary containing specific class information for level 3 of player class "Shrieking Stumbler".

    :return: dictionary containing specific class information for level 3 of player class "Shrieking Stumbler"
    """
    shrieking_stumbler = {"special_attack": "FOREST BARRAGE", "class_level": "WOOD-WANDERER"}
    return shrieking_stumbler


def PLAYER_CLASS_SCHOOL_JOCK():
    """
    Return dictionary containing specific class information for the player class "School Jock".

    :return: dictionary containing specific class information for the player class "School Jock"
    """
    school_jock = {"player_class": "SCHOOL JOCK", "re-rolls": 0, "special_attack": "HOCKEY STICK SWING", "class_level":
                   "FRESHMAN"}
    return school_jock


def PLAYER_CLASS_SCHOOL_JOCK_LEVEL_2():
    """
    Return dictionary containing specific class information for level 2 of player class "School Jock".

    :return: dictionary containing specific class information for level 2 of player class "School Jock"
    """
    school_jock = {"special_attack": "SCHOOL SPIRIT BLESSING", "class_level": "VARSITY"}
    return school_jock


def PLAYER_CLASS_SCHOOL_JOCK_LEVEL_3():
    """
    Return dictionary containing specific class information for level 3 of player class "School Jock".

    :return: dictionary containing specific class information for level 3 of player class "School Jock"
    """
    school_jock = {"special_attack": "FULL SCHOLARSHIP BLAST", "class_level": "CHAMPION"}
    return school_jock


def PLAYER_CLASS_COMPUTER_NERD():
    """
    Return dictionary containing specific class information for the player class "Computer Nerd".

    :return: dictionary containing specific class information for the player class "Computer Nerd"
    """
    computer_nerd = {"player_class": "COMPUTER NERD", "light_attack_critical_hit_chance": 10, "re-rolls": 0,
                     "special_attack": "MECHANICAL KEYBOARD CLICKING", "class_level": "n00b"}
    return computer_nerd


def PLAYER_CLASS_COMPUTER_NERD_LEVEL_2():
    """
    Return dictionary containing specific class information for level 2 of player class "Computer Nerd".

    :return: dictionary containing specific class information for level 2 of player class "Computer Nerd"
    """
    computer_nerd = {"special_attack": "MULTIPLE MONITOR LIGHT SHOW", "class_level": "pwnz0r"}
    return computer_nerd


def PLAYER_CLASS_COMPUTER_NERD_LEVEL_3():
    """
    Return dictionary containing specific class information for level 3 of player class "Computer Nerd".

    :return: dictionary containing specific class information for level 3 of player class "Computer Nerd"
    """
    computer_nerd = {"special_attack": "BATTLESTATION SYMPHONY", "class_level": "1337 h4x0r"}
    return computer_nerd


def PLAYER_CLASS_THE_NATURAL():
    """
    Return dictionary containing specific class information for player class "The Natural".

    :return: dictionary containing specific class information for player class "The Natural"
    """
    the_natural = {"player_class": "THE NATURAL", "heavy_attack_hit_chance": 6, "re-rolls": 0, "special_attack":
                   "LUCKY STRIKE", "class_level": "DAYDREAMER"}
    return the_natural


def PLAYER_CLASS_THE_NATURAL_LEVEL_2():
    """
    Return dictionary containing specific class information for level 2 of player class "The Natural".

    :return: dictionary containing specific class information for level 2 of player class "The Natural"
    """
    the_natural = {"special_attack": "STRATEGIC ATTACK", "class_level": "IDEALIST"}
    return the_natural


def PLAYER_CLASS_THE_NATURAL_LEVEL_3():
    """
    Return dictionary containing specific class information for level 3 of player class "The Natural".

    :return: dictionary containing specific class information for level 3 of player class "The Natural"
    """
    the_natural = {"special_attack": "BLOODY MASSACRE", "class_level": "SURVIVALIST"}
    return the_natural


def SCHOOL_JOCK_HP_BUFF():
    """
    Return the HP buff unique to the "School Jock" class.

    :return: integer representing the HP buff unique to the "School Jock" class
    """
    return 10


def HEALING_FOUNTAIN_WELCOME_MESSAGE():
    """
    Return healing fountain welcome message.

    :return: string containing healing fountain welcome message
    """
    return f"{TextColors.BLUE}Yay good job you made it to the healing fountain! \n\nWondering what the fountain " \
           f"does? \nIf you'd like some healing, the coins on the ground could help!\n (Though you still cannot " \
           f"exceed your maximum hp)\n"


def REJECT_HEALING_FOUNTAIN_MESSAGE():
    """
    Return the message to user when user chooses to reject healing from the healing fountain.

    :return: string containing reject message to user when user chooses to reject healing from the healing fountain
    """
    return f"\nI see that you're quite confident of your ability to survive without the help of healing fountain\n" \
           f"Hmm ... I hope you made the right choice... good luck brave soul...{TextColors.ENDC}\n"


def SHRIEKING_STUMBLER_EXTRA_HIT_MESSAGE():
    """
    Return the extra hit message unique to the Shrieking Stumbler class.

    :return: string containing Shrieking Stumbler extra hit message
    """
    return f"But no worries, you're a {TextColors.PURPLE}SHRIEKING STUMBLER{TextColors.ENDC}, so you get one more " \
           f"chance to attack!\n"


def EXIT_GAME_MESSAGE():
    """
    Return end game message to user when user exits the game.

    :return: string of exit game message
    """
    return f"\nThis is the end...but the adventure may continue on if you choose a new character..."


class TextColors:
    """ Create class of colours that can used as text colour. """
    BLACK = '\033[30m'
    PURPLE = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    WHITE = '\033[37m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    NEGATIVE = '\033[3m'


class Background:
    """ Create a class of colours that can used as background colour. """
    RED = '\033[41m'
    GREEN = '\033[42m'
    YELLOW = '\033[43m'
    BLUE = '\033[44m'
    PURPLE = '\033[45m'
    CYAN = '\033[46m'
    WHITE = '\033[47m'
    ENDC = '\033[0m'


def start_screen():
    """
    Print welcome screen and accept user input if user decides to continue game.

    :pre-condition: user must enter a valid input
    :post-condition: correctly prints welcome screen and accepts user input if user decides to continue game
    :return: None
    """
    print(GAME_TITLE())
    start_game = input(f"{TextColors.YELLOW}Welcome to {TextColors.PURPLE}HORROR MOVIE ESCAPE{TextColors.YELLOW}...\n"
                       f"Please press ENTER to START.\n\n{TextColors.ENDC}> ")
    if start_game is None:
        return None


def create_character(character_stats: dict):
    """
    Create and store a new character's information.

    Ask user to input character name and update character_stats dictionary with character name and other starting
    information.

    :param character_stats: dictionary containing character information
    :pre-condition: user must enter a valid input
    :post-condition: correctly updates character_stats dictionary with starting information and character name
    :return: None
    """
    name = input(f"\nPlease enter a character name: \n> ")
    character_stats["name"] = name
    character_stats["x_coordinate"] = INITIAL_X_COORDINATE()
    character_stats["y_coordinate"] = INITIAL_Y_COORDINATE()
    character_stats["current_location"] = (character_stats["x_coordinate"], character_stats["y_coordinate"])
    character_stats["player_xp"] = INITIAL_EXPERIENCE_POINT()
    character_stats.update(LEVEL_ONE_STATS())
    character_stats.update(ATTACK_STATS())


def assign_class(character_stats: dict, class_choice: str) -> dict:
    """
    Assign player to a class or print player class description until player gets assigned a class.

    :param character_stats: dictionary containing character information
    :param class_choice: string containing player class choice information
    :pre-condition: character_stats must be a dictionary
    :pre-condition: class_choice must be a string
    :post-condition: correctly assigns player to a class or prints player class descriptions until player assigns
                     their character to a class
    :post-condition: correctly updates class-specific information in character_stats
    :return: dictionary containing character information
    """
    while class_choice == "0d" or class_choice == "1d" or class_choice == "2d" or class_choice == "3d":
        description_print(class_choice)
        class_choice = class_choice_prompt()
    if class_choice == "0":
        character_stats.update(PLAYER_CLASS_SHRIEKING_STUMBLER())
    elif class_choice == "1":
        character_stats.update(PLAYER_CLASS_SCHOOL_JOCK())
        character_stats["player_hp"] += SCHOOL_JOCK_HP_BUFF()
        character_stats["max_player_hp"] += SCHOOL_JOCK_HP_BUFF()
    elif class_choice == "2":
        character_stats.update(PLAYER_CLASS_COMPUTER_NERD())
    elif class_choice == "3":
        character_stats.update(PLAYER_CLASS_THE_NATURAL())
    print(f"\nYou are now player class {TextColors.PURPLE}{character_stats['player_class']}{TextColors.ENDC}\n")
    return character_stats


def class_choice_prompt() -> str:
    """
    Prompt user to select a player class.

    :pre-condition: user must enter a valid input
    :post-condition: correctly returns user player class choice as a string
    :return: string containing player's class choice
    """
    class_options = ["SHRIEKING STUMBLER", "SCHOOL JOCK", "COMPUTER NERD", "THE NATURAL"]
    numbered_menu = number_menu_items(class_options)
    class_choice = input(f"\n{Background.YELLOW}{TextColors.BLACK}{numbered_menu}{Background.ENDC}\n\n{TextColors.ENDC}"
                         f"What class would you like to play as? \nPlease type the {TextColors.PURPLE}number"
                         f"{TextColors.ENDC} of the class and {TextColors.PURPLE}\"d\"{TextColors.ENDC} to read a "
                         f"description (e.g., {TextColors.PURPLE}\"1d\"{TextColors.ENDC})\n> ")
    if class_choice != "0" or "1" or "2" or "3":
        print("Please enter a valid input.\n")
        return class_choice
    else:
        return class_choice


def description_print(class_choice: str):
    """
    Print player class description based on input value.

    :param class_choice: string containing player class choice information
    :pre-condition: class_choice must be a string
    :post-condition: correctly prints player class description based on input value
    :return: None
    """
    if class_choice == "0d":
        print(SHRIEKING_STUMBLER_DESCRIPTION())
    elif class_choice == "1d":
        print(SCHOOL_JOCK_DESCRIPTION())
    elif class_choice == "2d":
        print(COMPUTER_NERD_DESCRIPTION())
    else:
        print(THE_NATURAL_DESCRIPTION())


def suburban_neighborhood_screen():
    """
    Print suburban neighborhood screen and accept user input if user decides to continue game.

    :pre-condition: user must enter a valid input
    :post-condition: correctly prints suburban neighborhood screen and accepts user input if user decides to
                        continue game
    :return: None
    """
    print(SUBURBAN_NEIGHBORHOOD_IMAGE())
    start_game = input(f"\n\n\n{TextColors.YELLOW}::TROUBLE IN SUBURBIA::\n\nYou find yourself in a suburban "
                       f"neighborhood. You grew up here. But something doesn't feel right. You walk down the street to"
                       f" explore.\n\n{TextColors.RED}Please press ENTER to CONTINUE.{TextColors.ENDC}\n\n> ")
    if start_game is None:
        return


def make_board(character_stats: dict) -> dict:
    """
    Create a 25 x 25 game board dictionary.

    User location tuple key has value of True, healing landmarks location tuple key has value of "heal", boss location
    tuple key has value of "boss", and the remaining location tuple keys have values of False.

    :param character_stats: dictionary containing character information
    :pre-condition: character_stats must be a dictionary
    :pre-condition: player location must be a location tuple within the scope of board dictionary
    :pre-condition: healing landmarks location tuples must be within the scope of board dictionary
    :pre-condition: final boss location must be a location tuple within the scope of board dictionary
    :post-condition: correctly creates a game board dictionary marking locations of player location, healing landmarks,
                     and final boss location
    :return: dictionary representing a game board
    >>> player_stats = {"healing_landmarks": [(19, 11), (5, 19), (1, 5), (11, 12), (7, 8), (2, 6), (12, 18), \
                       (14, 20)], "current_location": (0, 0)}
    >>> game_board = make_board(player_stats)
    >>> game_board # doctest: +NORMALIZE_WHITESPACE
    {(0, 0): True, (0, 1): False, (0, 2): False, (0, 3): False, (0, 4): False, (0, 5): False, (0, 6): False,
    (0, 7): False, (0, 8): False, (0, 9): False, (0, 10): False, (0, 11): False, (0, 12): False, (0, 13): False,
    (0, 14): False, (0, 15): False, (0, 16): False, (0, 17): False, (0, 18): False, (0, 19): False, (0, 20): False,
    (0, 21): False, (0, 22): False, (0, 23): False, (0, 24): False, (1, 0): False, (1, 1): False, (1, 2): False,
    (1, 3): False, (1, 4): False, (1, 5): 'heal', (1, 6): False, (1, 7): False, (1, 8): False, (1, 9): False,
    (1, 10): False, (1, 11): False, (1, 12): False, (1, 13): False, (1, 14): False, (1, 15): False, (1, 16): False,
    (1, 17): False, (1, 18): False, (1, 19): False, (1, 20): False, (1, 21): False, (1, 22): False, (1, 23): False,
    (1, 24): False, (2, 0): False, (2, 1): False, (2, 2): False, (2, 3): False, (2, 4): False, (2, 5): False,
    (2, 6): 'heal', (2, 7): False, (2, 8): False, (2, 9): False, (2, 10): False, (2, 11): False, (2, 12): False,
    (2, 13): False, (2, 14): False, (2, 15): False, (2, 16): False, (2, 17): False, (2, 18): False, (2, 19): False,
    (2, 20): False, (2, 21): False, (2, 22): False, (2, 23): False, (2, 24): False, (3, 0): False, (3, 1): False,
    (3, 2): False, (3, 3): False, (3, 4): False, (3, 5): False, (3, 6): False, (3, 7): False, (3, 8): False,
    (3, 9): False, (3, 10): False, (3, 11): False, (3, 12): False, (3, 13): False, (3, 14): False, (3, 15): False,
    (3, 16): False, (3, 17): False, (3, 18): False, (3, 19): False, (3, 20): False, (3, 21): False, (3, 22): False,
    (3, 23): False, (3, 24): False, (4, 0): False, (4, 1): False, (4, 2): False, (4, 3): False, (4, 4): False,
    (4, 5): False, (4, 6): False, (4, 7): False, (4, 8): False, (4, 9): False, (4, 10): False, (4, 11): False,
    (4, 12): False, (4, 13): False, (4, 14): False, (4, 15): False, (4, 16): False, (4, 17): False, (4, 18): False,
    (4, 19): False, (4, 20): False, (4, 21): False, (4, 22): False, (4, 23): False, (4, 24): False, (5, 0): False,
    (5, 1): False, (5, 2): False, (5, 3): False, (5, 4): False, (5, 5): False, (5, 6): False, (5, 7): False,
    (5, 8): False, (5, 9): False, (5, 10): False, (5, 11): False, (5, 12): False, (5, 13): False, (5, 14): False,
    (5, 15): False, (5, 16): False, (5, 17): False, (5, 18): False, (5, 19): 'heal', (5, 20): False, (5, 21): False,
    (5, 22): False, (5, 23): False, (5, 24): False, (6, 0): False, (6, 1): False, (6, 2): False, (6, 3): False,
    (6, 4): False, (6, 5): False, (6, 6): False, (6, 7): False, (6, 8): False, (6, 9): False, (6, 10): False,
    (6, 11): False, (6, 12): False, (6, 13): False, (6, 14): False, (6, 15): False, (6, 16): False, (6, 17): False,
    (6, 18): False, (6, 19): False, (6, 20): False, (6, 21): False, (6, 22): False, (6, 23): False, (6, 24): False,
    (7, 0): False, (7, 1): False, (7, 2): False, (7, 3): False, (7, 4): False, (7, 5): False, (7, 6): False,
    (7, 7): False, (7, 8): 'heal', (7, 9): False, (7, 10): False, (7, 11): False, (7, 12): False, (7, 13): False,
    (7, 14): False, (7, 15): False, (7, 16): False, (7, 17): False, (7, 18): False, (7, 19): False, (7, 20): False,
    (7, 21): False, (7, 22): False, (7, 23): False, (7, 24): False, (8, 0): False, (8, 1): False, (8, 2): False,
    (8, 3): False, (8, 4): False, (8, 5): False, (8, 6): False, (8, 7): False, (8, 8): False, (8, 9): False,
    (8, 10): False, (8, 11): False, (8, 12): False, (8, 13): False, (8, 14): False, (8, 15): False, (8, 16): False,
    (8, 17): False, (8, 18): False, (8, 19): False, (8, 20): False, (8, 21): False, (8, 22): False, (8, 23): False,
    (8, 24): False, (9, 0): False, (9, 1): False, (9, 2): False, (9, 3): False, (9, 4): False, (9, 5): False,
    (9, 6): False, (9, 7): False, (9, 8): False, (9, 9): False, (9, 10): False, (9, 11): False, (9, 12): False,
    (9, 13): False, (9, 14): False, (9, 15): False, (9, 16): False, (9, 17): False, (9, 18): False, (9, 19): False,
    (9, 20): False, (9, 21): False, (9, 22): False, (9, 23): False, (9, 24): False, (10, 0): False, (10, 1): False,
    (10, 2): False, (10, 3): False, (10, 4): False, (10, 5): False, (10, 6): False, (10, 7): False, (10, 8): False,
    (10, 9): False, (10, 10): False, (10, 11): False, (10, 12): False, (10, 13): False, (10, 14): False,
    (10, 15): False, (10, 16): False, (10, 17): False, (10, 18): False, (10, 19): False, (10, 20): False,
    (10, 21): False, (10, 22): False, (10, 23): False, (10, 24): False, (11, 0): False, (11, 1): False,
    (11, 2): False, (11, 3): False, (11, 4): False, (11, 5): False, (11, 6): False, (11, 7): False, (11, 8): False,
    (11, 9): False, (11, 10): False, (11, 11): False, (11, 12): 'heal', (11, 13): False, (11, 14): False,
    (11, 15): False, (11, 16): False, (11, 17): False, (11, 18): False, (11, 19): False, (11, 20): False,
    (11, 21): False, (11, 22): False, (11, 23): False, (11, 24): False, (12, 0): False, (12, 1): False,
    (12, 2): False, (12, 3): False, (12, 4): False, (12, 5): False, (12, 6): False, (12, 7): False, (12, 8): False,
    (12, 9): False, (12, 10): False, (12, 11): False, (12, 12): False, (12, 13): False, (12, 14): False,
    (12, 15): False, (12, 16): False, (12, 17): False, (12, 18): 'heal', (12, 19): False, (12, 20): False,
    (12, 21): False, (12, 22): False, (12, 23): False, (12, 24): 'boss', (13, 0): False, (13, 1): False,
    (13, 2): False, (13, 3): False, (13, 4): False, (13, 5): False, (13, 6): False, (13, 7): False, (13, 8): False,
    (13, 9): False, (13, 10): False, (13, 11): False, (13, 12): False, (13, 13): False, (13, 14): False,
    (13, 15): False, (13, 16): False, (13, 17): False, (13, 18): False, (13, 19): False, (13, 20): False,
    (13, 21): False, (13, 22): False, (13, 23): False, (13, 24): False, (14, 0): False, (14, 1): False,
    (14, 2): False, (14, 3): False, (14, 4): False, (14, 5): False, (14, 6): False, (14, 7): False, (14, 8): False,
    (14, 9): False, (14, 10): False, (14, 11): False, (14, 12): False, (14, 13): False, (14, 14): False,
    (14, 15): False, (14, 16): False, (14, 17): False, (14, 18): False, (14, 19): False, (14, 20): 'heal',
    (14, 21): False, (14, 22): False, (14, 23): False, (14, 24): False, (15, 0): False, (15, 1): False, (15, 2): False,
    (15, 3): False, (15, 4): False, (15, 5): False, (15, 6): False, (15, 7): False, (15, 8): False, (15, 9): False,
    (15, 10): False, (15, 11): False, (15, 12): False, (15, 13): False, (15, 14): False, (15, 15): False,
    (15, 16): False, (15, 17): False, (15, 18): False, (15, 19): False, (15, 20): False, (15, 21): False,
    (15, 22): False, (15, 23): False, (15, 24): False, (16, 0): False, (16, 1): False, (16, 2): False, (16, 3): False,
    (16, 4): False, (16, 5): False, (16, 6): False, (16, 7): False, (16, 8): False, (16, 9): False, (16, 10): False,
    (16, 11): False, (16, 12): False, (16, 13): False, (16, 14): False, (16, 15): False, (16, 16): False,
    (16, 17): False, (16, 18): False, (16, 19): False, (16, 20): False, (16, 21): False, (16, 22): False,
    (16, 23): False, (16, 24): False, (17, 0): False, (17, 1): False, (17, 2): False, (17, 3): False, (17, 4): False,
    (17, 5): False, (17, 6): False, (17, 7): False, (17, 8): False, (17, 9): False, (17, 10): False, (17, 11): False,
    (17, 12): False, (17, 13): False, (17, 14): False, (17, 15): False, (17, 16): False, (17, 17): False,
    (17, 18): False, (17, 19): False, (17, 20): False, (17, 21): False, (17, 22): False, (17, 23): False,
    (17, 24): False, (18, 0): False, (18, 1): False, (18, 2): False, (18, 3): False, (18, 4): False, (18, 5): False,
    (18, 6): False, (18, 7): False, (18, 8): False, (18, 9): False, (18, 10): False, (18, 11): False, (18, 12): False,
    (18, 13): False, (18, 14): False, (18, 15): False, (18, 16): False, (18, 17): False, (18, 18): False,
    (18, 19): False, (18, 20): False, (18, 21): False, (18, 22): False, (18, 23): False, (18, 24): False,
    (19, 0): False, (19, 1): False, (19, 2): False, (19, 3): False, (19, 4): False, (19, 5): False, (19, 6): False,
    (19, 7): False, (19, 8): False, (19, 9): False, (19, 10): False, (19, 11): 'heal', (19, 12): False, (19, 13): False,
    (19, 14): False, (19, 15): False, (19, 16): False, (19, 17): False, (19, 18): False, (19, 19): False,
    (19, 20): False, (19, 21): False, (19, 22): False, (19, 23): False, (19, 24): False, (20, 0): False, (20, 1): False,
    (20, 2): False, (20, 3): False, (20, 4): False, (20, 5): False, (20, 6): False, (20, 7): False, (20, 8): False,
    (20, 9): False, (20, 10): False, (20, 11): False, (20, 12): False, (20, 13): False, (20, 14): False,
    (20, 15): False, (20, 16): False, (20, 17): False, (20, 18): False, (20, 19): False, (20, 20): False,
    (20, 21): False, (20, 22): False, (20, 23): False, (20, 24): False, (21, 0): False, (21, 1): False, (21, 2): False,
    (21, 3): False, (21, 4): False, (21, 5): False, (21, 6): False, (21, 7): False, (21, 8): False, (21, 9): False,
    (21, 10): False, (21, 11): False, (21, 12): False, (21, 13): False, (21, 14): False, (21, 15): False,
    (21, 16): False, (21, 17): False, (21, 18): False, (21, 19): False, (21, 20): False, (21, 21): False,
    (21, 22): False, (21, 23): False, (21, 24): False, (22, 0): False, (22, 1): False, (22, 2): False, (22, 3): False,
    (22, 4): False, (22, 5): False, (22, 6): False, (22, 7): False, (22, 8): False, (22, 9): False, (22, 10): False,
    (22, 11): False, (22, 12): False, (22, 13): False, (22, 14): False, (22, 15): False, (22, 16): False,
    (22, 17): False, (22, 18): False, (22, 19): False, (22, 20): False, (22, 21): False, (22, 22): False,
    (22, 23): False, (22, 24): False, (23, 0): False, (23, 1): False, (23, 2): False, (23, 3): False, (23, 4): False,
    (23, 5): False, (23, 6): False, (23, 7): False, (23, 8): False, (23, 9): False, (23, 10): False, (23, 11): False,
    (23, 12): False, (23, 13): False, (23, 14): False, (23, 15): False, (23, 16): False, (23, 17): False,
    (23, 18): False, (23, 19): False, (23, 20): False, (23, 21): False, (23, 22): False, (23, 23): False,
    (23, 24): False, (24, 0): False, (24, 1): False, (24, 2): False, (24, 3): False, (24, 4): False, (24, 5): False,
    (24, 6): False, (24, 7): False, (24, 8): False, (24, 9): False, (24, 10): False, (24, 11): False, (24, 12): False,
    (24, 13): False, (24, 14): False, (24, 15): False, (24, 16): False, (24, 17): False, (24, 18): False,
    (24, 19): False, (24, 20): False, (24, 21): False, (24, 22): False, (24, 23): False, (24, 24): False}
    >>> player_stats = {"healing_landmarks": [(17, 24), (5, 19), (1, 5), (10, 9), (7, 8), (2, 6), (12, 18), \
                       (14, 20)], "current_location": (3, 5)}
    >>> game_board = make_board(player_stats)
    >>> game_board # doctest: +NORMALIZE_WHITESPACE
    {(0, 0): False, (0, 1): False, (0, 2): False, (0, 3): False, (0, 4): False, (0, 5): False, (0, 6): False,
    (0, 7): False, (0, 8): False, (0, 9): False, (0, 10): False, (0, 11): False, (0, 12): False, (0, 13): False,
    (0, 14): False, (0, 15): False, (0, 16): False, (0, 17): False, (0, 18): False, (0, 19): False, (0, 20): False,
    (0, 21): False, (0, 22): False, (0, 23): False, (0, 24): False, (1, 0): False, (1, 1): False, (1, 2): False,
    (1, 3): False, (1, 4): False, (1, 5): 'heal', (1, 6): False, (1, 7): False, (1, 8): False, (1, 9): False,
    (1, 10): False, (1, 11): False, (1, 12): False, (1, 13): False, (1, 14): False, (1, 15): False, (1, 16): False,
    (1, 17): False, (1, 18): False, (1, 19): False, (1, 20): False, (1, 21): False, (1, 22): False, (1, 23): False,
    (1, 24): False, (2, 0): False, (2, 1): False, (2, 2): False, (2, 3): False, (2, 4): False, (2, 5): False,
    (2, 6): 'heal', (2, 7): False, (2, 8): False, (2, 9): False, (2, 10): False, (2, 11): False, (2, 12): False,
    (2, 13): False, (2, 14): False, (2, 15): False, (2, 16): False, (2, 17): False, (2, 18): False, (2, 19): False,
    (2, 20): False, (2, 21): False, (2, 22): False, (2, 23): False, (2, 24): False, (3, 0): False, (3, 1): False,
    (3, 2): False, (3, 3): False, (3, 4): False, (3, 5): True, (3, 6): False, (3, 7): False, (3, 8): False,
    (3, 9): False, (3, 10): False, (3, 11): False, (3, 12): False, (3, 13): False, (3, 14): False, (3, 15): False,
    (3, 16): False, (3, 17): False, (3, 18): False, (3, 19): False, (3, 20): False, (3, 21): False, (3, 22): False,
    (3, 23): False, (3, 24): False, (4, 0): False, (4, 1): False, (4, 2): False, (4, 3): False, (4, 4): False,
    (4, 5): False, (4, 6): False, (4, 7): False, (4, 8): False, (4, 9): False, (4, 10): False, (4, 11): False,
    (4, 12): False, (4, 13): False, (4, 14): False, (4, 15): False, (4, 16): False, (4, 17): False, (4, 18): False,
    (4, 19): False, (4, 20): False, (4, 21): False, (4, 22): False, (4, 23): False, (4, 24): False, (5, 0): False,
    (5, 1): False, (5, 2): False, (5, 3): False, (5, 4): False, (5, 5): False, (5, 6): False, (5, 7): False,
    (5, 8): False, (5, 9): False, (5, 10): False, (5, 11): False, (5, 12): False, (5, 13): False, (5, 14): False,
    (5, 15): False, (5, 16): False, (5, 17): False, (5, 18): False, (5, 19): 'heal', (5, 20): False, (5, 21): False,
    (5, 22): False, (5, 23): False, (5, 24): False, (6, 0): False, (6, 1): False, (6, 2): False, (6, 3): False,
    (6, 4): False, (6, 5): False, (6, 6): False, (6, 7): False, (6, 8): False, (6, 9): False, (6, 10): False,
    (6, 11): False, (6, 12): False, (6, 13): False, (6, 14): False, (6, 15): False, (6, 16): False, (6, 17): False,
    (6, 18): False, (6, 19): False, (6, 20): False, (6, 21): False, (6, 22): False, (6, 23): False, (6, 24): False,
    (7, 0): False, (7, 1): False, (7, 2): False, (7, 3): False, (7, 4): False, (7, 5): False, (7, 6): False,
    (7, 7): False, (7, 8): 'heal', (7, 9): False, (7, 10): False, (7, 11): False, (7, 12): False, (7, 13): False,
    (7, 14): False, (7, 15): False, (7, 16): False, (7, 17): False, (7, 18): False, (7, 19): False, (7, 20): False,
    (7, 21): False, (7, 22): False, (7, 23): False, (7, 24): False, (8, 0): False, (8, 1): False, (8, 2): False,
    (8, 3): False, (8, 4): False, (8, 5): False, (8, 6): False, (8, 7): False, (8, 8): False, (8, 9): False,
    (8, 10): False, (8, 11): False, (8, 12): False, (8, 13): False, (8, 14): False, (8, 15): False, (8, 16): False,
    (8, 17): False, (8, 18): False, (8, 19): False, (8, 20): False, (8, 21): False, (8, 22): False, (8, 23): False,
    (8, 24): False, (9, 0): False, (9, 1): False, (9, 2): False, (9, 3): False, (9, 4): False, (9, 5): False,
    (9, 6): False, (9, 7): False, (9, 8): False, (9, 9): False, (9, 10): False, (9, 11): False, (9, 12): False,
    (9, 13): False, (9, 14): False, (9, 15): False, (9, 16): False, (9, 17): False, (9, 18): False, (9, 19): False,
    (9, 20): False, (9, 21): False, (9, 22): False, (9, 23): False, (9, 24): False, (10, 0): False, (10, 1): False,
    (10, 2): False, (10, 3): False, (10, 4): False, (10, 5): False, (10, 6): False, (10, 7): False, (10, 8): False,
    (10, 9): 'heal', (10, 10): False, (10, 11): False, (10, 12): False, (10, 13): False, (10, 14): False,
    (10, 15): False, (10, 16): False, (10, 17): False, (10, 18): False, (10, 19): False, (10, 20): False,
    (10, 21): False, (10, 22): False, (10, 23): False, (10, 24): False, (11, 0): False, (11, 1): False, (11, 2): False,
    (11, 3): False, (11, 4): False, (11, 5): False, (11, 6): False, (11, 7): False, (11, 8): False, (11, 9): False,
    (11, 10): False, (11, 11): False, (11, 12): False, (11, 13): False, (11, 14): False, (11, 15): False,
    (11, 16): False, (11, 17): False, (11, 18): False, (11, 19): False, (11, 20): False, (11, 21): False,
    (11, 22): False, (11, 23): False, (11, 24): False, (12, 0): False, (12, 1): False, (12, 2): False, (12, 3): False,
    (12, 4): False, (12, 5): False, (12, 6): False, (12, 7): False, (12, 8): False, (12, 9): False, (12, 10): False,
    (12, 11): False, (12, 12): False, (12, 13): False, (12, 14): False, (12, 15): False, (12, 16): False,
    (12, 17): False, (12, 18): 'heal', (12, 19): False, (12, 20): False, (12, 21): False, (12, 22): False,
    (12, 23): False, (12, 24): 'boss', (13, 0): False, (13, 1): False, (13, 2): False, (13, 3): False, (13, 4): False,
    (13, 5): False, (13, 6): False, (13, 7): False, (13, 8): False, (13, 9): False, (13, 10): False, (13, 11): False,
    (13, 12): False, (13, 13): False, (13, 14): False, (13, 15): False, (13, 16): False, (13, 17): False,
    (13, 18): False, (13, 19): False, (13, 20): False, (13, 21): False, (13, 22): False, (13, 23): False,
    (13, 24): False, (14, 0): False, (14, 1): False, (14, 2): False, (14, 3): False, (14, 4): False, (14, 5): False,
    (14, 6): False, (14, 7): False, (14, 8): False, (14, 9): False, (14, 10): False, (14, 11): False, (14, 12): False,
    (14, 13): False, (14, 14): False, (14, 15): False, (14, 16): False, (14, 17): False, (14, 18): False,
    (14, 19): False, (14, 20): 'heal', (14, 21): False, (14, 22): False, (14, 23): False, (14, 24): False,
    (15, 0): False, (15, 1): False, (15, 2): False, (15, 3): False, (15, 4): False, (15, 5): False, (15, 6): False,
    (15, 7): False, (15, 8): False, (15, 9): False, (15, 10): False, (15, 11): False, (15, 12): False, (15, 13): False,
    (15, 14): False, (15, 15): False, (15, 16): False, (15, 17): False, (15, 18): False, (15, 19): False,
    (15, 20): False, (15, 21): False, (15, 22): False, (15, 23): False, (15, 24): False, (16, 0): False, (16, 1): False,
    (16, 2): False, (16, 3): False, (16, 4): False, (16, 5): False, (16, 6): False, (16, 7): False, (16, 8): False,
    (16, 9): False, (16, 10): False, (16, 11): False, (16, 12): False, (16, 13): False, (16, 14): False,
    (16, 15): False, (16, 16): False, (16, 17): False, (16, 18): False, (16, 19): False, (16, 20): False,
    (16, 21): False, (16, 22): False, (16, 23): False, (16, 24): False, (17, 0): False, (17, 1): False, (17, 2): False,
    (17, 3): False, (17, 4): False, (17, 5): False, (17, 6): False, (17, 7): False, (17, 8): False, (17, 9): False,
    (17, 10): False, (17, 11): False, (17, 12): False, (17, 13): False, (17, 14): False, (17, 15): False,
    (17, 16): False, (17, 17): False, (17, 18): False, (17, 19): False, (17, 20): False, (17, 21): False,
    (17, 22): False, (17, 23): False, (17, 24): 'heal', (18, 0): False, (18, 1): False, (18, 2): False, (18, 3): False,
    (18, 4): False, (18, 5): False, (18, 6): False, (18, 7): False, (18, 8): False, (18, 9): False, (18, 10): False,
    (18, 11): False, (18, 12): False, (18, 13): False, (18, 14): False, (18, 15): False, (18, 16): False,
    (18, 17): False, (18, 18): False, (18, 19): False, (18, 20): False, (18, 21): False, (18, 22): False,
    (18, 23): False, (18, 24): False, (19, 0): False, (19, 1): False, (19, 2): False, (19, 3): False, (19, 4): False,
    (19, 5): False, (19, 6): False, (19, 7): False, (19, 8): False, (19, 9): False, (19, 10): False, (19, 11): False,
    (19, 12): False, (19, 13): False, (19, 14): False, (19, 15): False, (19, 16): False, (19, 17): False,
    (19, 18): False, (19, 19): False, (19, 20): False, (19, 21): False, (19, 22): False, (19, 23): False,
    (19, 24): False, (20, 0): False, (20, 1): False, (20, 2): False, (20, 3): False, (20, 4): False, (20, 5): False,
    (20, 6): False, (20, 7): False, (20, 8): False, (20, 9): False, (20, 10): False, (20, 11): False, (20, 12): False,
    (20, 13): False, (20, 14): False, (20, 15): False, (20, 16): False, (20, 17): False, (20, 18): False,
    (20, 19): False, (20, 20): False, (20, 21): False, (20, 22): False, (20, 23): False, (20, 24): False,
    (21, 0): False, (21, 1): False, (21, 2): False, (21, 3): False, (21, 4): False, (21, 5): False, (21, 6): False,
    (21, 7): False, (21, 8): False, (21, 9): False, (21, 10): False, (21, 11): False, (21, 12): False,
    (21, 13): False, (21, 14): False, (21, 15): False, (21, 16): False, (21, 17): False, (21, 18): False,
    (21, 19): False, (21, 20): False, (21, 21): False, (21, 22): False, (21, 23): False, (21, 24): False,
    (22, 0): False, (22, 1): False, (22, 2): False, (22, 3): False, (22, 4): False, (22, 5): False, (22, 6): False,
    (22, 7): False, (22, 8): False, (22, 9): False, (22, 10): False, (22, 11): False, (22, 12): False, (22, 13): False,
    (22, 14): False, (22, 15): False, (22, 16): False, (22, 17): False, (22, 18): False, (22, 19): False,
    (22, 20): False, (22, 21): False, (22, 22): False, (22, 23): False, (22, 24): False, (23, 0): False, (23, 1): False,
    (23, 2): False, (23, 3): False, (23, 4): False, (23, 5): False, (23, 6): False, (23, 7): False, (23, 8): False,
    (23, 9): False, (23, 10): False, (23, 11): False, (23, 12): False, (23, 13): False, (23, 14): False,
    (23, 15): False, (23, 16): False, (23, 17): False, (23, 18): False, (23, 19): False, (23, 20): False,
    (23, 21): False, (23, 22): False, (23, 23): False, (23, 24): False, (24, 0): False, (24, 1): False,
    (24, 2): False, (24, 3): False, (24, 4): False, (24, 5): False, (24, 6): False, (24, 7): False, (24, 8): False,
    (24, 9): False, (24, 10): False, (24, 11): False, (24, 12): False, (24, 13): False, (24, 14): False,
    (24, 15): False, (24, 16): False, (24, 17): False, (24, 18): False, (24, 19): False, (24, 20): False,
    (24, 21): False, (24, 22): False, (24, 23): False, (24, 24): False}
    """
    character_stats["height"] = BOARD_HEIGHT()
    character_stats["width"] = BOARD_WIDTH()
    board = {(x_coordinate, y_coordinate): False for x_coordinate in range(character_stats["width"]) for y_coordinate
             in range(character_stats["height"])}
    for counter in range(8):
        board[character_stats["healing_landmarks"][counter]] = "heal"
    board[character_stats["current_location"]] = True
    boss_stats = BOSS_INFORMATION()
    board[(boss_stats["x_coordinate"], boss_stats["y_coordinate"])] = "boss"
    return board


def print_board(character_stats: dict, board: dict):
    """
    Display the game board with ASCII art.

    User location is indicated by "#", healing landmark locations are indicated by "@", boss location is indicated by
    "$", and the remaining locations are indicated by "."

    :param character_stats: dictionary containing character information
    :param board: dictionary representing a game board
    :pre-condition: character_stats must be a dictionary
    :pre-condition: player location must be a location tuple within the scope of board dictionary
    :pre-condition: healing landmarks location tuples must be within the scope of board dictionary
    :pre-condition: final boss location must be a location tuple within the scope of board dictionary
    :post-condition: correctly displays the game board with ASCII art
    :return: None

    >>> player_stats = {'name': '', 'x_coordinate': 0, 'y_coordinate': 0, 'current_location': (0, 0), \
                           'healing_landmarks': [(11, 17), (4, 7), (18, 11), (13, 1), (7, 21), (6, 5), (9, 18), \
                           (8, 10)], 'height': 25, 'width': 25}
    >>> game_board = make_board(player_stats)
    >>> print_board(player_stats, game_board) # doctest: +NORMALIZE_WHITESPACE
    +-----------------------------------------------+
    # . . . . . . . . . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . @ . . . . . . . . . . .
    . . . . . . . . . . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . . . . . . . . . . .
    . . . . . . @ . . . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . . . . . . . . . . .
    . . . . @ . . . . . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . . . . . . . . . . .
    +--------------------[     ]--------------------+
    . . . . . . . . . . . . . . . . . . . . . . . . .
    . . . . . . . . @ . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . . . . @ . . . . . .
    . . . . . . . . . . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . . . . . . . . . . .
    +--------------------[     ]--------------------+
    . . . . . . . . . . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . . . . . . . . . . .
    . . . . . . . . . . . @ . . . . . . . . . . . . .
    . . . . . . . . . @ . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . . . . . . . . . . .
    . . . . . . . @ . . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . $ . . . . . . . . . . . .
    +-----------------------------------------------+
    """
    print("\n+" + "-" * 47 + "+")
    for y_coordinate in range(character_stats["height"]):
        if y_coordinate == 9 or y_coordinate == 15:
            print("+" + "-" * 20 + "[     ]" + "-" * 20 + "+")
        for x_coordinate in range(character_stats["width"]):
            if board[(x_coordinate, y_coordinate)] is True:
                print("#", end=" ")
            elif board[(x_coordinate, y_coordinate)] is False:
                print(".", end=" ")
            elif board[(x_coordinate, y_coordinate)] == "heal":
                print("@", end=" ")
            elif board[(x_coordinate, y_coordinate)] == "boss":
                print("$", end=" ")
        print()
    print("+" + "-" * 47 + "+\n")


def joining_tuple(first_number: int, second_number: int) -> tuple:
    """
    Join two integers into a tuple.

    :param first_number: an integer
    :param second_number: an integer
    :pre-condition: first_number must be an integer
    :pre-condition: second_number must be an integer
    :post-condition: correctly joins two integers into a tuple
    :return: tuple of the two integers

    >>> joining_tuple(0, 0)
    (0, 0)
    >>> joining_tuple(2, 17)
    (2, 17)
    """
    return first_number, second_number


def healing_landmarks(character_stats: dict):
    """
    Generate 8 coordinate tuples and update the information in the character stats dictionary.

    The 8 coordinate tuples are converted to a list and the list is added to the character stats dictionary with
    "healing_landmarks" as the key.

    :param character_stats: dictionary containing character information
    :pre-condition: character_stats must be a dictionary
    :post-condition: correctly generates 8 coordinate tuples and updates the information in character stats dictionary
    :return: None
    """
    number_pool = list(range(1, 23))
    x_coordinate_number_list = []
    y_coordinate_number_list = []
    for counter in range(8):
        x_coordinate_number_list = (random.sample(number_pool, 8))
        y_coordinate_number_list = (random.sample(number_pool, 8))
    joined_coordinates = map(joining_tuple, x_coordinate_number_list, y_coordinate_number_list)
    healing_landmarks_coordinates = list(joined_coordinates)
    character_stats["healing_landmarks"] = healing_landmarks_coordinates


def healing_fountain(character_stats: dict):
    """
    Heal player health points with the number of coins randomly generated at healing landmark locations.

    :param character_stats: dictionary containing character information
    :pre-condition: character_stats must be a dictionary
    :pre-condition: user must enter a valid input
    :post-condition: correctly heals player health points with the number of coins randomly generated at healing
                     landmark locations
    :post-condition: correctly updates player health points in character_stats
    :return: None
    """
    healing_coins = random.randint(5, 10)
    print(HEALING_FOUNTAIN_WELCOME_MESSAGE())
    healing_options = ["Yes", "No"]
    numbered_menu = number_menu_items(healing_options)
    healing_choice = input(f"{numbered_menu}\n\nYou found {healing_coins} coins on the ground.\nWant to throw the "
                           f"coins you picked up into the fountain to replenish your hp? \nOne coin = 1 hp ;)\n> ")
    if healing_choice == "0":
        print(list(itertools.repeat("SPLISH-SPLASH...", healing_coins)))
        character_stats["player_hp"] += healing_coins
        if character_stats["player_hp"] > character_stats["max_player_hp"]:
            extra_hp = character_stats["player_hp"] - character_stats["max_player_hp"]
            character_stats["player_hp"] -= extra_hp
        print(f"\nWow! You healed! You now have {character_stats['player_hp']} hp!{TextColors.ENDC}\n")
    elif healing_choice == "1":
        print(REJECT_HEALING_FOUNTAIN_MESSAGE())


def boss_trigger(character_stats: dict) -> bool:
    """
    Update enemy information stored in character_stats dictionary if the player is on the final boss coordinate.

    :param character_stats: dictionary containing character information
    :pre-condition: character_stats must be a dictionary
    :pre-condition: player must at final boss location
    :post-condition: correctly updates enemy information stored in character_stats dictionary if the player is on the
                     final boss coordinate
    :return: boolean True or False representing user choice to enter combat

    >>> player_stats = {"current_location": (12, 24), "enemy_hp": 20, "current_enemy": "Hannibal", \
                        "enemy_description": "foo"}
    >>> at_boss_location = boss_trigger(player_stats)
    >>> at_boss_location
    True
    >>> player_stats = {"current_location": (15, 19), "enemy_hp": 20, "current_enemy": "Hannibal", \
                        "enemy_description": "foo"}
    >>> at_boss_location = boss_trigger(player_stats)
    >>> at_boss_location
    False
    """
    boss_stats = BOSS_INFORMATION()
    if character_stats["current_location"] == (boss_stats["x_coordinate"], boss_stats["y_coordinate"]):
        character_stats["enemy_hp"] = boss_stats["enemy_hp"]
        character_stats["current_enemy"] = boss_stats["boss_name"]
        character_stats["enemy_description"] = boss_stats["description"]
        return True
    else:
        return False


def number_menu_items(menu_items) -> list:
    """
    Create number menu items for user selection choice.

    :param menu_items: list containing the user selection choices
    :pre-condition: menu_items must be a list
    :post-condition: correctly creates numbered menu items for user selection choice
    :post-condition: returns a list
    :return: an enumerated list to present numbered menu items for user selection choice
    >>> choice_items = ["Yes", "No"]
    >>> number_menu = number_menu_items(choice_items)
    >>> number_menu
    [(0, 'Yes'), (1, 'No')]
    >>> choice_items = ["Quit", "North", "South", "East", "West"]
    >>> number_menu = number_menu_items(choice_items)
    >>> number_menu
    [(0, 'Quit'), (1, 'North'), (2, 'South'), (3, 'East'), (4, 'West')]
    """
    numbered_menu = enumerate(menu_items, 0)
    return list(numbered_menu)


def get_user_direction_choice(character_stats: dict) -> str:
    """
    Accept user input of movement direction choice and return a string representing the direction choice.

    :param character_stats: dictionary containing character information
    :pre-condition: character_stats must be a dictionary
    :pre-condition: user must enter a valid input
    :post-condition: correctly accepts user input of movement direction choice and returns a string representing
                     the direction choice
    :return: string representing user direction choice
    """
    validated = False
    current_location = character_stats["current_location"]
    while not validated:
        print(f"\nYour current location is {current_location}")
        menu_items = ["Quit", "North", "South", "East", "West"]
        numbered_menu = number_menu_items(menu_items)
        user_input = input(f"{numbered_menu}\n\nType the number of the way you wish to go: \n> ")
        return user_input


def movement_coordinator(character_stats: dict, user_direction_choice: str):
    """
    Coordinator function that calls movement-related functions.

    :param character_stats: dictionary containing character information
    :param user_direction_choice: string representing user direction choice
    :pre-condition: character_stats must be a dictionary
    :pre-condition: user_direction_choice must be a string
    :post-condition: correctly calls other movement-related functions
    :post-condition: correctly updates player current location in character_stats
    :return: None
    """
    if (character_stats["y_coordinate"] == 8) and (character_stats["x_coordinate"] in (11, 12, 13)) and \
            (user_direction_choice == "2") and (character_stats["player_level"] == 2):
        graveyard_screen()
    if (character_stats["y_coordinate"] == 14) and (character_stats["x_coordinate"] in (11, 12, 13)) and \
            (user_direction_choice == "2") and (character_stats["player_level"] == 3):
        circus_screen()
    level_one_region_restriction(user_direction_choice, character_stats)
    level_two_region_restriction(user_direction_choice, character_stats)
    validated_move = validate_move(user_direction_choice, character_stats)
    if validated_move:
        move_direction(character_stats, user_direction_choice)
        board = make_board(character_stats)
        print_board(character_stats, board)
        if character_stats["current_location"] in character_stats["healing_landmarks"]:
            healing_fountain(character_stats)


def validate_move(user_input: str, character_stats: dict) -> bool:
    """
    Check if the user's desired movement choice is a valid move on the game board.

    :param character_stats: dictionary containing character information
    :param user_input: string representing user direction choice
    :pre-condition: character_stats must be a dictionary
    :pre-condition: user_input must be a string
    :post-condition: correctly checks if the user's desired movement choice is a valid move on the game board
    :return: Boolean True or False representing if user's desired movement choice is a valid move on the game board

    >>> player_stats = {"x_coordinate": 0, "y_coordinate": 2}
    >>> valid_move = validate_move("1", player_stats)
    >>> valid_move
    True
    >>> player_stats = {"x_coordinate": 14, "y_coordinate": 24}
    >>> valid_move = validate_move("3", player_stats)
    >>> valid_move
    True
    """
    if user_input == "1" and character_stats["y_coordinate"] != 0:
        return True
    elif user_input == "2" and character_stats["y_coordinate"] != 24:
        return True
    elif user_input == "3" and character_stats["x_coordinate"] != 24:
        return True
    elif user_input == "4" and character_stats["x_coordinate"] != 0:
        return True
    else:
        print(f"\n{TextColors.RED}You've hit a wall! You cannot go that way. Please try again.{TextColors.ENDC}")
        return False


def move_direction(character_stats: dict, user_input: str):
    """
    Move player location based on user's desired movement choice.

    :param character_stats: dictionary containing character information
    :param user_input: string representing user direction choice
    :pre-condition: user must be on the game board
    :pre-condition: character_stats must be a dictionary
    :pre-condition: user_input must be a string
    :pre-condition: user's desired movement choice must be valid
    :post-condition: correctly updates player current location in character_stats
    :return: None

    >>> player_stats = {"x_coordinate": 2, "y_coordinate": 2, "current_location": (2, 2)}
    >>> move_direction(player_stats, "1")
    <BLANKLINE>
    Your new location is (2, 1)
    <BLANKLINE>
    >>> player_stats
    {'x_coordinate': 2, 'y_coordinate': 1, 'current_location': (2, 1)}
    >>> player_stats = {"x_coordinate": 23, "y_coordinate": 23, "current_location": (23, 23)}
    >>> move_direction(player_stats, "4")
    <BLANKLINE>
    Your new location is (22, 23)
    <BLANKLINE>
    >>> player_stats
    {'x_coordinate': 22, 'y_coordinate': 23, 'current_location': (22, 23)}
    """
    if user_input == "1":
        character_stats["y_coordinate"] -= 1
    elif user_input == "2":
        character_stats["y_coordinate"] += 1
    elif user_input == "3":
        character_stats["x_coordinate"] += 1
    elif user_input == "4":
        character_stats["x_coordinate"] -= 1
    else:
        print("I didn't catch what you said because you can't type properly! UGH! Let's try again and please type "
              "better this time or I'm sending a ghost your way D:<")
    character_stats["current_location"] = (character_stats["x_coordinate"], character_stats["y_coordinate"])
    print(f"\nYour new location is {character_stats['current_location']}\n")


def check_for_enemy(character_stats: dict) -> bool:
    """
    Check if an enemy is present at a player's location and heal player for 4 health points if there's no enemy.

    :param character_stats: dictionary containing character information
    :pre-condition: character_stats must be a dictionary
    :pre-condition: player must be on the game board
    :pre-condition: player's location must not be at the boss coordinate or healing landmarks
    :post-condition: correctly checks if an enemy is present at a player's location, and heals player for 4 health
                        points if there's no enemy
    :return: Boolean True or False representing if an enemy is present at a player's location
    """
    monster_probability = random.randint(1, 10)
    if monster_probability <= 2:
        print("You've encountered an enemy!")
        return True
    else:
        print("No enemy in sight! You heal for 4 HP!")
        character_stats["player_hp"] += AUTOHEAL_HP()
        if character_stats["player_hp"] > character_stats["max_player_hp"]:
            extra_hp = character_stats["player_hp"] - character_stats["max_player_hp"]
            character_stats["player_hp"] -= extra_hp
        print(f"You now have {character_stats['player_hp']} health points!\n")
        return False


def assign_enemy_stats(character_stats: dict):
    """
    Assign enemy and enemy description based on level regions and update information in character_stats dictionary

    :param character_stats: dictionary containing character information
    :pre-condition: character_stats must be a dictionary
    :pre-condition: player must be on the game board
    :pre-condition: players location must not be at the boss coordinate or healing landmarks
    :post-condition: correctly assigns enemy statistics and description based on level regions and updates information
                     in the character_stats dictionary
    :return: None
    """
    enemy_selection = random.randint(1, 6)
    enemy_names = LEVEL_1_ENEMY_NAMES()
    enemy_description = LEVEL_1_ENEMY_DESCRIPTIONS()
    if character_stats["y_coordinate"] > 8 and (character_stats["y_coordinate"] <= 14):
        character_stats["enemy_hp"] = LEVEL_2_ENEMIES_HP()
        enemy_names = LEVEL_2_ENEMY_NAMES()
        enemy_description = LEVEL_2_ENEMY_DESCRIPTIONS()
    elif character_stats["y_coordinate"] > 14:
        character_stats["enemy_hp"] = LEVEL_3_ENEMIES_HP()
        enemy_names = LEVEL_3_ENEMY_NAMES()
        enemy_description = LEVEL_3_ENEMY_DESCRIPTIONS()
    else:
        character_stats["enemy_hp"] = LEVEL_1_ENEMIES_HP()
    character_stats["current_enemy"] = enemy_names[enemy_selection]
    character_stats["enemy_description"] = enemy_description[enemy_selection]


def choose_to_combat(character_stats: dict) -> bool:
    """
    Ask if the user would like to enter combat.

    Accept user input and return True if the user would like to enter combat and False if not.

    :param character_stats: dictionary containing character information
    :pre-condition: character_stats must be a dictionary
    :pre-condition: user must enter a valid input
    :post-condition: correctly accepts user input and returns user choice as a Boolean value
    :return: boolean True or False representing user choice to enter combat
    """
    menu_items = ["Yes", "No"]
    numbered_menu = number_menu_items(menu_items)
    print(f"{TextColors.RED}{character_stats['enemy_description']}{TextColors.ENDC}")
    combat_decision = input(f"\n{numbered_menu}\n\nBrave adventurer, you currently have {character_stats['player_hp']} "
                            f"hp. {TextColors.PURPLE}{character_stats['current_enemy']}{TextColors.ENDC} has "
                            f"{character_stats['enemy_hp']} health points. Would you like to enter combat? \n> ")
    if combat_decision == "0":
        return True
    elif combat_decision == "1":
        return False


def player_flee(character_stats: dict):
    """
    Decide if the user suffers damage or death for running away from combat.

    :param character_stats: dictionary containing character information
    :pre-condition: character_stats must be a dictionary
    :post-condition: decides if the user receives damage or death for fleeing
    :post-condition: allocates damage or death if necessary and prints confirmations
    :post-condition: prints a message if player flees safely
    :return: None
    """
    backstabbing_probability = random.randint(1, 10)
    if backstabbing_probability <= 2:
        monster_attack = random.randint(1, 10)
        print(f"AH! OUCH! OH NO! You've been back-stabbed by the enemy! You lost {monster_attack} hp.")
        character_stats["player_hp"] -= monster_attack
        if character_stats["player_hp"] > 0:
            print(f"You now have {character_stats['player_hp']} health points.")
        else:
            print(f"Oh no you died. This is the end of your journey, brave warrior ...")
            sys.exit()
    else:
        print("Luck is on your side! You have successfully run away from the enemy.")


def enemy_flee() -> bool:
    """
    Decide if enemy flees combat.

    :post-condition: decides if enemy flees and returns True if enemy flees or False if enemy does not
    :return: True if enemy flees or False if enemy does not
    """
    enemy_flee_probability = random.randint(1, 10)
    if enemy_flee_probability <= 2:
        print("\nThe enemy ran away.\n")
        return True
    else:
        return False


def roll_for_initiative() -> str:
    """
    Rolls for initiative to decide which party has first round of combat.

    :post-condition: checks which party rolled highest and returns the name of that party, else, another check is done
    return: None
    """
    print(f"\nEnter combat round !!!!!! \nRoll die for initiative (drumroll please ......)\n")
    player_roll = random.randint(1, 100)
    monster_roll = random.randint(1, 100)
    if player_roll > monster_roll:
        print("You've rolled a bigger number! You're striking first!")
        return "player"
    elif monster_roll > player_roll:
        print("The enemy rolled a bigger number! The enemy is striking first!")
        return "enemy"
    else:
        print("Wow you just experienced the 0.0001 probability where both sides roll the same number on a 100 side die."
              "\nIf I were you, I'd go buy a lottery ticket right now ;)")


def enemy_attack(character_stats: dict):
    """
    Allocate damage the character takes from the enemy and initiate death sequence if necessary

    :param character_stats: dictionary containing character information
    :pre-condition: character_stats must be a dictionary
    :pre-condition: the player's hp must be greater than zero at the start of the enemy attack
    :post-condition: allocates damage the character receives and initiates death sequence if necessary
    :return: None
    """
    print(f"\nYour foe attacks!")
    damage_points = enemy_damage_calculation(character_stats)
    print(f"You take {damage_points} damage!")
    character_stats["player_hp"] -= damage_points
    if character_stats["player_hp"] <= 0:
        print(f"You have died. This is the end...but the adventure may continue if you choose a new character...")
        sys.exit()
    print(f"You now have {character_stats['player_hp']} health points.")


def enemy_damage_calculation(character_stats: dict) -> int:
    """
    Calculate damage enemy can do to the character.

    :param character_stats: dictionary containing character information
    :pre-condition: character_stats must be a dictionary
    :post-condition: assigns max damage according to the player's current enemy and decides the damage value the
                        character will take
    :return: damage value the character will take
    """
    enemy_damage = LEVEL_1_ENEMY_DAMAGE()
    boss_stats = BOSS_INFORMATION()
    if character_stats["current_location"] == (boss_stats["x_coordinate"], boss_stats["y_coordinate"]):
        enemy_damage = boss_stats["enemy_damage"]
        return random.randint(boss_stats["enemy_damage_minimum"], enemy_damage)
    elif character_stats["player_level"] == 2:
        enemy_damage = LEVEL_2_ENEMY_DAMAGE()
    elif character_stats["player_level"] == 3:
        enemy_damage = LEVEL_3_ENEMY_DAMAGE()
    else:
        return random.randint(1, enemy_damage)
    return random.randint(1, enemy_damage)


def combat_coordinator(character_stats: dict, initiative_winner: str):
    """
    Process through the combat flow.

    :param character_stats: dictionary containing character information
    :param initiative_winner: a string
    :pre-condition: character_stats must be a dictionary
    :pre-condition: initiative_winner is either "player" or "enemy"
    :post-condition: character engages in combat according to their win or loss in the intiative roll
    :return: None
    """
    if initiative_winner == "player":
        outcome = player_attack(character_stats)
        if character_stats["re-rolls"] > 0 and outcome == "missed":
            print(SHRIEKING_STUMBLER_EXTRA_HIT_MESSAGE())
            player_attack(character_stats)
        if character_stats["player_hp"] > 0 and character_stats["enemy_hp"] > 0:
            enemy_attack(character_stats)
    elif initiative_winner == "enemy":
        enemy_attack(character_stats)
        if character_stats["player_hp"] > 0 and character_stats["enemy_hp"] > 0:
            outcome = player_attack(character_stats)
            if character_stats["re-rolls"] > 0 and outcome == "missed":
                print(SHRIEKING_STUMBLER_EXTRA_HIT_MESSAGE())
                player_attack(character_stats)


def light_attack(character_stats: dict):
    """
    Allocate damage to enemy from dealing light attack.

    :param character_stats: dictionary containing character information
    :pre-condition: character_stats must be a dictionary
    :post-condition: enemy receives damage from light attack
    :return: None

    >>> my_character_stats = {"enemy_hp": 10, "light_damage": 5}
    >>> light_attack(my_character_stats) # doctest: +NORMALIZE_WHITESPACE
    You have chosen light attack. Risk free with light but consistent attack.
    You attack!
    You deal 5 damage!
    >>> my_character_stats
    {'enemy_hp': 5, 'light_damage': 5}
    >>> my_character_stats = {"enemy_hp": 1, "light_damage": 5}
    >>> light_attack(my_character_stats) # doctest: +NORMALIZE_WHITESPACE
    You have chosen light attack. Risk free with light but consistent attack.
    You attack!
    You deal 5 damage!
    """
    print("\nYou have chosen light attack. Risk free with light but consistent attack.")
    character_stats["enemy_hp"] -= character_stats["light_damage"]
    print(f"\nYou attack! \nYou deal {character_stats['light_damage']} damage!")


def medium_attack(character_stats: dict, attack_hit_chance: int):
    """
    Allocate damage to enemy from dealing medium attack.

    :param character_stats: dictionary containing character information
    :param attack_hit_chance: chance of attack landing
    :pre-condition: character_stats must be a dictionary
    :pre-condition: attack_hit_chance must be a non-zero positive number
    :post-condition: enemy receives damage from medium attack or it misses
    :return: None

    >>> my_character_stats = {"enemy_hp": 20, "medium_damage": 10, "medium_attack_hit_chance": 7}
    >>> medium_attack(my_character_stats, 7) # doctest: +NORMALIZE_WHITESPACE
    You have chosen medium attack. Solid safe choice.
    You attack!
    You deal 10 damage!
    """
    print("\nYou have chosen medium attack. Solid safe choice.")
    if attack_hit_chance <= character_stats["medium_attack_hit_chance"]:
        character_stats["enemy_hp"] -= character_stats["medium_damage"]
        print(f"\nYou attack! \nYou deal {character_stats['medium_damage']} damage!")
    else:
        print("Oh no! You panicked and missed your shot!")


def heavy_attack(character_stats: dict):
    """
    Allocate damage to enemy from dealing medium attack.

    :param character_stats: dictionary containing character information
    :pre-condition: character_stats must be a dictionary
    :post-condition: enemy receives damage from heavy attack
    :return: None

    >>> my_character_stats = {"enemy_hp": 20, "heavy_damage": 15}
    >>> heavy_attack(my_character_stats) # doctest: +NORMALIZE_WHITESPACE
    You have chosen heavy attack. Seems like you're a fan of high risk high reward.
    You attack!
    You deal 15 damage!
    """
    print("\nYou have chosen heavy attack. Seems like you're a fan of high risk high reward.")
    character_stats["enemy_hp"] -= character_stats["heavy_damage"]
    print(f"\nYou attack! \nYou deal {character_stats['heavy_damage']} damage!")


def critical_attack(character_stats: dict, user_input: str):
    """
    Allocate damage for a critical attack/special attack.

    :param character_stats: dictionary containing character information
    :param user_input: a string
    :pre-condition: character_stats must be a dictionary
    :pre-condition: user_input must be either "0" or "2"
    :post-condition: enemy takes special attack/critical attack damage
    :return: None
    """
    if user_input == "0":
        character_stats["enemy_hp"] -= character_stats["light_damage"] * 2
        print(f"\nWow! A special attack! \nYou perform {TextColors.GREEN}{character_stats['special_attack']}"
              f"{TextColors.GREEN}{TextColors.ENDC} and deal {TextColors.RED}{character_stats['light_damage'] * 2}"
              f"{TextColors.ENDC} damage to the enemy!")
    elif user_input == "2":
        character_stats["enemy_hp"] -= character_stats["heavy_damage"] * 2
        print(f"\nWow! A special attack! \nYou perform {TextColors.GREEN}{character_stats['special_attack']}"
              f"{TextColors.GREEN}{TextColors.ENDC} and deal {TextColors.RED}{character_stats['heavy_damage'] * 2}"
              f"{TextColors.ENDC} damage to the enemy!")


def print_attack_menu(character_stats: dict):
    """
    Print a menu listing attacks to choose from.

    :param character_stats: dictionary containing character information
    :pre-condition: character_stats must be a dictionary
    :pre-condition: character_stats must have valid values for all attack values needed for the attack menu
    :post-condition: prints an attack menu in color listing possible attacks for the player to choose
    :return: None
    """
    print()
    attack_menu = PrettyTable()
    attack_menu.field_names = [f"{TextColors.YELLOW}ATTACKS{TextColors.ENDC}", f"{TextColors.YELLOW}ATTACK % HIT"
                               f"{TextColors.ENDC}", f"{TextColors.YELLOW}SPECIAL ATTACK (CRIT) % HIT{TextColors.ENDC}"]
    attack_menu.add_row([f"{TextColors.GREEN}0. LIGHT{TextColors.ENDC}", f"{TextColors.GREEN}"
                         f"{character_stats['light_attack_hit_chance']}0%{TextColors.ENDC}",
                         f"{TextColors.GREEN}{character_stats['light_attack_critical_hit_chance']}0%{TextColors.ENDC}"])
    attack_menu.add_row([f"{TextColors.GREEN}1. MEDIUM{TextColors.ENDC}", f"{TextColors.GREEN}"
                         f"{character_stats['medium_attack_hit_chance']}0%{TextColors.ENDC}", f"{TextColors.GREEN}0%"
                         f"{TextColors.ENDC}"])
    attack_menu.add_row([f"{TextColors.GREEN}2. HEAVY{TextColors.ENDC}", f"{TextColors.GREEN}"
                         f"{character_stats['heavy_attack_hit_chance']}0%{TextColors.ENDC}",
                         f"{TextColors.GREEN}{character_stats['heavy_attack_critical_hit_chance']}0%{TextColors.ENDC}"])
    print(attack_menu)
    print()


def player_attack(character_stats: dict) -> str:
    """
    Decide what attack the player will do and if it is successful.

    :param character_stats: dictionary containing character information
    :pre-condition: character_stats must be a dictionary
    :pre-condition: enemy hp must not be zero
    :post-condition: decide what kind of attack the character will do and if it is successful
    :return: "missed" or None
    """
    initial_enemy_hp = character_stats["enemy_hp"]
    print_attack_menu(character_stats)
    user_input = input(f"What type of attack do you want to go for? (Please type the number of the attack)\n> ")
    critical_hit_chance = random.randint(1, 10)
    attack_hit_chance = random.randint(1, 10)
    type_of_attack(character_stats, user_input, critical_hit_chance, attack_hit_chance)
    if initial_enemy_hp == character_stats["enemy_hp"]:
        return "missed"


def validate_missed_attack(character_stats: dict, initial_enemy_hp: int) -> str:
    """
    Validate if the player landed their attack.

    :param character_stats: dictionary containing character information
    :param initial_enemy_hp: an integer
    :pre-condition: character_stats must be a dictionary
    :pre-condition: initial_enemy_hp must be nonzero
    :post-condition: checks if attack was missed
    :return: "missed" or None

    >>> my_character_stats = {"enemy_hp": 10}
    >>> test_initial_enemy_hp = 10
    >>> validate_missed_attack(my_character_stats, test_initial_enemy_hp)
    'missed'
    >>> my_character_stats = {"enemy_hp": 5}
    >>> test_initial_enemy_hp = 10
    >>> validate_missed_attack(my_character_stats, test_initial_enemy_hp)
    """
    if initial_enemy_hp == character_stats["enemy_hp"]:
        return "missed"


def type_of_attack(character_stats: dict, user_input: str, critical_hit_chance: int, attack_hit_chance: int):
    """
    Use player input to initiative an attack.

    Use player input to initiate an attack and check if a special attack is triggered.

    :param character_stats: dictionary containing character information
    :param user_input: a string
    :param critical_hit_chance: an integer
    :param attack_hit_chance: an integer
    :pre-condition: character_stats must be a dictionary
    :pre-condition: user_input must be either "0", "1", or "2"
    :pre-condition: critical_hit_chance must be a non-zero positive integer
    :pre-condition: attack_hit_chance must be a non-zero positive integer
    :post-condition: initiates attack or confirms attack miss
    :return: None
    """
    if user_input == "0":
        if critical_hit_chance <= character_stats["light_attack_critical_hit_chance"]:
            critical_attack(character_stats, user_input)
        else:
            light_attack(character_stats)
    elif user_input == "1":
        medium_attack(character_stats, attack_hit_chance)
    elif user_input == "2":
        if critical_hit_chance <= character_stats["heavy_attack_critical_hit_chance"] and attack_hit_chance <= \
         character_stats["heavy_attack_hit_chance"]:
            critical_attack(character_stats, user_input)
        elif attack_hit_chance <= character_stats["heavy_attack_hit_chance"]:
            heavy_attack(character_stats)
        else:
            print("Oh no! You panicked and missed your shot!")


def validate_enemy_death(character_stats: dict) -> bool:
    """
    Allocate experience points if enemy has died.

    :param character_stats: dictionary containing character information
    :pre-condition: character_stats must be a dictionary
    :pre-condition: character_stats must contain a valid value for enemy hp
    :post-condition: prints a confirmation of experience awarded if enemy has died and returns True, else, returns False
    :return: True or False

    >>> my_character_stats = {"enemy_hp": 0, "player_xp": 100}
    >>> validate_enemy_death(my_character_stats)
    You have defeated your foe! You're a true warrior! You gained 100 experience points and now you have 200 xp.
    True
    >>> my_character_stats = {"enemy_hp": 10, "player_xp": 100}
    >>> validate_enemy_death(my_character_stats)
    False
    """
    if character_stats["enemy_hp"] <= 0:
        character_stats["player_xp"] += EXPERIENCE_POINT_GAINS()
        print(f"You have defeated your foe! You're a true warrior! "
              f"You gained 100 experience points and now you have {character_stats['player_xp']} xp.")
        return True
    else:
        return False


def level_up(character_stats: dict):
    """
    Level up character when they have reached a level's experience point threshold.

    :param character_stats: dictionary containing character information
    :pre-condition: character_stats must be a dictionary
    :pre-condition: the player xp dictionary key in character_stats must be a positive integer
    :post-condition: updates all character stats if the player has reached a level's experience point threshold
    :return: None
    """
    if character_stats["player_xp"] == LEVEL_TWO_XP_THRESHOLD():
        character_stats.update(LEVEL_TWO_STATS())
        class_level_2(character_stats)
        character_stats["max_player_hp"] += LEVEL_UP_HP_INCREASE()
        character_stats["player_hp"] = character_stats["max_player_hp"]
    elif character_stats["player_xp"] == LEVEL_THREE_XP_THRESHOLD():
        character_stats.update(LEVEL_THREE_STATS())
        class_level_3(character_stats)
        character_stats["max_player_hp"] += LEVEL_UP_HP_INCREASE()
        character_stats["player_hp"] = character_stats["max_player_hp"]


def class_level_2(character_stats: dict) -> dict:
    """
    Update class stats if the player has leveled to level two and confirm level up to player.

    :param character_stats: dictionary containing character information
    :pre-condition: character_stats must be a dictionary
    :post-condition: character_stats is updated with new level values and prints a levelling confirmation message
    :return: character_stats
    """
    if character_stats['player_class'] == "SHRIEKING STUMBLER":
        character_stats.update(PLAYER_CLASS_SHRIEKING_STUMBLER_LEVEL_2())
    elif character_stats['player_class'] == "SCHOOL JOCK":
        character_stats.update(PLAYER_CLASS_SCHOOL_JOCK_LEVEL_2())
    elif character_stats['player_class'] == "COMPUTER NERD":
        character_stats.update(PLAYER_CLASS_COMPUTER_NERD_LEVEL_2())
    else:
        character_stats.update(PLAYER_CLASS_THE_NATURAL_LEVEL_2())
    print(f"\n{TextColors.YELLOW}~~~~You have leveled up to level 2. Congratulations!~~~~\n\n")
    print(f"{TextColors.PURPLE}CLASS: {character_stats['player_class']}\n\n{TextColors.YELLOW}::LEVEL GAINS::\n"
          f"{TextColors.BLUE}SUBCLASS: {character_stats['class_level']}\n{TextColors.RED}SPECIAL ATTACK: "
          f"{character_stats['special_attack']}\nDAMAGE +10\n{TextColors.CYAN}+10 HP{TextColors.ENDC}")
    return character_stats


def class_level_3(character_stats: dict) -> dict:
    """
    Update class stats if the player has leveled to level three and confirm level up to player.

    :param character_stats: dictionary containing character information
    :pre-condition: character_stats must be a dictionary
    :post-condition: character_stats is updated with new level values and prints a levelling confirmation message
    :return: character_stats
    """
    if character_stats['player_class'] == "SHRIEKING STUMBLER":
        character_stats.update(PLAYER_CLASS_SHRIEKING_STUMBLER_LEVEL_3())
    elif character_stats['player_class'] == "SCHOOL JOCK":
        character_stats.update(PLAYER_CLASS_SCHOOL_JOCK_LEVEL_3())
    elif character_stats['player_class'] == "COMPUTER NERD":
        character_stats.update(PLAYER_CLASS_COMPUTER_NERD_LEVEL_3())
    else:
        character_stats.update(PLAYER_CLASS_THE_NATURAL_LEVEL_3())
    print(f"\n{TextColors.YELLOW}~~~~You have leveled up to level 3. Congratulations!~~~~\n\n")
    print(f"{TextColors.PURPLE}CLASS: {character_stats['player_class']}\n\n{TextColors.YELLOW}::LEVEL GAINS::\n"
          f"{TextColors.BLUE}SUBCLASS: {character_stats['class_level']}\n{TextColors.RED}SPECIAL ATTACK: "
          f"{character_stats['special_attack']}\nDAMAGE +10\n{TextColors.CYAN}+10 HP{TextColors.ENDC}")
    return character_stats


def level_one_region_restriction(user_input: str, character_stats: dict):
    """
    Check if player is attempting to enter an area they are not allowed, stop them, and notify them.

    :param character_stats: dictionary containing character information
    :param user_input: a string
    :pre-condition: character_stats must be a dictionary
    :pre-condition: user_input must be "2"
    :post-condition: checks if player is attempting to enter an area they are not allowed, resets their coordinates,
                        and prints a message notifying them
    :return: None
    """
    if (character_stats["y_coordinate"] == 8) and (character_stats["x_coordinate"] in (11, 12, 13)) and \
            (user_input == "2"):
        if character_stats["player_level"] == 1:
            print(f"\n{TextColors.RED}You have arrived at the gate! \nHowever, the next region is locked until you "
                  f"reach level 2! \nGo kill more enemies then come back!{TextColors.ENDC}")
            character_stats["y_coordinate"] -= 1
    elif character_stats["y_coordinate"] == 8 and user_input == "2":
        print(f"\n{TextColors.RED}You think you can just walk past me?! \nNope! I'm a wall that separates you "
              f"and the next zone. \nPlease use the gates to go to the next region like a normal "
              f"human being!{TextColors.ENDC}")
        character_stats["y_coordinate"] -= 1


def level_two_region_restriction(user_input: str, character_stats: dict):
    """
    Check if player is attempting to enter an area they are not allowed, stop them, and notify them.

    :param character_stats: dictionary containing character information
    :param user_input: a string
    :pre-condition: character_stats must be a dictionary
    :pre-condition: user_input must be "2"
    :post-condition: checks if player is attempting to enter an area they are not allowed, resets their coordinates,
                        and prints a message notifying them
    :return: None
    """
    if (character_stats["y_coordinate"] == 14) and (character_stats["x_coordinate"] in (11, 12, 13)) and \
            (user_input == "2"):
        if character_stats["player_level"] == 2:
            print(f"\n{TextColors.RED}You have arrived at the gate! \nHowever, the next region is locked until you "
                  f"reach level 3! \nGo kill more enemies then come back!{TextColors.ENDC}")
            character_stats["y_coordinate"] -= 1
    elif character_stats["y_coordinate"] == 14 and user_input == "2":
        print(f"\n{TextColors.RED}You think you can just walk past me?! \nNope! I'm a wall that separates you "
              f"and the next zone. \nPlease use the gates to go to the next region like a normal "
              f"human being!{TextColors.ENDC}")
        character_stats["y_coordinate"] -= 1


def boss_sequence(character_stats: dict):
    """
    Proceed through the boss combat flow.

    :param character_stats: dictionary containing character information
    :pre-condition: character_stats must be a dictionary
    :pre-condition: the current enemy must be the boss
    :post-condition: proceeds through the combat sequence and triggers player death if player dies, else, begins game
                        victory sequence and exits the game
    :return: None
    """
    combat_decision = choose_to_combat(character_stats)
    if combat_decision:
        while character_stats["player_hp"] > 0 and character_stats["enemy_hp"] > 0:
            initiative_winner = roll_for_initiative()
            combat_coordinator(character_stats, initiative_winner)
            enemy_death = validate_enemy_death(character_stats)
            if not enemy_death:
                print(f"The enemy now has {character_stats['enemy_hp']} hp.")
            else:
                win_game(character_stats)
                sys.exit()


def enemy_sequence(character_stats: dict):
    """
    Proceed through enemy combat sequence.

    :param character_stats: dictionary containing character information
    :pre-condition: character_stats must be a dictionary
    :post-condition: character fights to the death, wins combat, or flees combat
    :return: None
    """
    assign_enemy_stats(character_stats)
    while character_stats["player_hp"] > 0 and character_stats["enemy_hp"] > 0:
        combat_decision = choose_to_combat(character_stats)
        if combat_decision is False:
            player_flee(character_stats)
            break
        elif combat_decision:
            if character_stats["enemy_hp"] > 0:
                initiative_winner = roll_for_initiative()
                combat_coordinator(character_stats, initiative_winner)
    enemy_death = validate_enemy_death(character_stats)
    if enemy_death is False:
        print(f"The enemy now has {character_stats['enemy_hp']} hp.")
    elif enemy_death:
        level_up(character_stats)


def graveyard_screen():
    """Print graveyard region screen and accept user input if user decides to continue game.

    :pre-condition: user must enter a valid input
    :post-condition: correctly prints graveyard screen and accepts user input if user decides to continue game
    :return: None
    """
    print(GRAVEYARD_IMAGE())
    start_game = input(f"\n\n\n{TextColors.YELLOW}::BRAVING THE GRAVEYARD::\n\nFinally, you find yourself drawn to "
                       f"some gates. You can't quite explain it, but something inside you is telling you that you must "
                       f"go through.\n\n{TextColors.RED}Please press ENTER to CONTINUE.{TextColors.ENDC}\n\n> ")
    if start_game is None:
        return


def circus_screen():
    """Print circus region screen and accept user input if user decides to continue game.

    :pre-condition: user must enter a valid input
    :post-condition: correctly prints circus screen and accepts user input if user decides to continue game
    :return: None
    """
    print(CIRCUS_IMAGE())
    start_game = input(f"\n\n\n{TextColors.YELLOW}::HORROR AT THE CIRCUS::\n\nYou stumble out of the graveyard, wiping"
                       f" the last bits of ghoulish nasty who knows what off your shirt. You look up and find yourself"
                       f" in front of what\nlooks like a circus tent. Feelings come rushing back of your fear of "
                       f"clowns. After the night you've been having, you're expecting the worst.\nIn fact, the clown "
                       f"you see at the entrance to the tent has some teeth that look pretty...sharp. Nonetheless, you "
                       f"know that you must go inside and brave what\nlies within.\n\n{TextColors.RED}Please press "
                       f"ENTER to CONTINUE.{TextColors.ENDC}\n\n> ")
    if start_game is None:
        return


def win_game(character_stats: dict):
    """Print victory screen.

     :post-condition: correctly prints victory screen
     :return: None
     """
    print(VICTORY_IMAGE())
    print(f"{TextColors.PURPLE}You have defeated {character_stats['current_enemy']}, the boss of this world!\n\n"
          f"{TextColors.YELLOW}You see the world fade around you, and you are back in front of your home. You wonder"
          f" if it might have been all a dream.\nPerhaps in another life, you may be able to experience the adventure"
          f" again. For now, you are just glad to be safe at home.\n\n\nThank you for playing {TextColors.RED}"
          f"HORROR MOVIE ESCAPE{TextColors.YELLOW} from Hannah and Kelly, the CONFUSED SCREAMING dev team!")


def game():
    """ Call all other functions. Loop until user beats the final boss, dies, or enter 'quit'. """
    start_screen()
    character_stats = {}
    create_character(character_stats)
    class_choice = class_choice_prompt()
    assign_class(character_stats, class_choice)
    healing_landmarks(character_stats)
    suburban_neighborhood_screen()
    board = make_board(character_stats)
    print_board(character_stats, board)

    boss_defeated = False
    exit_game = False
    while not boss_defeated and not exit_game:
        user_direction_choice = get_user_direction_choice(character_stats)
        if user_direction_choice == "0":
            print(EXIT_GAME_MESSAGE())
            break
        else:
            movement_coordinator(character_stats, user_direction_choice)
            at_boss_location = boss_trigger(character_stats)
            if at_boss_location is True:
                boss_sequence(character_stats)
            else:
                enemy_exists = check_for_enemy(character_stats)
                if enemy_exists:
                    enemy_sequence(character_stats)


def main():
    """Drive the program."""
    doctest.testmod(verbose=True)
    game()


if __name__ == '__main__':
    main()
