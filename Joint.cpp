#include "Joint.h"
#include "Naub.h"
#include "QJoint.h"
#include "Naubino.h"

Joint::Joint(Naubino *naubino, Naub *a, Naub *b)
    : naubino(naubino), a(a), b(b) {

    setup();
}

Joint::~Joint() {
    if (qjoint != NULL) qjoint->jointDeleted();
    naubino->world->DestroyJoint(joint);
}

void Joint::changed() {
    if (qjoint != NULL) qjoint->jointChanged();
}

void Joint::deleted() {
    naubino->world->DestroyJoint(joint);
    if (qjoint != NULL) qjoint->jointDeleted();
}

void Joint::setup() {
    qjoint = NULL;

    frequencyHz = 0.5f;
    dampingRatio = 0.1f;
    length = 40.0f;

    b2DistanceJointDef jointDef;
    jointDef.bodyA = a->body;
    jointDef.bodyB = b->body;
    jointDef.localAnchorA = a->body->GetLocalCenter();
    jointDef.localAnchorB = b->body->GetLocalCenter();
    jointDef.collideConnected = true;
    jointDef.frequencyHz = frequencyHz;
    jointDef.dampingRatio = dampingRatio;
    jointDef.length = length;
    joint = naubino->world->CreateJoint(&jointDef);
}
