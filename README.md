# Enterprise ETL Pipeline & Data Warehouse Synchronizer

> A resilient, automated data engineering pipeline for extracting, validating, transforming, and synchronizing customer data from multiple third-party platforms into a centralized PostgreSQL data warehouse.

---

## Overview

The **Enterprise ETL Pipeline & Data Warehouse Synchronizer** is a production-oriented data engineering project designed to consolidate customer data from multiple third-party platforms into a unified and analytics-ready data model.

The system automates the complete **Extract → Transform → Load (ETL)** lifecycle while addressing common data integration challenges such as API pagination, rate limiting, transient failures, inconsistent data formats, duplicate records, and incremental synchronization.

### Primary Data Sources

- Salesforce
- Stripe

### Target Data Warehouse

- PostgreSQL

### Primary Objectives

- Automate customer data extraction
- Standardize data from multiple sources
- Validate data before loading
- Remove duplicate records
- Support incremental data synchronization
- Maintain a centralized PostgreSQL data warehouse
- Automate pipeline execution using Apache Airflow
- Provide reliable error handling and monitoring

---

## Architecture

The pipeline follows a modular ETL architecture in which each stage has a specific responsibility.

```text
Salesforce ──────┐
                 │
                 ▼
          Data Extraction
                 │
                 ▼
          Raw Data Storage
               AWS S3
                 │
                 ▼
       Data Cleaning & Transformation
                 │
                 ▼
          Data Validation
                 │
                 ▼
           Deduplication
                 │
                 ▼
       Incremental UPSERT
                 │
                 ▼
        PostgreSQL Warehouse
                 │
                 ▼
        Apache Airflow
        Orchestration


Stripe ──────────┘
Core Capabilities
API Data Extraction
Salesforce API integration
Stripe API integration
API authentication
Cursor-based pagination
Rate-limit handling
Automatic retry mechanisms
Raw API response capture
Data Transformation
Null and missing-value handling
Data type normalization
Date and time standardization
Currency standardization
Source-specific field mapping
Unified customer data model
Data Quality
Pydantic schema validation
Data type validation
Required-field validation
Duplicate detection
Invalid-record handling
Data consistency checks
Data Warehouse Synchronization
PostgreSQL integration
SQLAlchemy database access
Incremental loading
Insert and update operations
UPSERT operations
Duplicate prevention
Orchestration
Apache Airflow DAGs
Scheduled ETL execution
Task dependency management
Pipeline failure handling
Email notifications
Execution logging
Deployment
Docker containerization
Environment-based configuration
Automated testing
CI/CD integration
Technology Stack
Category	Technology
Programming Language	Python 3.11+
API Integration	Requests
Data Validation	Pydantic
Data Processing	Pandas, Polars
Retry Handling	Tenacity
Database Toolkit	SQLAlchemy
Data Warehouse	PostgreSQL
Object Storage	AWS S3
Workflow Orchestration	Apache Airflow
Testing	Pytest
Containerization	Docker
Version Control	Git & GitHub
Repository Structure
Enterprise_ETL_Project/
│
├── extract/
│   ├── api_client.py
│   ├── stripe.py
│   └── salesforce.py
│
├── transform/
│   ├── clean_data.py
│   ├── mapping.py
│   └── validation.py
│
├── load/
│   ├── database.py
│   ├── loader.py
│   └── models.py
│
├── airflow/
│   ├── etl_dag.py
│   └── alerts.py
│
├── tests/
├── logs/
├── data/
├── config/
├── docs/
│
├── main.py
├── README.md
├── requirements.txt
├── .gitignore
└── .env.example
Directory Responsibilities
Directory	Purpose
extract/	API clients and data extraction
transform/	Cleaning, mapping and validation
load/	PostgreSQL connection and data loading
airflow/	Airflow DAGs and alerting
tests/	Unit and integration tests
logs/	Pipeline execution logs
data/	Local development data
config/	Configuration files
docs/	Project documentation
ETL Workflow

The complete pipeline follows this sequence:

Third-Party APIs
       |
       v
   EXTRACTION
       |
       v
 Raw Data Storage
       |
       v
 Data Cleaning
       |
       v
 Transformation
       |
       v
 Field Mapping
       |
       v
 Data Validation
       |
       v
 Deduplication
       |
       v
 Incremental UPSERT
       |
       v
 PostgreSQL Warehouse
       |
       v
 Airflow Scheduling
       |
       v
 Monitoring & Alerts
Extract

Data is retrieved from Salesforce and Stripe through their APIs.

The extraction layer handles:

Authentication
Pagination
Rate limits
Network failures
Retry attempts
Raw data capture
Transform

The extracted records are cleaned and converted into a common internal format.

Transformation includes:

Null handling
Data type conversion
Date normalization
Currency normalization
Field mapping
Standardization
Validate

Records are validated against predefined schemas before they are loaded into the warehouse.

Load

Validated records are loaded into PostgreSQL using incremental synchronization and UPSERT operations.

Orchestrate

Apache Airflow coordinates the complete ETL workflow and controls task dependencies and scheduled execution.

Data Integration Strategy

Salesforce and Stripe may represent customer information differently.

The transformation layer converts source-specific records into a common internal customer schema.

Salesforce Record
       |
       v
Source Transformation
       |
       v
Unified Customer Schema
       ^
       |
Source Transformation
       ^
       |
Stripe Record

The unified schema provides a consistent representation of customer data for downstream analytics and reporting.

Reliability & Error Handling

The pipeline is designed to handle temporary failures and unreliable external services.

Retry Handling

Tenacity is used to retry operations that fail due to temporary network or service issues.

Rate Limiting

The extraction layer detects API rate limits and applies appropriate retry and backoff behavior.

Pagination

The extraction layer processes paginated API responses to ensure that all available records are retrieved.

Logging

Pipeline operations and failures are recorded through structured logging.

Failure Handling

Failures are captured and reported so that pipeline execution can be diagnosed without silently losing data.

Notifications

Email notifications are planned for important pipeline failures.

Data Warehouse Synchronization

The loading layer uses an incremental synchronization strategy.

The pipeline checks whether a record already exists before writing it to the warehouse.

Incoming Record
      |
      v
Record Exists?
   /       \
 NO         YES
 |           |
 v           v
INSERT      UPDATE
 |           |
 └─────┬─────┘
       |
       v
PostgreSQL
Benefits
Prevents duplicate records
Updates existing customer information
Supports incremental processing
Reduces unnecessary database writes
Maintains a consistent warehouse
Configuration

Sensitive credentials are managed using environment variables.

The project uses a .env file locally while .env is excluded from Git version control.

Required Configuration
STRIPE_API_KEY=
SALESFORCE_USERNAME=
SALESFORCE_PASSWORD=
DATABASE_URL=
AWS_ACCESS_KEY=
AWS_SECRET_KEY=

A sample configuration is provided in:

.env.example

Security: Real credentials must never be committed to GitHub.

Development Workflow

The project follows a collaborative Git workflow.

main
 |
 +-- feature/api-extraction
 |
 +-- feature/data-transformation
 |
 +-- feature/database-loading
 |
 +-- feature/airflow-automation
 |
 v
Pull Request
 |
 v
Code Review
 |
 v
Merge into main
Development Rules

Each team member must:

Work on their assigned branch
Make regular commits
Use meaningful commit messages
Push changes regularly
Create Pull Requests for completed work
Avoid modifying another member's assigned module
Resolve merge conflicts before final review
Team
Role	Responsibility	Team Member
Team Lead	Project setup, integration, testing, documentation and coordination	Mansa
Data Extraction Engineer	Salesforce, Stripe, pagination, retries and raw data extraction	Fayaz
Data Transformation Engineer	Cleaning, mapping, validation and unified schema	Sunny
Data Warehouse Engineer	PostgreSQL, SQLAlchemy, models, loading and UPSERT	Hariprasad
Orchestration Engineer	Airflow, scheduling, alerts and monitoring	Baswaraj
Four-Week Development Plan
Week 1 — API Integration & Data Extraction
Define Pydantic models
Configure environment variables
Implement common API client functionality
Integrate Salesforce
Integrate Stripe
Implement pagination
Implement rate-limit handling
Implement retry mechanisms
Store raw extracted data

Deliverable: A working extraction layer capable of retrieving data from Salesforce and Stripe.

Week 2 — Data Transformation & Validation
Clean raw records
Handle null values
Standardize dates
Standardize currency fields
Map source-specific fields
Create unified customer schema
Validate records
Detect duplicates
Write transformation tests

Deliverable: Validated and standardized customer records ready for database loading.

Week 3 — Data Loading & Database Synchronization
Configure PostgreSQL
Configure SQLAlchemy
Create database models
Create database connection layer
Implement data loading
Implement incremental loading
Implement UPSERT operations
Prevent duplicate records
Test the complete ETL process

Deliverable: A working ETL pipeline that loads validated data into PostgreSQL.

Week 4 — Orchestration, Monitoring & Deployment
Create Apache Airflow DAG
Configure task dependencies
Schedule pipeline execution
Implement failure handling
Implement email alerts
Improve logging
Create Docker configuration
Configure CI/CD
Perform end-to-end testing
Complete documentation

Deliverable: An automated and containerized ETL pipeline with scheduling, monitoring, testing and deployment support.

Testing

The project uses Pytest for automated testing.

Testing Areas
Extraction Tests
API responses
Pagination
Retry behavior
Rate-limit handling
Transformation Tests
Null handling
Data type conversion
Field mapping
Date formatting
Currency formatting
Validation Tests
Required fields
Invalid values
Incorrect data types
Schema validation
Database Tests
Record insertion
Record updates
UPSERT behavior
Duplicate prevention
Integration Tests

The complete pipeline will be tested from extraction through database loading.

Run Tests
pytest
Security Practices

The project follows secure configuration and credential management practices.

Credentials

API keys, passwords, database credentials and AWS credentials are stored through environment variables.

Git Security

The following sensitive files are excluded from Git:

.env
venv/
__pycache__/
*.pyc
logs/
Important

Never commit:

API keys
Passwords
AWS secret keys
Database credentials
Personal access tokens
