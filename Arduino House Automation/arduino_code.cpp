// variaveis que controlam as mudanças de estado
bool luz_ligada = false;
bool correio_vazio = true;
bool terra_seca = false;
bool sensor_luz = false;

// variavel de comunicação com o app
char bt_sinal; 
/*essa variavel vai de 1 a 7:
1 - ligar as luzes
2 - desligar as luzes
3 - deixar o sensor sontrolar as luzes
4 - avisar que a terra esta seca
5 - avisar que a terra esta molhada
6 - avisar que a caixa de correio esta vazia
7 - avisar que entrou algo na caixa de correio */

// inicializacao do sistema
void setup()
{
  Serial.begin(9600);

  pinMode(A0, INPUT); // sensor de luz
  pinMode(A1, INPUT); // sensor de umidade
  pinMode(A2, INPUT); // sensor de movimento
  
  pinMode(9, OUTPUT); // led 1
  pinMode(10, OUTPUT);// led 2
  pinMode(11, OUTPUT);// led 3
}

// looping do sistema 
void loop()
{
  delay(1000); // pausa o loop por 1 segundo
  
  // saida das informacoes no monitor serial para monitoramento 
  Serial.print("luz: ");
  Serial.println(analogRead(A0));
  Serial.print("umidade: ");
  Serial.println(analogRead(A1));
  Serial.print("movimento: ");
  Serial.println(analogRead(A2));
  Serial.println("");
  
  //leitura dos dados recebidos por bluetooth
  if(Serial.available()){
    bt_sinal = Serial.read();
  }
  
  switch(bt_sinal){
    
      case '1':
      luz_ligada = true;
      sensor_luz = false;
      break;
      
      case '2':
      luz_ligada = false;
      sensor_luz = false;
      break;
      
      case '3':
      sensor_luz = true;
      break;
    
      default:
      break;
  }
  
  // analisa luz do ambiente
  if (sensor_luz == true){
    if (analogRead(A0) > 512) {
      luz_ligada = false;
    }
    else {
      luz_ligada = true;
    }
  }
  
  // acende e apaga as luzes
  if (luz_ligada == true) {
    digitalWrite(9, HIGH);
    digitalWrite(10, HIGH);
    digitalWrite(11, HIGH);
  }
  else {
   	digitalWrite(9, LOW);
    digitalWrite(10, LOW);
    digitalWrite(11, LOW); 
  }
  
  //leitura do sensor de umidade
  if (analogRead(A1) > 512) {
    terra_seca = true;
  }
  else {
    terra_seca = false;
  }
  
  /*leitura do sensor de movimento
  if (analogRead(A2) > 512) {
    
  }
  else {
    
  }*/
}