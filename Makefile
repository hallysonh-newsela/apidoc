CUR_DIR=$(shell pwd)
VENV=.env
BIN=$(CUR_DIR)/$(VENV)/Scripts/
FASTAPI=fastapi
BLACKSHEEP=blacksheep
FLASK=flask
NESTJS=nestjs

.PHONY: clean
clean:
	rm -rf $(VENV)
	find -iname "*.pyc" -delete

install: venv
	$(BIN)pip install --upgrade pip || 
	$(BIN)pip install -r requirements.txt

venv:
	test -d $(VENV) || python -m venv .env

freeze:
	$(BIN)pip freeze > requirements.txt

test:
	$(BIN)pytest $(FASTAPI)
	$(BIN)pytest $(BLACKSHEEP)
	$(BIN)pytest $(FLASK)
	cd $(NESTJS) && yarn test

# Run FastApi version
.PHONY: fastapi
fastapi:
	$(BIN)uvicorn --app-dir $(FASTAPI) --no-use-colors app.main:app --reload

# Run BlackSheep version
.PHONY: blacksheep
blacksheep:
	$(BIN)uvicorn --app-dir $(BLACKSHEEP) --no-use-colors app.main:app --reload

# Run Flask version
.PHONY: flask
flask:
	cd $(FLASK) && $(BIN)flask run -h 0.0.0.0 -p 8000 --reload

# Run NestJS version
.PHONY: nestjs
nestjs:
	cd $(NESTJS) && yarn start:dev
