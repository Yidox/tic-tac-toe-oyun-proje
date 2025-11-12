from random import randrange  # Rastgele sayı üretmek için kullanılır (bilgisayar hamlesi)

# -------------------------------
# TAHTAYI EKRANA ÇİZME
# -------------------------------
def display_board(board):
    """
    Tahtayı ekranda biçimli şekilde gösterir.
    Board, 3x3'lük bir listedir.
    """
    print("+-------+-------+-------+")
    for row in board:
        print("|       |       |       |")
        print(f"|   {row[0]}   |   {row[1]}   |   {row[2]}   |")
        print("|       |       |       |")
        print("+-------+-------+-------+")


# -------------------------------
# KULLANICIDAN HAMLE ALMA
# -------------------------------
def enter_move(board):
    """
    Kullanıcıdan 1-9 arası geçerli bir kare numarası alır.
    Kare doluysa veya sayı geçersizse tekrar ister.
    """
    while True:
        move = input("Hamleni yap (1-9): ")

        if not move.isdigit():  # Sayı değilse uyar
            print("Geçerli bir sayı gir.")
            continue

        move = int(move)
        if move < 1 or move > 9:  # Aralık kontrolü
            print("1 ile 9 arasında bir sayı gir.")
            continue

        # Seçilen hücreye erişim
        row = (move - 1) // 3
        col = (move - 1) % 3

        # Hücre boş mu kontrolü
        if board[row][col] in ['X', 'O']:
            print("Bu kare dolu, başka bir kare seç.")
            continue

        board[row][col] = 'O'  # Kullanıcı hamlesini tahtaya işle
        break


# -------------------------------
# BOŞ ALANLARI BULMA
# -------------------------------
def make_list_of_free_fields(board):
    """
    Tahtadaki boş karelerin listesini döndürür.
    Her eleman (satır, sütun) şeklinde bir tuple’dır.
    """
    free = []
    for row in range(3):
        for col in range(3):
            if board[row][col] not in ['X', 'O']:
                free.append((row, col))
    return free


# -------------------------------
# KAZANMA DURUMU KONTROLÜ
# -------------------------------
def victory_for(board, sign):
    """
    Verilen işaretin (X veya O) kazanıp kazanmadığını kontrol eder.
    Satırlar, sütunlar ve çaprazlar taranır.
    """
    # Satır kontrolü
    for row in board:
        if all(cell == sign for cell in row):
            return True

    # Sütun kontrolü
    for col in range(3):
        if all(board[row][col] == sign for row in range(3)):
            return True

    # Çapraz kontrolü
    if all(board[i][i] == sign for i in range(3)) or all(board[i][2 - i] == sign for i in range(3)):
        return True

    return False


# -------------------------------
# BİLGİSAYARIN HAMLESİ
# -------------------------------
def draw_move(board):
    """
    Bilgisayar rastgele bir boş kare seçer ve 'X' koyar.
    """
    free = make_list_of_free_fields(board)
    if free:
        row, col = free[randrange(len(free))]
        board[row][col] = 'X'


# -------------------------------
# ANA OYUN AKIŞI
# -------------------------------
board = [
    ['1', '2', '3'],
    ['4', 'X', '6'],  # Bilgisayar her zaman ortadan başlar
    ['7', '8', '9']
]

print("Tic-Tac-Toe Oyunu Başladı! (Sen: O, Bilgisayar: X)\n")
display_board(board)

while True:
    # Kullanıcının hamlesi
    enter_move(board)
    display_board(board)

    # Kullanıcı kazanırsa oyun biter
    if victory_for(board, 'O'):
        print("Tebrikler, kazandın!")
        break

    # Boş kare kalmazsa berabere
    if not make_list_of_free_fields(board):
        print("Oyun berabere!")
        break

    # Bilgisayarın hamlesi
    print("\nBilgisayar hamle yapıyor...\n")
    draw_move(board)
    display_board(board)

    # Bilgisayar kazanırsa oyun biter
    if victory_for(board, 'X'):
        print("Bilgisayar kazandı!")
        break

    # Tekrar berabere kontrolü
    if not make_list_of_free_fields(board):
        print("Oyun berabere!")
        break
