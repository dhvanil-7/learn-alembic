/opt/mssql/bin/sqlservr &
pid=$1

until /opt/mssql-tools/bin/sqlcmd -S localhost -U sa -P $MSSQL_SA_PASSWORD -d master -Q "SELECT 1";
do
    echo "Waiting..."
    sleep 5
done

/opt/mssql-tools/bin/sqlcmd -S localhost -U sa -P $MSSQL_SA_PASSWORD -Q "CREATE DATABASE $DB_DATABASE";

wait $pid