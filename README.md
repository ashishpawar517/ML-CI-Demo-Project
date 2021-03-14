# ML-CI-Demo 

> Machine Learning Continuous Integration using Github actions. 
[(Using CML Library)](https://github.com/iterative/cml)
<br>

[![📟](https://raw.githubusercontent.com/ahmadawais/stuff/master/images/git/install.png)](./../../)

## Install

Create a new file in `.github/workflows/cml.yml` with the following:

```yml
name: first_ML_workflow
on: [push]
jobs:
  run:
    runs-on: [ubuntu-latest]
    container: docker://dvcorg/cml-py3:latest
    steps:
      - uses: actions/checkout@v2
      - name: cml_run
        env:
          repo_token: ${{ secrets.GITHUB_TOKEN }}
        run: |
          # Your ML workflow goes here
          pip install -r requirements.txt
          python train.py
          # Write your CML report
          # cat results.txt >> report.md
          # cml-send-comment report.md
            cat metrics.txt >> report.md
          echo >> report.md
          cml-publish confusion_matrix.png --md --title 'confusion-matrix' >> report.md
          cml-send-comment report.md 

```

<br>

[![⚙️](https://raw.githubusercontent.com/ahmadawais/stuff/master/images/git/usage.png)](./../../)

## Usage

Now, whenever you commit/push onto GitHub master branch,This workflow will calculate model's accuracy and auto-generate confusion matrix as Commit comment.


<br>

<!-- [![📝](https://raw.githubusercontent.com/ahmadawais/stuff/master/images/git/log.png)](changelog.md) -->

<!-- ## Changelog

[❯ Read the changelog here →](changelog.md)

<br> -->

<!-- <small>**KEY**: `📦 NEW`, `👌 IMPROVE`, `🐛 FIX`, `📖 DOC`, `🚀 RELEASE`, and `✅ TEST`

> _I use [Emoji-log](https://github.com/ahmadawais/Emoji-Log), you should try it and simplify your git commits._

</small> -->

<br>

[![📃](https://raw.githubusercontent.com/ahmadawais/stuff/master/images/git/license.png)](./../../)

## License & Conduct

- VJIT © [Aashish Pawar](https://github.com/pawarashish564)
<!-- - [Code of Conduct](code-of-conduct.md) -->

<br>

[![🙌](https://raw.githubusercontent.com/ahmadawais/stuff/master/images/git/connect.png)](./../../)

## Connect

<div align="left">
    <p><a href="https://github.com/pawarashish564"><img  align="center" src="https://img.shields.io/badge/GITHUB-gray.svg?colorB=6cc644&colorA=6cc644&style=flat" /></a>&nbsp;<small><strong>(follow)</strong> To stay up to date on with my free & open-source software contribution.</small></p>
    <p><a href="https://twitter.com/aashishpawar9/"><img alt="Twitter @MrAhmadAwais" align="center" src="https://img.shields.io/badge/TWITTER-gray.svg?colorB=1da1f2&colorA=1da1f2&style=flat" /></a>&nbsp;
    <small><strong>(follow)</strong> 
    To get latest of ALL Tech news & Events.
    </small></p>
    
</div>
