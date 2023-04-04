# RemoveCommission
автоматизация коротких задачи по удалению комисси из жд билетов по их номерам(все версии, ваучеры, счета, операции и тд)
покрытие дельты по питону(1 уровень)<br>

Для запуска:<br>
добавить в config.json подключение к бд в формате<br>   
"connectionStringSQLAlchemy" : "mssql+pyodbc://UserId:Pasword@IpDbAdres/DbName?driver=ODBC Driver 17 for SQL Server", <br>
"connectionStringPyodbc" : "Driver={ODBC Driver 17 for SQL Server};Server=ipadres;Database=bdName;UID=userId;PWD=pass;", <br>
в файл tickets.cvs поместить номера билетов через запятую
