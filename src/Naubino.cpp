    #include "Naubino.h"
#include <Simulator.h>
#include <Naub.h>
#include <NaubJoint.h>
#include <Box2D/Dynamics/b2World.h>
#include <Box2D/Dynamics/b2Body.h>

Naubino::Naubino(QObject *parent) : QObject(parent) {
    sim = new Simulator(this);
    connect(sim,
            SIGNAL(naubOnNaub(Naub*,Naub*)),
            SIGNAL(naubOnNaub(Naub*,Naub*)));

    b2BodyDef def;
    def.type = b2_kinematicBody;
    def.position = Vec();
    center = world().CreateBody(&def);
}

b2World& Naubino::world() const {
    return sim->world();
}

void Naubino::add(Joint *joint) {
    connect(joint,
            SIGNAL(removed(Joint*)),
            SLOT(remove(Joint*)));
    emit added(joint);
}

void Naubino::add(Naub *naub) {
    naub->setNaubino(*this);
    connect(naub,
            SIGNAL(removed(Naub*)),
            SLOT(remove(Naub*)));
    connect(naub,
            SIGNAL(added(Joint*)),
            SLOT(add(Joint*)));
    connect(naub,
            SIGNAL(merged(Naub*)),
            SIGNAL(merged(Naub*)));
    naub->connect(this,
                  SIGNAL(naubOnNaub(Naub*,Naub*)),
                  SLOT(touch(Naub*,Naub*)));
    emit added(naub);
}

void Naubino::remove(QList<Naub*> &naubs) {
    foreach(Naub *naub, naubs)
        naub->remove();
}

void Naubino::remove(Naub *obj) {
    obj->deleteLater();
}

void Naubino::remove(Joint *obj) {
    obj->deleteLater();
}

void Naubino::start() {
    sim->start(50);
    emit started();
}

void Naubino::pause() {
    sim->stop();
    emit paused();
}
