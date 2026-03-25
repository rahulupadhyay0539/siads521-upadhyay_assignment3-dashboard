# Assignment 3: Interactive Dashboard for Vehicle Efficiency Analysis

# Imports in the model
import pandas as pd
import panel as pn
import hvplot.pandas
import seaborn as sns

pn.extension()

# this is my Load dataset
df = sns.load_dataset('mpg').dropna()

numeric_cols = df.select_dtypes(include='number').columns.tolist()
categorical_cols = df.select_dtypes(include='object').columns.tolist()

# Widgets in my tool
var_select = pn.widgets.Select(name='Variable', options=numeric_cols, value='mpg')
x_select = pn.widgets.Select(name='X Variable', options=numeric_cols, value='weight')
y_select = pn.widgets.Select(name='Y Variable', options=numeric_cols, value='mpg')
category_select = pn.widgets.Select(name='Category', options=categorical_cols, value='origin')

range_slider = pn.widgets.RangeSlider(
    name='Value Range',
    start=float(df['mpg'].min()),
    end=float(df['mpg'].max()),
    value=(float(df['mpg'].min()), float(df['mpg'].max()))
)


# Update the range slider whenever the selected variable changes
@pn.depends(var_select, watch=True)
def update_range_slider(var):
    range_slider.start = float(df[var].min())
    range_slider.end = float(df[var].max())
    range_slider.value = (float(df[var].min()), float(df[var].max()))


# Plots | Here each func has exactly one @pn.depends listing its reactive inputs
@pn.depends(var_select, range_slider)
def histogram(var, range_val):
    filtered = df[(df[var] >= range_val[0]) & (df[var] <= range_val[1])]
    return filtered.hvplot.hist(
        y=var,
        bins=20,
        xlabel=var.upper(),
        ylabel='Count',
        title=f'Distribution of {var.upper()}'
    )


@pn.depends(x_select, y_select, category_select)
def scatter(x, y, category):
    return df.hvplot.scatter(
        x=x, y=y, by=category,
        title=f'{y.upper()} vs {x.upper()} by {category.upper()}'
    )


@pn.depends(category_select, var_select)
def boxplot(category, var):
    return df.hvplot.box(
        y=var, by=category,
        title=f'{var.upper()} by {category.upper()}'
    )


@pn.depends(var_select)
def lineplot(var):
    grouped = df.groupby('model_year')[var].mean().reset_index()
    return grouped.hvplot.line(
        x='model_year', y=var,
        xlabel='Model Year',
        ylabel=f'Mean {var.upper()}',
        title=f'Mean {var.upper()} by Model Year'
    )


dashboard = pn.Column(
    pn.Row(var_select, x_select, y_select),
    pn.Row(category_select, range_slider),
    pn.Row(histogram, scatter),
    pn.Row(boxplot, lineplot)
)

dashboard.servable()
