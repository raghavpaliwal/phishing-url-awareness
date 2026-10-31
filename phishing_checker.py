
import re
from urllib.parse import urlparse


def inspect_url(raw_url):
    """Check URL text for phishing warning signs."""

    url = raw_url.strip()
    findings = []

    if not url:
        return ["No URL entered."]

    candidate = url if "://" in url else "http://" + url

    try:
        parsed = urlparse(candidate)
    except ValueError:
        return ["This text is not a valid URL format."]

    host = (parsed.hostname or "").lower()

    if not host:
        return ["Could not identify a hostname."]

    # Check 1: @ symbol
    if "@" in candidate:
        findings.append("@ symbol detected. Inspect carefully.")

    # Check 2: Long URL
    if len(url) > 100:
        findings.append("Unusually long URL (over 100 characters).")

    # Check 3: IP address
    if re.fullmatch(r"(?:\d{1,3}\.){3}\d{1,3}", host):
        findings.append("Uses an IP address instead of a familiar domain.")

    # Check 4: Multiple hostname segments
    labels = [part for part in host.split(".") if part]

    if len(labels) >= 5:
        findings.append("Contains many hostname segments/subdomains.")

    # Check 5: Punycode
    if "xn--" in host:
        findings.append("Contains a punycode-style hostname.")

    # Check 6: HTTP
    if parsed.scheme.lower() == "http":
        findings.append("Uses HTTP instead of HTTPS.")

    if not findings:
        findings.append(
            "No listed warning signs found. This does NOT prove safety."
        )

    return findings


def has_warnings(findings):
    info_messages = (
        "No URL entered",
        "Could not identify",
        "This text is not",
        "No listed warning"
    )

    return not findings[0].startswith(info_messages)


def main():

    print("=" * 45)
    print("     PHISHING URL AWARENESS CHECKER")
    print("=" * 45)

    print("Text-based analysis only.")
    print("This program never opens URLs.")

    while True:

        url = input("\nEnter URL (or q to quit): ")

        if url.strip().lower() in ("q", "quit", "exit"):
            print("Goodbye! Stay alert online.")
            break

        findings = inspect_url(url)

        print("\n-------- ANALYSIS RESULT --------")

        for item in findings:
            print("[!] " + item)

        if has_warnings(findings):
            print("\nREVIEW CAREFULLY!")
            print("Warning signs found:", len(findings))
        else:
            print("\nNo active warning signs detected.")

        print("---------------------------------")


if __name__ == "__main__":
    main()
