SIZE_WINDOW = 900, 800
IMAGE_BACKGROUND = 'background.jpg'
FONT = 'font.ttf'
BUTTON_SOUND = 'click_button.wav'
SILVER_COLOR = '#c0c0c0'
DARK_SILVER_COLOR = '#a6a6a6'

TABLE_HEADERS = ['name', 'games', 'wins', ' lose', 'score']

LETTERS_GAME = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']


HEAD_INFO_GAME = ['Goal of the game', 'How to arrange ships?', 'How to walk?']
TEXT_INFO_GAME = {'Goal of the game': '''The goal of the game is to defeat the enemy fleet by sinking all its ships.
The cell field is designed to accommodate the flotilla.

It consists of the following units:
    + 4 single-deck (1 cell);
    + 3 double-deck (2 cells);
    + 2 double-deck (3 cells);
    + 1 four-deck (4 cells).''', 'How to arrange ships?': '''Ships are placed so that they do not touch the side and angle.
At the same time, they should stand horizontally or vertically, 
but not diagonally.

For the placement of ships, you can use the following tips:
1) Place large ships in one part of the field, small ships in another:
small ships the enemy will find it quickly, but it will take many
moves to find the big ones.
2) Do not put the ships on the same diagonals.
3) Place ships along the walls of the square: the enemy will be
forced to shoot through empty space.''', 'How to walk?': '''Players report a combination of letters and numbers indicating
the cell on the opponent's field that is being hit.
There can be three results:
    - by (the cell is empty);
    - wounded (multi-deck vessel hit);
    - kill (all cells of the ship are hit).
If the player misses, he passes the move to the enemy, but if he
wounded or killed the ship, he has the right to continue firing until
the first miss. All actions are marked on the cell field.'''}
