from bokeh.plotting import figure, show

##  defines values on each axis
x = [1, 2, 3, 4, 5]
y = [7, 1, 10, 15, 5]

## Create a new graph plot with a title and axis labels 
plot = figure(title="An Example Line Graph", x_axis_label='X Axis', y_axis_label='Y axis')

#plots the line on the graph with a legend label
plot.line(x, y, legend_label="A Key Example.", line_width=5)

#shows the plot in the browser
show(plot)
