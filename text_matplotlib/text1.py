from text_matplotlib.cartogram import *

x_data = np.random.normal(200, 20, 50000)
get_histogram(x_data, 15)


x_data = np.arange(-4, 4, 0.5)
y_data = np.sin(x_data)
get_line_graph(x_data, y_data, "x1", "y1", "line1")

x_data = np.arange(1, 20, 1)
y_data_0 = np.cos(x_data)
y_data_1 = np.sin(x_data)
get_double_line(x_data, y_data_0, y_data_1, "0", "1", "横轴", "纵轴")

get_curve(np.cos, 10)
