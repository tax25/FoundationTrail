import argparse
import sys

from foundationTrail.operationHandlers.send_help import send_help

def foundationTrail_entrypoint() -> None:
    if len(sys.argv) == 1:
        send_help()
        sys.exit()
    
    _parser = argparse.ArgumentParser(
        prog='FoundationTrail',
        description='A tool for odoo developing',
        epilog='Stay the reading of our swan song and epilogue',
        add_help=False
    )



if __name__ == '__main__':
    foundationTrail_entrypoint()
