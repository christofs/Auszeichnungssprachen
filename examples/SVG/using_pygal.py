import pygal

data = [("IE",19.5), ("Firefox", 36.6), ('Chrome', 36.3), ('Safari', 4.5), ("Opera", 2.3)]

chart = pygal.HorizontalBar()
chart.title = 'Browser usage in February 2012 (in %)'
for item in data: 
    chart.add(item[0], item[1])
chart.render_to_file("barchart.svg")
