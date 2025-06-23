FROM python:3.10

RUN git clone https://github.com/SciCodes/somef-core

RUN curl -sSL https://install.python-poetry.org | python3 -

RUN pip install poetry-plugin-shell

WORKDIR "/somef-core"

RUN poetry install 

RUN poetry run somef_core configure -a

RUN echo 'source $(poetry env info --path)/bin/activate' >> ~/.bashrc


CMD ["bash", "--login"]

