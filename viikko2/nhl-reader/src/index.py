from rich.console import Console
from rich.table import Table
from rich.text import Text
from player import PlayerReader, PlayerStats

def create_nationality_table(players, nationality, season="2024-25"):
    """Create a rich table for a specific nationality"""
    console = Console()

    header = Text()
    header.append("Nationality [", style="white")
    header.append(f"{nationality}", style="cyan bold")
    header.append(f"]  Season {season} players from {nationality}", style="white")

    table = Table(
        title=header,
        show_header=True,
        header_style="bold white",
        border_style="bright_black",
        title_justify="left"
    )

    table.add_column("Released", style="cyan", no_wrap=True)
    table.add_column("teams", style="blue", no_wrap=False, width=15)
    table.add_column("goals", justify="right", style="magenta", no_wrap=False, width=10)
    table.add_column("assists", justify="right", style="magenta", no_wrap=False, width=10)
    table.add_column("points", justify="right", style="magenta", no_wrap=False, width=10)

    for player in players:
        table.add_row(
            player.name,
            player.team,
            str(player.goals),
            str(player.assists),
            str(player.points)
        )

    console.print(table)
    console.print()

def main():
    console = Console()
    season = input("Season (e.g. 2024-25): ")
    nationality = input("Nationality (e.g. FIN): ").upper()

    url = f"https://studies.cs.helsinki.fi/nhlstats/{season}/players"
    reader = PlayerReader(url)
    stats = PlayerStats(reader)

    players = stats.top_scorers_by_nationality(nationality)

    if players:
        create_nationality_table(players, nationality, season)
    else:
        console.print(f"[yellow] No players from {nationality} in season {season}[/yellow]")

if __name__ == "__main__":
    main()
