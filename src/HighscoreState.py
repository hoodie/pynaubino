from GameStates import State
from ItemFader import ItemFader
from PyQt4.QtCore import *
from PyQt4.QtGui import *

class HighscoreState(State):
    def __init__(self, machine):
        super(HighscoreState, self).__init__(machine)

        self.layer = layer = QGraphicsRectItem()
        layer.setVisible(False)
        layer.setOpacity(0)
        self.scene.add_item(layer)
        self.fader = fader = ItemFader(layer)

        self.table = table = QGraphicsTextItem()
        table.setPos(0, -100)
        table.setParentItem(layer)

    def enter(self):
        highscore = self.scene.highscore
        table = self.table
        if not highscore: return
        score = highscore.load_score()
        score = score[:5]
        score = self.generate_highscore_html(score)
        table.setHtml(score)
        table.adjustSize()
        r = table.boundingRect()
        w, h = r.width(), r.height()
        pos = table.pos()
        table.setPos(-0.5 * w, -0.5 * h)
        self.fader.fade_in()

    def leave(self):
        self.fader.fade_out()

    def generate_highscore_html(self, score_table):
        sizes = [u"xx-large", u"x-large", u"large"]

        def score_style(sizes):
            if not sizes: return u""
            size = sizes.pop(0)

            style = [
                u"font-size:{0}".format(size),
                u"vertical-align:bottom",
                u"padding-right:40px"]
            return u";".join(style)

        style = [u"vertical-align:bottom"]
        name_style = u";".join(style)

        html = "<h1>Highscore</h1>"
        html += "<table>"
        for line in score_table:
            score, name = line
            html += u'<tr>'
            html += u'<td style="{0}">'.format(score_style(sizes))
            html += unicode(score)
            html += u'</td>'
            html += u'<td style="{0}">'.format(name_style)
            html += name
            html += u'</td>'
            html += u'</tr>'
        html += u"</table>"
        return html
