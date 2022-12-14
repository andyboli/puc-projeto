from dash import (dash_table, dcc, html)
from math import ceil
from plotly.subplots import make_subplots
import dash_bootstrap_components as dbc
import plotly.graph_objects as go

from controller.reader import lang
from database.constants import PUC_DB_HOMELESS_COLUMNS_TABLE_LABELS


def ALERT(children, color="success"):
    return dbc.Alert(
        children=children,
        className="default-section default-row-section default-border",
        color=color,
    )


def BAR_CHART(figure):
    return dcc.Graph(
        className='default-section',
        figure=figure,
    )


def BOLD_TEXT(key: str):
    return html.P(
        children=lang(key),
        className='default-bold-typography',
    )


def BUTTON(children, id: str, color="primary"):
    return dbc.Button(
        children=children,
        class_name='default-section default-row-section default-border',
        color=color,
        id=id,
    )


def CARD(children):
    return html.Div(
        children,
        className='default-section default-white-section default-border'
    )


def COLUMN_SECTION(children: any = '', id='', hide=False):
    if hide:
        return html.Div(
            children,
            className='default-section default-column-section default-hide-section',
            id=id
        )
    return html.Div(children,
                    className='default-section default-column-section',
                    id=id
                    )


def DATE_PICKER_RANGE(id: str):
    return dcc.DatePickerRange(
        calendar_orientation='vertical',
        className='default-section default-border',
        display_format="DD MM YYYY",
        end_date_placeholder_text=lang("component_end_date_placeholder"),
        id=id,
        min_date_allowed='2019-01-01',
        start_date_placeholder_text=lang('component_start_date_placeholder'),
    )


def DROPDOWN_ITEM(option: tuple, id: str):
    key, value = option
    return dbc.DropdownMenuItem(value, id=key + '-' + id)


def DROPDOWN(options: dict = {}, id=''):
    return dbc.DropdownMenu([*map(lambda option: DROPDOWN_ITEM(option=option, id=id), options.items())], id=id, label=lang("component_dropdown_label"), class_name='default-border')


def ERROR_ICON():
    return html.I(className="bi bi-x-octagon-fill me-2")


def INTERVAL(id: str, max_intervals: int, interval=2.1*1000):
    return dcc.Interval(
        disabled=True,
        id=id,
        interval=interval,
        max_intervals=max_intervals,
        n_intervals=0,
    )


def LINK(key: str, href: str):
    return html.A(
        children=lang(key),
        className='default-typography',
        href=lang(href),
        target='_blank'
    )


def MAIN_SECTION(children: any = ""):
    return html.Div(
        children,
        className='main-section default-column-section'
    )


def MAIN_TITLE():
    return html.H1(
        children=lang('component_main_title_text'),
        className='default-typography main-title'
    )


def PIE_CHART(first_column_values, second_column_values):
    second_column_length = len(second_column_values)

    cols = 2
    rows = ceil(second_column_length / cols)

    initial_x = cols * 0.20
    initial_y = rows*1

    x_gap = 0.60
    y_gap = 0.42

    fig = make_subplots(rows=rows, cols=cols, specs=[
                        [{'type': 'domain'} for _ in range(cols)] for _ in range(rows)])

    annotations = []

    for name, values in second_column_values.items():
        value_index = list(second_column_values.keys()).index(name) + 1

        col = cols - value_index % cols
        row = ceil(value_index / cols)

        x = initial_x + (col - 1)*x_gap
        y = initial_y - (row - 1)*y_gap

        fig.add_trace(
            go.Pie(
                labels=first_column_values,
                name=name,
                values=values,
            ),
            col=col,
            row=row
        )

        annotations.append(dict(text=name, x=x, y=y,
                           font_size=20, showarrow=False))

    fig.update_traces(hoverinfo="label+percent+name")

    fig.update_layout(
        annotations=annotations)

    return dcc.Graph(figure=fig, id="pie-graph")


def ROW_SECTION(children: any = "", id="", hide=False):
    if hide:
        return html.Div(
            children,
            className='default-section default-row-section default-hide-section',
            id=id
        )
    return html.Div(
        children,
        className='default-section default-row-section',
        id=id
    )


def SPINNER(id='', size='sm', color='light', hide=False):
    if hide:
        return html.Div(children=dbc.Spinner(size=size, color=color), id=id, className="default-hide-section")
    return html.Div(children=dbc.Spinner(size=size, color=color), id=id, className="default-section")


def STORE(id: str):
    return dcc.Store(id=id)


def SUCCESS_ICON():
    return html.I(className="bi bi-check-circle-fill me-2")


def TABLE(data: list):
    return dash_table.DataTable(data=[{"month_year": month_year, "age": age,
                                       "gender": gender, "birthday": birthday,
                                       "schooling": schooling, "ethnicity": ethnicity,
                                       "region": region, "period": period, "social_welfare": social_welfare} for _, month_year, age, gender, birthday, schooling, ethnicity, region, period, social_welfare in data],
                                columns=[{"name": PUC_DB_HOMELESS_COLUMNS_TABLE_LABELS[column], "id": column} for column in ['month_year', 'age', 'gender', 'birthday', 'schooling', 'ethnicity', 'region', 'period', 'social_welfare']])


def TEXT(key: str, id=''):
    return html.P(
        children=lang(key),
        className='default-typography',
        id=id
    )
