#ifndef PROCEDURAL_ANIMATION_OWINDOW_H
#define PROCEDURAL_ANIMATION_OWINDOW_H


class OWindow {
public:
    OWindow();
    ~OWindow();

private:
    void* m_handle = nullptr;
};


#endif //PROCEDURAL_ANIMATION_OWINDOW_H
