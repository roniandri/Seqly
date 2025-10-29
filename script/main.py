import argparse
from analyze import analyze
from utils import help

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
                      "blast", "bl",
                      "pairwise", "pw",
                      "transcript", "tc",
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
    elif args.command in ("blast", "bl"):
        print("coming soon blast")
    elif args.command in ("pairwise", "pw"):
        print("coming soon pair")
    elif args.command in ("transcript", "tc"):
        print("coming soon transcript")
    elif args.command in ("translate", "tl"):
        print("coming soon translate")
    else:
        help()
        return

if __name__ == "__main__":
    main()