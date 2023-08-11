"""
Purpose: Display output for MT Cars dataset.

@imports shiny.ui as ui
@imports shinywidgets.output_widget for interactive charts
"""
from shiny import ui
from shinywidgets import output_widget


def get_pairs_outputs():
    return ui.panel_main(
        ui.h2("Main Panel with Continuous and Reactive Output"),
        ui.tags.hr(),
        ui.tags.section(
            ui.h3("Continuous Updates (Forex API)"),
            ui.tags.br(),
            
        ),
    )
