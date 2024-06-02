#ifndef GITHUB_OGRAPHICSENGINE_H
#define GITHUB_OGRAPHICSENGINE_H

#include "../Math/OVec4.h"

class OGraphicsEngine {
public:
    OGraphicsEngine();
    ~OGraphicsEngine();

public:
    void clear(const OVec4& color);
};


#endif //GITHUB_OGRAPHICSENGINE_H
