""" Module for Class GameStats """
class GameStats:
    """Track statistics for Alien Invasion."""

    def __init__(self, ai_game):
        """
        Initialize statistics.

        Args:
            ai_game (Class): Alien_Invasion Class
        """
        # Start Alien Invasion in an active state.
        self.game_active = True

        self.settings = ai_game.settings
        self.reset_stats()

    def reset_stats(self):
        """Initialize statistics that can change during the game."""
        self.ships_left = self.settings.ship_limit