from typing import List

import pyodbc


class PureSql:
    def __init__(self, connection_string: str):
        self.connection = pyodbc.connect(connection_string)

    def get_version_id(self, ticket_numbers, company_id):
        tickets = ','.join([str(item) for item in ticket_numbers])
        query = f'''select
                                    DTIV.id as version_id
                                from DbTripItemVersions DTIV
                                where CompanyId = {company_id}
                                and JSON_VALUE(DTIV.JsonData, '$.TicketNumber') in ({tickets})
                                '''
        cursor = self.connection.cursor()
        cursor.execute(query)
        row = [id[0] for id in cursor.fetchall()]
        print(row)
        return row

    def get_payment_operation_id(self, version_id: List[int]):
        ids = ','.join([str(item) for item in version_id])
        query = f'''select distinct DPI.OperationId
                              from DbTripItemVersions DTIV
                              join DbOperationDetails DOD on DTIV.Id = DOD.TripItemVersionId
                              join DbOperations DO on DO.Id = DOD.OperationId
                              join DbPaymentInvoices DPI on DO.Id = DPI.OperationId
                              where DTIV.Id in ({ids})
                    '''
        cursor = self.connection.cursor()
        cursor.execute(query)
        row = [id[0] for id in cursor.fetchall()]
        print(row)
        return row
