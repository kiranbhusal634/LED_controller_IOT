int ledPin = 12;
String command;

void setup() {
  pinMode(ledPin, OUTPUT);
  Serial.begin(9600);
}

void loop() {
  if (Serial.available()) {
    command = Serial.readStringUntil('\n');
    command.trim();

    if (command == "on") {
      digitalWrite(ledPin, HIGH);
    } 
    else if (command == "off") {
      digitalWrite(ledPin, LOW);
    }
  }
}
