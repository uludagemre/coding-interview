import sys
from questions import *


def list_args(args):
    return "\n\t- ".join(args)


if __name__ == "__main__":
    module, func = sys.argv[1].split(".")
    args = sys.argv[2 : ]


    print(f"Function:\n\t{module}.{func}")
    print()
    print(f"Args:\n\t- {list_args(args)}")


    ret = getattr(locals()[module], func)(*args)
    
    
    print()
    print(f"Return:\n\t{ret}")