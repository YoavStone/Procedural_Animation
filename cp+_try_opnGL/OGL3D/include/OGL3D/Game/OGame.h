#ifndef PROCEDURAL_ANIMATION_OGAME_H
#define PROCEDURAL_ANIMATION_OGAME_H


class OWindow;

class OGame{
public:
    OGame();
    ~OGame();

    void run();
    void quit();
protected:
    bool m_isRunning = true;
    OWindow* m_display = nullptr;
};


#endif //PROCEDURAL_ANIMATION_OGAME_H
