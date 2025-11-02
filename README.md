# Covid19-DatabricksAndDataflow

This project demonstrates end-to-end data processing for COVID-19 data using Azure cloud services. This project showcases data engineering practices with Azure Databricks, Azure Data Factory, and Azure Data Lake Storage Gen2.

## Overview

This project processes COVID-19 datasets including cases, deaths, hospital admissions, testing data, and population demographics. The data flows through a modern data pipeline architecture:

1. **Raw Data** → Azure Data Lake Storage Gen2 (raw container)
2. **Processing** → Azure Databricks (PySpark transformations)
3. **Orchestration** → Azure Data Factory (pipeline orchestration)
4. **Data Flows** → Azure Data Factory Mapping Data Flows (transformations)
5. **Final Destination** → Azure SQL Database (for reporting and analysis)

## Project Structure

```
Covid19-DatabricksAndDataflow/
├── dataflow/                    # Azure Data Factory Mapping Data Flows
│   ├── CasesDeaths.json        # Data flow for cases and deaths processing
│   └── HospitalAdmission.json  # Data flow for hospital admission processing
├── dataset/                     # Azure Data Factory dataset definitions
│   ├── Cases_deaths.json
│   ├── hospital_admissions.json
│   ├── Country_lookup.json
│   ├── dim_date.json
│   └── ... (processed datasets)
├── factory/                     # Azure Data Factory configuration
│   └── aniket-covid-19-adf.json
├── linkedService/              # Linked service configurations
│   ├── AzureDatabricksCovid19.json
│   ├── AzureSqlDatabaseCovid19.json
│   ├── AzureKeyVault1.json
│   └── Covid19ADLSGen2.json
├── pipeline/                    # Azure Data Factory pipelines
│   ├── Covid-19.json           # Main processing pipeline
│   └── Load_Covid19_SQL.json   # Pipeline to load data into SQL Database
├── Mounting Storage.py          # Databricks notebook for mounting ADLS Gen2
├── testing.py                   # Databricks notebook for processing testing data
├── population.py                # Databricks notebook for processing population data
└── aniket-covid-19-adf/         # ARM templates for deployment
```

## Key Components

### Azure Databricks Notebooks

- **Mounting Storage.py**: Sets up mount points for Azure Data Lake Storage Gen2 containers (raw, processed, presentation)
- **testing.py**: Processes COVID-19 testing data, joins with country lookup and date dimensions
- **population.py**: Processes population demographics by age groups

### Azure Data Factory

- **Pipelines**: Orchestrate data processing workflows
  - `Covid-19.json`: Main pipeline executing data flows for cases/deaths and hospital admissions
  - `Load_Covid19_SQL.json`: Loads processed data into Azure SQL Database

- **Data Flows**: Transformations using Mapping Data Flows
  - `CasesDeaths`: Processes cases and deaths data with country lookups
  - `HospitalAdmission`: Processes hospital admission data

## Data Sources

The project processes the following COVID-19 datasets:
- Cases and Deaths
- Hospital Admissions
- Testing Data
- Population Demographics
- Country Lookup (dimension table)
- Date Dimension (dim_date)

## Azure Services Used

- **Azure Databricks**: Big data processing using PySpark
- **Azure Data Factory**: Data orchestration and ETL workflows
- **Azure Data Lake Storage Gen2**: Data lake storage (raw, processed, presentation layers)
- **Azure SQL Database**: Final destination for processed data
- **Azure Key Vault**: Secure credential management

## Learning Outcomes

This project demonstrates:
- Data lake architecture (raw → processed → presentation)
- PySpark transformations for data processing
- Azure Data Factory pipeline orchestration
- Mapping Data Flows for visual data transformations
- Integrating multiple Azure services
- Data warehouse loading patterns

## Prerequisites

- Azure subscription
- Azure Data Factory instance
- Azure Databricks workspace
- Azure Data Lake Storage Gen2 account
- Azure SQL Database
- Azure Key Vault (for secret management)

## Notes

This was created as a learning project to understand Azure data engineering services and best practices for building end-to-end data pipelines.
