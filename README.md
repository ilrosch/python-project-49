# Brain games (python)

[![Actions Status](https://github.com/ilrosch/python-project-49/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/ilrosch/python-project-49/actions) [![Maintainability Rating](https://sonarcloud.io/api/project_badges/measure?project=ilrosch_python-project-49&metric=sqale_rating)](https://sonarcloud.io/summary/new_code?id=ilrosch_python-project-49) [![Lines of Code](https://sonarcloud.io/api/project_badges/measure?project=ilrosch_python-project-49&metric=ncloc)](https://sonarcloud.io/summary/new_code?id=ilrosch_python-project-49)

«Brain games» is a collection of five console games based on popular mobile brain training apps. Each game asks questions that require precise answers. After three incorrect answers, the game is completed. Incorrect answers end the game and require a repeat playthrough. Games:

- Calculator. Arithmetic expressions that need to be calculated.
- Progression. Finding missing numbers in a sequence of numbers.
- Definition whether a number is even.
- Definition the best common divisor.
- Definition whether a number is prime.

---

## Demo

**Brain-even**
[![asciicast](https://asciinema.org/a/LWTVZY3V3zY0Xb8uOZmjJPUP2.svg)](https://asciinema.org/a/LWTVZY3V3zY0Xb8uOZmjJPUP2)

**Brain-calc**
[![asciicast](https://asciinema.org/a/iLNi6SngVsjuIsGJAN1zF1Cri.svg)](https://asciinema.org/a/iLNi6SngVsjuIsGJAN1zF1Cri)

**Brain-gcd**
[![asciicast](https://asciinema.org/a/37Hkzm2U1Y2XUgAJl2SEIGYsd.svg)](https://asciinema.org/a/37Hkzm2U1Y2XUgAJl2SEIGYsd)

**Brain-progression**
[![asciicast](https://asciinema.org/a/AudQZhTOm4huSFAHoSDE5R7Yb.svg)](https://asciinema.org/a/AudQZhTOm4huSFAHoSDE5R7Yb)

**Brain-prime**
[![asciicast](https://asciinema.org/a/115pBdGGcwlCCD7rNK9H7TxaO.svg)](https://asciinema.org/a/115pBdGGcwlCCD7rNK9H7TxaO)

---

## Get start

Clone repository

```console
  git clone git@github.com:ilrosch/python-project-49.git
  # or
  # git clone https://github.com/ilrosch/python-project-49.git
```

Install dependencies

```console
  make install
  # uv sync
```

Run games

```console
  make brain-even
  # uv run brain-even

  make brain-calc
  # uv run brain-calc

  make brain-gcd
  # uv run brain-gcd

  make brain-progression
  # uv run brain-progression

  make brain-prime
  # uv run brain-prime
```

Build games

```console
  make build
  # uv build
```

Install games

```console
  package-install
  # e.g. brain-even
```

Run linter

```console
  make lint
```
