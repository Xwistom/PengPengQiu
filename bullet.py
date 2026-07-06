import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """管理飞船所射子弹的类"""

    def __init__(self,ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color
        self.rect=pygame.Rect(0,0,self.settings.bullet_width,self.settings.bullet_height)
        self.rect.midtop=ai_game.ship.rect.midtop

        #存储用小数表述的子弹位置
        self.y=float(self.rect.y)

    def update(self):
        """向上移动子弹"""
        #更新子弹位置的小数值
        self.y-=self.settings.bullet_speed
        #更新表示子弹的rect的位置
        self.rect.y=self.y

    def draw_bullet(self):
        """绘制子弹"""
        pygame.draw.rect(self.screen,self.color,self.rect)


