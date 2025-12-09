FROM quay.io/jupyter/minimal-notebook:afe30f0c9ad8

COPY conda-linux-64.lock /tmp/conda-linux-64.lock

USER root

RUN apt-get update && apt-get install -y --no-install-recommends \
    texlive-luatex \
    && rm -rf /var/lib/apt/lists/*

USER $NB_UID

RUN conda update --quiet --file /tmp/conda-linux-64.lock \
    && conda clean --all -y -f \
    && fix-permissions "${CONDA_DIR}" \
    && fix-permissions "/home/${NB_USER}"

RUN pip install --no-cache-dir deepchecks==0.18.1

COPY --chown=${NB_UID}:${NB_GID} . /home/jovyan/work
WORKDIR /home/jovyan/work
