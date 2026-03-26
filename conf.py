project = "NearAI Agent Hosting Infra"
copyright = "2026, NEAR AI"
author = "NEAR AI"

extensions = [
    "sphinx_wagtail_theme",
    "sphinx_copybutton",
]

templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

html_theme = "sphinx_wagtail_theme"
html_theme_options = {
    "project_name": "NearAI Agent Hosting Infra API",
    "logo": "",
    "logo_alt": "NearAI Agent Hosting Infra",
    "logo_url": "/",
    "logo_height": 50,
    "logo_width": 50,
    "github_url": "https://github.com/nearai/ai-infra-agent-hosting",
    "footer_links": ",".join([
        "NEAR AI|https://near.ai",
        "GitHub|https://github.com/nearai/ai-infra-agent-hosting",
    ]),
}
html_static_path = ["_static"]
html_css_files = ["custom.css"]

pygments_style = "friendly"
