#ifndef NAUB_H
#define NAUB_H

#include "Joint.h"

#include "Vec.h"
#include "NaubContext.h"

#include <Box2D/Box2D.h>
#include <QGraphicsEllipseItem>
#include <QList>
#include <QObject>

class Joint;

class Naub : public QObject {
 public:
	Naub(NaubContext *context, Vec pos);
	void setPos(Vec pos);
	qreal x();
	qreal y();
	void adjust();
	void setup();
	void join(Naub *other);
	NaubContext *context;
	QGraphicsItem *graphics;
	b2Body *body;
	void joinWithCenter();	
	void setupFixture();
	void setupBody();
	QList<Joint *> *joints;
};

#endif
