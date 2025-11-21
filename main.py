name: learn-github-actions
run-name: ${{ github.actor }} is learning Github Actions 
on: [push]
jobs:
  build:
    runs-on: ubuntu-latest
    strategy:
      matrix:
        python-version: ["pypy3.10", "3.13", "3.13.5"]
    steps:
      - uses: actions/checkout@v5
      - name: Set up Python ${{ matrix.python-version }}
        uses: actions/setup-python@v5
        with:
          python-version: ${{ matrix.python-version }}
      - name: Display Python version 
        run: |
          echo "Content checking"
          ls -la
          echo "Checked successfully"
      - name: Run python file
        run: python main.py
