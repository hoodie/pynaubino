#ifndef NAUB_H
#define NAUB_H

#include "Prereqs.h"

#include <QColor>
#include <Box2D/Box2D.h>
#include "Vec.h"
class Joint;
class Pointer;

class Naub : public QObject {
    Q_OBJECT
signals:
    void removed(Naub *naub);
    void changed(Naub *naub);
    void added(Joint *joint);
    void joined(Joint *joint);
    void merged(Naub *a, Naub *b);
    void selected(Pointer *pointer);
    void deselected(Pointer *pointer);
public slots:
    void select(Pointer *pointer);
    void deselect(Pointer *pointer);
    void contact(Naub *naub);
    void update();
    //void remove();
    //void join(Naub *naub);
    //void merge(Naub *naub);
public:
    Naub(b2World *world);
    virtual ~Naub();

    const Vec& pos() const { return _pos; }
    void setPos(const Vec &pos) {
        if (_body != NULL) _body->SetTransform(pos, _body->GetAngle());
        _pos = pos;
    }

    const QColor& color() const { return _color; }

    b2World* world() const { return _world; }

    b2Body* body() const { return _body; }
private:
    b2World *_world;
    b2Body *_body;
    Vec _pos;
    QColor _color;
    bool _isSelected;
};

#endif // NAUB_H

