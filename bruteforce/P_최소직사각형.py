def solution(sizes):
    m_w = 0
    m_h = 0
    space = m_w * m_h
    for i, size in enumerate(sizes):
        if i == 0:
            m_w, m_h = size[0], size[1]
            space = m_w * m_h
        else:
            tmp_w = max(m_w, size[0])
            tmp_h = max(m_h, size[1])
            tmp_space = tmp_w * tmp_h

            tmp_w2 = max(m_w, size[1])
            tmp_h2 = max(m_h, size[0])
            tmp_space2 = tmp_w2 * tmp_h2
            if tmp_space < tmp_space2:
                m_w = tmp_w
                m_h = tmp_h
                space = m_w * m_h
            else:
                m_w = tmp_w2
                m_h = tmp_h2
                space = m_w * m_h

    return space