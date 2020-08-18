# CML basic use case

This repository contains a sample project using [CML](https://github.com/iterative/cml). When a pull request is made in this repository, the following will occur:
- GitLab will deploy a runner machine with a specified CML Docker environment
- The runner will execute a workflow to train a ML model (`python train.py`)
- A visual CML report about the model performance will be returned as a comment in the pull request

The key file enabling these actions is `.gitlab-ci.yml`.

## CI/CD variables
Please set the following CI/CD variable:

| Variable  | Description  | 
|---|---|
|  repo_token | A personal access token with api, read_repository and write_repository privileges.  |

⚠️ Variables should be masked but not protected.
# CML_Demo_Project 
