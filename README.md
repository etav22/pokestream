# Pokestream
In between school semesters, I wanted to complete a fun, little project that I could put together to learn something new. This project was borne out of two thoughts:

1. Streamlit has been a popular topic in the python UI discussion for some time now and so I thought why not deepen my understanding of the package?
2. This [pokemon dataset](https://www.kaggle.com/datasets/onurgitmez/pokemon-stats-gen-1-9) on Kaggle looks awesome! I played a ton of pokemon as a kid and so I thought it would be fun to play around with the data.

## Setup
To run this application, you will first need to have [poetry](https://python-poetry.org/) installed. Once you have poetry installed, you can run the following command to install the dependencies for this project:
```bash
poetry install
```

As an optional point, I always like to have my virtual environment in the same directory as my project. To do this, you can run the following command:
```bash
poetry config virtualenvs.in-project true
```

Now, to run the application, you have two options. You can either run the application using the following command:
```bash
poetry run streamlit run app.py # OR
make run # if you have make installed
```

## Data
To donwnload the data, you can run the following command:
```bash
make data
```
This command will create a `data` directory and download the `PokemonStats.csv` file into that directory.

You will have to make sure that you have a kaggle API key setup on your machine. You can find instructions on how to do that [here](https://www.kaggle.com/docs/api)

## Docker
To run the application in a docker container, you can run the following command:
```bash
docker build -t pokestream .
```

Once the image is built, you can run the following command to start the container:
```bash
docker run -p 8501:8501 pokestream
```

## Testing
To run the tests, you can run the following command:
```bash
poetry run pytest # OR
make test # if you have make installed
```
