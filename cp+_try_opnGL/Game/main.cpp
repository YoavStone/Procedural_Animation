#include "../OGL3D/include/OGL3D/Game/OGame.h"
#include <iostream>

int main()
{
    try
    {
        OGame game;
        game.run();
    }
    catch(const std::exception& e)
    {
        std::cout << "EXCEPTION AT MAIN: " << e.what() << "\n";
        return 1;
    }

    return 0;
}