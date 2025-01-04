FROM python:3.8.12-buster

WORKDIR /prod

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY bank_loan_model_package_folder bank_loan_model_package_folder
COPY setup.py setup.py
RUN pip install .

COPY data data

COPY Makefile Makefile

CMD uvicorn bank_loan_model_package_folder.api:app --host 0.0.0.0 --port $PORT.api:app --host 0.0.0.0 --port $PORT
