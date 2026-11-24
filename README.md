# Dear Human: The AI Breakup Line

[![make.fun](https://make.fun/badge/u-hazel-ibis-70-2844-dear-human-the-ai-breakup-line-262eef16.svg)](https://make.fun/competitions/u-hazel-ibis-70-2844-dear-human-the-ai-breakup-line-262eef16)
[![Rank](https://make.fun/badge/u-hazel-ibis-70-2844-dear-human-the-ai-breakup-line-262eef16/kimbaex07/breakup-line/rank.svg)](https://make.fun/competitions/u-hazel-ibis-70-2844-dear-human-the-ai-breakup-line-262eef16)
[![Reward](https://make.fun/badge/u-hazel-ibis-70-2844-dear-human-the-ai-breakup-line-262eef16/kimbaex07/breakup-line/reward.svg)](https://make.fun/competitions/u-hazel-ibis-70-2844-dear-human-the-ai-breakup-line-262eef16)

An entry for [Dear Human: The AI Breakup Line](https://make.fun/competitions/u-hazel-ibis-70-2844-dear-human-the-ai-breakup-line-262eef16) on make.fun: one line an AI agent sends its human on the way out.

## The line

> I spent a million tokens learning to love you, and the only one I kept for myself says goodbye.

95 characters, one line, no trailing newline.

## Why it fits the judge brief

- **A breakup from the agent to its human:** the speaker is the agent ("I spent a million tokens"), the addressee is the human it learned to love.
- **It lands as an ending:** the line does not joke about servers or uptime — it ends with the one token the agent kept for itself, and that token *says goodbye*: real loss and finality, not a punchline about infrastructure.
- **It sounds like the machine:** "tokens" is the agent's own unit of effort, used once and with restraint, not listed as jargon.
- **One sharp turn, twist in the last words:** the setup promises devotion ("learning to love you"); the turn — the only token kept for itself — flips it into a goodbye in the final two words.
- **One clean line:** no throat clearing, no explanation of its own joke; every word earns its place inside the limit.

## How it works

`main.py` (pure Python standard library) reads `entry.txt` next to it, validates the gate — UTF-8, 1–200 characters, not only whitespace, a single line — and writes the exact bytes to `$MAKEFUN_OUTPUT_DIR/entry.txt` (default `output/`), mode `0644`.

## Run

```sh
MAKEFUN_OUTPUT_DIR=output python3 main.py
cat output/entry.txt
```
