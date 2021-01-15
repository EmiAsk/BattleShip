import sys
import pygame
import random
import config

from error_main import ErrorForm

pygame.font.init()


# рисует клетчатое поле, подписывает его
class Board:
    def __init__(self):
        self.ship = []
        self.height = self.width = 10

    def board(self, row, col, cell_size, ship):
        self.ship = ship
        y = col
        for i in range(1, self.height + 1):
            x = row
            for j in range(self.width):
                color = 'white'
                width = 0
                if self.ship[i - 1][j] == 0:
                    width = 1
                elif self.ship[i - 1][j] == 2:
                    color = 'red'
                elif self.ship[i - 1][j] == 3:
                    color = 'grey'
                pygame.draw.rect(screen, color, (x, y, cell_size, cell_size), width=width)
                pygame.draw.rect(screen, 'white', (x, y, cell_size, cell_size), width=1)

                if i == 1:
                    self.title(x + 10, y - 22, j, 'alpha')
                if j == 0:
                    self.title(x - 25, y + 5, i, 'number')
                x += cell_size
            y += cell_size

    def title(self, x, y, n, type):
        letters = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j')
        color = (255, 255, 255)
        font = pygame.font.Font(None, 30)
        if type == 'number':
            text = font.render(f"{n}", True, color)
        elif type == 'alpha':
            text = font.render(f"{letters[n]}", True, color)
        screen.blit(text, (x, y))

    def headline(self, x, y, text):
        color = 'white'
        font = pygame.font.Font(None, 30)
        text = font.render(text, True, color)
        screen.blit(text, (x + 100, y - 80))


# работа с файлами
class Files:
    def __init__(self):
        self.width = self.height = 10
        if config.map_flag:
            self.read_computer_map()

    def read_computer_map(self):
        with open('computer_ships.txt', 'r') as mapFile:
            ships = []
            all_map = []
            ship = [line.strip().split() for line in mapFile]
            for line in ship:
                if line != ['//']:
                    line = [int(x) for x in line]
                    ships.append(line)
                else:
                    ships = []
                    all_map.append(ships)
            self.write('computer_ships_game.txt', random.choice(all_map))
            config.map_flag = False

    def read(self, file):
        ships = []
        with open(file, 'r') as mapFile:
            ship = [line.strip().split() for line in mapFile]
            for line in ship:
                elem = [int(x) for x in line]
                ships.append(elem)
        return ships

    def write(self, file, ships):
        level_map = open(file, 'w')
        for i in range(self.width):
            for j in range(self.height):
                level_map.write(str(ships[i][j]) + ' ')
            level_map.write('\n')


# проверяет расстановку кораблей
class Ship:
    def __init__(self):
        self.width = self.height = 10
        self.board = [[0] * self.width for _ in range(height)]
        self.left, self.top = 280, 150
        self.cell_size = 30
        self.x_btn, self.y_btn = 380, 500
        self.width_btn, self.height_btn = 100, 40

    def render(self, screen):
        screen.fill((0, 0, 0))
        self.buttons()
        board = Board()
        board.board(self.left, self.top, self.cell_size, self.board)
        board.headline(self.left, self.top, 'you')
        pygame.display.flip()

    def ship(self, x, y):
        if self.left + self.cell_size * 10 >= x >= self.left:
            if self.top + self.cell_size * 10 >= y >= self.top:
                row = (y - self.top) // self.cell_size
                col = (x - self.left) // self.cell_size
                if row < 10 and col < 10:
                    self.board[row][col] ^= 1
                    files = Files()
                    files.write('user_ships.txt', self.board)
                    self.render(screen)

    def buttons(self):
        color = 'white'
        x, y, width, height = 20, 550, 40, 40
        pygame.draw.rect(screen, color, (x, y, width, height), width=1)
        pygame.draw.rect(screen, color, (self.x_btn, self.y_btn, self.width_btn, self.height_btn), width=1)

    def check(self, x, y):
        flag = True
        start = False
        if self.x_btn + self.width_btn >= x >= self.x_btn:
            if self.y_btn + self.height_btn >= y >= self.y_btn:
                start = True
        if start:
            ship_1 = ship_2 = ship_3 = ship_4 = 0
            cnt_w = cnt_h = 0
            for i in range(self.height):
                for j in range(self.width):
                    if self.board[i][j] == 1:
                        flag_1, neighbors_1 = self.check_ship(i, j)
                        if flag_1 is False:
                            flag = False
                        cnt_w += 1
                        if cnt_w > 4:
                            flag = False
                        if neighbors_1 == 0 and flag_1:
                            ship_1 += 1
                            cnt_w = 0
                    if (cnt_w != 0 and self.board[i][j] != 1) or j == 9:
                        if cnt_w == 2 and flag_1:
                            ship_2 += 1
                        elif cnt_w == 3 and flag_1:
                            ship_3 += 1
                        elif cnt_w == 4 and flag_1:
                            ship_4 += 1
                        cnt_w = 0

                    if self.board[j][i] == 1:
                        flag_1, neighbors_1 = self.check_ship(j, i)
                        if flag_1 is False:
                            flag = False
                        cnt_h += 1
                        if neighbors_1 == 0 and flag_1:
                            cnt_h = 0
                        if cnt_h > 4:
                            flag = False
                    if (cnt_h != 0 and self.board[j][i] != 1) or j == 9:
                        if cnt_h == 2 and flag_1:
                            ship_2 += 1
                        elif cnt_h == 3 and flag_1:
                            ship_3 += 1
                        elif cnt_h == 4 and flag_1:
                            ship_4 += 1
                        cnt_h = 0

            if ship_1 != 4 or ship_2 != 3 or ship_3 != 2 or ship_4 != 1:
                flag = False
            if flag:
                files = Files()
                files.write('user_ships.txt', self.board)
            if flag is False:
                ErrorForm()
            return flag

    def check_ship(self, i, j):
        flag = True
        count = 0
        if i == 0 and j == 0:
            if self.board[i][j + 1] == 1:
                count += 1
            if self.board[i + 1][j] == 1:
                count += 1
            if self.board[i + 1][j + 1] == 1:
                flag = False
        elif i == 0 and j == 9:
            if self.board[i][j - 1] == 1:
                count += 1
            if self.board[i + 1][j] == 1:
                count += 1
            if self.board[i + 1][j - 1] == 1:
                flag = False
        elif i == 9 and j == 0:
            if self.board[i - 1][j] == 1:
                count += 1
            if self.board[i][j + 1] == 1:
                count += 1
            if self.board[i - 1][j + 1] == 1:
                flag = False
        elif i == 9 and j == 9:
            if self.board[i][j - 1] == 1:
                count += 1
            if self.board[i - 1][j] == 1:
                count += 1
            if self.board[i - 1][j - 1] == 1:
                flag = False
        elif i == 0:
            if self.board[i][j - 1] == 1:
                count += 1
            if self.board[i][j + 1] == 1:
                count += 1
            if self.board[i + 1][j] == 1:
                count += 1
            if self.board[i + 1][j - 1] == 1 or self.board[i + 1][j + 1]:
                flag = False
        elif i == 9:
            if self.board[i][j - 1] == 1:
                count += 1
            if self.board[i][j + 1] == 1:
                count += 1
            if self.board[i - 1][j] == 1:
                count += 1
            if self.board[i - 1][j - 1] == 1 or self.board[i - 1][j + 1]:
                flag = False
        elif j == 0:
            if self.board[i][j + 1] == 1:
                count += 1
            if self.board[i + 1][j] == 1:
                count += 1
            if self.board[i - 1][j] == 1:
                count += 1
            if self.board[i + 1][j + 1] == 1 or self.board[i - 1][j + 1]:
                flag = False
        elif j == 9:
            if self.board[i][j - 1] == 1:
                count += 1
            if self.board[i - 1][j] == 1:
                count += 1
            if self.board[i + 1][j] == 1:
                count += 1
            if self.board[i + 1][j - 1] == 1 or self.board[i - 1][j - 1]:
                flag = False
        else:
            if self.board[i][j - 1] == 1:
                count += 1
            if self.board[i][j + 1] == 1:
                count += 1
            if self.board[i - 1][j] == 1:
                count += 1
            if self.board[i + 1][j] == 1:
                count += 1
            if self.board[i + 1][j - 1] == 1 or self.board[i - 1][j - 1] or self.board[i + 1][j + 1] == 1 or\
                    self.board[i - 1][j + 1]:
                flag = False
        return flag, count


# сама игра
class Play:
    def __init__(self):
        screen.fill((0, 0, 0))
        self.width = self.height = 10
        self.left, self.top = 70, 150
        self.left_2 = 430
        self.cell_size = 30
        self.x_btn_pause, self.y_btn_pause, self.width_btn_pause, self.height_btn_pause = 20, 550, 40, 40
        self.x_btn, self.y_btn, self.width_btn, self.height_btn = 345, 550, 60, 40
        self.x_user_count, self.y_user_count, self.width_user_count, self.height_user_count = 700, 50, 60, 40
        self.user_count, self.cnt, self.hp = 0, 20, 1
        self.color = 'white'
        self.files = Files()
        self.user_ships = self.files.read('user_ships.txt')
        self.computer_ships = self.files.read('computer_ships_game.txt')
        self.ship = Ship()
        self.board = Board()
        self.boards()
        self.buttons()
        self.count()

    def boards(self):
        board = Board()
        board.board(self.left, self.top, self.cell_size, self.user_ships)
        self.board_game(self.left_2, self.top, self.cell_size)
        board.headline(self.left, self.top, 'you')
        board.headline(self.left_2, self.top, 'computer')
        self.buttons()
        self.count()
        pygame.display.update()

    def buttons(self):
        pygame.draw.rect(screen, self.color, (self.x_btn_pause, self.y_btn_pause, self.width_btn_pause,
                                         self.height_btn_pause), width=1)
        font = pygame.font.Font(None, 30)
        text = font.render(f"?", True, self.color)
        screen.blit(text, (self.x_btn_pause + config.coef, self.y_btn_pause + config.coef))
        pygame.draw.rect(screen, self.color, (self.x_btn, self.y_btn, self.width_btn,
                                              self.height_btn), width=1)

    def count(self):
        pygame.draw.rect(screen, self.color, (self.x_user_count, self.y_user_count, self.width_user_count,
                                  self.height_user_count), width=1)
        font = pygame.font.Font(None, 30)
        text = font.render(f"{self.user_count}", True, self.color)
        screen.blit(text, (self.x_user_count + config.coef, self.y_user_count + config.coef))

    def move_user(self, x, y):
        if self.left_2 + self.cell_size * 10 >= x >= self.left_2:
            if self.top + self.cell_size * 10 >= y >= self.top:
                row = (y - self.top) // self.cell_size
                col = (x - self.left_2) // self.cell_size
                if row < 10 and col < 10:
                    self.check(row, col)
                    return True

    def check(self, row, col):
        if self.computer_ships[row][col] == 0:
            self.computer_ships[row][col] = 3
            self.hp -= 0.1
        elif self.computer_ships[row][col] == 1:
            self.computer_ships[row][col] = 6
            self.user_count = self.user_count + self.cnt * self.hp
            self.hp += 0.15
            self.check_ship_computer(row, col, self.computer_ships)
        self.files.write('computer_ships_game.txt', self.computer_ships)
        self.count()

    def move_computer(self, x_mouse, y_mouse):
        flag = False
        if self.x_btn + self.cell_size * 10 >= x_mouse >= self.x_btn:
            if self.y_btn + self.cell_size * 10 >= y_mouse >= self.y_btn:
                flag = True
        while flag:
            x = random.randint(0, 9)
            y = random.randint(0, 9)
            if [x, y] not in config.ship:
                config.ship.append([x, y])
                config.ship.append([x + 1, y + 1])
                config.ship.append([x + 1, y - 1])
                config.ship.append([x - 1, y + 1])
                config.ship.append([x - 1, y - 1])
                break
        if flag:
            if self.user_ships[x][y] == 0:
                self.user_ships[x][y] = 3
            elif self.user_ships[x][y] == 1:
                self.user_ships[x][y] = 2
                self.check_ship_computer(x, y, self.user_ships)
            if self.ship.check_ship(x, y)[0] == 0:
                self.user_ships[x][y] = 3
                self.check_ship_computer(x, y, self.user_ships)
            self.files.write('user_ships.txt', self.user_ships)
            return True

    def check_ship_computer(self, i, j, ship_color):
        if i == 0 and j == 0:
            ship_color[i + 1][j + 1] = 3
        elif i == 0 and j == 9:
            ship_color[i + 1][j - 1] == 3
        elif i == 9 and j == 0:
            ship_color[i - 1][j + 1] = 3
        elif i == 9 and j == 9:
            ship_color[i - 1][j - 1] = 3
        elif i == 0:
            ship_color[i + 1][j - 1] = 3
            ship_color[i + 1][j + 1] = 3
        elif i == 9:
            ship_color[i - 1][j - 1] = 3
            ship_color[i - 1][j + 1] = 3
        elif j == 0:
            ship_color[i + 1][j + 1] = 3
            ship_color[i - 1][j + 1] = 3
        elif j == 9:
            ship_color[i + 1][j - 1] = 3
            ship_color[i - 1][j - 1] = 3
        else:
            ship_color[i + 1][j + 1] = 3
            ship_color[i + 1][j - 1] = 3
            ship_color[i - 1][j + 1] = 3
            ship_color[i - 1][j - 1] = 3

    def win(self):
        win_user = win_computer = True
        for elem in self.user_ships:
            if 1 in elem:
                win_computer = False
        for elem in self.computer_ships:
            if 1 in elem:
                win_user = False
        return win_user, win_computer

    def move(self):
        self.board.board(self.left, self.top, self.cell_size, self.files.read('user_ships.txt'))
        self.board_game(self.left_2, self.top, self.cell_size)
        if self.win()[0]:
            return False, 'user'
        if self.win()[1]:
            return False, 'computer'
        pygame.display.update()
        return True

    def board_game(self, row, col, cell_size):
        self.ships = self.files.read('computer_ships_game.txt')
        y = col
        for i in range(1, self.height + 1):
            x = row
            for j in range(self.width):
                color = 'white'
                width = 0
                if self.ships[i - 1][j] == 0:
                    width = 1
                if self.ships[i - 1][j] == 1:
                    width = 1
                elif self.ships[i - 1][j] == 2:
                    color = 'red'
                elif self.ships[i - 1][j] == 6:
                    color = 'white'
                elif self.ships[i - 1][j] == 3:
                    color = 'grey'
                pygame.draw.rect(screen_1, color, (x, y, cell_size, cell_size), width=width)
                pygame.draw.rect(screen_1, self.color, (x, y, cell_size, cell_size), width=1)
                if i == 1:
                    self.board.title(x + 10, y - 22, j, 'alpha')
                if j == 0:
                    self.board.title(x - 25, y + 5, i, 'number')
                x += cell_size
            y += cell_size


if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption('BattleShip')
    size = width, height = 800, 600
    screen = pygame.display.set_mode(size)
    screen.fill((0, 0, 0))
    screen_2 = pygame.display.set_mode(size)
    screen_1 = pygame.display.set_mode(size)
    pygame.display.flip()
    ship = Ship()
    running = True
    game = False
    check = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.fill((0, 0, 0))
        ship.render(screen)
        running = False

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                open('computer_ships_game.txt', 'w').close()
                open('user_ships.txt', 'w').close()
                files = Files()
                files.write('user_ships.txt', [[0] * 10 for _ in range(10)])
                pygame.quit()
                sys.exit(0)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x_mouse, y_mouse = pygame.mouse.get_pos()
                if check:
                    ship.ship(x_mouse, y_mouse)
                    flag = ship.check(x_mouse, y_mouse)
                    if flag:
                        play = Play()
                        play.boards()
                        flag = False
                        check = False
                        game = True
                if game:
                    screen.fill((0, 0, 0))
                    play = Play()
                    if config.move_flag:
                        if play.move_user(x_mouse, y_mouse):
                            config.move_flag = False
                    else:
                        if play.move_computer(x_mouse, y_mouse):
                            config.move_flag = True
                    game = play.move()
