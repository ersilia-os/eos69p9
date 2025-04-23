FROM bentoml/model-server:0.11.0-py38
MAINTAINER ersilia

RUN pip install rdkit==2024.3.5
RUN pip install dgl==2.4.0 -f https://data.dgl.ai/wheels/torch-2.1/repo.html
RUN pip install dgllife==0.3.2
RUN pip install openpyxl==3.1.5
RUN pip install xgboost==1.3.3
RUN pip install pandas==2.0.3
RUN pip install joblib==1.4.2
RUN pip install packaging==25.0
RUN pip install pyyaml==6.0.2
RUN pip install pydantic==2.10.6

WORKDIR /repo
COPY . /repo
