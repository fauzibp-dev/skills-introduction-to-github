#!/usr/bin/env python3
"""Offline exact-host scope reminder. Does not send network traffic.

This helper is NOT authorization: always verify the live Bugcrowd policy.
"""
import argparse
import ipaddress
from pathlib import Path
from urllib.parse import urlsplit


def valid_dns_hostname(host: str) -> bool:
    if not isinstance(host, str) or not host or len(host) > 253:
        return False
    if host != host.strip() or host.startswith(".") or host.endswith("."):
        return False
    labels = host.split(".")
    if len(labels) < 2:
        return False
    return all(
        1 <= len(label) <= 63
        and label[0].isalnum()
        and label[-1].isalnum()
        and all(char.isascii() and (char.isalnum() or char == "-") for char in label)
        for label in labels
    )


def get_hostname(url: str) -> str | None:
    """Parse strict HTTPS URL without networking."""
    if not isinstance(url, str) or not url or url != url.strip():
        return None
    try:
        parsed = urlsplit(url)
        if parsed.scheme != "https" or not parsed.netloc:
            return None
        if parsed.username is not None or parsed.password is not None or parsed.fragment:
            return None
        if parsed.port not in (None, 443):
            return None
        host = parsed.hostname
        if not host:
            return None
        ascii_host = host.encode("idna").decode("ascii").lower()
        if not valid_dns_hostname(ascii_host):
            return None
        try:
            ipaddress.ip_address(ascii_host)
            return None
        except ValueError:
            return ascii_host
    except (ValueError, UnicodeError):
        return None


def load_exact_hosts(file_path: Path) -> set[str]:
    """Read explicitly verified hosts; no wildcards, URLs, or implicit suffixes."""
    hosts: set[str] = set()
    for raw in file_path.read_text(encoding="utf-8").splitlines():
        entry = raw.strip().lower()
        if not entry or entry.startswith("#"):
            continue
        if not valid_dns_hostname(entry):
            raise ValueError("Invalid scope entry: exact DNS hostnames only (no wildcards)")
        hosts.add(entry)
    return hosts


def is_allowed(url: str, hosts: set[str]) -> bool:
    host = get_hostname(url)
    return host is not None and host in hosts


def main() -> int:
    parser = argparse.ArgumentParser(description="OFFLINE exact-host scope reminder, not a scan")
    parser.add_argument("url", help="HTTPS URL to check locally (no request is sent)")
    parser.add_argument("--scope", type=Path, default=Path(__file__).resolve().parent.parent / "scope.txt")
    args = parser.parse_args()
    try:
        allowed = is_allowed(args.url, load_exact_hosts(args.scope))
    except (OSError, ValueError) as error:
        print(f"DENIED: Scope file invalid/unavailable ({error})")
        return 2
    print("LISTED (verify live policy before testing)" if allowed else "DENIED: not an exact listed HTTPS host")
    return 0 if allowed else 1


if __name__ == "__main__":
    raise SystemExit(main())
