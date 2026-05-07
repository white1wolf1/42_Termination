
import os
import time
import random
import shutil

width, height = shutil.get_terminal_size()

snowflakes = ["*", ".", "❄", "+"]

flakes = [random.randint(0, height) for _ in range(width)]

try:
    while True:
        os.system("clear")

        screen = [" "] * (width * height)

        for i in range(width):
           
            char = random.choice(snowflakes)

            pos = flakes[i] * width + i

            if 0 <= pos < len(screen):
                screen[pos] = char

            flakes[i] += 1

            if flakes[i] >= height:
                flakes[i] = 0

        for y in range(height):
            line = "".join(screen[y * width:(y + 1) * width])
            print(line)

        time.sleep(0.08)

except KeyboardInterrupt:
    os.system("clear")
    print("Kar efekti durduruldu ❄️")