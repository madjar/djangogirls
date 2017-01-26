import subprocess


def fill_form(pdf_file, data):
    """Fill the form in pdf_file with the given data.

    Returns the resulting pdf as bytes."""
    xfdf = generate_xfdf(data)

    command = ['pdftk', pdf_file, 'fill_form', '/dev/stdin', 'output',
               '/dev/stdout']
    process = subprocess.run(command, input=xfdf.encode('utf8'),
                             stdout=subprocess.PIPE)
    return process.stdout


def generate_xfdf(data):
    buffer = []

    buffer.append(
        '<?xml version="1.0" encoding="UTF-8"?>'
        '<xfdf xmlns="http://ns.adobe.com/xfdf/" xml:space="preserve">'
        '<fields>')

    for k, v in data.items():
        buffer.append('<field name="')
        buffer.append(k)
        buffer.append('"><value>')
        buffer.append(v)
        buffer.append('</value></field>')

    buffer.append('</fields></xfdf>')

    return ''.join(buffer)
