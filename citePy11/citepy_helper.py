def __add_specialization__(result, segment):
    if not hasattr(segment, 'specialization'):
        return result

    if segment.specialization is None:
        return result

    result += '<'
    for i, arg in enumerate(segment.specialization.args):
        result += get_cpp_type(arg.arg.typename.segments)
        if i < len(segment.specialization.args) - 1:
            result += ', '
    result += '>'
    return result


def get_cpp_type(segments):
    result = segments[0].name
    result = __add_specialization__(result, segments[0])

    for seg in segments[1:]:
        result += '::' + seg.name
        result = __add_specialization__(result, seg)

    return result
