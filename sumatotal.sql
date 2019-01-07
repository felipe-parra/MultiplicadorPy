--select fecha, sum(importe) as SumaTotal from operaciones where fecha like "%2019-01-07";
select fecha, sum(importe) as SumaTotal from operaciones where fecha like '2019-01-07%';