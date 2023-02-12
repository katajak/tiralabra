# Testausdokumentti

## Yksikkötestaus

### Yksikkötestauksen kattavuusraportti

![kattavuus](./kuvat/kattavuus.png)

Ajankohtaisimman kattavuusraportin näet [codecovista](https://app.codecov.io/gh/katajak/tiralabra).

### Testaus

Ohjelma on testattu automaattisilla yksikkötesteillä ja käsin.

### Testien suoritus

Yksikkötestit voidaan suorittaa komennolla:

```bash
poetry run invoke test
```

## Suorituskykytestaus

### Testaus

Suorituskykytestaus toteutettiin performance.py tiedostolla, jossa lasketaan avainten generointiin kuluvan ajan keskiarvo jokaisella ohjelman tarjoamalla avainkoolla. Kaikissa testeissä keskiarvo laskettiin ottamalla keskiarvo 20:stä suorituskerrasta.

### Tulokset

- 1024 bit: 0.08865889310836791 sekuntia
- 2048 bit: 0.8492814064025879 sekuntia
- 4096 bit: 10.42284803390503 sekuntia

### Testien suoritus

Suorituskykytestit voidaan suorittaa komennolla:

```bash
poetry run invoke performance-test
```
