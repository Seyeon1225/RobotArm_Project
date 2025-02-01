#include <SCServo.h>

SMS_STS sts;

void setup() {
  Serial.begin(1000000);
  sts.pSerial = &Serial;
  delay(500);
}

void loop() {
  if (Serial.available() > 0) {
    String input = Serial.readStringUntil('\n');
    int angle;

    angle = input.toInt();

    if (angle >= 0 && angle <= 4095) {
      sts.RegWritePosEx(1, angle, 500, 0);
      delay(1000);
      sts.RegWriteAction();
      delay(1000);
    }
  }

  Serial.flush();
  delay(100);
}
