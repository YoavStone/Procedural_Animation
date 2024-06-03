#include "../../../../include/OGL3D/Game/OGame.h"
#include "../../../../include/OGL3D/Window/OWindow.h"
#include "../../../../include/OGL3D/Graphics/OGraphicsEngine.h"
#include <windows.h>
#include <iostream>


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