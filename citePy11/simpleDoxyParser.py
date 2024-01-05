tag_start = ['@', '\\']
comment_start = '/**'
comment_continue = '*'
comment_end = '*/'

known_tags = ['brief', 'name', 'param', 'return', 'fn']
multi_tags = ['param', 'exception', 'note', 'warning']


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
        parsed_data[multi_tag] = []
        known_tags.append(multi_tag)

    if len(comment) == 0:
        return parsed_data

    current_pos = find_next_tag_pos(comment, 0)
    next_pos = find_next_tag_pos(comment, current_pos + 1)

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
        next_pos = find_next_tag_pos(comment, current_pos + 1)

    return parsed_data


def find_next_tag_pos(comment, current_pos):
    next_pos = len(comment)
    for tag in known_tags:
        for ts in tag_start:
            tag_pos = comment.find(ts + tag, current_pos)
            if tag_pos != -1 and tag_pos < next_pos:
                next_pos = tag_pos
    return next_pos
