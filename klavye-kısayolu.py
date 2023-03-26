import random
import json

#Kodu hazırlayan, Derleyen 
# BY omer_X_kiyak

#Logo Text-to-ASCII-Art-GEnerator(TAGG)
print(r"""
   /$ /$   /$$      /$$ /$$$$$$$$ /$$$$$$$        /$$   /$$ /$$$$$$ /$$     /$$ /$$$$$$  /$$   /$$
  |_/|_/  | $$$    /$$$| $$_____/| $$__  $$      | $$  /$$/|_  $$_/|  $$   /$$//$$__  $$| $$  /$$/
  /$$$$$$ | $$$$  /$$$$| $$      | $$  \ $$      | $$ /$$/   | $$   \  $$ /$$/| $$  \ $$| $$ /$$/ 
 /$$__  $$| $$ $$/$$ $$| $$$$$   | $$$$$$$/      | $$$$$/    | $$    \  $$$$/ | $$$$$$$$| $$$$$/  
| $$  \ $$| $$  $$$| $$| $$__/   | $$__  $$      | $$  $$    | $$     \  $$/  | $$__  $$| $$  $$  
| $$  | $$| $$\  $ | $$| $$      | $$  \ $$      | $$\  $$   | $$      | $$   | $$  | $$| $$\  $$ 
|  $$$$$$/| $$ \/  | $$| $$$$$$$$| $$  | $$      | $$ \  $$ /$$$$$$    | $$   | $$  | $$| $$ \  $$
 \______/ |__/     |__/|________/|__/  |__/      |__/  \__/|______/    |__/   |__/  |__/|__/  \__/
                                                                                                  
                                                                                                  
                                                                                                  
 """)
print("\n***************************************************************** *")
print("\n* Copyright of Ömer KIYAK, 2023                                 * *")
print("\n* https://www.instagram.com/omer_x_kiyak/                       * *")
print("\n*  https://github.com/omer-X-kiyak/                             * *")
print("\n*  https://t.me/omer_X_kiyak/                                   * *")
print("\n***************************************************************** *\n \n")

# Kelimeler ve soruları
with open("1.json", "r", encoding="utf-8") as f:
    words = json.load(f)



# Rastgele bir kelime seçme fonksiyonu
def choose_word(words):
    return random.choice(list(words.keys()))

# Bir kelimeyi tahmin etmek için oyun fonksiyonu
def play_game(word):
    word = word.lower() # kelimeyi küçük harflere dönüştür
    print("\n Kelimenin uzunluğu: ", len(word))
    guess = ""
    guesses = []
    turns = 10
    while turns > 0:
        failed = 0
        for char in word:
            if char in guesses:
                print(char, end=" ")
            else:
                print("_", end=" ")
                failed += 1
        if failed == 0:
            print("\nTebrikler, kelimeyi doğru tahmin ettiniz!")
            return
        guess = input("\nBir harf veya kelime tahmin edin: ").lower() # kullanıcının girdiği harfleri küçük harfe dönüştür
        if len(guess) == len(word):
            if guess == word:
                print("\nTebrikler, kelimeyi doğru tahmin ettiniz!")
                return
            else:
                turns -= 1
                print("Yanlış tahmin! Kalan tahmin hakkınız:", turns)
                if turns == 0:
                    print("Maalesef, kelimeyi tahmin edemediniz. Doğru kelime: " + word)
        else:
            guesses.append(guess)
            if guess in word:
                print("Doğru tahmin!")
            else:
                turns -= 1
                print("Yanlış tahmin! Kalan tahmin hakkınız:", turns)
                if turns == 0:
                    print("Maalesef, kelimeyi tahmin edemediniz. Doğru kelime: " + word)

# Oyunu başlatan fonksiyon
def start_game():
    print("Kelime tahmin oyununa hoş geldiniz!")
    while True:
        word = choose_word(words)
        print("\nİpuçları:\n", words[word])
        play_game(word)
        response = input("Tekrar oynamak istiyor musunuz? (E/H)=(Y/N): ")
        if response.lower() != "e" and response.lower() != "y":

            break
    print("Oyun bitti, teşekkürler!")

# Oyunu başlat
start_game()
