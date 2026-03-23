"""CLI entry point for the project pipeline."""

import click


@click.group()
def main():
    """Project data pipeline CLI."""
    pass


@main.command()
@click.option("--source", default="all", help="Data source to scrape (or 'all')")
def scrape(source):
    """Scrape data from configured sources."""
    click.echo(f"Scraping from: {source}")
    # TODO: Implement scraping logic


@main.command()
def extract():
    """Extract structured data from raw sources."""
    click.echo("Extracting...")
    # TODO: Implement extraction logic


@main.command()
def normalize():
    """Normalize and cross-link entities across sources."""
    click.echo("Normalizing...")
    # TODO: Implement normalization logic


@main.command()
def validate():
    """Validate records and compute quality scores."""
    click.echo("Validating...")
    # TODO: Implement validation logic


@main.command()
@click.option("--format", "fmt", default="csv", type=click.Choice(["csv", "json", "excel", "markdown"]))
def export(fmt):
    """Export data in the specified format."""
    click.echo(f"Exporting as: {fmt}")
    # TODO: Implement export logic


@main.command()
def dashboard():
    """Launch the Streamlit dashboard."""
    import subprocess
    subprocess.run(["streamlit", "run", "src/dashboard/app.py"])


@main.command()
@click.option("--source", default="all", help="Data source to process (or 'all')")
def pipeline(source):
    """Run the full pipeline: scrape -> extract -> normalize -> validate -> store."""
    click.echo(f"Running full pipeline for: {source}")
    # TODO: Wire up the full pipeline


if __name__ == "__main__":
    main()
