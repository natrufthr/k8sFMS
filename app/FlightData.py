from textual import events
from textual.app import ComposeResult
from textual.screen import Screen
from textual.widgets import DataTable, Header
from kubernetes import client, config

config_file_location = '/app/data/config.yaml'

ROWS = []

class FlightApp(Screen):
    def compose(self) -> ComposeResult:
        yield DataTable()
        yield Header()

    def on_mount(self) -> None:

        self.title = "To return to menu"
        self.sub_title = "-- Press X --"

        config.load_kube_config(config_file=config_file_location)

        cOa = client.CustomObjectsApi()

        v1 = client.CoreV1Api()

        flightList = cOa.list_namespaced_custom_object("example.air.com", "v1", "default", "flights").get('items')
        airlineList = cOa.list_namespaced_custom_object("example.air.com", "v1", "default", "airlines").get('items')
        hubList = cOa.list_namespaced_custom_object("example.air.com", "v1", "default", "hubs").get('items')
        spokeList = cOa.list_namespaced_custom_object("example.air.com", "v1", "default", "spokes").get('items')
        flight_table = [["flight_name", "leaving", "going"]]
        airline_table = [["airline_name"]]
        spoke_table = [["spoke_name", "hub_name", "airlineName"]]
        hub_table = [["hub_name", "airlineName"]]

        for i in airlineList:
            test = i['metadata']
            spec = i['spec']

            airline_name = ''
            for k, v in test.items():
                if k == 'name':
                    airline_name = v

            table = [airline_name]
            airline_table.append(table)

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
            flight_table.append(table)

        for i in hubList:
            hub = (eval(i.get('metadata').get('annotations').get('kubectl.kubernetes.io/last-applied-configuration')))
            hub_name = hub.get('metadata').get('name')
            hub_spec = hub.get('spec')
            airlineName = hub_spec.get('airLineName')
            spoke_name = hub_spec.get('spokeName')
            # ## print(flight_spec)
            table = [hub_name, airlineName]
            hub_table.append(table)

        for i in spokeList:
            # print(i)
            test = i['metadata']
            # print(test)
            # print(type(test))
            hub_name = (i['spec']['hubName'])
            # print(hub_name)
            airlineName = (i['spec']['airLineName'])
            # print(airlineName)
            # print(i['name'])

            spoke_name = ''

            for key, value in test.items():
                if key == 'name':
                    spoke_name = value
                    # print(spoke_name)
                    # print(hub_name)
                    # print(airlineName)

            table = [spoke_name, hub_name, airlineName]
            spoke_table.append(table)

        ROWS = flight_table

        table = self.query_one(DataTable)
        table.add_columns(*ROWS[0])
        table.add_rows(ROWS[1:])

    def on_key(self, event: events.Key) -> None:
        if event.key == "x":
            self.app.pop_screen()


class HubApp(Screen):
    def compose(self) -> ComposeResult:
        yield DataTable()
        yield Header()

    def on_mount(self) -> None:
        self.title = "To return to menu"
        self.sub_title = "-- Press X --"

        config.load_kube_config(config_file=config_file_location)

        cOa = client.CustomObjectsApi()

        v1 = client.CoreV1Api()

        flightList = cOa.list_namespaced_custom_object("example.air.com", "v1", "default", "flights").get('items')
        airlineList = cOa.list_namespaced_custom_object("example.air.com", "v1", "default", "airlines").get('items')
        hubList = cOa.list_namespaced_custom_object("example.air.com", "v1", "default", "hubs").get('items')
        spokeList = cOa.list_namespaced_custom_object("example.air.com", "v1", "default", "spokes").get('items')
        flight_table = [["flight_name", "leaving", "going"]]
        airline_table = [["airline_name"]]
        spoke_table = [["spoke_name", "hub_name", "airlineName"]]
        hub_table = [["hub_name", "airlineName"]]

        for i in airlineList:
            test = i['metadata']
            spec = i['spec']

            airline_name = ''
            for k, v in test.items():
                if k == 'name':
                    airline_name = v

            table = [airline_name]
            airline_table.append(table)

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
            flight_table.append(table)

        for i in hubList:
            hub = (eval(i.get('metadata').get('annotations').get('kubectl.kubernetes.io/last-applied-configuration')))
            hub_name = hub.get('metadata').get('name')
            hub_spec = hub.get('spec')
            airlineName = hub_spec.get('airLineName')
            spoke_name = hub_spec.get('spokeName')
            # ## print(flight_spec)
            table = [hub_name, airlineName]
            hub_table.append(table)

        for i in spokeList:
            # print(i)
            test = i['metadata']
            # print(test)
            # print(type(test))
            hub_name = (i['spec']['hubName'])
            # print(hub_name)
            airlineName = (i['spec']['airLineName'])
            # print(airlineName)
            # print(i['name'])

            spoke_name = ''

            for key, value in test.items():
                if key == 'name':
                    spoke_name = value
                    # print(spoke_name)
                    # print(hub_name)
                    # print(airlineName)

            table = [spoke_name, hub_name, airlineName]
            spoke_table.append(table)

        ROWS = hub_table

        table = self.query_one(DataTable)
        table.add_columns(*ROWS[0])
        table.add_rows(ROWS[1:])

    def on_key(self, event: events.Key) -> None:
        if event.key == "x":
            self.app.pop_screen()


class SpokeApp(Screen):
    def compose(self) -> ComposeResult:
        yield DataTable()
        yield Header()

    def on_mount(self) -> None:
        self.title = "To return to menu"
        self.sub_title = "-- Press X --"

        config.load_kube_config(config_file=config_file_location)

        cOa = client.CustomObjectsApi()

        v1 = client.CoreV1Api()

        flightList = cOa.list_namespaced_custom_object("example.air.com", "v1", "default", "flights").get('items')
        airlineList = cOa.list_namespaced_custom_object("example.air.com", "v1", "default", "airlines").get('items')
        hubList = cOa.list_namespaced_custom_object("example.air.com", "v1", "default", "hubs").get('items')
        spokeList = cOa.list_namespaced_custom_object("example.air.com", "v1", "default", "spokes").get('items')
        flight_table = [["flight_name", "leaving", "going"]]
        airline_table = [["airline_name"]]
        spoke_table = [["spoke_name", "hub_name", "airlineName"]]
        hub_table = [["hub_name", "airlineName"]]

        for i in airlineList:
            test = i['metadata']
            spec = i['spec']

            airline_name = ''
            for k, v in test.items():
                if k == 'name':
                    airline_name = v

            table = [airline_name]
            airline_table.append(table)

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
            flight_table.append(table)

        for i in hubList:
            hub = (eval(i.get('metadata').get('annotations').get('kubectl.kubernetes.io/last-applied-configuration')))
            hub_name = hub.get('metadata').get('name')
            hub_spec = hub.get('spec')
            airlineName = hub_spec.get('airLineName')
            spoke_name = hub_spec.get('spokeName')
            # ## print(flight_spec)
            table = [hub_name, airlineName]
            hub_table.append(table)

        for i in spokeList:
            # print(i)
            test = i['metadata']
            # print(test)
            # print(type(test))
            hub_name = (i['spec']['hubName'])
            # print(hub_name)
            airlineName = (i['spec']['airLineName'])
            # print(airlineName)
            # print(i['name'])

            spoke_name = ''

            for key, value in test.items():
                if key == 'name':
                    spoke_name = value
                    # print(spoke_name)
                    # print(hub_name)
                    # print(airlineName)

            table = [spoke_name, hub_name, airlineName]
            spoke_table.append(table)

        ROWS = spoke_table

        table = self.query_one(DataTable)
        table.add_columns(*ROWS[0])
        table.add_rows(ROWS[1:])

    def on_key(self, event: events.Key) -> None:
        if event.key == "x":
            self.app.pop_screen()


class AirlineApp(Screen):
    def compose(self) -> ComposeResult:
        yield DataTable()
        yield Header()

    def on_mount(self) -> None:
        self.title = "To return to menu"
        self.sub_title = "-- Press X --"

        config.load_kube_config(config_file=config_file_location)

        cOa = client.CustomObjectsApi()

        v1 = client.CoreV1Api()

        flightList = cOa.list_namespaced_custom_object("example.air.com", "v1", "default", "flights").get('items')
        airlineList = cOa.list_namespaced_custom_object("example.air.com", "v1", "default", "airlines").get('items')
        hubList = cOa.list_namespaced_custom_object("example.air.com", "v1", "default", "hubs").get('items')
        spokeList = cOa.list_namespaced_custom_object("example.air.com", "v1", "default", "spokes").get('items')
        flight_table = [["flight_name", "leaving", "going"]]
        airline_table = [["airline_name"]]
        spoke_table = [["spoke_name", "hub_name", "airlineName"]]
        hub_table = [["hub_name", "airlineName"]]

        for i in airlineList:
            test = i['metadata']
            spec = i['spec']

            airline_name = ''
            for k, v in test.items():
                if k == 'name':
                    airline_name = v

            table = [airline_name]
            airline_table.append(table)

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
            flight_table.append(table)

        for i in hubList:
            hub = (eval(i.get('metadata').get('annotations').get('kubectl.kubernetes.io/last-applied-configuration')))
            hub_name = hub.get('metadata').get('name')
            hub_spec = hub.get('spec')
            airlineName = hub_spec.get('airLineName')
            spoke_name = hub_spec.get('spokeName')
            # ## print(flight_spec)
            table = [hub_name, airlineName]
            hub_table.append(table)

        for i in spokeList:
            # print(i)
            test = i['metadata']
            # print(test)
            # print(type(test))
            hub_name = (i['spec']['hubName'])
            # print(hub_name)
            airlineName = (i['spec']['airLineName'])
            # print(airlineName)
            # print(i['name'])

            spoke_name = ''

            for key, value in test.items():
                if key == 'name':
                    spoke_name = value
                    # print(spoke_name)
                    # print(hub_name)
                    # print(airlineName)

            table = [spoke_name, hub_name, airlineName]
            spoke_table.append(table)

        ROWS = airline_table

        table = self.query_one(DataTable)
        table.add_columns(*ROWS[0])
        table.add_rows(ROWS[1:])

    def on_key(self, event: events.Key) -> None:
        if event.key == "x":
            self.app.pop_screen()