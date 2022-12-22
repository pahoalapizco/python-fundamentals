import matplotlib.pyplot as plt


def generate_bar_chart(labels, values, name = ""):
  chart_name = f"./app/imgs/{name.capitalize()}_bar_chart.png"
  fig, ax = plt.subplots()
  ax.bar(labels, values)
  plt.savefig(chart_name)
  print("Your bar chart has been created on ", chart_name)


def generate_pie_chart(labels, values, name = ""):
  chart_name = f"./app/imgs/{name.capitalize()}_pie_chart.png"
  fig, ax = plt.subplots()
  ax.pie(values, labels=labels)
  ax.axis('equal')
  plt.savefig(chart_name)
  print("Your bar chart has been created on ", chart_name)


if __name__ == "__main__":
  labes = ["a", "b", "c", "d"]
  values = [120, 200, 80, 152]

  generate_bar_chart(labes, values)
  # generate_pie_chart(labes, values)
