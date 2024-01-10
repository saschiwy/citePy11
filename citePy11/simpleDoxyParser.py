tag_start = ['@', '\\']
comment_start = '/**'
comment_continue = '*'
comment_end = '*/'

known_tags = ['brief', 'param', 'returns', 'fn']
multi_tags = ['param', 'exception', 'note', 'warning']

field_comments = ['///<', '//!<', '//!', '///']

map_python_to_cpp = {
    'brief': '',
    'param': 'Parameter:',
    'returns': 'Returns:',
    'fn': 'Function:',
    'exception': 'Raises:',
    'note': 'Notes:',
    'warning': 'Warnings:'
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


def create_method_docstring(parsed_docs):
    if len(parsed_docs) == 0:
        return ''

    result = '"""\n'

    if not isinstance(parsed_docs, list):
        parsed_docs = [parsed_docs]

    combined_doc = {}
    for tag in known_tags:
        combined_doc[tag] = []
        for parsed_doc in parsed_docs:
            if tag in parsed_doc:
                combined_doc[tag].append(parsed_doc[tag])

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

    # for parsed_doc in parsed_docs:
    #     for tag in known_tags:
    #
    #         if tag in parsed_doc:
    #             if not len(parsed_doc[tag]) > 0:
    #                 continue
    #             if len(map_python_to_cpp[tag]) > 0:
    #                 result += map_python_to_cpp[tag] + '\n'
    #                 prefix = '    '
    #             else:
    #                 prefix = ''
    #             if tag in multi_tags:
    #                 for multi_tag in parsed_doc[tag]:
    #                     result += f'{prefix}- {multi_tag}\n'
    #             else:
    #                 result += f'{prefix}{parsed_doc[tag]}\n'

    result += '"""\n'
    return result


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
