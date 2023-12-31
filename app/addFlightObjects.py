from textual.app import App, ComposeResult
from textual.widgets import Button, Footer, Label, Static, Input, Select
from textual.containers import Grid, Horizontal, VerticalScroll
import addObjects
from textual.screen import Screen, ModalScreen
import BasicTui
import FlightData
import buildList


blank_spoke_table_list = []

for a in buildList.blank_spoke_table:
    # print(a)
    for b in a:
        # print(b)
        blank_spoke_table_list.append(b)

blank_hub_table_list = []

for a in buildList.blank_hub_table:
    # print(a)
    for b in a:
        # print(b)
        blank_hub_table_list.append(b)

blank_airline_table_list = []

for a in buildList.blank_airline_table:
    # print(a)
    for b in a:
        # print(b)
        blank_airline_table_list.append(b)

blank_flight_table_list = []

for a in buildList.blank_flight_table:
    # print(a)
    for b in a:
        # print(b)
        blank_flight_table_list.append(b)

blank_combined_table_list = blank_hub_table_list + blank_spoke_table_list

class AddSpoke(ModalScreen):   #failing
    """Screen with a dialog to quit."""
    CSS_PATH = "button.tcss"

    BINDINGS = [("q", "request_quit", "Quit"), ("f", "view_flights", "Flights"), ("h", "view_hubs", "Hubs"),
                ("s", "view_spokes", "Spokes"), ("a", "view_airlines", "Airlines"), ("c", "view_create", "Create")]

    def compose(self) -> ComposeResult:
        yield Footer()
        yield Horizontal(
            VerticalScroll(
                Static("Add Spoke", classes="header"),
                Input(placeholder="SpokeName", id="spoke_name"),
                # Input(placeholder="HubName", id="hub_name"),
                # Input(placeholder="AirlineName", id="airline_name"),
                Select(((line, line) for line in blank_hub_table_list), id="hub_name", prompt="Hub"),
                Select(((line, line) for line in blank_airline_table_list), id="airline_name", prompt="Airline"),
                Button("Submit", variant="primary", id="submit_button")
            )
        )

    def on_button_pressed(self, event: Button.Pressed) -> None:
        button_id = event.button.id
        if button_id == "submit_button":
            spoke_name = self.query_one("#spoke_name")
            spoke_name = str(spoke_name.value).lower().replace('_', '-')

            hub_name = self.query_one("#hub_name")
            hub_name = hub_name.value

            airline_name = self.query_one("#airline_name")
            airline_name = airline_name.value
            
            try:
                addObjects.createSpoke(hub_name, airline_name, spoke_name)
                self.mount(Label("Added " + spoke_name + " press s to confirm"))
            except Exception as e:
                error_message = str(e)
                if e.status == 422:
                    self.mount(Label("---- error 422 invalid character please correct ----"))
                else:     
                    self.mount(Label(f"Caught an exception: {error_message}"))

    def action_request_quit(self) -> None:
        """Action to display the quit dialog."""
        self.app.push_screen(BasicTui.QuitScreen())

    def action_view_flights(self) -> None:
        self.app.push_screen(FlightData.FlightApp())

    def action_view_hubs(self) -> None:
        self.app.push_screen(FlightData.HubApp())

    def action_view_spokes(self) -> None:
        self.app.push_screen(FlightData.SpokeApp())

    def action_view_airlines(self) -> None:
        self.app.push_screen(FlightData.AirlineApp())

    def action_view_create(self) -> None:
        self.app.push_screen(BasicTui.Create())

class AddHub(ModalScreen):   #failing
    """Screen with a dialog to quit."""
    CSS_PATH = "button.tcss"

    BINDINGS = [("q", "request_quit", "Quit"), ("f", "view_flights", "Flights"), ("h", "view_hubs", "Hubs"),
                ("s", "view_spokes", "Spokes"), ("a", "view_airlines", "Airlines"), ("c", "view_create", "Create")]

    def compose(self) -> ComposeResult:
        yield Footer()
        yield Horizontal(
            VerticalScroll(
                Static("Add Hub", classes="header"),
                Input(placeholder="HubName", id="hub_name"),
                # Input(placeholder="AirlineName", id="airline_name"),
                Select(((line, line) for line in blank_airline_table_list), id="airline_name", prompt="Airline"),
                Button("Submit", variant="primary", id="submit_button")
            )
        )

    def on_button_pressed(self, event: Button.Pressed) -> None:
        button_id = event.button.id
        if button_id == "submit_button":

            hub_name = self.query_one("#hub_name")
            hub_name = str(hub_name.value).lower().replace('_', '-')

            airline_name = self.query_one("#airline_name")
            airline_name = airline_name.value

            try:
                addObjects.createHub(hub_name, airline_name)
                self.mount(Label("Added " + hub_name + " press h to confirm"))
            except Exception as e:
                error_message = str(e)
                if e.status == 422:
                    self.mount(Label("---- error 422 invalid character please correct ----"))
                else:     
                    self.mount(Label(f"Caught an exception: {error_message}"))


    def action_request_quit(self) -> None:
        """Action to display the quit dialog."""
        self.app.push_screen(BasicTui.QuitScreen())


    def action_view_flights(self) -> None:
        self.app.push_screen(FlightData.FlightApp())


    def action_view_hubs(self) -> None:
        self.app.push_screen(FlightData.HubApp())


    def action_view_spokes(self) -> None:
        self.app.push_screen(FlightData.SpokeApp())


    def action_view_airlines(self) -> None:
        self.app.push_screen(FlightData.AirlineApp())


    def action_view_create(self) -> None:
        self.app.push_screen(BasicTui.Create())


class AddAirline(ModalScreen):   #failing
    """Screen with a dialog to quit."""
    CSS_PATH = "button.tcss"

    BINDINGS = [("q", "request_quit", "Quit"), ("f", "view_flights", "Flights"), ("h", "view_hubs", "Hubs"),
                ("s", "view_spokes", "Spokes"), ("a", "view_airlines", "Airlines"), ("c", "view_create", "Create")]

    def compose(self) -> ComposeResult:
        yield Footer()
        yield Horizontal(
            VerticalScroll(
                Static("Add Airline", classes="header"),
                Input(placeholder="AirlineName", id="airline_name"),
                Button("Submit", variant="primary", id="submit_button")
            )
        )

    def on_button_pressed(self, event: Button.Pressed) -> None:
        button_id = event.button.id
        if button_id == "submit_button":

            airline_name = self.query_one("#airline_name")
            airline_name = str(airline_name.value).lower().replace('_', '-')

            try:
                addObjects.createAirLine(airline_name)
                self.mount(Label("Added " + airline_name + " press a to confirm"))
            except Exception as e:
                error_message = str(e)
                if e.status == 422:
                    self.mount(Label("---- error 422 invalid character please correct ----"))
                else:     
                    self.mount(Label(f"Caught an exception: {error_message}"))

    def action_request_quit(self) -> None:
        """Action to display the quit dialog."""
        self.app.push_screen(BasicTui.QuitScreen())

    def action_view_flights(self) -> None:
        self.app.push_screen(FlightData.FlightApp())

    def action_view_hubs(self) -> None:
        self.app.push_screen(FlightData.HubApp())

    def action_view_spokes(self) -> None:
        self.app.push_screen(FlightData.SpokeApp())

    def action_view_airlines(self) -> None:
        self.app.push_screen(FlightData.AirlineApp())

    def action_view_create(self) -> None:
        self.app.push_screen(BasicTui.Create())


class AddFlight(ModalScreen):   #failing
    """Screen with a dialog to quit."""
    CSS_PATH = "button.tcss"

    BINDINGS = [("q", "request_quit", "Quit"), ("f", "view_flights", "Flights"), ("h", "view_hubs", "Hubs"),
                ("s", "view_spokes", "Spokes"), ("a", "view_airlines", "Airlines"), ("c", "view_create", "Create")]

    def compose(self) -> ComposeResult:
        yield Footer()
        yield Horizontal(
            VerticalScroll(
                Static("Add Flight", classes="header"),
                Input(placeholder="FlightName", id="flight_name"),
                # Input(placeholder="Leaving", id="leaving_name"),
                # Input(placeholder="Going", id="going_name"),
                Select(((line, line) for line in blank_combined_table_list), id="leaving_name", prompt="Leaving"),
                Select(((line, line) for line in blank_combined_table_list), id="going_name", prompt="Going"),
                Select(((line, line) for line in blank_airline_table_list), id="airline_name", prompt="Airline"),
                # Input(placeholder="AirlineName", id="airline_name"),
                Button("Submit", variant="primary", id="submit_button")
            )
        )

    def on_button_pressed(self, event: Button.Pressed) -> None:
        button_id = event.button.id
        if button_id == "submit_button":
            flight_name = self.query_one("#flight_name")
            flight_name = str(flight_name.value).lower().replace('_', '-')

            leaving_name = self.query_one("#leaving_name")
            leaving_name = leaving_name.value

            going_name = self.query_one("#going_name")
            going_name = going_name.value

            airline_name = self.query_one("#airline_name")
            airline_name = airline_name.value

            try:

                addObjects.createFlight(flight_name, going_name, leaving_name, airline_name)
                self.mount(Label("Added " + flight_name + " press f to confirm"))
            except Exception as e:
                error_message = str(e)
                if e.status == 422:
                    self.mount(Label("---- error 422 invalid character please correct ----"))
                else:     
                    self.mount(Label(f"Caught an exception: {error_message}"))

    def action_request_quit(self) -> None:
        """Action to display the quit dialog."""
        self.app.push_screen(BasicTui.QuitScreen())

    def action_view_flights(self) -> None:
        self.app.push_screen(FlightData.FlightApp())

    def action_view_hubs(self) -> None:
        self.app.push_screen(FlightData.HubApp())

    def action_view_spokes(self) -> None:
        self.app.push_screen(FlightData.SpokeApp())

    def action_view_airlines(self) -> None:
        self.app.push_screen(FlightData.AirlineApp())

    def action_view_create(self) -> None:
        self.app.push_screen(BasicTui.Create())