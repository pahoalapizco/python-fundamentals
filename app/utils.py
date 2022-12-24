def get_population(country_dict):
  years_population = {
    key[0:4]: int(value)
    for (key, value) in country_dict if key[0:4].isdigit()
  }
  keys = years_population.keys()
  values = years_population.values()
  return keys, values


def get_world_percent(data):
  percent_dict = {country: percent for (country, percent) in data.items()}
  return percent_dict


def population_by_country(data, country, key_name):
  population = filter(lambda item: item[key_name].upper() == country.upper(),
                      data)
  return list(population)


def get_single_column(data, coumn_key, column_value):
  column_data = [{item[coumn_key]: item[column_value]} for item in data]
  return column_data


if __name__ == "__main__":
  data = [{
    'Rank': '172',
    'CCA3': 'ESH',
    'Country/Territory': 'Western Sahara',
    'Capital': 'El Aaiún',
    'Continent': 'Africa',
    '2022 Population': '575986',
    '2020 Population': '556048',
    '2015 Population': '491824',
    '2010 Population': '413296',
    '2000 Population': '270375',
    '1990 Population': '178529',
    '1980 Population': '116775',
    '1970 Population': '76371',
    'Area (km²)': '266000',
    'Density (per km²)': '2.1654',
    'Growth Rate': '1.0184',
    'World Population Percentage': '0.01'
  }, {
    'Rank': '46',
    'CCA3': 'YEM',
    'Country/Territory': 'Yemen',
    'Capital': 'Sanaa',
    'Continent': 'Asia',
    '2022 Population': '33696614',
    '2020 Population': '32284046',
    '2015 Population': '28516545',
    '2010 Population': '24743946',
    '2000 Population': '18628700',
    '1990 Population': '13375121',
    '1980 Population': '9204938',
    '1970 Population': '6843607',
    'Area (km²)': '527968',
    'Density (per km²)': '63.8232',
    'Growth Rate': '1.0217',
    'World Population Percentage': '0.42'
  }, {
    'Rank': '63',
    'CCA3': 'ZMB',
    'Country/Territory': 'Zambia',
    'Capital': 'Lusaka',
    'Continent': 'Africa',
    '2022 Population': '20017675',
    '2020 Population': '18927715',
    '2015 Population': '16248230',
    '2010 Population': '13792086',
    '2000 Population': '9891136',
    '1990 Population': '7686401',
    '1980 Population': '5720438',
    '1970 Population': '4281671',
    'Area (km²)': '752612',
    'Density (per km²)': '26.5976',
    'Growth Rate': '1.028',
    'World Population Percentage': '0.25'
  }, {
    'Rank': '74',
    'CCA3': 'ZWE',
    'Country/Territory': 'Zimbabwe',
    'Capital': 'Harare',
    'Continent': 'Africa',
    '2022 Population': '16320537',
    '2020 Population': '15669666',
    '2015 Population': '14154937',
    '2010 Population': '12839771',
    '2000 Population': '11834676',
    '1990 Population': '10113893',
    '1980 Population': '7049926',
    '1970 Population': '5202918',
    'Area (km²)': '390757',
    'Density (per km²)': '41.7665',
    'Growth Rate': '1.0204',
    'World Population Percentage': '0.2'
  }]
  result = get_single_column(data, "Country/Territory",
                               "World Population Percentage")
  print(result)
