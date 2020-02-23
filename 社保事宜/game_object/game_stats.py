class Game_stats():
    """  游戏的统计数据"""
    def __init__(self,setting):
        """剩余命数及游戏是否开始"""
        self.setting = setting
        self.reset_stats()
        self.game_active = False

    def reset_stats(self):
        self.ships_left = self.setting.ships_limit
        
       
