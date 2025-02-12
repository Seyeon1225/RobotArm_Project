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
    int servoID, angle;

    int commaIndex = input.indexOf(',');
    if (commaIndex != -1) {
      servoID = input.substring(0, commaIndex).toInt();
      angle = input.substring(commaIndex + 1).toInt();

      sts.RegWritePosEx(servoID, angle, 500, 0);
      delay(500);
      sts.RegWriteAction();
    }
  }

  Serial.flush();
  delay(1000);
}
