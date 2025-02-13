FROM postgres:latest
ENV POSTGRES_DB covid_data
ENV POSTGRES_USER user
ENV POSTGRES_PASSWORD password
COPY postgresql.conf /etc/postgresql/postgresql.conf
COPY pg_hba.conf /etc/postgresql/pg_hba.conf
EXPOSE 5432
