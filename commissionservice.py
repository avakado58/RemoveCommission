class CommissionService:
    def __init__(self, repository):
        self.repository = repository

    def remove_ticket_commission(self, ticket_number):
        id = self.repository.get_version_id(ticket_number)
        return id

