import pyodbc


class PureSql:
    def __init__(self, connection_string: str):
        self.connection = pyodbc.connect(connection_string)

    def get_version_id(self, ticket_numbers, company_id):
        cursor = self.connection.cursor()
        tickets = ','.join([str(item) for item in ticket_numbers])
        get_version_id_sql = f'''select
                                    DTIV.id as version_id
                                from DbTripItemVersions DTIV
                                where CompanyId = {company_id}
                                and JSON_VALUE(DTIV.JsonData, '$.TicketNumber') in
                                (
                                    {tickets}                                 
                                )
                                '''

        cursor.execute(get_version_id_sql)
        row = [id[0] for id in cursor.fetchall()]
        print(row)
        return row

# ''
