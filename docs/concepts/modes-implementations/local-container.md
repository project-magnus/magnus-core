# Local Container

Local container is an interactive mode. In this mode, the traversal of the dag is done on the
local computer but the
actual execution happens on a container (running on local machine). This mode should enable you to test
the pipeline and execution of your code in containers. This mode could also be useful in
debugging a container based cloud run.

In this mode, max run time is completely ignored.

Apart from Buffered Run Log store, all other run log stores are compatible.
All secrets and catalog providers are compatible with this mode.

!!! Note
    Magnus does not build the docker image for you but uses a docker image provided.

## Configuration

The full configuration of this mode is:

```yaml
mode:
  type: local-container
  config:
    enable_parallel:
    docker_image:
```

### Enabling parallel

By default, none of the branches in parallel or a map node are executed parallelly.
You can enable it by setting enable_parallel to 'true' (case-insensitive).


!!! Note
    Please note that 'enable_parallel' needs a string 'true' and not a boolean true.


### Docker image

The ```docker_image``` to run the individual nodes of the graph.

!!! Requirements
    The docker image should have magnus installed in it and available as CMD.
    <br>
    The docker image should also its working directory as your project root.
    <br>
    Please use python3.7 or higher.


An example docker image to start with:

```dockerfile
# Python 3.7 Image without Dependencies
FROM python:3.7

LABEL maintainer=<Your Name here>

# If you want git versioning ability
RUN apt-get update && apt-get install -y --no-install-recommends \
    git \
    && rm -rf /var/lib/apt/lists/*

RUN pip install poetry

ENV VIRTUAL_ENV=/opt/venv
RUN python -m virtualenv --python=/usr/local/bin/python $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

COPY . /app
WORKDIR /app

RUN poetry install
```

### Node over-rides

The docker image provided at ```mode``` can be over-ridden by individual nodes of the graph by providing a
```mode_config``` as part of the definition.

For example:

```yaml
run_log:
  type: file-system

mode:
  type: local-container
  config:
    docker_image: project_default

dag:
  description: Getting started
  start_at: step1
  steps:
    step1:
      type: as-is
      mode_config:
        docker_image: step1_image
      command: my_function_does_all.func
      next: step2
    step2:
      type: as-is
      next: step3
    step3:
      type: success
    step4:
      type: fail
```

In the above example, if we assume project_default and step1_image to be 2 different images that satisfy
the requirements, step1 would run in step1_image while the remaining nodes would run in project_default image.
