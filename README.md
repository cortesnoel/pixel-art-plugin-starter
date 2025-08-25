# Pixel Art Plugin Starter

This project contains starter files to create your own Pixel Art [RGB](rgb/template), [AI](ai/template), and [game](game/template) plugins using Python.

## Create Your First Plugin

1. Clone this repo into your Pixel Art device.

```bash
git clone https://github.com/cortesnoel/pixel-art-plugin-starter.git
```

2. Rename and copy your new plugin to the Pixel Art plugins folder.

```bash
cd pixel-art-plugin-starter/rgb && cp -r template /opt/pixel-art/plugins/rgb/my_custom_plugins
```

3. Create, source, and install Pixel Art virtualenv if not done already.

```bash
cd /opt/pixel-art && python3 -m venv .venv && source .venv/bin/activate && pip install -r requirements.txt
```

4. Develop and test your custom plugin within the Pixel Art virtualenv.
    - Give unique names to your module, class, and plugin method so they are unlikely to clash with other plugins

5. After your plugin is complete, open a [PR](https://github.com/cortesnoel/pixel-art/pulls) in the Pixel Art repo to either add your plugin or mention it as a "Community Plugin".

    *Note*: Not all plugins will be accepted within the Pixel Art repo. Alternatively, your plugin may be mentioned as a "Community Plugin".

## Plugin Examples

For plugin examples, review Pixel Art's existing [plugins](https://github.com/cortesnoel/pixel-art/tree/main/plugins).

## More Info

For more info on plugin development, including docs and tutorials, visit the [Pixel Art](https://github.com/cortesnoel/pixel-art) repo.

## License

[MIT](LICENSE)

---

> LinkedIn [Noel Cortes](https://www.linkedin.com/in/noel-cortes-00ab8b181/)
&nbsp;&middot;&nbsp;
> Instagram [@noelcortes.libre](https://www.instagram.com/noelcortes.libre/)