void setup() {
  // put your setup code here, to run once:
  // set up at 9600 baud speed
  Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:
// Check if any data has arrived from the Pi
  if (Serial.available()) {
    // Read the incoming message up to a newline character
    String msg = Serial.readStringUntil('\n');
    
    // Echo it back to the Pi so we can confirm it was received
    Serial.println("Arduino received: " + msg);
  }
}
