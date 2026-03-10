// testing hall effect sensor on breadboard

void setup() {
  // put your setup code here, to run once:

  // set arduino input D2 pin for reading 
  // D2 connected to output of hall effect on breadboard
  pinMode(2, INPUT);
  //start serial comms at 9600 baud speed
  Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:

  // read D2 pin - will be HIGH (1) or LOW (0)
  int val = digitalRead(2);

  // LOW when magnet is near:
  if (val == LOW) {
    Serial.println("MAGNET DETECTED");
  } else {
    Serial.println("no magnet");
  }

  // wait 100ms before looping again
  delay(200);

}
