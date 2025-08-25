"""Template for creating your own AI plugin.
"""
from pathlib import Path
from threading import Event
from queue import Queue

import pluggy

from config.config import PluginConfig, get_env
from plugins.ai_pico_plugin import AIPicoPlugin, PicoAI, PicoEvents

hookimpl = pluggy.HookimplMarker("pixel_art") # plugin annotation

class TemplateAIPlugins(AIPicoPlugin):
    """Template AI plugin class."""
    PLUGIN_BASE_PATH = Path(__file__).parent
    PLUGIN_CONFIG_PATH = PLUGIN_BASE_PATH / "plugin.toml"
    PLUGIN_ASSETS_PATH = PLUGIN_BASE_PATH / "assets"
    
    def __init__(self, rgb_start_event: Event, ai_end_event: Event, ai_result_queue: Queue, terminate_thread: Event):
        super().__init__(rgb_start_event, ai_end_event, ai_result_queue, terminate_thread)
        self.config = PluginConfig(self.PLUGIN_CONFIG_PATH)
        self.debug = self.config.get_item("debug", False)
        # TODO: parse any additional properties from `plugin.toml`

    @hookimpl(specname="ai_hook") # marks method as an AI plugin
    @PicoEvents()
    def example(self):
        """Template AI plugin.\n
        TODO: implement this method to your desired AI plugin.
        """
        # TODO: Add your plugin logic here.
        pass
