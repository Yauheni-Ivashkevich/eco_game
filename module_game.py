from random import randint

from superwires import games

games.init(screen_width=604, screen_height=377, fps=50)
"""background"""
wall_image = games.load_image('background_1.jpg', transparent=False)
games.screen.background = wall_image

"""Картинка корзины, кот. предполоительно может быть разной"""
bin_image = games.load_image('bin_1.png')

"""super возвращает временный объект супер класса, кот. позволяет вызвать метод суперкласса, 
вызов ранее созданных методов с помощью super, избавляет вас от необходимости переписывать 
эти методы в вашем подклассе и позволяет заменить какие-то суперклассы с минимальными изменениями кода"""
class BinSprite(games.Sprite):
    def __init__(self, x, type_name):
        self.type_name = type_name
        super(BinSprite, self).__init__(image=bin_image, x=-200, y=-200)


"""Описание класса мусора. И если type_name подходит, то мы правильно выбрали карзину, а если нет - конец игры"""
class WasteSprite(games.Sprite):
    def __init__(self, image, type_name):
        self.type_name = type_name
        super(WasteSprite, self).__init__(image=image, x=games.screen.width / 2, y=games.height - 417, dx=0, dy=2)


"""Это логика игры, действие в отношение поступающего мусора"""
class WasteBuilderSprite(games.Sprite):
    def __init__(self):
        self.passed_frame = 0
        self.created_waste = 0
        super(WasteBuilderSprite, self).__init__(image=bin_image, x=x, y=300)

"""Отвечает за главные изменения в Builder, проврить сколько прошло фрэймов, 
и сколько за фрэйм создано мусора, сколько было создано нового мусора, и не было ли такого , что наш"""
    def update(self):
        if self.passed_frame == 0:
            self.created_waste += 1
            new_waste = random_waste()



"""Добавляем описание для каждой карзины"""
bin_banana = BinSprite(x=100, type_name='banana')
bin_bottle = BinSprite(x=300, type_name='bottle')
bin_paper = BinSprite(x=510, type_name='paper')

builder = WasteBuilderSprite()

def random_waste():
    value = randint(1, 3)

    if value == 1:
        return banana_waste()
    elif value == 2:
        return bottle_waste()
    else:
        return paper_waste()


def banana_waste():
    return WasteSprite(image=games.load_image('banana_2.png'), type_name='banana')

def bottle_waste():
    return WasteSprite(image=games.load_image('bottle_2.png'), type_name='bottle')

def paper_waste():
    return WasteSprite(image=games.load_image('text-document_2.png'), type_name='paper')


games.screen.add(bin_banana)
games.screen.add(bin_bottle)
games.screen.add(bin_paper)
games.screen.add(builder)

games.screen.mainloop()
