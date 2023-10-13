AIRFLOW_VERSION=2.5.3

PYTHON_VERSION="3.10"

CONSTRAINT_URL="https://raw.githubusercontent.com/apache/airflow/constraints-${AIRFLOW_VERSION}/constraints-${PYTHON_VERSION}.txt"

pip install pandas
pip install awswrangler
pip install "apache-airflow==${AIRFLOW_VERSION}" --constraint "${CONSTRAINT_URL}"
pip install apache-airflow-providers-cncf-kubernetes
pip install apache-airflow-providers-postgres
pip install apache-airflow-providers-amazon
pip install apache-airflow-providers-slack
pip install mlflow

# Initialize the database
airflow db init

# The path to dags in this directory to $AIRFLOW_HOME/airflow.cfg
sed -i '' 's#dags_folder =.*#dags_folder = '"$PWD/dags"'#g' "$AIRFLOW_HOME"/airflow.cfg

airflow users create \                                                                                       ─╯
  --username "admin" \
  --firstname "uiseop" \
  --lastname "eom" \
  --role "Admin" \
  --email "aesop@zaikorea.org"

# Then run
# airflow webserver --port 8080
# airflow scheduler
