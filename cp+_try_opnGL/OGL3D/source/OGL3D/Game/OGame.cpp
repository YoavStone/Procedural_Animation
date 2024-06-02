#include "../../../include/OGL3D/Game/OGame.h"
#include "../../../include/OGL3D/Window/OWindow.h"
#include "../../../include/OGL3D/Graphics/OGraphicsEngine.h"
#include <Windows.h>
#include <iostream>


OGame::OGame()
{
    m_graphicsEngine = std::make_unique<OGraphicsEngine>();
    m_display = std::make_unique<OWindow>();

    m_display->makeCurrentContext();
}

OGame::~OGame() {}

void OGame::quit()
{
    m_isRunning = false;
}

void OGame::onCreate()
{
}

void OGame::onUpdate()
{
    m_graphicsEngine->clear(OVec4(1, 0, 0, 1));



    m_display->present(false);
}

void OGame::onQuit()
{
}

void OGame::run()
{
    onCreate();

    while(m_isRunning)
    {
        MSG msg = {};
        if(PeekMessage(&msg, NULL, NULL, NULL, PM_REMOVE))
        {
            if(msg.message == WM_QUIT){
                m_isRunning = false;
                continue;
            }
            else
            {
                TranslateMessage(&msg);
                DispatchMessage(&msg);
            }
        }
        onUpdate();
    }

    onQuit();
}