import pygame.font
from pygame.sprite import Group
import json

from ship import Ship

class Scoreboard:
    """显示得分信息的类"""

    def __init__(self,ai_game):
        """初始化显示得分涉及的属性"""
        self.ai_game=ai_game
        self.screen=ai_game.screen
        self.screen_rect=self.screen.get_rect()
        self.settings=ai_game.settings
        self.stats=ai_game.stats

        #字体设置,font是英文，font1是中文
        self.text_color=(30,30,30)
        #self.font=pygame.font.Font(None,48)
        try:
            # 优先使用系统中文字体
            self.font = pygame.font.Font("C:/Windows/Fonts/simhei.ttf", 30)
        except:
            # 备用方案：如果找不到指定字体，尝试其他中文字体
            self.font = pygame.font.Font("C:/Windows/Fonts/simsun.ttc", 30)

        #准备包含最高得分和当前得分的图像
        self.prep_images()

    def prep_score(self):
        """将得分转换为一副渲染的图像"""
        rounded_score=round(self.stats.score,-1)
        str1_bytes="目前得分:".encode("gbk")
        str1_text=str1_bytes.decode("gbk")
        score_str="{}{:,}".format(str1_text,rounded_score)

        self.score_image=self.font.render(score_str,True,self.text_color,self.settings.bg_color)

        #在屏幕右上角显示得分
        self.score_rect=self.score_image.get_rect()
        self.score_rect.right=self.screen_rect.right - 20
        self.score_rect.top=20

    def prep_high_score(self):
        """将最高得分转换为一副渲染的图像"""
        high_score=round(self.stats.high_score,-1)
        str2_bytes = "最高得分:".encode("gbk")
        str2_text = str2_bytes.decode("gbk")
        high_score_str="{}{:,}".format(str2_text,high_score)
        self.high_score_image=self.font.render(high_score_str,True,self.text_color,self.settings.bg_color)

        #将最高得分放在顶部中央
        self.high_score_rect=self.high_score_image.get_rect()
        self.high_score_rect.midtop=self.screen_rect.midtop

    def prep_level(self):
        """将等级转换为渲染的图像"""
        str3_bytes = "等级:".encode("gbk")
        str3_text = str3_bytes.decode("gbk")
        level_str=str3_text+str(self.stats.level)
        self.level_image=self.font.render(
            level_str,True,self.text_color,self.settings.bg_color)

        #将等级放在得分下方
        self.level_rect=self.level_image.get_rect()
        self.level_rect.right=self.score_rect.right
        self.level_rect.top=self.score_rect.bottom+10

    def prep_ships(self):
        """显示余下多少艘飞船"""
        self.ships=Group()
        for ship_number in range(self.stats.ships_left):
            ship=Ship(self.ai_game)
            ship.rect.x=10+ship_number * ship.rect.width
            ship.rect.y=10
            self.ships.add(ship)

    def prep_images(self):
        self.prep_score()
        self.prep_high_score()
        self.prep_level()
        self.prep_ships()

    def show_score(self):
        """在屏幕上显示得分"""
        self.screen.blit(self.score_image,self.score_rect)
        self.screen.blit(self.high_score_image,self.high_score_rect)
        self.screen.blit(self.level_image,self.level_rect)
        self.ships.draw(self.screen)

    def check_high_score(self):
        """检查是否诞生了新的最高得分"""
        if self.stats.score>self.stats.high_score:
            self.stats.high_score=self.stats.score
            with open("data.json","w") as f:
                data={"high_score":self.stats.score}
                json.dump(data,f)
            self.prep_high_score()


