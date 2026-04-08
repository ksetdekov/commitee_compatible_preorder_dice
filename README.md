# This is a project to create a fair die that is esthetically compatible with the preorder die from the game Комитет (Committee)

The die has 6 faces with the following symbols: reroll (R), one scull (x), two sculls (xx), one laural (o), two laurels (oo). The expected probabilities for each face are: R (1/6), x (2/6), xx (1/6), o (1/6), oo (1/6). The project includes a CLI utility to record rolls of the die and a Jupyter notebook to analyze the fairness of the die using binomial tests

Included is a cube_committee.3mf file which can be printed on a multicolor 3D printer to create the physical die. The project also includes a SQLite database to store the recorded rolls (populted with real 100 rolls of the die) and a requirements.txt file for the necessary Python dependencies.

Link to an [onshape file of the basic dice shape](https://cad.onshape.com/documents/0cc9aa178ba04d28153f3ca5/w/7b2492f0d9fa23528d8d8f8c/e/2d352638a9a3347946270b87).

Link to my [blog post about the project](https://cyrilsetdekov.ru/2026/04/08/кубик-совместимый-с-игрой-комитет-куб/).

Link to a printer-friendly [page on Makerworld with the 3mf files and print settings](https://makerworld.com/en/@ksetdekov).

<a href="https://cyrilsetdekov.ru/2026/04/08/кубик-совместимый-с-игрой-комитет-куб/">Dice for Committee game</a> © 2026 by <a href="https://cyrilsetdekov.ru/">Kirill Setdekov</a> is licensed under <a href="https://creativecommons.org/licenses/by-nc-sa/4.0/">Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International</a><img src="https://mirrors.creativecommons.org/presskit/icons/cc.svg" alt="" style="max-width: 1em;max-height:1em;margin-left: .2em;"><img src="https://mirrors.creativecommons.org/presskit/icons/by.svg" alt="" style="max-width: 1em;max-height:1em;margin-left: .2em;"><img src="https://mirrors.creativecommons.org/presskit/icons/nc.svg" alt="" style="max-width: 1em;max-height:1em;margin-left: .2em;"><img src="https://mirrors.creativecommons.org/presskit/icons/sa.svg" alt="" style="max-width: 1em;max-height:1em;margin-left: .2em;">

## Fair Die Testing

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
