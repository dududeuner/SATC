Table cliente {
  id_cliente integer [primary key]
}

Table telefone {
  id_telefone integer [primary key]
  id_cliente integer [ref: > cliente.id_cliente]
}

Table carro {
  id_Carro integer [primary key]
  id_sinistro integer [ref: <> Sinistro.id_sinistro]
  id_apolice integer [ref: < Apolice.id_apolice]
}

Table Sinistro {
  id_sinistro integer [primary key]
  id_Condutor integer [ref: > Condutor.id_Condutor]
}

Table Apolice {
  id_apolice integer [primary key]
}

Table Condutor {
  id_Condutor integer [primary key]
}

//Ref: cliente.id_cliente < telefone.id_telefone // many-to-one

Ref: cliente.id_cliente <> Apolice.id_apolice

Ref: cliente.id_cliente <> carro.id_Carro