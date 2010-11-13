import pymunk

class Space(pymunk.Space):
    def __init__(self):
        pymunk.Space.__init__(self)
        self.damping = 0.4
        self.set_default_collision_handler(None, None, self.collide, None)

    def remove(self, *objs):
        for obj in objs:
            def callback(obj):
                pymunk.Space.remove(self, obj)
            self.add_post_step_callback(callback, obj)

    def collide(self, space, arbiter, *args, **kwargs):
        if len(arbiter.shapes) != 2: return
        a, b = arbiter.shapes
        if a == None or b == None: return
        a, b = [x.body.naubino_obj for x in [a, b]]

        if hasattr(a, u"collide"): a.collide(b, arbiter)
        if hasattr(b, u"collide"): b.collide(a, arbiter)
