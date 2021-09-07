"""
Name: Kelly Olsson & Hannah Kuo
Student number: A01030513 & A01068509
Date: March 28, 2021
"""

from unittest import TestCase
from unittest.mock import patch
import unittest.mock
import io
import game


class TextColors:
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


class TestStartScreen(TestCase):

    @patch('builtins.input', side_effect=[''])
    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_victory_screen_print(self, mock_stdout, mock_input):
        character_stats = {'current_enemy': "THE QUEEN XENOMORPH"}
        game.win_game(character_stats)
        expected = r"""                                                                          / /
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
                            `-'
"""f"{TextColors.PURPLE}You have defeated {character_stats['current_enemy']}, the boss " \
                   f"of this world!\n\n{TextColors.YELLOW}You see the world fade around you, and you are back in " \
                   f"front of your home. You wonder if it might have been all a dream.\nPerhaps in another life, " \
                   f"you may be able to experience the adventure again. For now, you are just glad to be safe at " \
                   f"home.\n\n\nThank you for playing {TextColors.RED}HORROR MOVIE ESCAPE{TextColors.YELLOW} from " \
                   f"Hannah and Kelly, the CONFUSED SCREAMING dev team!\n"
        self.assertEqual(mock_stdout.getvalue(), expected)
