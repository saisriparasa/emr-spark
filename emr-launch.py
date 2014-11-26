#! /usr/bin/python
import boto.emr
from boto.emr.bootstrap_action import BootstrapAction
from boto.emr.step import InstallHiveStep
import time

spark_bootstrap = BootstrapAction("Install Spark", "s3://support.elasticmapreduce/spark/install-spark", "")
ganglia_bootstrap = BootstrapAction("Install Ganglia","s3://elasticmapreduce/bootstrap-actions/install-ganglia", "") 
hive_install = InstallHiveStep()

conn = boto.emr.connect_to_region('us-west-2')

job_id = conn.run_jobflow(
	name="Spark/Hive/Ganglia",
	log_uri="s3://aws-sai-sriparasa/logs/hive",
	ec2_keyname="sriparas",
	master_instance_type="m3.xlarge",
	slave_instance_type="m1.large",
	num_instances=3,
	keep_alive=True,
	enable_debugging=True,
	ami_version="3.3.1",
	steps=[hive_install],
	bootstrap_actions=[spark_bootstrap, ganglia_bootstrap]
)

while True:
	time.sleep(0.1)
	print conn.describe_jobflow(job_id).state


