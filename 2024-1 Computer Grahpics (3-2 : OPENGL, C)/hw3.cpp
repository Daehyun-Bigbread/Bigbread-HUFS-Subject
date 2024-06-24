#include <GL/glut.h>
#include <iostream>
#include <cmath>

// 관찰자 위치와 방향
float observerPosX = 0.0f, observerPosY = 2.0f, observerPosZ = 20.0f;
float observerAngle = 0.0f;

void init() {
    glEnable(GL_DEPTH_TEST);
    glEnable(GL_LIGHTING);
    glEnable(GL_LIGHT0);
    glEnable(GL_COLOR_MATERIAL);

    GLfloat lightPos[] = { 1.0f, 1.0f, 1.0f, 0.0f };
    glLightfv(GL_LIGHT0, GL_POSITION, lightPos);

    glClearColor(0.6f, 0.8f, 1.0f, 1.0f); // 하늘색 배경
}

void drawCube(float x, float y, float z, float size) {
    glPushMatrix();
    glTranslatef(x, y, z);
    glutSolidCube(size);
    glPopMatrix();
}

void drawBuilding(float x, float y, float z, float width, float height, float depth) {
    glPushMatrix();
    glTranslatef(x, y + height / 2.0f, z);
    glScalef(width, height, depth);
    glutSolidCube(1.0f);
    glPopMatrix();
}

void drawRoad(float x, float z, float width, float length) {
    glPushMatrix();
    glTranslatef(x, 0.0f, z);
    glScalef(width, 0.1f, length);

    // 도로 색상 변경
    glColor3f(0.4f, 0.4f, 0.4f);

    // 도로 표면 패턴 추가
    for (float i = 0.0f; i < 1.0f; i += 0.1f) {
        glBegin(GL_QUADS);
        glVertex3f(-0.5f + i, 0.0f, -0.5f);
        glVertex3f(-0.5f + i, 0.0f, 0.5f);
        glVertex3f(-0.5f + i + 0.05f, 0.0f, 0.5f);
        glVertex3f(-0.5f + i + 0.05f, 0.0f, -0.5f);
        glEnd();
    }

    // 도로 경계선 추가
    glColor3f(0.2f, 0.2f, 0.2f);
    glBegin(GL_QUADS);
    glVertex3f(-0.5f, 0.01f, -0.5f);
    glVertex3f(-0.5f, 0.01f, 0.5f);
    glVertex3f(0.5f, 0.01f, 0.5f);
    glVertex3f(0.5f, 0.01f, -0.5f);
    glEnd();

    glPopMatrix();
}

void drawScene() {
    // 넓은 도로와 교차로
    drawRoad(0.0f, 0.0f, 10.0f, 100.0f);  // 직선 도로
    drawRoad(-25.0f, 0.0f, 50.0f, 10.0f); // 횡단 도로
    drawRoad(25.0f, 0.0f, 50.0f, 10.0f);  // 횡단 도로 (우회전)

    // 다양한 건물들
    glColor3f(0.7f, 0.2f, 0.2f);
    drawBuilding(-30.0f, 0.0f, -10.0f, 3.0f, 6.0f, 3.0f);

    glColor3f(0.2f, 0.7f, 0.2f);
    drawBuilding(30.0f, 0.0f, -10.0f, 4.0f, 8.0f, 4.0f);

    glColor3f(0.2f, 0.2f, 0.7f);
    drawBuilding(-30.0f, 0.0f, 10.0f, 2.0f, 5.0f, 2.0f);

    glColor3f(0.7f, 0.7f, 0.2f);
    drawBuilding(30.0f, 0.0f, 10.0f, 3.5f, 7.0f, 3.5f);

    glColor3f(0.7f, 0.2f, 0.7f);
    drawBuilding(-15.0f, 0.0f, 15.0f, 2.0f, 4.0f, 2.0f);

    glColor3f(0.2f, 0.7f, 0.7f);
    drawBuilding(15.0f, 0.0f, -15.0f, 3.0f, 6.0f, 3.0f);

    glColor3f(0.7f, 0.5f, 0.2f);
    drawBuilding(-20.0f, 0.0f, -25.0f, 4.0f, 8.0f, 4.0f);

    glColor3f(0.5f, 0.2f, 0.7f);
    drawBuilding(20.0f, 0.0f, -25.0f, 3.0f, 5.0f, 3.0f);

    glColor3f(0.2f, 0.5f, 0.7f);
    drawBuilding(-25.0f, 0.0f, 20.0f, 2.5f, 6.0f, 2.5f);

    glColor3f(0.7f, 0.2f, 0.5f);
    drawBuilding(25.0f, 0.0f, 20.0f, 4.0f, 8.0f, 4.0f);

    glColor3f(0.2f, 0.7f, 0.2f);
    drawBuilding(-35.0f, 0.0f, -5.0f, 3.5f, 7.0f, 3.5f);

    glColor3f(0.7f, 0.2f, 0.2f);
    drawBuilding(35.0f, 0.0f, -5.0f, 2.0f, 4.0f, 2.0f);

    // 차량
    glColor3f(0.2f, 0.2f, 0.7f);
    drawCube(0.0f, 0.5f, -2.0f, 1.0f);
}

void display() {
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);

    glLoadIdentity();
    gluLookAt(observerPosX, observerPosY, observerPosZ,
        observerPosX + sin(observerAngle), observerPosY, observerPosZ - cos(observerAngle),
        0.0f, 1.0f, 0.0f);

    drawScene();

    glutSwapBuffers();
}

void reshape(int w, int h) {
    glViewport(0, 0, w, h);
    glMatrixMode(GL_PROJECTION);
    glLoadIdentity();
    gluPerspective(45.0, (double)w / (double)h, 1.0, 200.0);
    glMatrixMode(GL_MODELVIEW);
}

void keyboard(unsigned char key, int x, int y) {
    const float moveSpeed = 0.5f;
    const float rotateSpeed = 0.05f;

    switch (key) {
    case 's': // 's' 키: 약간 전진
        observerPosX += moveSpeed * sin(observerAngle);
        observerPosZ -= moveSpeed * cos(observerAngle);
        break;
    case 'd': // 'd' 키: 약간 후진
        observerPosX -= moveSpeed * sin(observerAngle);
        observerPosZ += moveSpeed * cos(observerAngle);
        break;
    case 'r': // 'r' 키: 시계 방향으로 약간 회전
        observerAngle -= rotateSpeed;
        break;
    case 'l': // 'l' 키: 반시계 방향으로 약간 회전
        observerAngle += rotateSpeed;
        break;
    case 27: // ESC 키
        exit(0);
        break;
    }

    glutPostRedisplay();
}

int main(int argc, char** argv) {
    glutInit(&argc, argv);
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH);
    glutInitWindowSize(800, 600);
    glutCreateWindow("Mohyeon intersection");

    init();

    glutDisplayFunc(display);
    glutReshapeFunc(reshape);
    glutKeyboardFunc(keyboard);

    glutMainLoop();
    return 0;
}

