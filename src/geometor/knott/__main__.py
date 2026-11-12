"""Command-line entry point for inspecting and verifying ``geometor.knott``."""

from __future__ import annotations

import argparse
from collections.abc import Sequence

from rich.console import Console
from rich.table import Table

from geometor.knott.catalog import CATALOG_ITEMS, COLLECTIONS, verify_all_catalog_items


def build_parser() -> argparse.ArgumentParser:
    """Create the CLI argument parser for ``knott``.

    Returns:
        Configured :class:`argparse.ArgumentParser`.
    """
    parser = argparse.ArgumentParser(
        prog="knott",
        description="GEOMETOR Mathematical Catalog of Dr. Ron Knott's Golden Ratio Archive.",
    )
    sub = parser.add_subparsers(dest="command")
    sub.add_parser("list", help="List all 6 collections and 22 cataloged items.")
    sub.add_parser("verify", help="Run exact SymPy + geometor.model verification on all 22 items.")
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    """Execute the ``knott`` CLI.

    Args:
        argv: Optional sequence of CLI arguments.

    Returns:
        Process exit status (``0`` on success).
    """
    parser = build_parser()
    args = parser.parse_args(list(argv) if argv is not None else None)
    console = Console()

    if args.command == "verify":
        results = verify_all_catalog_items()
        table = Table(title="GEOMETOR Knott — Symbolic Verification Summary")
        table.add_column("ID", style="bold yellow")
        table.add_column("Title")
        table.add_column("Elements", justify="right")
        table.add_column("Invariants", justify="right")
        for item in CATALOG_ITEMS:
            res = results[item.canonical_id]
            table.add_row(
                item.canonical_id,
                item.title,
                str(len(res.model)),
                str(len(res.invariants)),
            )
        console.print(table)
        console.print(f"[bold green]Verified all {len(results)} catalog items with 0 sp.Float atoms.[/bold green]")
        return 0

    table = Table(title=f"GEOMETOR Knott Catalog ({len(COLLECTIONS)} Collections, {len(CATALOG_ITEMS)} Items)")
    table.add_column("ID", style="bold yellow")
    table.add_column("Collection", style="cyan")
    table.add_column("Title")
    table.add_column("Source Anchor", style="dim")
    for item in CATALOG_ITEMS:
        table.add_row(
            item.canonical_id,
            item.collection_slug,
            item.title,
            f"{item.knott_url.rsplit('/', 1)[-1]}",
        )
    console.print(table)
    return 0


if __name__ == "__main__":  # pragma: no cover
    raise SystemExit(main())
