//Classe
class bco {
    constructor(agencia, conta, tipo, saldo){
      this.agencia = agencia
      this.conta = conta
      this.tipo = tipo
      this.saldo = saldo
    }  
    get_agencia() {return this.agencia}
    get_conta(){return this.conta}
    get_tipo(){return this.tipo}
    get_saldo(){return this.saldo}
  
  
  //metodos
   versaldo () {
      console.log('Seu saldo atual é de:', this.saldo)
    }   
     deposito(valor) { 
      this.saldo += valor }
  
    saque(valor) {
      if (this.saldo >= valor) {this.
  saldo -= valor
      }
      else{
       console.log ('Transação não autorizada')
      }
    }
     nconta () {
      console.log('O número da sua conta é:', this.conta)
    }
  }
  
  //instanciando o objeto
  const banco = new bco(0001, 097000, 'poupança', 100)
  deposita100 = banco.deposito(100)
  console.log(banco.versaldo())
  saque50 = banco.saque(50)
  console.log(banco.versaldo())
  console.log(banco.nconta())
