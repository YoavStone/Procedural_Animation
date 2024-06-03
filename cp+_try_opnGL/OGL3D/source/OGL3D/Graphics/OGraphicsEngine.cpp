#include "../../../include/OGL3D/Graphics/OGraphicsEngine.h"
#include "../../../vendor/glad/include/glad/glad.h"
#include <assert.h>
#include <stdexcept>


void OGraphicsEngine::clear(const OVec4 &color)
{
    glClearColor(color.x, color.y, color.z, color.w);
    glClear(GL_COLOR_BUFFER_BIT);
}
