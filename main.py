import os
import sys


if __name__ == '__main__':
    sys.path.append(os.path.dirname(os.path.abspath(__file__)))
    os.system('pytest suite/educa.py --driver Chrome')
