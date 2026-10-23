from rich.console import Console
from rich.text import Text

STYLES = {
    "A": "bold cyan",
    "B": "bold magenta",
    "C": "bold green",
    "D": "bold yellow",
}

console = Console()


def scale_bar(value, maximum, width=40):
    """Rechnet einen Wert in eine Balkenlänge (Anzahl Zeichen) um."""
    if maximum <= 0:
        return 0
    return round(value / maximum * width)


def render_bar_chart(values, width=40):
    """Gibt ein horizontales Balkendiagramm aus.

    values: Liste von Tupeln, z. B. [("A", 2.16), ("B", 4.33), ...]
    """
    if not values:
        console.print("Keine Daten zum Anzeigen.")
        return

    maximum = max(value for _label, value in values)
    label_width = max(len(label) for label, _value in values)

    for label, value in values:
        length = scale_bar(value, maximum, width)
        line = Text(f"{label:<{label_width}} | ")
        line.append("█" * length, style=STYLES.get(label, "bold white"))
        line.append(f" {value:.2f}")
        console.print(line)


if __name__ == "__main__":
    # Feste Beispieldaten zum Testen, solange Person A noch nicht fertig ist
    values = [
        ("A", 2.16),
        ("B", 4.33),
        ("C", 6.57),
        ("D", 8.71),
    ]
    render_bar_chart(values)