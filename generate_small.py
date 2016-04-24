import random

import svgwrite

phodal_width = 176
secondary_text_x = 224
basic_text_y = 35


def generate_idea():
    y_text_split = phodal_width + 1
    height = 50
    rect_length = 2
    width = 327
    max_rect_length = 10

    dwg = svgwrite.Drawing('shields/idea-small.svg', profile='full', size=(u'327', u'50'))

    shapes = dwg.add(dwg.g(id='shapes', fill='none'))
    shapes.add(dwg.rect((0, 0), (phodal_width, height), fill='#5E6772'))
    shapes.add(dwg.rect((phodal_width, 0), (width - phodal_width, height), fill='#2196F3'))
    shapes.add(dwg.text('phodal', insert=(27, basic_text_y), fill='#FFFFFF', font_size=40, font_family='Helvetica'))

    def draw_for_bg_plus():
        for x in range(y_text_split + rect_length, width, rect_length):
            shapes.add(dwg.line((x, 0), (x, height), stroke='#EEEEEE', stroke_width='0.5', stroke_opacity=0.3))

        for y in range(rect_length, height, rect_length):
            shapes.add(dwg.line((y_text_split, y), (width, y), stroke='#EEEEEE', stroke_width='0.5', stroke_opacity=0.3))

        for x in range(y_text_split + max_rect_length, width, max_rect_length):
            for y in range(0, height, max_rect_length):
                shapes.add(dwg.line((x, y - 2), (x, y + 2), stroke='#EEEEEE', stroke_width='1', stroke_opacity=0.4))

        for y in range(0, height, max_rect_length):
            for x in range(y_text_split + max_rect_length, width, max_rect_length):
                shapes.add(dwg.line((x - 2, y), (x + 2, y), stroke='#EEEEEE', stroke_width='1', stroke_opacity=0.4))

    draw_for_bg_plus()

    shapes.add(dwg.text('idea', insert=(secondary_text_x, basic_text_y), fill='#FFFFFF', font_size=40,
                        font_family='Helvetica'))
    dwg.save()


def generate_article():
    dwg = svgwrite.Drawing('shields/article.svg', size=(u'970', u'150'))

    shapes = dwg.add(dwg.g(id='shapes', fill='none'))
    shapes.add(dwg.rect((0, 0), (phodal_width, 150), fill='#5E6772'))
    shapes.add(dwg.text('phodal', insert=(83, basic_text_y), fill='#FFFFFF', font_size=120, font_family='Helvetica'))

    shapes.add(dwg.rect((phodal_width, 0), (446, 150), fill='#ffeb3b'))
    shapes.add(dwg.text(insert=(phodal_width, 16), fill='#34495e', opacity=0.2, font_size=12,
                        text='Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Vestibulum tortor quam, fe-'))
    shapes.add(dwg.text(insert=(phodal_width, 32), fill='#34495e', opacity=0.2, font_size=12,
                        text='ugiat vitae, ultricies eget, tempor sit amet, ante. Donec eu libero sit amet quam egestas semper. Aenean ultricies mi'))
    shapes.add(dwg.text(insert=(phodal_width, 48), fill='#34495e', opacity=0.2, font_size=12,
                        text='vitae est. Mauris placerat eleifend leo. Quisque sit amet est et sapien ullamcorper pharetra. Vestibulum erat wisi, '))
    shapes.add(dwg.text(insert=(phodal_width, 64), fill='#34495e', opacity=0.2, font_size=12,
                        text='condimentum sed, commodo vitae, ornare sit amet, wisi. Aenean fermentum, elit eget tincidunt condimentum, eros ipsum '))
    shapes.add(dwg.text(insert=(phodal_width, 80), fill='#34495e', opacity=0.2, font_size=12,
                        text='rutrum orci, sagittis tempus lacus enim ac dui. Donec non enim in turpis pulvinar facilisis. Ut felis. Praesent dapibus,'))
    shapes.add(dwg.text(insert=(phodal_width, 96), fill='#34495e', opacity=0.2, font_size=12,
                        text=' neque id cursus faucibus, tortor neque egestas augue, eu vulputate magna eros eu erat. Aliquam erat volutpat. Nam dui mi,'))
    shapes.add(dwg.text(insert=(phodal_width, 112), fill='#34495e', opacity=0.2, font_size=12,
                        text=' tincidunt quis, accumsan porttitor, facilisis luctus, metus'))
    shapes.add(dwg.text(insert=(phodal_width, 128), fill='#34495e', opacity=0.2, font_size=12,
                        text='Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus magna. Cras in mi at felis aliquet congue. Ut a est eget '))
    shapes.add(dwg.text(insert=(phodal_width, 144), fill='#34495e', opacity=0.2, font_size=12,
                        text='ligula molestie gravida. Curabitur massa. Donec eleifend, libero at sagittis mollis, tellus est malesuada tellus, at luctus '))
    shapes.add(dwg.text(insert=(phodal_width, 160), fill='#34495e', opacity=0.2, font_size=12,
                        text='turpis elit sit amet quam. Vivamus pretium ornare est.'))

    shapes.add(dwg.text('article', insert=(secondary_text_x, basic_text_y), fill='#34495e', font_size=120, font_family='Helvetica'))

    dwg.save()


def get_some_random10(num):
    results = ''
    for x in range(1, num):
        results += str(random.getrandbits(1))
    return results


def generate_works():
    dwg = svgwrite.Drawing('shields/works.svg', size=(u'950', u'150'))

    shapes = dwg.add(dwg.g(id='shapes', fill='none'))

    shapes.add(dwg.rect((phodal_width, 0), (426, 150), fill='#2c3e50'))
    for x in range(0, 300, 10):
        text = get_some_random10(100)
        shapes.add(
            dwg.text(text, insert=(phodal_width + 1, x), fill='#27ae60', font_size=12,
                     font_family='Inconsolata for Powerline',
                     opacity=0.3, transform="rotate(15 1000, 0)"))

    shapes.add(dwg.rect((0, 0), (phodal_width, 150), fill='#5E6772'))
    shapes.add(dwg.text('phodal', insert=(83, basic_text_y), fill='#FFFFFF', font_size=120, font_family='Helvetica'))
    shapes.add(dwg.text('works', insert=(secondary_text_x, basic_text_y), fill='#FFFFFF', font_size=120, font_family='Helvetica'))

    dwg.save()


def generate_design():
    dwg = svgwrite.Drawing('shields/design.svg', size=(u'1014', u'150'))

    # for D Rect
    red_point = 798
    design_width = 486

    shapes = dwg.add(dwg.g(id='shapes', fill='none'))
    shapes.add(dwg.rect((0, 0), (phodal_width, 150), fill='#5E6772'))

    def draw_design_word():
        shapes.add(dwg.rect((phodal_width, 90), (design_width, 60), fill='#2196f3'))
        shapes.add(dwg.text('design', insert=(secondary_text_x + 6, 120), fill='#000', stroke_width=4, font_size=120,
                            font_family='Helvetica'))
        shapes.add(dwg.rect((phodal_width, 0), (design_width, 90), fill='#03a9f4'))
        # shapes.add(dwg.rect((phodal_width, 88), (486, 3), fill='#e91e63'))
        shapes.add(dwg.rect((phodal_width, 90), (design_width, 0.2), fill='#000'))
        shapes.add(dwg.text('design', insert=(secondary_text_x + 4, basic_text_y), fill='#FFFFFF', font_size=120,
                            font_family='Helvetica'))

    def draw_red_point():
        shapes.add(dwg.ellipse((red_point, 40), (9, 9), fill='#000'))
        shapes.add(dwg.ellipse((red_point + 1, 39), (9, 9), fill='#f44336'))

    def draw_d_arround():
        shapes.add(dwg.line((secondary_text_x, 90), (secondary_text_x, 130), stroke='#EEEEEE', stroke_width='1',
                            stroke_opacity=1, stroke_dasharray="2,2"))
        shapes.add(
            dwg.line((secondary_text_x + 70, 90), (secondary_text_x + 70, 130), stroke='#EEEEEE', stroke_width='1',
                     stroke_opacity=1, stroke_dasharray="2,2"))
        # shapes.add(dwg.line((700, 25), (770, 25), stroke='#EEEEEE', stroke_width='1', stroke_opacity=1, stroke_dasharray="2,2"))
        shapes.add(dwg.line((secondary_text_x, 130), (secondary_text_x + 70, 130), stroke='#EEEEEE', stroke_width='1',
                            stroke_opacity=1, stroke_dasharray="2,2"))

    draw_design_word()
    draw_red_point()
    draw_d_arround()

    shapes.add(dwg.text('phodal', insert=(83, basic_text_y), fill='#FFFFFF', font_size=120, font_family='Helvetica'))

    dwg.save()


generate_idea()
# generate_article()
#generate_works()
# generate_design()