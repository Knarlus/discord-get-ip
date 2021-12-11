import json
import requests

ipv4_tool = "https://iptools-4.top10vpn.com/ip/"


def get_ip(url: str = ipv4_tool) -> str:
    ip_string = requests.get(url=url)
    return json.loads(ip_string.content.decode("utf-8"))["ip"]
