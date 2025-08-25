"""Template for creating your own game plugin.
"""
from pathlib import Path
from threading import Event
from queue import Queue

import pluggy

from config.config import PluginConfig
from plugins.game_plugin import pygame, GamePlugin, AIGame

hookimpl = pluggy.HookimplMarker("pixel_art") # plugin annotation

class TemplateGame(GamePlugin):
    """Template game plugin class."""
    PLUGIN_BASE_PATH = Path(__file__).parent
    PLUGIN_CONFIG_PATH = PLUGIN_BASE_PATH / "plugin.toml"
    PLUGIN_ASSETS_PATH = PLUGIN_BASE_PATH / "assets"

    def __init__(self, rgb_start_event: Event, ai_end_event: Event, ai_result_queue: Queue, terminate_thread: Event):
        super().__init__(rgb_start_event, ai_end_event, ai_result_queue, terminate_thread)
        self.config = PluginConfig(self.PLUGIN_CONFIG_PATH)
        self.runtime = self.config.get_item("runtime", 15)
        # TODO: parse any additional properties from `plugin.toml`
    
    @hookimpl(specname="game_hook") # marks method as a game plugin
    @AIGame()
    def play(self):
        """Template game plugin.\n
        TODO: refactor this method to your desired game plugin.
        """
        # run game for `runtime` seconds
        FPS = 30
        for _ in range(FPS * self.runtime):
            """TODO: Add your game logic here and draw the next pygame screen.
            """
            # At the end of the game loop, send the pygame screen (gameplay frame) to the paired RGB plugin
            self.draw() # replaces flip()
            self.clock.tick(FPS)
