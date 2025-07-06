class Player:
    def __init__(self, name, sign='X'):
        self.name = name
        self.sign = sign

    def choose(self):
        self.choice = input(f"{self.name}, введите номер строки, а затем номер колонки через пробел:\n").lower()
        return self.choice

class Game:
    def __init__(self, player1, player2, n =3):
        if player1.sign == player2.sign:
            # Если оба выбрали 'X', то второму назначим 'O'
            player2.sign = 'O' if player1.sign.upper() == 'X' else 'X'
            print(f"Игроку '{player2.name}' автоматически назначен знак '{player2.sign}'")
        self.player1 = player1
        self.player2 = player2
        self.n = n
        self.field = [['_']*n for __ in range(n)]

    def get_winner(self, player):
        if self.check_row(player) or self.check_column(player) or self.check_diag(player):
            return player
        return None
    
    def add_sign(self, player):
        try:
            i,j = list(map(int, player.choose().split()))
            if not (1 <= i <= self.n and 1 <= j <= self.n):
                print("Координаты вне поля. Попробуйте снова.")
                return self.add_sign(player)
            if self.field[i-1][j-1] != '_':
                print("Клетка занята")
                return self.add_sign(player)
            self.field[i-1][j-1]=player.sign #отнимаем, чтобы были индексы
        except ValueError:
            print("Неверный формат ввода. Введите два числа через пробел.")
            return self.add_sign(player)

    def play(self):
        total_step = 0

        while total_step <self.n *self.n:
            self.add_sign(self.player1)
            self.display_field()
            winner = self.get_winner(self.player1)
            if winner:
                break
            total_step+=1
            if total_step == self.n * self.n:
                print("У нас ничья.")
                return None
            self.add_sign(self.player2)
            self.display_field()
            winner = self.get_winner(self.player2)
            if winner:
                break
            total_step+=1

        if total_step ==self.n *self.n:
            print("У нас ничья.")

    def check_row(self, player: Player):
        for row in self.field:
            if all([cell == player.sign for cell in row]):
                return player.name
        return None
    
    def check_column(self, player: Player):
        for col in range(self.n):
            if all(self.field[row][col] == player.sign for row in range(self.n)):
                return player.name
        return None

    def check_diag(self, player: Player):
        if all(self.field[row][col] == player.sign for row in range(self.n) for col in range(self.n) if row == col):
                return player.name
        if all(self.field[row][col] == player.sign for row in range(self.n) for col in range(self.n) if row == self.n-1-col):
                return player.name
        return None
    
    # def check_diag(self, player: Player):
    # if all(self.field[i][i] == player.sign for i in range(self.n)):
    #     return player.name
    # if all(self.field[i][self.n - 1 - i] == player.sign for i in range(self.n)):
    #     return player.name
    # return None

    def display_field(self):
        for row in self.field:
            lst =[ str(i) for i in row]
            print(' '.join(lst))

# Пример использования
player1 = Player("Игрок 1")
player2 = Player("Игрок 2")
game = Game(player1, player2)

game.play()