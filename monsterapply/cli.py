

import click

from typing import List, TextIO
"""

Examples:

monsterapply --raw "Entry Python Developer" "Entry Java eveloper" --hours 4
monsterapply --raw "Senior Developer" "Senior Java Developer" --run-until 01/07/23 --hours 3
monsterapply -filer job_hopers.txt --run-until 01/07/23 --hours 2

Options:
  --file      FILE      Read names of jobs from file.
  --raw       TEXT[]    Names of jobs.
  --hours     INT       time you want to spend scraping
  --run-until DATE      run until this date
  --run-on    DATE      run on this date
  --location
  --help      NONE      Show this message and exit.


"""

@click.command()
@click.option('--file', 
              help='Input file for the bot to read form.', 
              type=click.Path(exists=True),
              nargs=1)

def file(file) -> List[TextIO]:
    if(file):
        files: List[TextIO] = []
        for job in file:
            print(job)

def raw():
    pass

def hours():
    pass

def run_until():
    pass

def run_at():
    pass
