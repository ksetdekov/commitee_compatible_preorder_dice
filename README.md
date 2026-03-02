# Dice Tester

CLI utility and analysis notebook for testing fairness of a custom die with faces:

`['oo', 'o', 'xx', 'x', 'x', 'R']`

## Setup

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Initialize database

```bash
python -m dice_tester.cli init-db
```

This creates `dice_rolls.db` in the project root.

## Record real rolls (interactive)

```bash
python -m dice_tester.cli record
```

Enter one result per roll (`oo`, `o`, `xx`, `x`, `R`) and `q` to quit.

## Optional: simulated rolls

```bash
python -m dice_tester.cli simulate --n 50
```

## See counts

```bash
python -m dice_tester.cli summary
```

## Run notebook

```bash
jupyter notebook notebooks/dice_fairness_binomial_test.ipynb
```

The notebook computes binomial tests for each symbol vs expected probability from the die design.
