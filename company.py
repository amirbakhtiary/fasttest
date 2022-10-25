from exceptions import CompanyNotExistsError, CompanyWithSameNameExistError

company_list = ["google", "microsoft", "cluepoints"]

class Company:
    def create_company(self, name: str) -> str:
        if name in company_list:
            raise CompanyWithSameNameExistError()
        
        company_list.append(name)
        return name
    
    def get_company(self, name) -> str:
        if name not in company_list:
            raise CompanyNotExistsError()
        return name
