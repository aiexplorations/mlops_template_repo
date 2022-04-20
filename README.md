# MLOps Template Repo 
This is a template for building ML applications of different kinds. It implements the basic elements of the repo required for 
1. Building a wheel file for distributing the repo as a library
2. Ensuring that code, trained models, datasets are separated out
3. Git LFS underpinnings for large trained models, datasets, etc are provided in the documentation in the respective subdirectories
4. Enables CI/CD pipelines to run based on a simple provided template.

The repo makes some assumptions about the build and development environment:
1. Python programming language is assumed by default
2. Default branch assumed to be `master`, not `main`
3. Pipelines set up based on simple and common workflows, with feature branches following from a base branch named `dev`


[![Python application](https://github.com/aiexplorations/mlops_template_repo/actions/workflows/python-app.yml/badge.svg?branch=master)](https://github.com/aiexplorations/mlops_template_repo/actions/workflows/python-app.yml)
