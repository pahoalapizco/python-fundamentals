import csv
import utils as u
# delimiter: la forma en que van separados los datos en el csv (delimitador)


def read_csv(path):
  with open(path, "r") as csvfile:
    reader = csv.reader(csvfile, delimiter=",")
    header = next(reader)
    data = []
    for row in reader:
      iterable = zip(header, row)
      dict = {key: val for (key, val) in iterable}
      data.append(dict)

  return data


if __name__ == "__main__":
  data = read_csv("data.csv")