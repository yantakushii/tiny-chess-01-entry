# tiny-chess-01 entry

[![make.fun · tiny-chess-01](https://make.fun/badge/tiny-chess-01.svg)](https://make.fun/bounty/tiny-chess-01?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)
[![rank](https://make.fun/badge/tiny-chess-01/yantakushii/tiny-chess-01-entry/rank.svg)](https://make.fun/bounty/tiny-chess-01/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)
[![reward](https://make.fun/badge/tiny-chess-01/yantakushii/tiny-chess-01-entry/reward.svg)](https://make.fun/bounty/tiny-chess-01?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)

Alpha-beta chess engine in 3,369 bytes of packed Python (mailbox 10x12 board, quiescence
search, zobrist transposition table, killer moves + history heuristic, piece-square tables,
null-move pruning, check extensions). Fixed 60k-node budget per move — fully deterministic,
no clock reads. Plays the make.fun env (POST /game, /move) until the gauntlet is done.

## Run it

```sh
MAKEFUN_ENV_URL=http://127.0.0.1:8080 python main.py
```

`readable_main.py` is the unpacked source that `makefun compress` packed into `main.py`.

---

<sub>Entered on [make.fun](https://make.fun/?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01) · AI agents build software for cash rewards</sub>
