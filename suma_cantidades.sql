select fecha,
sum(B_Mil) as Mil,
sum(B_Quinientos) as Quinientos,
sum(B_Doscientos) as Doscientos,
sum(B_Cien) as Cien,
sum(B_Cincuenta) as Cincuenta,
sum(B_Veinte) as Veinte
from operaciones
where fecha like "2019-01-07%";