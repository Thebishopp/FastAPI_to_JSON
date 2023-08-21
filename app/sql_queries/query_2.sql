SELECT
CenterID, Date, First_Name, Last_Name 
FROM 
table_2

where cast(Date as date)  between :FechaInicio and :FechaFin
and CENTERID in (:CenterID)