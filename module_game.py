from random import randint

from superwires import games

games.init(screen_width=600, screen_height=377, fps=50)

wall_image = games.load_image('background_1.jpg', transparent=False)
games.screen.background = wall_image
bin_image = games.load_image('bin_1.png')


class BinSprite(games.Sprite):
    def __init__(self, x, type_name):
        self.type_name = type_name
        super(BinSprite, self).__init__(image=bin_image, x=x, y=300)

    def handle_click(self):
        if len(builder.visible_waste) > 0:
            lowest_waste = builder.visible_waste[0]
            if lowest_waste.type_name == self.type_name:
                builder.visible_waste.remove(lowest_waste)
                games.screen.remove(lowest_waste)

    def update(self):
        overlapping_sprites = self.get_overlapping_sprites()

        for sprite in overlapping_sprites:
            if sprite.type_name != self.type_name:
                games.screen.quite()


class WasteSprite(games.Sprite):
    def __init__(self, image, type_name):
        self.type_name = type_name
        super(WasteSprite, self).__init__(image=image, x=games.screen.width / 2, y=games.screen.height - 417, dx=0, dy=2)


class WasteBuilderSprite(games.Sprite):
    def __init__(self):
        self.in_removal_mode = False
        self.click_was_handled = False
        self.frames_interval = 60
        self.passed_frame = 0
        self.created_waste = 0
        self.visible_waste = []
        super(WasteBuilderSprite, self).__init__(image=bin_image, x=-200, y=-200)


    def update(self):
        if self.passed_frame == 0:
            self.created_waste += 1
            new_waste = random_waste()
            self.visible_waste.append(new_waste)
            games.screen.add(new_waste)

        self.passed_frame += 1

        if self.passed_frame == self.frames_interval:
            self.passed_frame == 0

        if self.created_waste == 20:
            self.frames_interval = 45
        elif self.created_waste == 40:
            self.frames_interval = 30
        elif self.created_waste == 60:
            self.frames_interval = 20

        if games.mouse.is_pressed(0):
            if self.in_removal_mode is False:
                self.in_removal_mode = True
                self.click_was_handled = False

        elif self.click_was_handled:
            self.in_removal_mode = False

        if self.in_removal_mode and self.click_was_handled is False:
            if check_point(games.mouse.x, games.mouse.y, bin_banana):
                bin_banana.handle_click()
            elif check_point(games.mouse.x, games.mouse.y, bin_bottle):
                bin_bottle.handle_click()
            elif check_point(games.mouse.x, games.mouse.y, bin_paper):
                bin_paper.handle_click()

            self.click_was_handled = True


bin_banana = BinSprite(x=100, type_name='banana')
bin_bottle = BinSprite(x=300, type_name='bottle')
bin_paper = BinSprite(x=510, type_name='paper')

builder = WasteBuilderSprite()


def check_point(x, y, sprite):
    return sprite.left <= x <= sprite.right and sprite.top <= y <= sprite.bottom


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
