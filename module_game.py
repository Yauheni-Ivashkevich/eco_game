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
        super(WasteBuilderSprite, self).__init__(image=bin_image, x=x, y=300)


"""Добавляем описание для каждой карзины"""
bin_banana = BinSprite(x=100, type_name='banana')
bin_bottle = BinSprite(x=300, type_name='bottle')
bin_paper = BinSprite(x=510, type_name='paper')

builder = WasteBuilderSprite()


games.screen.add(bin_banana)
games.screen.add(bin_bottle)
games.screen.add(bin_paper)
games.screen.add(builder)

games.screen.mainloop()
