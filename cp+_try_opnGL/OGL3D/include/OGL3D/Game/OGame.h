#ifndef PROCEDURAL_ANIMATION_OGAME_H
#define PROCEDURAL_ANIMATION_OGAME_H

#include <memory>


class OWindow;

class OGame{
public:
    OGame();
    ~OGame();

    void run();
    void quit();
protected:
    bool m_isRunning = true;
    std::unique_ptr<OWindow> m_display;
};


#endif //PROCEDURAL_ANIMATION_OGAME_H
