[![CI](https://github.com/nogibjj/python-ruff-template/actions/workflows/cicd.yml/badge.svg)](https://github.com/nogibjj/python-ruff-template/actions/workflows/cicd.yml)

## 706-Data-Engineering-Template

This is a repo template for course 706_Data_Engineering Mini Project. It contains:

- ``.devcontainer`` including a Dockerfile and devcontainer.json
                The 'Dockerfile' within this folder specifies how the container should be built, and other settings in this directory may control development environment configurations.

- ``workflows`` including GitHub Actions, which contain configuration files for setting up automated build, test and deployment pipelines for your project.

- ``.gitignore`` this file is used to specify which files or directories should be excluded from vrsion control when using Git.

- ``Makefile`` a makefile is a configuration file used in Unix-based systems for autmating tasks and building software. It contains instructions and dependencies for compiling code, running tests, and other development tasks.

- ``README.md`` is the instrcation file for the readers.

- ``main.py`` a python file.

- ``requirements.txt`` this file is to specify the dependencies (libraries and packages) required to run the project.

- ``test_main.py`` is a test file for main.py that can successfully run in IDEs.

I use Github Actions to run the Makefile as follows: `make install`, `make test`, `make format`, `make lint`.The following pictures show the pass results:

<!-- <img decoding="async" src="https://github.com/carrieli15/706-Data-Engineering-Template/issues/1#issue-1885098942" width="50%">

<img decoding="async" src="https://github.com/carrieli15/706-Data-Engineering-Template/issues/2#issue-1885099594" width="50%">

<img decoding="async" src="https://github.com/carrieli15/706-Data-Engineering-Template/issues/3#issue-1885100877" width="50%">

<img decoding="async" src="https://github.com/carrieli15/706-Data-Engineering-Template/issues/4#issue-1885101545" width="50%"> -->

![img](./img/1截屏2023-09-07%20上午12.22.54.png)

![img](./img/2截屏2023-09-07%20上午12.16.53.png)

![img](./img/3截屏2023-09-07%20上午12.22.26.png)

![img](./img/4截屏2023-09-07%20上午12.24.49.png)