CUR_DIR=$(shell pwd)
VENV=.env
BIN=$(CUR_DIR)/$(VENV)/Scripts/
FASTAPI=fastapi
BLACKSHEEP=blacksheep

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

# Run FastApi version
.PHONY: fastapi
fastapi:
	$(BIN)uvicorn --app-dir $(FASTAPI) --no-use-colors app.main:app --reload

# Run BlackSheep version
.PHONY: blacksheep
blacksheep:
	$(BIN)uvicorn --app-dir $(BLACKSHEEP) --no-use-colors app.main:app --reload
