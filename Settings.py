"""Basic Setting class when pygame base surface is called."""
class Settings:
    """A class to store all settiong for Alien Invastion."""
    def __init__(self):
        """initalize the game's setting."""
        # Screen settings
        self.screen_width = 1500
        self.screen_height = 700
        self.bg_color = (230, 230, 230)

        # Ship Settings
        self.ship_speed = 1.5

        # Bullet settings
        self.bullet_speed = 1.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3

        # Alien settings
        self.alien_speed = 1.0
        self.fleet_drop_speed = 10
        # fleet_direction of 1 represent right; -1 represent left.
        self.fleet_direction = 1
