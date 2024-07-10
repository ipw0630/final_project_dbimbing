from datetime import timedelta
from airflow import DAG
from airflow.providers.apache.spark.operators.spark_submit import SparkSubmitOperator
from airflow.utils.dates import days_ago

default_args = {
    "owner": "dibimbing",
    "retries": 3,
    "retry_delay": timedelta(minutes=5),
    "start_date": days_ago(1),
}

with DAG(
    dag_id="spark_pet_adoption_etl",
    default_args=default_args,
    schedule_interval=None,
    dagrun_timeout=timedelta(minutes=60),
    description="ETL process for pet adoption data using Spark",
    catchup=False,
) as dag:

    extract_transform_load = SparkSubmitOperator(
        task_id="extract_transform_load",
        application="/opt/airflow/spark-scripts/pet-adoption.py",
        conn_id="spark_default",
        verbose=True,
        conf={
            "spark.driver.memory": "1g",
            "spark.executor.memory": "2g",
        },
    )

    extract_transform_load

if __name__ == "__main__":
    dag.cli()