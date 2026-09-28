"""DISCLAIMER! PLEASE ONLY USE THIS FOR PYGAME!"""

def wrap_text_a(font, text, screen, y, maximum_char=30):
    da_text = text
    words = list(da_text)
    if len(list(text)) > maximum_char:
        texts = list(text)
        for number in range(int(len(text) / 30)):
            texts.insert(maximum_char * (number + 1), '\n')
            da_text = ''
            for _ in texts:
                da_text += _
    words = da_text.split('\n')
    line_n = y
    for line in words:
        image = font.render(line, True, (255, 255, 255))
        rect = (0, (line_n))
        screen.blit(image, rect)
        line_n += 35
def wrap_text_m(font, text, screen,x,y,align='left', enter=35):
    da_text = text
    # words = list(da_text)
    # if len(list(text)) > maximum_char:
    #     texts = list(text)

    #     for number in range(int(len(text) / 30)):
    #         texts.insert(maximum_char * (number + 1), '\n')
    #         da_text = ''
    #         for _ in texts:
    #             da_text += _
    words = da_text.split('\n')
    line_n = y
    for line in words:
        image = font.render(line, True, (255, 255, 255))
        if align == 'left':
            rect = image.get_rect(topleft=(x, (line_n)))
        elif align == 'right':
            rect = image.get_rect(topright=(x, (line_n)))
        elif align == 'center':
            rect = image.get_rect(midtop=(x, (line_n)))

        screen.blit(image, rect)
        line_n += enter

