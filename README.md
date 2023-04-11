# Predictive Clinical Trial Matching System is a system built and designed to utilize emerging LLM technlogies to help connect participants to trials.


# Postgres Database

A Postgres database is included with default credentials (user: postgres, password: postgres) for convenience in local development environments. However, **these default credentials should never be used in production**, as they pose a major security risk.

For any production deployment, be sure to configure environment variables with secure Postgres credentials:

```bash
POSTGRES_USER=<secure_username> 
POSTGRES_PASSWORD=<secure_password>
Then update the POSTGRES_USER and POSTGRES_PASSWORD environment variables in the docker-compose.yml file to use these credentials instead of the defaults.

Failure to properly configure secure Postgres credentials in a production environment could result in data theft or loss. Use the defaults only for local setup, with the understanding that your database has full admin access. For production, environment variables with limited-privilege credentials are highly recommended for security best practices.
