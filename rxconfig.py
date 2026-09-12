import reflex as rx
from reflex.plugins.sitemap import SitemapPlugin

config = rx.Config(
    app_name="ifs",
    disable_plugins=[SitemapPlugin], #NMT: Disable SitemapPlugin to avoid generating sitemap.xml
    plugins=[rx.plugins.RadixThemesPlugin(theme=rx.theme(accent_color='cyan'))],
)