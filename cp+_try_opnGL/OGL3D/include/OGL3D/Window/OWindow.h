#ifndef PROCEDURAL_ANIMATION_OWINDOW_H
#define PROCEDURAL_ANIMATION_OWINDOW_H

#include "../Math/ORect.h"

class CWin32Window
{
public:
    CWin32Window();
    ~CWin32Window();

    ORect getInnerSize();

    void makeCurrentContext();
    void present(bool vsync);

private:
    void* m_handle = nullptr;
    void* m_context = nullptr;
};


#endif //PROCEDURAL_ANIMATION_OWINDOW_H
