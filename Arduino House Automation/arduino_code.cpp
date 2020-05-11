#include "SoftwareSerial.h"

// variaveis que controlam as mudanças de estado
bool luz_ligada = false;
bool correio_vazio = true;
bool terra_seca = false;
bool sensor_luz = false;

SoftwareSerial bluetooth(2, 3); //TX, RX (Bluetooth)

// variaveis de comunicação com o app
int sinal_ard; // sinal enviado pelo arduino
int sinal_app; // sinal enviado pelo app

// inicializacao do sistema
void setup()
{
  //Serial.begin(9600);
  bluetooth.begin(9600);// inicia o software serial
  
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
  if (bluetooth.available() > 0) {
    
    sinal_app = bluetooth.read();// lê o sinal mais antigo recebido
  
    switch(sinal_app){
      
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