// testing neopixel led strip on breadboard to flash origin and destinatiom files from opponent's move
// strip has 8 LEDs so each one represents a file on the chess board
// hall effect stuff is still included here as c/p from my other test script, but not used here

#include <Adafruit_NeoPixel.h>

// define arduino pins for led strip/hall sensors
#define HALL_PIN 2
#define LED_PIN 6
#define NUM_LEDS 8

Adafruit_NeoPixel strip(NUM_LEDS, LED_PIN, NEO_GRB + NEO_KHZ800);

void setup() {
  // put your setup code here, to run once:

  // set arduino input D2 pin for reading 
  // D2 connected to output of hall effect on breadboard
  pinMode(HALL_PIN, INPUT);
  //start serial comms at 9600 baud speed
  Serial.begin(9600);
  // set brightness at 10/255
  strip.setBrightness(10);
  // initialise led strip - begin/show = leds start off
  strip.begin();
  strip.show();
}

void loop() {
  if (Serial.available()) {
    // read the incoming serial comms message from laptop/pi
    String msg = Serial.readStringUntil('\n');

    if (msg.startsWith("FLASH:")) {
      // extract LED index (e.g for move starting on file e: msg = FLASH:4, idx = 4)
      int idx = msg.substring(6).toInt();
      // flash
      flashLED(idx);
    }
    else if (msg.startsWith("SETTLE:")) {
      // extract LED index and set green 
      int idx = msg.substring(7).toInt();
      settleLED(idx);
    }

    else if (msg == "CHECK") {
      // flash all LEDs red 3 times
      for (int i = 0; i < 3; i++) {
        strip.fill(strip.Color(255, 0, 0));
        strip.show();
        delay(200);
        strip.clear();
        strip.show();
        delay(200);
      }
    }
  }
}

void flashLED(int idx) {
  // flash orange 3 times to show origin square file
  for (int i = 0; i < 3; i++) {
    strip.clear();
    strip.setPixelColor(idx, strip.Color(255, 95, 0));
    // flash here!
    strip.show();
    delay(200);
    strip.clear();
    strip.show();
    delay(200);
  }
}

void settleLED(int idx) {
  // set destination file LED to green and leave it on
  strip.clear();
  strip.setPixelColor(idx, strip.Color(0, 255, 0));
  strip.show();
}
