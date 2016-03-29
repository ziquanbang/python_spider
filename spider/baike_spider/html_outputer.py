import sys

type = sys.getfilesystemencoding()
class HtmlOutputer(object):
    def __init__(self):
        self.datas = []

    def output_html(self):
        fout = open('output.html', 'w', encoding='UTF-8')
        fout.write("<html>")
        fout.write("<head>")
        fout.write("<meta charset='utf-8'>")
        fout.write("<meta http-equiv='Content-Type' content='text/html; charset=utf-8' />")
        fout.write("</head>")
        fout.write("<body>")
        fout.write("<table>")
        for data in self.datas:
            fout.write("<tr>")

            # fout.write("<td>%s</td>"%data['url'].encode('utf-8'))
            # fout.write("<td>%s</td>"%data['title'].encode('utf-8'))
            # fout.write("<td>%s</td>"%data['summary'].encode('utf-8'))
            # fout.write(str("<td>"+(str(data['url'])+"</td>")))
            # fout.write(str("<td>"+(str(data['title'])+"</td>")))
            # fout.write(str("<td>"+(str(data['summary'])+"</td>")))
            # fout.write("<td>%s</td>"%data['url'].encode(type))
            # fout.write("<td>%s</td>"%data['title'].encode(type))
            # fout.write("<td>%s</td>"%data['summary'].encode(type))


            print(data['url'])
            print(data['title'])
            print(data['summary'])
            fout.write("<td>%s</td>"%data['url'])
            fout.write("<td>%s</td>"%data['title'])
            fout.write("<td>%s</td>"%data['summary'])
            # fout.write("<td>%s</td>"%data['url'] )
            # fout.write("<td>%s</td>"%data['title'])
            # fout.write("<td>%s</td>"%data['summary'] )
            fout.write("</tr>")
        fout.write("</table>")
        fout.write("</body>")
        fout.write("</html>")

        fout.close()

    def collect_data(self, data):
        if data is None:
            return
        self.datas.append(data)

