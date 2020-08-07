import logging
import math
import pandas as pd
from bokeh import plotting
from bokeh.palettes import Category10_10 as PALETTE

logging.basicConfig(level=logging.INFO)
LOGGER = logging.getLogger(__name__)


def _setup_box_info(groups, num_col, cat_col):

    quant = {
        'qmin': 0.0,
        'q1': 0.25,
        'q2': 0.5,
        'q3': 0.75,
        'qmax': 1.0,
    }
    quant_data = [groups.quantile(q=quant[q]) for q in quant]
    box_info = pd.concat(quant_data, axis=1)
    box_info.columns = quant.keys()
    box_info['iqr'] = box_info.q3 - box_info.q1
    box_info['upper'] = box_info.q3 + 1.5 * box_info.iqr
    box_info['lower'] = box_info.q1 - 1.5 * box_info.iqr
    box_info['color'] = [PALETTE[i%len(PALETTE)] for i in range(len(box_info))]

    # find the outliers for each category
    def _check_outlier(group):
        cat = group.name
        mask_upper = (group[num_col] > box_info.loc[cat].upper)
        mask_lower = (group[num_col] < box_info.loc[cat].lower)
        return group[mask_upper | mask_lower]
    outliers = groups.apply(_check_outlier)
    outliers['color'] = box_info.color[outliers[cat_col]].values

    # if no outliers, shrink lengths of stems to be no longer than the minimums or maximums
    box_info.upper = box_info[['qmax', 'upper']].min(axis=1)
    box_info.lower = box_info[['qmin', 'lower']].max(axis=1)

    # box width proportional to group size
    group_count = groups.count()
    box_info['proportion'] = group_count / group_count.max()
    return box_info, outliers


def box_plot(data, x_col, y_col, **kwargs):
    columns = sorted(data.columns)
    cat_cols = [c for c in columns if data[c].dtype == object]
    x_cat = x_col in cat_cols
    y_cat = y_col in cat_cols
    if x_cat and y_cat:
        LOGGER.error(f'Neither {x_col} nor {y_col} are numeric.')
        return plotting.figure()
    elif x_cat:
        orient_v = True
        cat_col = x_col
        num_col = y_col
    elif y_cat:
        orient_v = False
        cat_col = y_col
        num_col = x_col
    else:
        LOGGER.error(f'Neither {x_col} nor {y_col} are categorical.')
        return plotting.figure()

    groups = data[[cat_col, num_col]].groupby(cat_col)
    box_info, outliers = _setup_box_info(groups, num_col, cat_col)

    cats = list(box_info.index)
    if orient_v:
        p = plotting.figure(x_axis_label=x_col, y_axis_label=y_col,
                            x_range=cats, **kwargs)
        p.xaxis.major_label_orientation = math.pi / 4
        p.xgrid.grid_line_color = None
        p.ygrid.grid_line_color = "lightgray"
        segments = [[cats, box_info.lower, cats, box_info.q1],
                    [cats, box_info.q3, cats, box_info.upper]]
        p.vbar(x=cats, width=box_info['proportion'].values,
               top=box_info.q2, bottom=box_info.q3,
               fill_color='white', line_color=box_info.color)
        p.vbar(x=cats, width=box_info['proportion'].values,
               top=box_info.q1, bottom=box_info.q2,
               fill_color='white', line_color=box_info.color)
        p.vbar(x=cats, width=box_info['proportion'].values,
               top=box_info.q2, bottom=box_info.q2,
               line_color='black')

    else:
        p = plotting.figure(x_axis_label=x_col, y_axis_label=y_col,
                            y_range=cats, **kwarg)
        p.xgrid.grid_line_color = "lightgray"
        p.ygrid.grid_line_color = None
        segments = [[box_info.lower, cats, box_info.q1, cats],
                    [box_info.q3, cats, box_info.upper, cats]]
        p.hbar(y=cats, height=box_info['proportion'].values,
               right=box_info.q3, left=box_info.q2,
               fill_color='white', line_color=box_info.color)
        p.hbar(y=cats, height=box_info['proportion'].values,
               right=box_info.q1, left=box_info.q2,
               fill_color='white', line_color=box_info.color)
        p.hbar(y=cats, height=box_info['proportion'].values,
               right=box_info.q2, left=box_info.q2,
               fill_color='black', line_color='black')

    for i in range(2):
        p.segment(*segments[i], line_width=1, line_color="black")
        if not outliers.empty:
            p.circle(outliers[cat_col], outliers[num_col], size=3,
            color=outliers.color, fill_alpha=0.6)

    return p
