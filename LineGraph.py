from bokeh.plotting import figure, show


x = [1, 2, 3, 4, 5]
y = [7, 1, 10, 15, 5]

## Create a new plot with a title and axis labels 

plot = figure(title="An Example Line Graph", x_axis_label='X Axis', y_axis_label='Y axis')

plot.line(x, y, legend_label="A Key Example.", line_width=5)

show(plot)
