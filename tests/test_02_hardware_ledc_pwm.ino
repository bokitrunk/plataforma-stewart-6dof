// Pines de salida PWM por Hardware
const int pwmPin1 = 4;   // Pin D4 (Conectado a la sonda del osciloscopio)
const int pwmPin2 = 18;  // Pin D18 (Para probar segundo canal)

const int freq = 50;        // 50 Hz (frecuencia estándar para servos)
const int resolution = 16;  // Resolución de 16 bits (0 a 65535)

void setup() {
  Serial.begin(115200);

  // Configurar periférico de Hardware (LEDC)
  // Nota: Sintaxis para versiones v3.x del core ESP32
  ledcAttachChannel(pwmPin1, freq, resolution, 0); // Canal 0 en D4
  ledcAttachChannel(pwmPin2, freq, resolution, 1); // Canal 1 en D18

  // Fijar ancho de pulso a ~1.5 ms (Posición central del servo)
  // Cálculo: (1.5 ms / 20 ms) * 65535 ≈ 4915
  ledcWrite(pwmPin1, 4915);
  ledcWrite(pwmPin2, 4915);

  Serial.println("PWM por Hardware listo a 50Hz.");
}

void loop() {
  // El loop queda vacío: el hardware mantiene la señal de forma autónoma
}