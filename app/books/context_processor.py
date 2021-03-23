from books import model_choices as mch


def model_choices_context(request):
    return {
        'mch': mch,
    }
