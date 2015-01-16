'''Python CLIColours object'''

class CLIColours(object):
    COLOURS = {
        'BLACK': '\033[30m',
        'BLUE': '\033[34m',
        'GREEN': '\033[32m',
        'CYAN': '\033[36m',
        'RED': '\033[31m',
        'PURPLE': '\033[35m',
        'YELLOW': '\033[33m',
        'LIGHT_GREY': '\033[37m',
        'DARK_GREY': '\033[1;30m',
        'BOLD_BLUE': '\033[1;34m',
        'BOLD_GREEN': '\033[1;32m',
        'BOLD_CYAN': '\033[1;36m',
        'BOLD_RED': '\033[1;31m',
        'BOLD_PURPLE': '\033[1;35m',
        'BOLD_YELLOW': '\033[1;33m',
        'BRIGHT_GREY': '\033[0;90m',
        'BRIGHT_BLUE': '\033[0;94m',
        'BRIGHT_GREEN': '\033[0;92m',
        'BRIGHT_CYAN': '\033[0;96m',
        'BRIGHT_RED': '\033[0;91m',
        'BRIGHT_PURPLE': '\033[0;95m',
        'BRIGHT_YELLOW': '\033[0;93m',
        'WHITE': '\033[1;37m',
        'NORMAL': '\033[0m',
    }

    def __init__(self):
        self._stream = None
        return super(CLIColours, self).__init__()

    def set_stream(self, stream):
        self._stream = stream

    def __getattr__(self, attr):
        if attr.upper() in CLIColours.COLOURS:
            def highlight(word, stream=None):
                output_stream = stream or self._stream
                if output_stream and not output_stream.isatty():
                    return word
                return '{}{}{}'.format(CLIColours.COLOURS[attr.upper()], word, CLIColours.COLOURS['NORMAL'])
            return highlight
        raise AttributeError('No colour %r defined.' % attr)

colour = CLIColours()
