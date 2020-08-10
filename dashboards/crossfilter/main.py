import pandas as pd

# from bokeh import resources
from bokeh.layouts import column, row
from bokeh.models import Select
from bokeh.palettes import Category10_10 as PALETTE
from bokeh.plotting import curdoc, figure
from bokeh.sampledata.autompg import autompg_clean as DATA
from bokeh_charts import box_plot, bubble_chart

DATA = DATA.copy()

SIZES = list(range(6, 22, 3))
N_SIZES = len(SIZES)
N_COLORS = len(PALETTE)

# data cleanup
DATA.cyl = DATA.cyl.astype(str)
DATA.yr = DATA.yr.astype(str)
del DATA['name']

columns = sorted(DATA.columns)
cat_cols = [x for x in columns if DATA[x].dtype == object]
num_cols = [x for x in columns if x not in cat_cols]


def create_figure():
    xs = DATA[x.value].values
    ys = DATA[y.value].values
    x_title = x.value.title()
    y_title = y.value.title()

    p_kwargs = {
        'plot_width': 800,
        'plot_height': 600,
        # 'tools': 'pan,box_zoom,reset',
    }

    if x.value in cat_cols and y.value in cat_cols:
        p = bubble_chart(DATA, x.value, y.value, **p_kwargs)

    elif x.value in cat_cols or y.value in cat_cols:
        p = box_plot(DATA, x.value, y.value, **p_kwargs)

    else:
        p = figure(x_axis_label=x_title, y_axis_label=y_title, **p_kwargs)
        sz = 9
        if size.value != 'None':
            if len(set(DATA[size.value])) > N_SIZES:
                groups = pd.qcut(DATA[size.value].values, N_SIZES,
                                 duplicates='drop')
            else:
                groups = pd.Categorical(DATA[size.value])
            sz = [SIZES[xx] for xx in groups.codes]

        c = PALETTE[0]
        if color.value != 'None':
            if len(set(DATA[color.value])) > N_COLORS:
                groups = pd.qcut(DATA[color.value].values, N_COLORS,
                                 duplicates='drop')
            else:
                groups = pd.Categorical(DATA[color.value])
            c = [PALETTE[xx] for xx in groups.codes]

        p.circle(x=xs, y=ys, color=c, size=sz, line_color="white", alpha=0.6,
                 hover_color='white', hover_alpha=0.5)
    return p


def update(attr, old, new):
    layout.children[1] = create_figure()


x = Select(title='X-Axis', value='mpg', options=columns)
x.on_change('value', update)

y = Select(title='Y-Axis', value='hp', options=columns)
y.on_change('value', update)

size = Select(title='Size', value='None', options=['None'] + num_cols)
size.on_change('value', update)

color = Select(title='Color', value='None', options=['None'] + num_cols)
color.on_change('value', update)

controls = column(x, y, color, size, width=200)
layout = row(controls, create_figure())

curdoc().add_root(layout)
curdoc().title = "Crossfilter"
