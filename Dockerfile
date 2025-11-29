FROM jupyter/minimal-notebook:x86_64-python-3.11.6

COPY . /home/jovyan/work
WORKDIR /home/jovyan/work

RUN mamba env update -n base -f environment.yml

CMD ["start-notebook.py", "--NotebookApp.notebook_dir=/home/jovyan/work/", "--NotebookApp.default_url=/lab/tree/analysis"]
