# Contributing

This outlines how to propose a change to our project, adjusted from the [dplyr](https://github.com/tidyverse/dplyr/blob/main/.github/CONTRIBUTING.md) contributing guide.

## Prerequisites

Before you make a substantial pull request, you should always file an issue and make sure someone from the team agrees that it's a problem. If you've found a bug, create an associated issue and illustrate the bug with a minimal [reprex](https://tidyverse.org/help/#reprex).

The guide of set up a development environment is listed in the [README.md](https://github.com/yhouyang02/DSCI_522_project-group01/blob/main/README.md) file.

## Pull requests

* We recommend that you create a Git branch for each pull request (PR).
* New code should follow the [PEP 8](https://peps.python.org/pep-0008/) style guide.
* Environment update should be made when new dependencies are added. See [Adding a new dependency](#dep) section below.

## <a name="dep"></a> Adding a new dependency

The section is adjusted from <https://github.com/UBC-MDS/dsci-522-individual-assignment-quarto-python/blob/main/README.md>.

1. Add the dependency to the `environment.yml` file on a new branch.

2. Run `conda-lock -f environment.yml` to update the multi-platform `conda-lock.yml` file.

3. Re-build the Docker image locally to ensure it builds and runs properly.

4. Push the changes to GitHub. A new Docker
   image will be built and pushed to Docker Hub automatically.
   It will be tagged with the SHA for the commit that changed the file.

5. Update the `docker-compose.yml` file on your branch to use the new
   container image (make sure to update the tag specifically).

6. Send a pull request to merge the changes into the `main` branch.

## Code of Conduct

Please note that this project is released with a Contributor [Code of Conduct](https://github.com/yhouyang02/DSCI_522_project-group01/blob/main/CODE_OF_CONDUCT.md). By participating in this project you agree to abide by its terms.
