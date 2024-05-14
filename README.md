![Inspiring Image](https://repository-images.githubusercontent.com/798930033/4c24d1e2-6d3f-4497-8566-b49f88ad35e1)

# TimeWarpForecast
Exploring the temporal realm: dive into the depths of time series forecasting with this repository. 
Experiment with various models, techniques, and datasets to predict future trends and unravel 
the mysteries hidden within sequential data.

# Setup
## Update PYTHONPATH
Add the current directory to the `PYTHONPATH` environment variables.
``` bash
export PYTHONPATH="$PYTHONPATH:/<absolute_path>/TimeWarpForecast"
```

## Justfile
> `just` is a handy way to save and run project-specific commands
> 
> The main benefit it to keep all configuration and scripts in one place.
> 
> It uses the `.env` file for ingesting variables.

You can install it by following the [Documentation](https://just.systems/man/en/chapter_4.html).
Afterwards, you can execute existing commands located in the `justfile`.

Type `just` to list all available commands.


## Poetry

> Python packaging and dependency management made easy

### Installation

[Reference Documentation](https://python-poetry.org/)

Run the following command from the terminal:
``` bash
curl -sSL https://install.python-poetry.org | python3 -
```

For **MacOS** with ZSH add the `.local/bin` to the `PATH` environment variable. Modify the `.zshrc` file with the following command:

``` bash
export PATH="$HOME/.local/bin:$PATH"
```

### Add Dependency
``` bash
# NOTE: Use '--group dev' to install in the 'dev' dependencies list
poetry add <library_name>

poetry add <library> --group dev

poetry add <libarry> --group <group_name>
```

### Install Dependencies
``` bash
# Install the dependencies listed in pyproject.toml [tool.poetry.dependencies]
poetry install

# Use the option '--without test,docs,dev' if you want to esclude the specified group from install
poetry install --without test,docs,dev
```
