#include <SCServo.h>

// SCSCL 객체 생성
SMS_STS sts;

void setup() {
  Serial.begin(1000000);
  sts.pSerial = &Serial;  
  delay(500);            
}

void loop() {
  if (Serial.available() > 0) {
    String input = Serial.readStringUntil('\n');
    
    int angle0, angle1, angle2, angle3, angle4, angle5;
    
    int comma1 = input.indexOf(',');
    int comma2 = input.indexOf(',', comma1 + 1);
    int comma3 = input.indexOf(',', comma2 + 1);
    int comma4 = input.indexOf(',', comma3 + 1);
    int comma5 = input.indexOf(',', comma4 + 1);
    
    if (comma1 != -1 && comma2 != -1 && comma3 != -1 && comma4 != -1 && comma5 != -1) {
      angle0 = input.substring(0, comma1).toInt();
      angle1 = input.substring(comma1 + 1, comma2).toInt();
      angle2 = input.substring(comma2 + 1, comma3).toInt();
      angle3 = input.substring(comma3 + 1, comma4).toInt();
      angle4 = input.substring(comma4 + 1, comma5).toInt();
      angle5 = input.substring(comma5 + 1).toInt();

      sts.RegWritePosEx(0, angle0, 500, 0);
      sts.RegWritePosEx(1, angle1, 500, 0);
      sts.RegWritePosEx(2, angle2, 500, 0);
      sts.RegWritePosEx(3, angle3, 500, 0);
      sts.RegWritePosEx(4, angle4, 500, 0);
      sts.RegWritePosEx(5, angle5, 500, 0);

      sts.RegWriteAction();
      delay(1000);
    }
  }

  Serial.flush();
  delay(100);
}
