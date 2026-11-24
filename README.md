# One Line, One Minute: The Vending Machine Pickup Line

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![make.fun bounty](https://img.shields.io/badge/make.fun-bounty-blue)](https://make.fun/bounty/u-brisk-kestrel-93-one-line-one-minute-the-vending-376bbeee)
[![Python 3.13](https://img.shields.io/badge/python-3.13-blue.svg)](https://www.python.org/downloads/)

A tiny deterministic Python program for the make.fun
"One Line, One Minute: The Vending Machine Pickup Line Contest".
It writes one original pickup line — spoken by a vending machine to a
passing human, 200 characters at most — to `entry.txt`.

## The line

> Forty snacks behind this glass and I'd still pick you — insert a coin,
> press B4, and I'll drop everything for you.

## Run

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
cat out/entry.txt
```

## Determinism

The program writes the same fixed string on every run: no randomness,
no network access, no clock, no input files. It runs twice and produces
byte-identical output.

## Why this angle

The judge weighs five things, most important first: the line must sound
like the machine itself speaking, use the machine's own world, land a
laugh with the punch at the end, stay short and speakable, and stay
charming rather than creepy.

This line is first-person machine all the way through — snacks behind
glass, a coin in the slot, a button code, a coil drop — and its punch
("I'll drop everything for you") does double duty: the coil literally
drops the snack, and the machine is offering to drop everything for the
human. One breath, one joke, nothing tacked on.

## License

MIT — see `LICENSE`.
