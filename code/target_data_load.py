from delta.tables import *

source_table= "gcp_workspace.default.stage_table"
target_table= "gcp_workspace.default.target_table"

# gcp_workspac3 --> databricks workspace name
# default is the database name
# stage_table --> it is the delta stage table name

stage_df = spark.read.table(source_table)
display(stage_df)

if not spark._jsparkSession.catalog().tableExists(target_table):
    stage_df.write.format("delta").saveAsTable(target_table)
else:
    target_table_obj = DeltaTable.forName(spark, target_table)

    merge_cond = "stage.tracking_num=target.tracking_num"

    target_table_obj.alias("target")\
      .merge(stage_df.alias("stage"), merge_cond)\
      .whenMatchedDelete()\
      .execute()

    stage_df.write.format("delta").mode("append").saveAsTable(target_table)
