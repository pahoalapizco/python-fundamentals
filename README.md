# Hello

This is a repository that contains all exercises from Platzi's course 
[Curso de Python: PIP y Entornos Virtuales](https://platzi.com/cursos/python-pip/)


## Game Project
**Game rules**
> Piedra gana a Tijeras <br>
> Papel gana a Piedra <br>
> Tijeras gana a Papel 

You must to win two rounds.
<br>
**How to start the game:**

```sh
python3 game/main.py
```

or 

```sh
cd game/
python3 main.py
```

## Population Charts Project
This project reads a .csv file with dataset of the world population.
[original sourse in kaggle](https://www.kaggle.com/datasets/iamsouravbanerjee/world-population-dataset)

Before run this poject, you have to create a virtual env.
```sh
cd app
python3 -m venv env
source env/bin/activate
pip3 install -r requirements.txt
```

**Run this project**
```sh
python3 app/main.py
```
or
```sh
cd app
python3 main.py
```

You have to chose a country name then you have to chose what chart you prefer to show the info.
```sh
Which country do you like to know its population? Mexico

Which chart do you prefer?
  [0] Pie Chart
  [1] Bar Chart
```

<br>

## Web Server
This project has two examples 
First of all, you need to create a virtual env and install dependencies. 

```sh
cd web-server
python3 -m venv env
source env/bin/activate
pip3 install -r requirements.txt
```


### **No.1:**

Sample of calling an API with library `requests`.
This short example call three endpoints
1. Get all categories
2. Get a single category by its id
3. Get all gategory's productos by category id


To run 1st example (on virtual env) follow these commands:
```sh
python3 web-server/main.py
```
or
```sh
cd web-server
python3 main.py
```
> This is te API I used for this example: https://fakeapi.platzi.com/doc


### **No.2:**
Little sample of an API created with libraries FastAPI and uvicorn
This example has three endpoints <br>
root endpint: `/`  returns an HTML template <br>

get a list of numbers: `/list` <br>
```json
[1, 2, 3, 4]
```

get a dictionary: `/dict` <br>
```json
{
  key 1: "Value 1",
  key 2: "Value 2",
  key 3: "Value 3"
}
```
To start this example run the following command
```sh
uvicorn web:app --reload
```