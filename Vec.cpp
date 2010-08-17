#include "Vec.h"

Vec::Vec(float32 x, float32 y) : b2Vec2(x, y) {}
Vec::Vec(b2Vec2 vec) : b2Vec2(vec.x, vec.y) {}
Vec::Vec(QPointF vec) : b2Vec2(vec.x(), vec.y()) {}
Vec::Vec() : b2Vec2() {}

QPointF Vec::q() { return QPointF(x, y); }

Vec Vec::rand() {
    qreal x = qrand()*2.0f*M_PI/RAND_MAX;
    return Vec(qCos(x), qSin(x));
}

