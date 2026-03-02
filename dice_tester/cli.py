"""CLI for recording and inspecting custom dice rolls."""

from __future__ import annotations

import argparse
import random
from pathlib import Path

from .config import FACES, VALID_RESULTS
from .db import fetch_counts, init_db, insert_roll


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Dice roll recorder")
    parser.add_argument(
        "--db-path",
        type=Path,
        default=Path("dice_rolls.db"),
        help="Path to SQLite database (default: dice_rolls.db)",
    )

    subparsers = parser.add_subparsers(dest="command", required=True)

    subparsers.add_parser("init-db", help="Initialize SQLite database schema")
    subparsers.add_parser("record", help="Record rolls interactively")
    subparsers.add_parser("summary", help="Show result counts")

    sim = subparsers.add_parser("simulate", help="Simulate and save random rolls")
    sim.add_argument("--n", type=int, default=1, help="Number of rolls to simulate")

    return parser


def cmd_record(db_path: Path) -> None:
    print("Enter roll results one by one. Type 'q' to quit.")
    print(f"Valid symbols: {', '.join(VALID_RESULTS)}")

    while True:
        value = input("Result: ").strip()
        if value.lower() in {"q", "quit", "exit"}:
            print("Stopped.")
            return
        if value not in VALID_RESULTS:
            print("Invalid result. Try again.")
            continue
        insert_roll(value, db_path=db_path)
        print(f"Saved: {value}")


def cmd_simulate(db_path: Path, n: int) -> None:
    if n <= 0:
        raise SystemExit("--n must be a positive integer")
    for _ in range(n):
        result = random.choice(FACES)
        insert_roll(result, db_path=db_path)
    print(f"Simulated and saved {n} rolls.")


def cmd_summary(db_path: Path) -> None:
    rows = fetch_counts(db_path=db_path)
    if not rows:
        print("No rolls recorded.")
        return
    total = sum(count for _, count in rows)
    print(f"Total rolls: {total}")
    for symbol, count in rows:
        pct = count / total * 100
        print(f"{symbol:>2}: {count:>5} ({pct:6.2f}%)")


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()

    if args.command == "init-db":
        init_db(db_path=args.db_path)
        print(f"Initialized database at: {args.db_path}")
    elif args.command == "record":
        init_db(db_path=args.db_path)
        cmd_record(db_path=args.db_path)
    elif args.command == "simulate":
        init_db(db_path=args.db_path)
        cmd_simulate(db_path=args.db_path, n=args.n)
    elif args.command == "summary":
        init_db(db_path=args.db_path)
        cmd_summary(db_path=args.db_path)


if __name__ == "__main__":
    main()

