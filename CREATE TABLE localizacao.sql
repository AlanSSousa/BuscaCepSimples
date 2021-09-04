create table localizacao (
id serial primary key, 
cep varchar(8), 
localidade varchar(100), 
uf varchar(2), 
ibge varchar(7), 
ddd varchar(2), 
siafi varchar(10)
)