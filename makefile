install:
	poetry install
	poetry run pre-commit install

run:
	poetry run streamlit run app.py

test:
	poetry run pytest

data:
	mkdir data
	poetry run kaggle datasets download -d onurgitmez/pokemon-stats-gen-1-9
	unzip pokemon-stats-gen-1-9.zip -d data
	rm pokemon-stats-gen-1-9.zip
