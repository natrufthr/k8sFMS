from textual import on
from textual.app import App, ComposeResult
from textual.widgets import Header, Select
import json
from kubernetes import client, config, utils
import os

listAirlines = ["apple", "banana", "cherry"]

config_file_location='/app/data/config.yaml'

nameSpace = os.environ.get('NAMESPACE')



config.load_kube_config(config_file=config_file_location)

cOa = client.CustomObjectsApi()

v1 = client.CoreV1Api()

flightList = cOa.list_namespaced_custom_object("example.air.com", "v1", str(nameSpace), "flights").get('items')
airlineList = cOa.list_namespaced_custom_object("example.air.com", "v1", str(nameSpace), "airlines").get('items')
hubList = cOa.list_namespaced_custom_object("example.air.com", "v1", str(nameSpace), "hubs").get('items')
spokeList = cOa.list_namespaced_custom_object("example.air.com", "v1", str(nameSpace), "spokes").get('items')
blank_spoke_table = []
blank_hub_table = []
blank_airline_table = []
blank_flight_table = []

for i in airlineList:
    test = i['metadata']
    spec = i['spec']

    airline_name = ''
    for k, v in test.items():
        if k == 'name':
            airline_name = v

    table = [airline_name]
    blank_airline_table.append(table)

for i in flightList:
    test = i['metadata']
    flight = (eval(i.get('metadata').get('annotations').get('kubectl.kubernetes.io/last-applied-configuration')))
    flight_spec = flight.get('spec')
    airlineName = flight_spec.get('airLineName')
    flightLeaving = flight_spec.get('leaving')
    flightGoing = flight_spec.get('going')

    flight_name = ''

    for k, v in test.items():
        if k == 'name':
            flight_name = v

    table = [flight_name, flightLeaving, flightGoing]
    blank_flight_table.append(table)

for i in hubList:
    test = i['metadata']
    spec = i['spec']
    airlineName = spec.get('airLineName')
    hub_name = ''

    for key, value in test.items():
        if key == 'name':
            hub_name = value
    table = [hub_name]
    blank_hub_table.append(table)

for i in spokeList:
    test = i['metadata']
    hub_name = (i['spec']['hubName'])
    airlineName = (i['spec']['airLineName'])

    spoke_name = ''

    for key, value in test.items():
        if key == 'name':
            spoke_name = value

    table = [spoke_name]
    blank_spoke_table.append(table)

####  creating lists

blank_spoke_table_list = []

for a in blank_spoke_table:
    # print(a)
    for b in a:
        # print(b)
        blank_spoke_table_list.append(b)

blank_hub_table_list = []

for a in blank_hub_table:
    # print(a)
    for b in a:
        # print(b)
        blank_hub_table_list.append(b)

blank_airline_table_list = []

for a in blank_airline_table:
    # print(a)
    for b in a:
        # print(b)
        blank_airline_table_list.append(b)

blank_flight_table_list = []

for a in blank_flight_table:
    # print(a)
    for b in a:
        # print(b)
        blank_flight_table_list.append(b)

# print(json.dumps(blank_hub_table_list))
# print(json.dumps(blank_airline_table_list))
# print(json.dumps(blank_spoke_table_list))

