# Databricks notebook source
source_dir = "dbfs:/FileStore/stage-zone"
target_dir= "dbfs:/FileStore/archive/"
delta_table= "gcp_workspace.default.stage_table"

# gcp_workspac3 --> databricks workspace name
# default is the database name
# stage_table --> it is the delta table name

df = spark.read.csv(source_dir, header=True, inferSchema=True)
display(df)

df.write.format("delta").mode("overwrite").saveAsTable(delta_table)

files=dbutils.fs.ls(source_dir)

for file in files:
  source_path = file.path
  target_path = target_dir + source_path.split("/")[-1]
  print(target_path)
  dbutils.fs.mv(source_path,target_path)



