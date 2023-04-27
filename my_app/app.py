# test shiny for python app
from shiny import *
from shiny.types import FileInfo
from io import StringIO
from htmltools import HTML
from simple_colors import *

import pandas as pd
import subprocess
import textwrap
import re

choices = ['Type in sequence', 'Upload file']

# ui section
app_ui = ui.page_fluid(

    ui.panel_title('Check any sequence for an insert'),

    ui.layout_sidebar(
        ui.panel_sidebar(

            # have user upload files as inputs 
            # user input oligos file
            ui.input_file(id = 'oligos', 
                label = 'Oligos', 
                placeholder = 'Select oligos file'),

            # user input sequence file(s)
            ui.input_file('sequence', 'Sequence files', 
                placeholder = 'Select seq file(s)', 
                multiple = True),

            # user presses button to check the sequence for the oligo insert
            ui.input_action_button(id = 'call_me', 
                label = 'Compare',
                class_= 'btn-success'),

      ),

    # output(s)
    ui.panel_main(
        ui.output_ui('check', inline = True),
    )
  )
)

# server section
def server(input, output, session):

    # run checkInserts on pt
    @output
    @render.ui
    @reactive.event(input.call_me)

    def check():

        f: list[FileInfo] = input.oligos()
        oligos_df = f[0]['datapath']
        oligos_str = str(oligos_df)
        file_infos = input.sequence()
        file_info = file_infos[0]
        pt = str(file_info['datapath'])

        # run checkInserts on the user inputs
        result = subprocess.run(['python', 'checkInserts_test.py', pt, oligos_str], text=True, capture_output=True)

#        result_stdout = pd.DataFrame(textwrap.wrap(re.sub('.\[0m', ')', re.sub('.\[32m', 'ui.div(', getattr(result, 'stdout')))))
        result_stdout = getattr(result, 'stdout')
        result_header = result_stdout[1]
        result_body = result_stdout[2]
        result_body = re.sub('.\[32m', '<u>', result_body)
        result_body = re.sub('.\[0m', '</u>', result_body)
        result_body = HTML(result_body)
        return result_head, result_body

#    @output
#    @render.ui
#    @reactive.event(check.result_body)
#    def display_as_table():
#        return


# call app
app = App(app_ui, server)
