#ifndef POINTER_H
#define POINTER_H

#include <Box2D.h>
#include "Vec.h"

class PointerJoint;

class Pointer {
public:
    Pointer(b2World &world);
    ~Pointer();
    void setPos(Vec pos);
    Vec pos();
    b2World& world();
    QList<PointerJoint *>& joints();
private:
    b2World *world_;
    b2Body *body_;
    QList<PointerJoint *> *joints_;
};

#endif // POINTER_H