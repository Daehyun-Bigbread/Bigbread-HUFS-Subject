#include <GL/glut.h>
#include <cmath>

#ifndef M_PI
#define M_PI 3.14159265358979323846
#endif

bool isClapping = false;
float upperArmTheta = 45.0;  // 초기 각도
float lowerArmTheta = 0.0;  // 하박의 초기 각도

void Draw_Polygon(int num_vertices, float radius, float x_center, float y_center, float r, float g, float b) {
    glColor3f(r, g, b);
    glBegin(GL_POLYGON);
    for (int i = 0; i < num_vertices; ++i) {
        float angle = 2.0f * M_PI * i / num_vertices;
        glVertex2f(cos(angle) * radius + x_center, sin(angle) * radius + y_center);
    }
    glEnd();
}

void Draw_ArmSegment(float x, float y, float width, float height, float r, float g, float b) {
    glColor3f(r, g, b);
    glBegin(GL_QUADS);
    glVertex2f(x, y);
    glVertex2f(x + width, y);
    glVertex2f(x + width, y + height);
    glVertex2f(x, y + height);
    glEnd();
}

void Draw_BodyAndHead() {
    // 몸통
    glColor3f(0.0, 0.0, 1.0);  // 짙은 파란색
    glBegin(GL_QUADS);
    glVertex2f(-5.0, -5.0);
    glVertex2f(5.0, -5.0);
    glVertex2f(5.0, 5.0);
    glVertex2f(-5.0, 5.0);
    glEnd();
    // 머리
    Draw_Polygon(30, 3.0, 0.0, 8.0, 1.0, 0.8, 0.6);  // 살구색 머리
}

void Draw_Arm(float x, float y, float upperAngle, float lowerAngle, bool isRightArm) {
    glPushMatrix();
    glTranslatef(x, y, 0.0);
    // 상박 색상을 녹색으로 통일
    glColor3f(0.0, 1.0, 0.0);  // 녹색
    glRotatef(isRightArm ? -upperAngle : upperAngle, 0.0, 0.0, 1.0);
    Draw_ArmSegment(0.0, 0.0, 7.0, 2.0, 0.0, 1.0, 0.0);  // 녹색 상박
    // 하박
    glTranslatef(7.0, 0.0, 0.0);
    glRotatef(isRightArm ? lowerAngle : -lowerAngle, 0.0, 0.0, 1.0);
    Draw_ArmSegment(0.0, 0.0, 7.0, 2.0, 0.7, 0.7, 1.0);  // 연한 파란색
    // 손
    Draw_Polygon(5, 2.0, 7.0, 0.0, 1.0, 0.8, 0.6);  // 살구색 손
    glPopMatrix();
}

void MyDisplay() {
    glClear(GL_COLOR_BUFFER_BIT);
    Draw_BodyAndHead();
    Draw_Arm(5.0, 5.0, upperArmTheta, lowerArmTheta, true);  // 오른쪽 팔
    Draw_Arm(-5.0, 5.0, -upperArmTheta, lowerArmTheta, false);  // 왼쪽 팔
    glFlush();
}

void UpdateClapping() {
    if (isClapping) {
        upperArmTheta += 2.0;
        lowerArmTheta -= 2.0;  // Reverse the movement for clapping
        if (upperArmTheta >= 90.0) {
            upperArmTheta = 45.0;  // Reset the arm angle to starting position
            lowerArmTheta = 0.0;  // Reset the lower arm angle
        }
    }
}

void MyKeyboard(unsigned char key, int x, int y) {
    switch (key) {
    case 's':
        isClapping = true;
        break;
    case 'q':
        isClapping = false;
        break;
    case 27:  // ESC 키
        exit(0);
        break;
    }
    glutPostRedisplay();
}

void Timer(int value) {
    UpdateClapping();
    glutPostRedisplay();
    glutTimerFunc(33, Timer, 0);
}

int main(int argc, char** argv) {
    glutInit(&argc, argv);
    glutInitDisplayMode(GLUT_RGB);
    glutInitWindowSize(400, 400);
    glutCreateWindow("OpenGL 로봇 박수 치기");
    glClearColor(1.0, 1.0, 1.0, 1.0);
    glMatrixMode(GL_PROJECTION);
    glLoadIdentity();
    gluOrtho2D(-10.0, 10.0, -10.0, 20.0);
    glutDisplayFunc(MyDisplay);
    glutKeyboardFunc(MyKeyboard);
    glutTimerFunc(0, Timer, 0);
    glutMainLoop();
    return 0;
}
