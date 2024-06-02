#ifndef PROCEDURAL_ANIMATION_OWINDOW_H
#define PROCEDURAL_ANIMATION_OWINDOW_H


class OWindow {
public:
    OWindow();
    ~OWindow();

    void makeCurrentContext();
    void present(bool vsync);

private:
    void* m_handle = nullptr;
    void* m_context = nullptr;
};


#endif //PROCEDURAL_ANIMATION_OWINDOW_H
