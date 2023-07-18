FROM bentoml/model-server:0.11.0-py37
MAINTAINER ersilia

RUN pip install rdkit==2022.9.5
RUN pip install dgl==0.5.2
RUN pip install dgllife==0.2.6
RUN pip install scikit-learn==0.23.2
RUN pip install pandas==1.2.3
RUN pip install openpyxl==3.0.7
RUN pip install xgboost==1.3.3
RUN pip install joblib==1.0.1
RUN pip install torch==1.7.1

WORKDIR /repo
COPY ./repo
