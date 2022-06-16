FROM bentoml/model-server:0.11.0-py37
MAINTAINER ersilia

RUN pip install rdkit-pypi
RUN pip install scikit-learn==0.23.2
RUN pip install pandas==1.2.3
RUN pip install openpyxl==3.0.7
RUN pip install xgboost==1.3.3
RUN pip install joblib==1.0.1
RUN pip install torch==1.7.0
RUN pip install dgl==0.5.2

FROM conda/miniconda3
RUN conda install -c dglteam dgl=0.5.2
RUN conda install -c dglteam dgllife

WORKDIR /repo
COPY ./repo
