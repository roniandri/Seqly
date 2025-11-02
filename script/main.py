import argparse
from .analyze import analyze
from .utils import help
from .transform import transform
from .pairwise import pairwise

def main():
    parser = argparse.ArgumentParser(prog = "seqly", add_help=False)
    parser.add_argument("command", nargs="?")
    parser.add_argument("-s", "--sequence", action="store_true")
    parser.add_argument("-f", "--file", action="store_true")
    args, unknown = parser.parse_known_args()
    
    if unknown:
        print("Invalid Input, please just type 'seqly help' to see tutorial")
        return
    
    valid_commands = ["analyze", "an",
                      "pairwise", "pw",
                      "transcribe", "tc",
                      "translate", "tl",
                      "help"]
    if args.command not in valid_commands:
        print("Invalid Input, please type 'seqly help' to see tutorial")
        return

    mode = None
    if args.sequence:
        mode = 0
    elif args.file:
        mode = 1

    if args.command in ("analyze", "an"):
        if mode is None:
            print("Invalid Input, please type 'seqly' to see tutorial")
            return
        analyze(mode)
    elif args.command in ("pairwise", "pw"):
        if mode is None:
            print("Invalid Input, please type 'seqly' to see tutorial")
            return
        pairwise(mode)
    elif args.command in ("transcribe", "tc"):
        if mode is None:
            print("Invalid Input, please type 'seqly' to see tutorial")
            return
        transform(mode, 0)
    elif args.command in ("translate", "tl"):
        if mode is None:
            print("Invalid Input, please type 'seqly' to see tutorial")
            return
        transform(mode, 1)
    else:
        help()
        return