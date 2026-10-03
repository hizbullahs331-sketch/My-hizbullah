"""
C Daily — नया कलर स्कीम (Navy / Royal Blue / Gold)

Reference: "C Daily Agri Shop" dashboard design.
हर कलर hex में है; Kivy के लिए rgba() helper से (r, g, b, a) 0-1 tuple मिलता है।
"""

PALETTE = {
    # Base
    "navy_900": "#0A2463",    # सबसे गहरा navy – header / dark cards
    "navy_800": "#0D3A8C",    # dark card gradient end
    "blue_600": "#1E6FE8",    # primary bright blue – highlights, bars
    "blue_100": "#E3EDFF",    # soft blue – chips, table borders
    "blue_50":  "#F2F6FD",    # page background
    "white":    "#FFFFFF",    # cards, input fields
    # Accents
    "gold":     "#FFC21A",    # yellow accent – titles on navy, Save button
    "green":    "#2E9E4F",    # positive / recovery
    "red":      "#E5484D",    # destructive (Clear)
    # Text
    "text_dark":  "#0E2A5C",  # text on light surfaces
    "text_muted": "#5B6B8C",  # placeholders, secondary text
    "text_light": "#FFFFFF",  # text on navy / blue
    "text_soft":  "#C9D8F5",  # secondary text on navy
}

# पुराने रंग -> नए रंग (screen element के हिसाब से)
ELEMENTS = {
    "top_bar_bg":          ("navy_900", "navy_800"),  # gradient
    "top_bar_label":       "text_light",
    "input_bg":            "white",
    "input_text":          "text_dark",
    "input_placeholder":   "text_muted",
    "search_btn_bg":       "blue_600",
    "save_btn_bg":         "gold",
    "save_btn_text":       "navy_900",

    "entry_row_bg":        "blue_50",                 # पहले beige था
    "entry_field_border":  "blue_100",

    "page_bg":             "blue_50",
    "card_dark_bg":        ("navy_900", "navy_800"),  # Total Sale, Balance, Best Sale
    "card_dark_title":     "gold",
    "card_dark_value":     "text_light",
    "card_dark_sub":       "text_soft",
    "card_light_bg":       "white",                   # Recovery, Best Recovery
    "card_light_title":    "text_dark",
    "card_light_value":    "green",

    "table_title_bg":      "navy_900",
    "table_title_text":    "gold",
    "table_header_bg":     "blue_600",
    "table_header_text":   "text_light",
    "table_no_col_bg":     "blue_100",
    "table_cell_bg":       "white",
    "table_border":        "blue_100",

    "nav_bar_bg":          "navy_900",
    "nav_btn_active_bg":   "blue_600",                # Main Dashboard
    "nav_btn_text":        "text_light",

    "action_btn_bg":       "white",                   # Search, Export, Import, Detail, icons
    "action_btn_text":     "navy_900",
    "action_btn_primary":  "blue_600",                # Edit
    "action_btn_danger":   "red",                     # Clear
}


def hex_color(name):
    return PALETTE[name]


def rgba(name, alpha=1.0):
    """Kivy-style (r, g, b, a) tuple, values 0-1."""
    h = PALETTE[name].lstrip("#")
    r, g, b = (int(h[i:i + 2], 16) / 255 for i in (0, 2, 4))
    return (r, g, b, alpha)
