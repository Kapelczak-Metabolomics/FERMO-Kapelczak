from dash import html, dcc
import dash_bootstrap_components as dbc

def call_processing_page():
    '''Create button that redirects to peaktable processing page'''
    return html.Div([
        dbc.Button(
            "Processing mode",
            id='call_processing_button',
            n_clicks=0,
            className="button_general_class",
            style={'width' : '100%',}
            ),
        ],
        style={'margin' : 'auto','width' : '50%',},
        )

# ~ def call_peakpicking_page():
    # ~ '''Create button that redirects to peakpicking preprocessing page'''
    # ~ return html.Div([
        # ~ dbc.Button(
            # ~ "NOT IMPLEMENTED YET",
            # ~ id='call_peakpicking_button',
            # ~ n_clicks=0,
            # ~ className="d-grid gap-2 col-6 mx-auto",
            # ~ disabled=True, #switch on when ready
            # ~ ),
        # ~ ])

def call_loading_page():
    '''Create the button that redirects to loading page'''
    return html.Div([
        dbc.Button(
            "Loading mode",
            id='call_loading_button',
            n_clicks=0,
            className="button_general_class",
            style={'width' : '100%',}
            ),
        ],
        style={'margin' : 'auto','width' : '50%',},
        )


def call_landing_header_intro_text():
    '''Div to hold intro text for landing page'''
    return html.H1(
            'LC-MS/MS data analysis and feature prioritization made easy',
        )


def call_landing_intro_text():
    '''Div to hold intro text for landing page'''
    return html.Div([
        dcc.Markdown('''FERMO is an app for the processing, visualization and analysis of **LC-MS/MS** data.'''),
        html.Div(style={'margin-top' : '10px'}),
        dcc.Markdown('''
        FERMO integrates **LC-MS/MS data**, **bioactivity**, and **group metadata** in a combined analysis platform. In each sample, features are assessed for their associatedness with **bioactivity**, their putative **novelty**, and the estimated **ease of isolation**. For these attributes, scores are calculated, and the **chemical diversity** of the samples is estimated. The resulting metrics allow for pragmatic **prioritization** of features and samples for further investigation.
        '''),
        html.Div(style={'margin-top' : '10px'}),
        html.Div('''
        FERMO can used in different modes, which can be accessed by clicking the buttons on the bottom of the page.
        '''),
        html.Div(style={'margin-top' : '10px'}),
        dcc.Markdown('''More information on FERMO can be found in the [**README**](https://github.com/mmzdouc/FERMO/) or in the [**FERMO Wiki**](https://github.com/mmzdouc/FERMO/wiki/).'''),
    ],
    style={
        'line-height' : '1.5',
        'text-align' : 'justify',
        'font-size' : '20px',
        }
    )

def call_landing_intro_workflow():
    '''Div to hold intro workflow for landing page'''

    return html.Div(
            html.Img(
                src='/assets/app-landing-workflow.svg',
                style={'height': '17vh'},
                ),
            style={
                'text-align' : 'center',
                'margin-top' : '60px'
                },
            )

def call_landing_header_peaktable_text():
    '''Div to hold header for peaktable processing start'''
    return html.H2(
            'Processing mode',
            style={'text-align' : 'center',}
        )

def call_landing_peaktable_text():
    '''Div to hold intro text on peaktable processing'''
    return html.Div([
        html.Div(style={'margin-top':'30px',}),
        dcc.Markdown(
        '''Standard peaktable processing mode. 
        '''),
        dcc.Markdown(
        '''This mode requires a **feature peaktable** and **MS/MS data** in the **MZmine3** format. Optionally, users can also provide files containing **grouping metadata**, **bioactivity data**, and a **spectral library** for annotation purposes. 
        '''),
    ],
    style={
        'line-height' : '1.5',
        'text-align' : 'center',
        'font-size' : '20px',
        },
    )

# ~ def call_landing_header_peakpicking_text():
    # ~ '''Div to hold header peakpicking processing start'''
    # ~ return html.H3(
            # ~ 'Data pre-processing (raw data mode)',
            # ~ style={'text-align' : 'center',}
        # ~ )

# ~ def call_landing_peakpicking_text():
    # ~ '''Div to hold text peakpicking processing start'''
    # ~ return html.Div([
    # ~ ],
    # ~ style={
        # ~ 'line-height' : '1.5',
        # ~ 'text-align' : 'center',
        # ~ },
    # ~ )

def call_landing_header_loading_text():
    '''Div to hold header loading start'''
    return html.H2(
            'Loading mode',
            style={'text-align' : 'center',}
        )

def call_landing_loading_text():
    '''Div to hold text loading start'''
    return html.Div([
        html.Div(style={'margin-top':'30px',}),
        dcc.Markdown(
        '''Session file loading mode.
        '''),
        dcc.Markdown(
        '''This mode requires a previously created **FERMO session file** in the **json format**. This file can be either created by running data in the peaktable processing (standard) mode, or by obtaining a session file from others.
        '''),
    ],
    style={
        'line-height' : '1.5',
        'text-align' : 'center',
        'font-size' : '20px',
        },
    )

def call_landing_peaktable_icon():
    '''Div to hold icon peaktable start'''
    return html.Div(
            html.Img(
                src='/assets/icon-peaktable-processing.svg',
                style={'height': '10vh'},
                ),
            style={
                'text-align' : 'center',
                'margin-top' : '20px',
                },
            )
            
# ~ def call_landing_peakpicking_icon():
    # ~ '''Div to hold icon peakpicking start'''
    # ~ return html.Div(
            # ~ html.Img(
                # ~ src='/assets/icon-peakpicking-processing.svg',
                # ~ style={'height': '10vh'},
                # ~ ),
            # ~ style={
                # ~ 'text-align' : 'center',
                # ~ 'margin-top' : '20px',
                # ~ },
            # ~ )
            
def call_landing_loading_icon():
    '''Div to hold icon loading start'''
    return html.Div(
            html.Img(
                src='/assets/icon-loading-processing.svg',
                style={'height': '10vh'},
                ),
            style={
                'text-align' : 'center',
                'margin-top' : '20px',
                },
            )





landing = html.Div([
    ###first row###
    dbc.Row([
        #first column#
        dbc.Col([
            html.Div([
                call_landing_header_intro_text(),
                call_landing_intro_text(),
            ],
            style={
                'margin-left':'30px',
                'margin-top':'30px',
                'margin-right':'30px',
                },
            )],
            id="landing_row_1_col_1",
            width=6,
            ),
        #second column#
        dbc.Col([
                call_landing_intro_workflow(),
                ],
            id="landing_row_1_col_2",
            width=6,
            ),
        ],
    id="landing_row_1",
    ),
    ###second row###
    dbc.Row([
       #first column#
        dbc.Col([
            html.Div(style={'margin-top':'30px',}),
            html.Div([
                call_landing_header_peaktable_text(),
                call_landing_peaktable_icon(),
                call_landing_peaktable_text(),
                ],
                style={
                    'margin' : 'auto',
                    'width' : '50%',
                    }
                ),
            html.Div(style={'margin-top':'30px',}),
            html.Div(
                call_processing_page(),
            ),
            ],
            id="landing_row_2_col_1",
            width=6,
            ),
        # ~ #second column#
        # ~ dbc.Col([
            # ~ html.Div([
                # ~ call_landing_header_peakpicking_text(),
                # ~ call_landing_peakpicking_icon(),
                # ~ call_landing_peakpicking_text(),
                # ~ ],
                # ~ style={
                    # ~ 'margin-left':'40px',
                    # ~ 'margin-right':'40px',
                    # ~ }
                # ~ ),
            # ~ ],
            # ~ id="landing_row_2_col_2",
            # ~ width=4,
            # ~ ),
        #third column#
        dbc.Col([
            html.Div(style={'margin-top':'30px',}),
            html.Div([
                call_landing_header_loading_text(),
                call_landing_loading_icon(),
                call_landing_loading_text(),
                ],
                style={
                    'margin' : 'auto',
                    'width' : '50%',
                    }
                ),
            html.Div(style={'margin-top':'30px',}),
            html.Div(
                call_loading_page(),
            ),
            
            ],
            id="landing_row_2_col_2",
            width=6,
            ),
        ],
    id="landing_row_2",
    ),
])

