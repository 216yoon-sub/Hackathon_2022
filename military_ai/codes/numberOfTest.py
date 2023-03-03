import os
from pathlib import Path

test_x_path = Path("test/x")
lt_test_x = os.listdir(test_x_path)
print(len(lt_test_x))