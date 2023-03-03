import os
from pathlib import Path

test_x_path = Path("test/x")

lt_test_x = os.listdir(test_x_path)

f = open('test_imgs.txt', 'w')
f.close()

f = open('test_imgs.txt', 'w')
for name in lt_test_x:
    f.write(name + '\n')
f.close()