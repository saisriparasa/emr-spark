emr-spark
=========

This project is to fire up EMR cluster with Spark

Dependency:

Need to export the AWS keys to bashrc

export AWS_ACCESS_KEY_ID=<access_id>
export AWS_SECRET_ACCESS_KEY=<access_key>

Python Script is used to load a file from S3 and run it.

./bin/spark path_to_script.py
