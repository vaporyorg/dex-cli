# dFusion CLI

![](docs/CLI-demo.gif)

## Setup

```bash
# Setup virtual env
python3 -m venv ENV
source ./ENV/bin/activate

# Install dependencies
pip install -r requirements.txt
```

## Basic commands

```bash
# help command
./dfusion --help
./dfusion

# Get trades
./dfusion trades

# Get first 5 trades
./dfusion trades --count 5 --skip 0

# Filter by trader
./dfusion trades --trader 0x7b2e78d4dfaaba045a167a70da285e30e8fca196
```

# Debug - Verbose

Verbose mode prints information that is useful for debugging, including the GraphQL query and the url for the endpoint and subgraph:

```
# Verbose mode (-v)
./dfusion trades -v
```

![](docs/CLI-verbose.png)

## Development

If you use Visual Studio code, make sure you install https://marketplace.visualstudio.com/items?itemName=ms-python.python plugin to auto-organize imports on save:

```
{
  "editor.codeActionsOnSave": {
    "source.organizeImports": true
  }
}
```

To organize the imports manually run:

```bash
isort -rc */**.py
```
