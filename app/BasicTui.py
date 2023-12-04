from textual.app import App, ComposeResult
from textual.widgets import Button, Footer, Label, Static, Input
from textual.screen import Screen, ModalScreen
from textual.containers import Grid, Horizontal, VerticalScroll
import FlightData
import addFlightObjects

HELLO_TEXT = """
                                    |
                                    |
                                    |
                                  .-'-.
                                 ' ___ '
                       ---------'  .-.  '---------
       _________________________'  '-'  '_________________________
        ''''''-|---|--/    \==][^',_m_,'^][==/    \--|---|-''''''
                      \    /  ||/   H   \||  \    /
                       '--'   OO   O|O   OO   '--'
 ▄    ▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄       ▄▄  ▄▄▄▄▄▄▄▄▄▄▄ 
▐░▌  ▐░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░▌     ▐░░▌▐░░░░░░░░░░░▌
▐░▌ ▐░▌ ▐░█▀▀▀▀▀▀▀█░▌▐░█▀▀▀▀▀▀▀▀▀ ▐░█▀▀▀▀▀▀▀▀▀ ▐░▌░▌   ▐░▐░▌▐░█▀▀▀▀▀▀▀▀▀ 
▐░▌▐░▌  ▐░▌       ▐░▌▐░▌          ▐░▌          ▐░▌▐░▌ ▐░▌▐░▌▐░▌          
▐░▌░▌   ▐░█▄▄▄▄▄▄▄█░▌▐░█▄▄▄▄▄▄▄▄▄ ▐░█▄▄▄▄▄▄▄▄▄ ▐░▌ ▐░▐░▌ ▐░▌▐░█▄▄▄▄▄▄▄▄▄ 
▐░░▌     ▐░░░░░░░░░▌ ▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░▌  ▐░▌  ▐░▌▐░░░░░░░░░░░▌
▐░▌░▌   ▐░█▀▀▀▀▀▀▀█░▌ ▀▀▀▀▀▀▀▀▀█░▌▐░█▀▀▀▀▀▀▀▀▀ ▐░▌   ▀   ▐░▌ ▀▀▀▀▀▀▀▀▀█░▌
▐░▌▐░▌  ▐░▌       ▐░▌          ▐░▌▐░▌          ▐░▌       ▐░▌          ▐░▌
▐░▌ ▐░▌ ▐░█▄▄▄▄▄▄▄█░▌ ▄▄▄▄▄▄▄▄▄█░▌▐░▌          ▐░▌       ▐░▌ ▄▄▄▄▄▄▄▄▄█░▌
▐░▌  ▐░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░▌          ▐░▌       ▐░▌▐░░░░░░░░░░░▌
 ▀    ▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀            ▀         ▀  ▀▀▀▀▀▀▀▀▀▀▀ 
-------------------------------------------------------------------------
                     K8s Flight Management System                  
-------------------------------------------------------------------------                                    
"""


class Blank(App):
    CSS_PATH = "modal01.tcss"
    BINDINGS = [("q", "request_quit", "Quit"), ("f", "view_flights", "Flights"), ("h", "view_hubs", "Hubs"),
                ("s", "view_spokes", "Spokes"), ("a", "view_airlines", "Airlines"), ("c", "view_create", "Create")]


    def compose(self) -> ComposeResult:
        yield Footer()
        yield Static(HELLO_TEXT)

    def action_request_quit(self) -> None:
        """Action to display the quit dialog."""
        self.app.push_screen(QuitScreen())

    def action_view_flights(self) -> None:
        self.app.push_screen(FlightData.FlightApp())

    def action_view_hubs(self) -> None:
        self.app.push_screen(FlightData.HubApp())

    def action_view_spokes(self) -> None:
        self.app.push_screen(FlightData.SpokeApp())

    def action_view_airlines(self) -> None:
        self.app.push_screen(FlightData.AirlineApp())

    def action_view_create(self) -> None:
        self.app.push_screen(Create())



class QuitScreen(ModalScreen):
    """Screen with a dialog to quit."""

    def compose(self) -> ComposeResult:
        yield Grid(
            Label("Are you sure you want to quit?", id="question"),
            Button("Quit", variant="error", id="quit"),
            Button("Cancel", variant="primary", id="cancel"),
            id="dialog"
        )

    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == "quit":
            self.app.exit()
        else:
            self.app.pop_screen()

class Create(Screen):
    CSS_PATH = "modal01.tcss"
    BINDINGS = [("q", "request_quit", "Quit"), ("f", "view_flights", "Flights"), ("h", "view_hubs", "Hubs"),
                ("s", "view_spokes", "Spokes"), ("a", "view_airlines", "Airlines"), ("c", "view_create", "Create")]
    def compose(self) -> ComposeResult:
        yield Footer()
        yield Horizontal(
            VerticalScroll(
                Static("Add Objects", classes="header"),
                Button("Airline", variant="primary", id="add_airline"),
                Button("Hub", variant="primary", id="add_hub"),
                Button("Spoke", variant="primary", id="add_spoke"),
                Button("Flight", variant="primary", id="add_flight"),
            )
        )

    def on_button_pressed(self, event: Button.Pressed) -> None:
        button_id = event.button.id
        if button_id == "add_airline":
            self.app.push_screen(addFlightObjects.AddAirline())
        elif button_id == "add_hub":
            self.app.push_screen(addFlightObjects.AddHub())
        elif button_id == "add_spoke":
            self.app.push_screen(addFlightObjects.AddSpoke())
        elif button_id == "add_flight":
            self.app.push_screen(addFlightObjects.AddFlight())

    def action_request_quit(self) -> None:
        """Action to display the quit dialog."""
        self.app.push_screen(QuitScreen())

    def action_view_flights(self) -> None:
        self.app.push_screen(FlightData.FlightApp())

    def action_view_hubs(self) -> None:
        self.app.push_screen(FlightData.HubApp())

    def action_view_spokes(self) -> None:
        self.app.push_screen(FlightData.SpokeApp())

    def action_view_airlines(self) -> None:
        self.app.push_screen(FlightData.AirlineApp())

    def action_view_create(self) -> None:
        self.app.push_screen(Create())

blankApp = Blank()
quitScreen = QuitScreen()
if __name__ == "__main__":
    blankApp.run()
