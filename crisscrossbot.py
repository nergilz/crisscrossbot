import config
import telebot
import random


bot = telebot.TeleBot(config.token)
global board
board = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']]


def draw_board(board):
    """ рисует игровое поле """
    text = '------------\n'
    for line in board:
        text = text + '|' + line[0] + '|' + line[1] + '|' + line[2] + '|' + '\n'
        text = text + '-------------\n'
    return text


def check_win(board):
    """ проверка выигрышных комбинаций """
    for line in board:
        if line[0] == line[1] == line[2]:
            return True
    if board[0][0] == board[1][1] == board[2][2]:
        return True
    if board[2][0] == board[1][1] == board[0][2]:
        return True
    if board[0][1] == board[1][1] == board[2][1]:
        return True
    if board[0][0] == board[1][0] == board[2][0]:
        return True
    if board[0][2] == board[1][2] == board[2][2]:
        return True
    return False


def get_position_and_move(symbol, player_move):
    """ делаем ход и замена номера клетки на символ """
    valid = False
    while not valid:
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == player_move:
                    board[i][j] = symbol
                    valid = True


@bot.message_handler(commands=['game'])
def get_start(message):
    global board
    board = [['1','2','3'],['4','5','6'],['7','8','9']]
    bot.send_message(message.chat.id, draw_board(board))
    bot.send_message(message.chat.id, 'yuor move (1-9) :')


@bot.message_handler(content_types=["text"])
def get_game(message):
    check_list = ['1','2','3','4','5','6','7','8','9']

    if message.text in check_list:
        symbol='X'
        get_position_and_move(symbol, message.text)
        symbol='0'
        get_position_and_move(symbol, str(random.randint(1, 10)))
    
    _check = check_win(board)

    if _check:
        bot.send_message(message.chat.id, 'STOP GAME, IS WINNER')

    bot.send_message(message.chat.id, draw_board(board))


if __name__ == '__main__':
     bot.polling()
