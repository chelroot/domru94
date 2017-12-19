
int ledPin0 = 0;
int ledPin1 = 1;
int ledPin2 = 2;
int ledPin3 = 3;
int ledPin4 = 4;
int ledPin5 = 5;
int ledPin6 = 6;
int ledPin7 = 7;
int ledPin8 = 8;
int ledPin9 = 9;
int ledPin10 = 10;
int ledPin11 = 11;
int ledPin12 = 12;
int ledPin13 = 13;

int incomingByte;

void setup() {
    Serial.begin(115200);
    pinMode(ledPin0, OUTPUT);
    pinMode(ledPin1, OUTPUT);
    pinMode(ledPin2, OUTPUT);
    pinMode(ledPin3, OUTPUT);
    pinMode(ledPin4, OUTPUT);
    pinMode(ledPin5, OUTPUT);
    pinMode(ledPin6, OUTPUT);
    pinMode(ledPin7, OUTPUT);
    pinMode(ledPin8, OUTPUT);
    pinMode(ledPin9, OUTPUT);
    pinMode(ledPin10, OUTPUT);
    pinMode(ledPin11, OUTPUT);
    pinMode(ledPin12, OUTPUT);
    pinMode(ledPin13, OUTPUT);
  }
void loop() {
  if (Serial.available() > 0) {
    incomingByte = Serial.read();
    if (incomingByte == 'q') {digitalWrite(0, HIGH);} 
    if (incomingByte == 'Q') {digitalWrite(0, LOW);}
    if (incomingByte == 'w') {digitalWrite(1, HIGH);} 
    if (incomingByte == 'W') {digitalWrite(1, LOW);}
    if (incomingByte == 'e') {digitalWrite(2, HIGH);} 
    if (incomingByte == 'E') {digitalWrite(2, LOW);}
    if (incomingByte == 'r') {digitalWrite(3, HIGH);} 
    if (incomingByte == 'R') {digitalWrite(3, LOW);}
    if (incomingByte == 't') {digitalWrite(4, HIGH);} 
    if (incomingByte == 'T') {digitalWrite(4, LOW);}
    if (incomingByte == 'y') {digitalWrite(5, HIGH);} 
    if (incomingByte == 'Y') {digitalWrite(5, LOW);}
    if (incomingByte == 'u') {digitalWrite(6, HIGH);} 
    if (incomingByte == 'U') {digitalWrite(6, LOW);}
    if (incomingByte == 'i') {digitalWrite(7, HIGH);} 
    if (incomingByte == 'I') {digitalWrite(7, LOW);}
    if (incomingByte == 'o') {digitalWrite(8, HIGH);} 
    if (incomingByte == 'O') {digitalWrite(8, LOW);}
    if (incomingByte == 'p') {digitalWrite(9, HIGH);} 
    if (incomingByte == 'P') {digitalWrite(9, LOW);}
    if (incomingByte == 'a') {digitalWrite(10, HIGH);} 
    if (incomingByte == 'A') {digitalWrite(10, LOW);}
    if (incomingByte == 's') {digitalWrite(11, HIGH);} 
    if (incomingByte == 'S') {digitalWrite(11, LOW);}
    if (incomingByte == 'd') {digitalWrite(12, HIGH);} 
    if (incomingByte == 'D') {digitalWrite(12, LOW);}
    if (incomingByte == 'f') {digitalWrite(13, HIGH);} 
    if (incomingByte == 'F') {digitalWrite(13, LOW);}
    
   }
} 
