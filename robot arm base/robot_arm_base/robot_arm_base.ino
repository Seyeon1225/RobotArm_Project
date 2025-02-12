#include <SCServo.h>

// SCSCL 객체 생성
SMS_STS sts;

void setup() {
  Serial.begin(1000000);  // 서보와 통신 (1Mbps)
  sts.pSerial = &Serial;  // Serial을 SCServo 객체에 할당
  delay(500);  // 통신 안정화 대기
}

void loop() {
  if (Serial.available() > 0) {
    // 시리얼 데이터 읽기
    String input = Serial.readStringUntil('\n'); // 한 줄 읽기
    int servoID, angle;

    // 입력값을 ',' 기준으로 분리
    int commaIndex = input.indexOf(',');
    if (commaIndex != -1) {
      servoID = input.substring(0, commaIndex).toInt();
      angle = input.substring(commaIndex + 1).toInt();

      // 받은 데이터로 특정 서보 모터 제어
      sts.RegWritePosEx(servoID, angle, 500, 0);  // 해당 ID의 서보 모터 움직임 예약
      delay(500);
      sts.RegWriteAction();  // 예약된 명령 실행
    }
  }

  Serial.flush();  // 버퍼 비우기
  delay(1000);  // 읽기 주기 설정
}
