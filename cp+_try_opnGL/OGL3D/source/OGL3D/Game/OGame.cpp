#include "../../../include/OGL3D/Game/OGame.h"
#include "../../../include/OGL3D/window/OWindow.h"
#include <Windows.h>


OGame::OGame() {
    m_display = new OWindow();
}

OGame::~OGame() {
    delete m_display;
}

void OGame::quit(){
    m_isRunning = false;
}

void OGame::run() {

    MSG msg;
    while(m_isRunning){
        if(PeekMessage(&msg, NULL, NULL, NULL, PM_REMOVE)){
            TranslateMessage(&msg);
            DispatchMessage(&msg);
        }
        Sleep(1);
    }
}