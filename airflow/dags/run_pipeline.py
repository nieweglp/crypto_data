from airflow.operators.bash import BashOperator
from airflow.models import DAG
from airflow.utils.dates import days_ago


default_args = {
    "owner": "paul",
    "start_date": days_ago(2)
}

with DAG(
    dag_id="run_app", 
    default_args=default_args,
    description="This is first test dag",
    schedule_interval="@hourly"
) as dag:

    task = BashOperator(
        task_id="run_app",
        bash_command="echo hello"
    )
