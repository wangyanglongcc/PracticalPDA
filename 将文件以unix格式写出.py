def write2unix(df,filepath):
    # title
    _title = [str(x) for x in df.columns]
    _title = '\t'.join(_title) + '\n'
    # content
    _content = []
    for _row in df.values:
        _row = [str(x) for x in _row]
        _row = '\t'.join(_row)
        _content.append(_row)
    _content = '\n'.join(_content)+'\n'
    # write2output
    data = _title + _content
    data = data.encode()
    EOL_UNIX = b'\n'
    EOL_WINDOWS = b'\r\n'
    EOL_MAC = b'\r'
    data = data.replace(EOL_WINDOWS, EOL_UNIX).replace(EOL_MAC, EOL_UNIX)
    f = open(filepath, 'wb')
    f.write(data)
    f.close()
if __name__ == '__main__':
    write2unix(df,filepath)
