# Order Tracking Incremental Load Project

<!-- TABLE OF CONTENTS -->
## Table of Contents

* [Overview](#Overview)
* [Architecture diagram](#architecture-diagram)
* [Features](#Features)
* [Technologies Used](#Technologies-Used)
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
Data Flow:
 - Source Directory(GCP Bucket) - (dbfs:/FileStore/stage-zone): Contains incoming raw order updates in CSV format.
 - Delta Table (gcp_workspace.default.stage_table): Stores processed data from the source directory.
 - Target Table (gcp_workspace.default.target_table): Holds the final up-to-date order status records.
 - Archive Directory(GCP Bucket) (dbfs:/FileStore/archive/): Stores processed files for backup.
