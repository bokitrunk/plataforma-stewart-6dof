// Definición de pines y parámetros
const int pulsePin = 4;          // Pin GPIO de salida para el pulso (puedes cambiarlo, ej: GPIO 4 o 23)
const unsigned long interval = 2000; // Periodo entre pulsos en milisegundos (2 segundos)
const unsigned long pulseWidth = 10; // Ancho del pulso en milisegundos (duración en nivel HIGH)

unsigned long previousMillis = 0;

void setup() {
  Serial.begin(115200);
  pinMode(pulsePin, OUTPUT);
  digitalWrite(pulsePin, LOW);
  
  Serial.println("Generador de pulsos ESP32 iniciado.");
  Serial.println("Enviando un pulso cada 2 segundos...");
}

void loop() {
  unsigned long currentMillis = millis();

  // Comprueba si han pasado 2 segundos desde el último pulso
  if (currentMillis - previousMillis >= interval) {
    previousMillis = currentMillis;
    
    // Generar el pulso
    digitalWrite(pulsePin, HIGH);
    delay(pulseWidth);              // Mantener en alto durante el ancho del pulso (ej. 10 ms)
    digitalWrite(pulsePin, LOW);    // Volver a nivel bajo
    
    Serial.println("Pulso enviado al osciloscopio");
  }
}