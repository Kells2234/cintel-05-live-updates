"""
Purpose: Display output for MT Cars dataset.

@imports shiny.ui as ui
@imports shinywidgets.output_widget for interactive charts
"""
from shiny import ui
from shinywidgets import output_widget


def get_mtcars_outputs():
    return ui.panel_main(
        ui.h2("Main Panel with Continuous and Reactive Output"),
        ui.tags.hr(),
        ui.tags.section(
            ui.h3("Continuous Updates (Weather API)"),
            ui.tags.br(),
            ui.output_text("mtcars_location_string"),
            ui.tags.br(),
            ui.output_ui("mtcars_location_table"),
            ui.tags.br(),
            output_widget("mtcars_location_chart"),
            ui.tags.br(),
            ui.tags.hr(),
            ui.h3('Continuous Updates (YFinance API)'),
            ui.tags.br(),
            ui.output_text('mtcars_stock_string'),
            ui.tags.br(),
            ui.output_ui('mtcars_stock_table'),
            ui.tags.br(),
            output_widget('mtcars_stock_chart'),
            ui.tags.br(),
            ui.tags.hr(),
            ui.h3("Filtered Cars: Charts"),
            output_widget("mtcars_output_widget1"),
            ui.output_plot("mtcars_plot1"),
            ui.output_plot("mtcars_plot2"),
            ui.tags.hr(),
            ui.h3("Filtered MT Cars Table"),
            ui.output_text("mtcars_record_count_string"),
            ui.output_table("mtcars_filtered_table"),
            ui.tags.hr(),
        ),
    )
