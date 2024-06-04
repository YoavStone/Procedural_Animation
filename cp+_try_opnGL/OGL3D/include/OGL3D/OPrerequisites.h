#ifndef GITHUB_OPREREQUISITES_H
#define GITHUB_OPREREQUISITES_H


#include <memory>

class OVertexArrayObject;

typedef std::shared_ptr<OVertexArrayObject> OVertexArrayObjectPtr;


typedef float f32;
typedef int i32;
typedef unsigned int ui32;


struct OVertexBufferData
{
    void* verticesList = nullptr;
    ui32 vertexSize = 0;
    ui32 listSize = 0;
};


#endif //GITHUB_OPREREQUISITES_H
