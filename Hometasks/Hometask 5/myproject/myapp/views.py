from django.shortcuts import render
from django.http import HttpResponse

def my_info(request):
    html = """
    <html>
        <body>
            <h2>Info</h2>
            <table border="1" cellpadding="5">
                <tr>
                    <th>Field</th>
                    <th>Values</th>
                </tr>
                <tr>
                    <td>Name</td>
                    <td>Alex</td>
                </tr>
                <tr>
                    <td>Last name</td>
                    <td>Mykhailov</td>
                </tr>
                <tr>
                    <td>Major</td>
                    <td>Software Engineer</td>
                </tr>
                <tr>
                    <td>City</td>
                    <td>Kyiv</td>
                </tr>
            </table>
        </body>
    </html>
    """
    return HttpResponse(html)

# Create your views here.
