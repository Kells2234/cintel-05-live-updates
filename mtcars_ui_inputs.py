"""
Purpose: Provide user interaction options for MT Cars dataset.

IDs must be unique. They are capitalized in this app for clarity (not typical).
The IDs are case-sensitive and must match the server code exactly.
Preface IDs with the dataset name to avoid naming conflicts.

"""
from shiny import ui

# Define the UI inputs and include our new selection options

def get_mtcars_inputs():
    return ui.panel_sidebar(
        ui.h2("MT Cars Interaction"),
        ui.tags.hr(),
        ui.input_slider(
            "MTCARS_MPG_RANGE",
            "Miles Per Gallon (MPG)",
            min=10,
            max=35,
            value=[10, 35],
        ),
        ui.input_select(
            id="MTCARS_LOCATION_SELECT",
            label="Choose a location",
            choices=["ELY MN", "Death Valley CA", "Maryville MO"],
            selected="ELY MN",
        ),
        ui.input_select(
            id='MTCARS_STOCK_SELECT',
            label='Choose a company',
            choices=['Tesla Inc', 'General Motors Company', 'Toyota Motor Corporation', 'Ford Motor Company', 'Honda Motor Co'],
            selected='Tesla Inc',
        ),
        ui.tags.hr(),
        ui.tags.section(
            ui.h3("MT Cars Table"),
            ui.tags.p("Description of each field in the table:"),
            ui.tags.ul(
                ui.tags.li("mpg: Miles per Gallon"),
                ui.tags.li("cyl: Number of cylinders"),
                ui.tags.li("disp: Displacement (cubic inches)"),
                ui.tags.li("hp: Gross horsepower"),
                ui.tags.li("drat: Rear axle ratio"),
                ui.tags.li("wt: Weight (1,000 lbs)"),
                ui.tags.li("qsec: 1/4 mile time"),
                ui.tags.li("vs: V/S (Engine shape; 0 = V-shaped, 1 = Straight)"),
                ui.tags.li("am: Transmission (0 = Automatic, 1 = Manual)"),
                ui.tags.li("gear: Number of forward gears"),
                ui.tags.li("carb: Number of carburetors"),
            ),
            ui.output_table("cars_table"),
        ),
        ui.tags.hr(),
        ui.p("🕒 Please be patient. Outputs may take a few seconds to load."),
        ui.tags.hr(),
    )
