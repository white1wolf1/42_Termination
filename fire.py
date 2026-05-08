import os
import random
import time

WIDTH = os.get_terminal_size().columns
HEIGHT = 45

# 🔥 ateş renkleri
palette = [
    " ",
    "\033[31m.\033[0m",
    "\033[31m:\033[0m",
    "\033[31m*\033[0m",
    "\033[33m+\033[0m",
    "\033[33mO\033[0m",
]

# 🪵 koyu yanmış odun
WOOD = "\033[38;5;52mX\033[0m"

fire = [[0 for _ in range(WIDTH)] for _ in range(HEIGHT)]

# 🔥 en alt odun
for x in range(WIDTH):
    fire[HEIGHT - 1][x] = -1

def update():
    for y in range(HEIGHT - 2, -1, -1):
        for x in range(WIDTH):

            below = fire[y + 1][x]

            # 🔥 odun üstü ateş başlatır
            if below == -1:
                fire[y][x] = len(palette) - 1

            elif below == 0:
                fire[y][x] = 0

            else:
                decay = random.randint(0, 2)

                nx = x + random.randint(-1, 1)

                if nx < 0:
                    nx = 0

                if nx >= WIDTH:
                    nx = WIDTH - 1

                fire[y][nx] = max(0, below - decay)

print("\033[2J")

try:

    while True:

        update()

        print("\033[H", end="")

        for y in range(HEIGHT):

            row = ""

            for x in range(WIDTH):

                if y == HEIGHT - 1:
                    row += WOOD
                else:
                    v = fire[y][x]
                    row += palette[v] if v > 0 else " "

            print(row)

        # 🔥 daha yavaş ve sakin animasyon
        time.sleep(0.07)

except KeyboardInterrupt:

    print("\n🔥 Ateş efekti durduruldu.")