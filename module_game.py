from superwires import games

games.init(screen_width=604, screen_height=377, fps=50)
"""background"""
wall_image = games.load_image('background_1.jpg', transparent=False)
games.screen.background = wall_image

bin_image = games.load_image('bin_1.png')


class BinSprite(games.Sprite):
    def __init__(self, x, type_name):
        self.type_name = type_name
        super(BinSprite, self).__init__(image=bin_image, x=x, y=300)

"""super возвращает временный объект супер класса, кот. позволяет вызвать метод суперкласса, 
вызов ранее созданных методов с помощью super, избавляет вас от необходимости переписывать 
эти методы в вашем подклассе и позволяет заменить какие-то суперклассы с минимальными изменениями кода"""

"""Добавляем описание для каждой карзины"""
bin_organic = BinSprite(x=100, type_name='organic')
bin_bottle = BinSprite(x=300, type_name='bottle')
bin_paper = BinSprite(x=510, type_name='paper')
