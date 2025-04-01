#include <Servo.h>

#define TRIG_PIN 7   // Ultrasonic sensor trigger pin
#define ECHO_PIN 8   // Ultrasonic sensor echo pin
#define SERVO_PIN 9  // Servo motor control pin

Servo dustbinLid;

void setup() {
    pinMode(TRIG_PIN, OUTPUT);
    pinMode(ECHO_PIN, INPUT);
    dustbinLid.attach(SERVO_PIN);
    dustbinLid.write(0);  // Start with lid closed
    Serial.begin(9600);
}

long getDistance() {
    digitalWrite(TRIG_PIN, LOW);
    delayMicroseconds(2);
    digitalWrite(TRIG_PIN, HIGH);
    delayMicroseconds(10);
    digitalWrite(TRIG_PIN, LOW);
    
    long duration = pulseIn(ECHO_PIN, HIGH);
    long distance = duration * 0.034 / 2;  // Convert time to distance (cm)
    return distance;
}

void loop() {
    long distance = getDistance();
    Serial.print("Distance: ");
    Serial.print(distance);
    Serial.println(" cm");
    
    if (distance < 10) {  // If trash is detected close to the sensor
        dustbinLid.write(90);  // Open lid
        delay(3000);  // Keep open for 3 seconds
        dustbinLid.write(0);  // Close lid
    }
    
    delay(1000);  // Check every second
}
