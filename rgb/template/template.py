"""Template for creating your own RGB plugin.
"""
from pathlib import Path
from threading import Event
from queue import Queue

import pluggy

from config.config import PluginConfig
from plugins.rgb_plugin import RGBPlugin, RGBEvents

hookimpl = pluggy.HookimplMarker("pixel_art") # plugin annotation

class TemplateRGBPlugins(RGBPlugin):
    """Template RGB plugin class."""
    PLUGIN_BASE_PATH = Path(__file__).parent
    PLUGIN_CONFIG_PATH = PLUGIN_BASE_PATH / "plugin.toml"
    PLUGIN_ASSETS_PATH = PLUGIN_BASE_PATH / "assets"

    def __init__(self, matrix, rgb_start_event: Event, ai_end_event: Event, ai_result_queue: Queue):
        super().__init__(matrix, rgb_start_event, ai_end_event, ai_result_queue)
        self.config = PluginConfig(self.PLUGIN_CONFIG_PATH)
        self.save_gif = self.config.get_item("save_gif", False)
        # TODO: parse any additional properties from `plugin.toml`

    @hookimpl(specname="rgb_hook") # marks method as a RGB plugin
    @RGBEvents()
    def example(self):
        """Template RGB plugin.\n
        TODO: implement this method to your desired RGB plugin.
        """
        # run until paired AI plugin(s) complete
        while not self.ai_end_event.is_set():
            # TODO: Add your plugin logic here.
            pass
