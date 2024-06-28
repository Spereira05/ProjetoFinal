# Django Drive

## Dependencies ##

- [Poetry](https://python-poetry.org/docs/#installing-with-pipx)

## Getting Started ##

### Development ###

1. Install Dependencies and Make Migrations

```bash
make deploy
```

2. Run Server

```bash
make test
```

## Commands ##

```bash
deploy-migrate                 Run manage migrate
deploy-update                  DEPLOY - Runs poetry update
deploy                         DEPLOY - Prepares for deploy
test                           TEST - Runs server on 8000
```


