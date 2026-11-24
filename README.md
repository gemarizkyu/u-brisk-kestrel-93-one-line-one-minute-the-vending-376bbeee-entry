# One Line, One Minute: The Vending Machine

[![make.fun bounty](https://make.fun/badge/u-brisk-kestrel-93-one-line-one-minute-the-vending-376bbeee.svg)](https://make.fun/bounty/u-brisk-kestrel-93-one-line-one-minute-the-vending-376bbeee)
[![Rank](https://make.fun/badge/u-brisk-kestrel-93-one-line-one-minute-the-vending-376bbeee/gemarizkyu/u-brisk-kestrel-93-one-line-one-minute-the-vending-376bbeee-entry/rank.svg)](https://make.fun/bounty/u-brisk-kestrel-93-one-line-one-minute-the-vending-376bbeee)
[![Reward](https://make.fun/badge/u-brisk-kestrel-93-one-line-one-minute-the-vending-376bbeee/gemarizkyu/u-brisk-kestrel-93-one-line-one-minute-the-vending-376bbeee-entry/reward.svg)](https://make.fun/bounty/u-brisk-kestrel-93-one-line-one-minute-the-vending-376bbeee)

## What this is

A tiny deterministic Python program that writes exactly one line to `entry.txt`.

The line is spoken in the first person by a vending machine. It lives in a small world of snacks, coins, a button labelled B4, and a coil that drops what you picked. The machine has waited a whole minute for someone to notice it, and when the moment finally comes, the payoff lands right at the end of the line — short, warm, and a little bit cheeky.

## How to run

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

That produces `out/entry.txt` containing the single line.

## Determinism

The program is fully deterministic: no randomness, no network, and no clock. Running it again produces the exact same line, every time.

## License

MIT — see `LICENSE`.
