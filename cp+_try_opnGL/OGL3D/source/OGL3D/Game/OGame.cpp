#include "../../../include/OGL3D/Game/OGame.h"
#include "../../../include/OGL3D/Window/OWindow.h"
#include <Windows.h>
#include <iostream>


OGame::OGame() {
    m_display = std::unique_ptr<OWindow> (new OWindow());
}

OGame::~OGame() {}

void OGame::quit(){
    m_isRunning = false;
}

void OGame::run() {

    MSG msg;
    while(m_isRunning && !m_display->isClosed()){
        if(PeekMessage(&msg, NULL, NULL, NULL, PM_REMOVE)){
            TranslateMessage(&msg);
            DispatchMessage(&msg);
        }
        Sleep(1);
    }
}