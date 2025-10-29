import argparse

def main():
    parser = argparse.ArgumentParser(
        prog = "seqly",
        add_help=False
    )
    parser.add_argument(
        "command",
        nargs="?",
        default=None
    )
    args=parser.parse_args()
    
    if args.command is None:
        print("Command required, type 'seqly help' to see tutorial")
    elif args.command in ("analyze", "an"):
        print("coming soon analyze")
    elif args.command in ("align", "al"):
        print("coming soon align")
    elif args.command in ("blast", "bl"):
        print("coming soon blast")
    elif args.command in ("pairwise", "pw"):
        print("coming soon pair")
    elif args.command in ("transcript", "tc"):
        print("coming soon transcript")
    elif args.command in ("translate", "tl"):
        print("coming soon translate")
    elif args.command in ("help, h"):
        print("for helper")
    else :
        print("Unknown command, type 'seqly help' to see available commands")
        return
    
if __name__ == "__main__":
    main()
