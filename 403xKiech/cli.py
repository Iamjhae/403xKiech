import argparse
from .scanner import run_scan

def main():

    parser = argparse.ArgumentParser(
        prog="403x",
        description="Pro 403 Bypass Scanner"
    )

    parser.add_argument("-u","--url", required=True)
    parser.add_argument("-t","--threads", default=20, type=int)
    parser.add_argument("-p","--proxy")
    parser.add_argument("-o","--output")
    parser.add_argument("-w","--wordlist")

    args = parser.parse_args()

    run_scan(args)
