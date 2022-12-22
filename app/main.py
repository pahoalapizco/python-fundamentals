import utils as mod
import read_csv as rcsv
import charts

menu = '''
  Which chart do you prefer?
  [0] Pie Chart
  [1] Bar Chart
'''

chart_types = ("pie", "bar")

def get_menu():
  while True:
    chart_type = input(menu)
    if not chart_type.isdigit():
      print(f"{chart_type} isn't include in the menu, please try again")
    elif int(chart_type) < 0 or int(chart_type) > 1:
      print(f"{chart_type} isn't include in the menu, please try again")
    else:
      return int(chart_type)


def chart_country_population(data):
  country_name = input("Which country do you like to know its population? ")
  country_data = mod.population_by_country(data, country_name,
                                           "Country/Territory")
  if len(country_data) == 0:
    print("Sorry!, there is no information for ", country_name)
    return

  labels, values = mod.get_population(country_data[0].items())
  option = get_menu()
  if chart_types[option] == "pie":
    charts.generate_pie_chart(labels, values, country_name)
  elif chart_types[option] == "bar":
    charts.generate_bar_chart(labels, values, country_name)


def run():
  data = rcsv.read_csv("./app/data.csv")
  chart_country_population(data)


if __name__ == "__main__":
  run()
