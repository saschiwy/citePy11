import cxxheaderparser.types
from citePy11.citepy_helper import get_cpp_type

tag_start = ['@', '\\']
comment_start = '/**'
comment_continue = '*'
comment_end = '*/'

known_tags = ['brief', 'param', 'returns', 'fn', 'return']
multi_tags = ['param', 'exception', 'note', 'warning']

field_comments = ['///<', '//!<', '//!', '///']

map_python_to_cpp = {
    'brief': '',
    'param': 'Parameter:',
    'returns': 'Returns:',
    'fn': 'Function:',
    'exception': 'Raises:',
    'note': 'Notes:',
    'warning': 'Warnings:',
    'return': 'Returns:'
}


def __make_single_line__(content):
    lines = content.split('\n')
    new_lines = []

    for line in lines:

        line = line.strip()

        if comment_end in line:
            line = line[:line.find(comment_end)].strip()

        if line.startswith(comment_start):
            line = line[len(comment_start):].strip()
        elif line.startswith(comment_continue):
            line = line[len(comment_continue):].strip()

        if len(line) == 0:
            continue

        new_lines.append(line)

    new_content = ' '.join(new_lines)
    return new_content


def parse_doxygen_comment(comment):
    parsed_data = {
        'brief': '',
        'name': '',
        'param': [],
        'return': '',
        'fn': '',
        'exception': []
    }

    if comment is None:
        return parsed_data

    for multi_tag in multi_tags:
        if multi_tag not in known_tags:
            known_tags.append(multi_tag)
        parsed_data[multi_tag] = []

    if len(comment) == 0:
        return parsed_data

    current_pos = __find_next_tag_pos__(comment, 0)
    next_pos = __find_next_tag_pos__(comment, current_pos + 1)

    first_content = __make_single_line__(comment[0:current_pos - 1])
    if len(first_content) > 0:
        parsed_data['brief'] = first_content

    while next_pos != current_pos:

        found_tag = comment[current_pos:next_pos].split(' ')[0].strip()

        content = __make_single_line__(comment[current_pos + len(found_tag): next_pos - 1])
        found_tag = found_tag[len(tag_start[0]):]

        if found_tag in multi_tags:
            parsed_data[found_tag].append(content)

        elif found_tag in known_tags:
            parsed_data[found_tag] = content

        if next_pos == len(comment):
            break

        current_pos = next_pos
        next_pos = __find_next_tag_pos__(comment, current_pos + 1)

    return parsed_data


def __print_parsed_tags__(combined_doc):
    result = '"""\n'

    for tag in known_tags:
        has_content = False
        for content in combined_doc[tag]:
            if isinstance(content, list) and len(content) > 0:
                has_content = True
                break
            elif len(content) > 0:
                has_content = True
                break

        if not has_content:
            continue

        if len(map_python_to_cpp[tag]) > 0:
            result += map_python_to_cpp[tag] + '\n'
        prefix = '  '
        for i, content in enumerate(combined_doc[tag]):
            if isinstance(content, list) > 0:
                result += f'{prefix}- Variant {i}:\n'
                for multi_content in content:
                    result += f'{prefix}  -- {multi_content}\n'
            else:
                result += f'{prefix}- {content}\n'

    result += '"""\n'
    return result


def create_docstring(parsed_docs):
    if len(parsed_docs) == 0:
        return ''

    if not isinstance(parsed_docs, list):
        parsed_docs = [parsed_docs]

    combined_doc = {}
    for tag in known_tags:
        combined_doc[tag] = []
        for parsed_doc in parsed_docs:
            if tag in parsed_doc:
                combined_doc[tag].append(parsed_doc[tag])

    return __print_parsed_tags__(combined_doc)


def create_method_docstring(parsed_docs):
    if len(parsed_docs) == 0:
        return ''

    if not isinstance(parsed_docs, list):
        parsed_docs = [parsed_docs]

    combined_doc = {}
    for tag in known_tags:
        combined_doc[tag] = []
        for parsed_doc, params in parsed_docs:
            if tag == 'param':
                types = []
                if len(params) == 0:
                    types.append('(void)')

                for param in params:
                    if isinstance(param.type, cxxheaderparser.types.Type):
                        typename = get_cpp_type(param.type.typename.segments)
                        if param.type.const:
                            typename = 'const ' + typename

                    elif isinstance(param.type, cxxheaderparser.types.Reference):
                        typename = get_cpp_type(param.type.ref_to.typename.segments) + '&'
                        if param.type.ref_to.const:
                            typename = 'const ' + typename

                    elif isinstance(param.type, cxxheaderparser.types.Pointer):
                        typename = get_cpp_type(param.type.ptr_to.typename.segments) + '*'
                        if param.type.ptr_to.const:
                            typename = 'const ' + typename

                    else:
                        typename = 'unknown'
                    # varname = param.name
                    types.append(f'({typename}) ')

                for i, t in enumerate(types):
                    if len(parsed_doc['param']) <= i:
                        parsed_doc['param'].append(t)
                    else:
                        parsed_doc['param'][i] = t + ' ' + parsed_doc['param'][i]

            if parsed_doc is not None and tag in parsed_doc:
                combined_doc[tag].append(parsed_doc[tag])

    return __print_parsed_tags__(combined_doc)


def create_field_docstring(parsed_doc):
    for field_comment in field_comments:
        parsed_doc = parsed_doc.replace(field_comment, '')

    result = '"""' + parsed_doc.strip() + '"""'
    return result


def __find_next_tag_pos__(comment, current_pos):
    next_pos = len(comment)
    for tag in known_tags:
        for ts in tag_start:
            tag_pos = comment.find(ts + tag, current_pos)
            if tag_pos != -1 and tag_pos < next_pos:
                next_pos = tag_pos
    return next_pos
