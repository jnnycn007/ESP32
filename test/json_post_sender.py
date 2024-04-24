#  /*
#   *   This file is part of DroneBridge: https://github.com/DroneBridge/ESP32
#   *
#   *   Copyright 2024 Wolfgang Christl
#   *
#   *   Licensed under the Apache License, Version 2.0 (the "License");
#   *   you may not use this file except in compliance with the License.
#   *   You may obtain a copy of the License at
#   *
#   *   http://www.apache.org/licenses/LICENSE-2.0
#   *
#   *   Unless required by applicable law or agreed to in writing, software
#   *   distributed under the License is distributed on an "AS IS" BASIS,
#   *   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   *   See the License for the specific language governing permissions and
#   *   limitations under the License.
#   *
#   */

import requests


def add_custom_up():
    url = "http://dronebridge.local/api/settings/addudp"
    data = {
        "ip": "192.168.10.53",
        "port": 456
    }
    # Send the POST request
    response = requests.post(url, json=data)

    # Check if the request was successful
    if response.status_code == 200:
        print("Request successful.")
    else:
        print(f"Request failed with status code: {response.status_code}")
    print(response.content.decode())


def add_static_ip():
    url = "http://dronebridge.local/api/settings/setstaticip"
    data = {
        "client_ip": "192.168.10.88",
        "netmask": "255.255.255.0",
        "gw_ip": "192.198.10.1"
    }
    # Send the POST request
    response = requests.post(url, json=data)

    # Check if the request was successful
    if response.status_code == 200:
        print("Request successful.")
    else:
        print(f"Request failed with status code: {response.status_code}")
    print(response.content.decode())


def reset_static_ip():
    url = "http://dronebridge.local/api/settings/setstaticip"
    data = {
        "client_ip": "",
        "netmask": "",
        "gw_ip": ""
    }
    # Send the POST request
    response = requests.post(url, json=data)

    # Check if the request was successful
    if response.status_code == 200:
        print("Request successful.")
    else:
        print(f"Request failed with status code: {response.status_code}")
    print(response.content.decode())


add_custom_up()
add_static_ip()
