# Order Tracking Incremental Load Project

<!-- TABLE OF CONTENTS -->
## Table of Contents

* [Overview](#Overview)
* [Architecture diagram](#architecture-diagram)
* [Features](#Features)
* [Technologies Used](#Technologies-Used)
* [Datasets and Source Code](#datasets-and-source-code)
* [Usage](#Usage)
* [Monitoring and Logging](#Monitoring-and-Logging)
* [Troubleshooting](#Troubleshooting)
* [Future Enhancements](#Future-Enhancements)
* [License](#license)
* [Contact](#contact)

<!-- Overview -->
## Overview
Developed and implemented an incremental data load pipeline for an order tracking system using Databricks and Delta Lake. The project involved processing order status updates and ensuring that the target table always reflected the most recent status for each order. Key statuses included "order placed," "shipped," "in transit," and "delivered."

<!-- ARCHITECTURE DIAGRAM -->
## Architecture diagram
### Data Flow:
 - Source Directory(GCP Bucket) - (dbfs:/FileStore/stage-zone): Contains incoming raw order updates in CSV format.
 - Delta Table (gcp_workspace.default.stage_table): Stores processed data from the source directory.
 - Target Table (gcp_workspace.default.target_table): Holds the final up-to-date order status records.
 - Archive Directory(GCP Bucket) (dbfs:/FileStore/archive/): Stores processed files for backup.

<!-- Features -->
## Features
 - Incremental Load: Efficiently updates only new or changed records.
 - Data Archiving: Moves processed files to an archive directory for auditing.
 - ACID Transactions: Uses Delta Lake to ensure data consistency.

<!-- Technologies Used -->
## Technologies Used
 - Databricks: For data processing and orchestration.
 - Delta Lake: For storage and incremental data updates.
 - PySpark: For ETL operations.

<!-- Datasets and Source Code -->
## Datasets and Source Code
 - The dataset files are located in the /datasets/ folder.
 - The code files are located in the /code/ folder.


<!-- Usage -->
## Usage
 - Upload order status CSV files to the source directory i.e., GCP bucket - (dbfs:/FileStore/stage-zone).
 - Run the notebook scripts sequentially:
    - Source to Delta Table Load section
    - Incremental Load to Target Table section
 - Verify the target table (gcp_workspace.default.target_table) for the latest order statuses.

<!-- Monitoring and Logging -->
## Monitoring and Logging
 - Use Databricks Job UI to monitor execution and view logs.
 - Track the movement of files in the archive directory (dbfs:/FileStore/archive/).
 - Check Delta Lake version history for any merge issues:
   ```sh
   spark.sql("DESCRIBE HISTORY delta.`gcp_workspace.default.target_table`").show()
   ```

<!-- Troubleshooting -->
## Troubleshooting
 - Table Not Found: Ensure the correct workspace, database, and table names are used in the script.
 - Permission Denied: Verify that your Databricks environment has access to the source and archive directories.
 - Merge Conflicts: Check merge condition and ensure that tracking_num is the unique identifier.


<!-- Future Enhancements -->
## Future Enhancements
 - Implement real-time streaming with Spark Structured Streaming for live updates.
 - Add data validation checks before loading data into Delta tables.
 - Integrate automated testing for ETL scripts using PyTest.

<!-- LICENSE -->
## License
Distributed under the MIT License. See [LICENSE](LICENSE) for more information.

<!-- CONTACT -->
## Contact
Please feel free to contact me if you have any questions.
[Prudhvi](https://www.linkedin.com/in/prudhvi-raju-vegeshna-a45606195/) 
