import json
import requests

ipv4_tool = "https://iptools-4.top10vpn.com/ip/"


def get_ip(url: str = ipv4_tool) -> str:
    """
    get_ip needs no parameters given and refers to the online service located at "https://iptools-4.top10vpn.com/ip/"
    to read the dynamic ip address of the machine.

    :param url: ip address of the online ip service
    :return: the ipv4 address as string
    """
    ip_string = requests.get(url=url)
    return json.loads(ip_string.content.decode("utf-8"))["ip"]


if __name__ == "__main__":
    print(get_ip())
