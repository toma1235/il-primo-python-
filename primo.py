meme_dict = {
            "saЖ": "Что-то очень странное или стыдное",
            "КРИНЖ": "Что-то очень странное или стыдное",
            "ЛОЛ": "Что-то очень смешное",
            "РОФЛ":  "шутка",
            "ЩИЩ":  "одобрение или восторг",
            "КРИПОВЫЙ":  "страшный, пугающий",
            "АГРИТЬСЯ":  "злиться",
            }
for i in range(3):
    word = input("Введите непонятное слово (большими буквами!): ")
    if word in meme_dict.keys():
        print(meme_dict[word])
    else:
        print("Error")
