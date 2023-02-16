# Import mimetypes module
import mimetypes
# import os module
import os
import subprocess
from pathlib import Path
from datetime import datetime, timedelta

from django.contrib.auth.decorators import login_required, permission_required
from django.http.response import HttpResponse


def download_user_file(filename):
    print('download_user_file')
    load_string = 'postgresql://postgres:12345678@localhost:5432/postgres'

    cmd = f'psql -a {load_string} -c "\copy (SELECT id_user, full_name, time_enter, ' \
          f'time_starttest, time_endtest, \\"time_regOnWebinar\\", \\"time_startWebinar\\", time_sendgame, ' \
          f'cost_result, cost_webinar, status, disabled, result, phone_number, public.\\"Advertizing\\".category , ' \
          f'public.\\"Advertizing\\".source, id_ref FROM public.\\"Users\\" LEFT JOIN public.\\"Advertizing\\" ON ' \
          f'public.\\"Users\\".id_advert = public.\\"Advertizing\\".id) to {filename} with csv HEADER delimiter \';\'' \
          f' encoding \'UTF8\'"'

    # filename='assada.csv'
    # copy = f'& \'C:\\Program Files\\PostgreSQL\\13\\bin\\psql.exe\'' \
    #        f'-a {load_string} ' \
    #        f'-c "\copy (SELECT id_user, full_name, time_enter, ' \
    #        f'time_starttest, time_endtest, \\"time_regOnWebinar\\", \\"time_startWebinar\\", time_sendgame, ' \
    #        f'cost_result, cost_webinar, status, disabled, result, phone_number, public.\\"Advertizing\\".category , ' \
    #        f'public.\\"Advertizing\\".source FROM public.\\"Users\\" LEFT JOIN public.\\"Advertizing\\" ON public.\\' \
    #        f'"Users\\".id_advert = public.\\"Advertizing\\".id) to {filename} with csv HEADER delimiter \';\' ' \
    #        f'encoding \'UTF8\'"'

    os.system(cmd)
    return True
    # process = subprocess.Popen('history',
    #                            stdout=subprocess.PIPE)
    # # proc = await create_subprocess_shell(cmd, stdout=subprocess.PIPE)
    # stdout, stderr = process.communicate()
    # if stdout:
    #     print(f'[stdout]\n{stdout.decode()}')
    #     return stdout.decode()
    # if stderr:
    #     print(f'[stderr]\n{stderr.decode()}')


# @login_required
# @permission_required()
def download_file(request):
    print(request.user)
        # return None #redirect('/login/?next=%s' % request.path)

    _s = (datetime.today() + timedelta(hours=3)).strftime('%H_%M_%S-%d_%m_%Y')
    # filename = f'users-{_s}.csv'
    filename = f'test.txt'
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    if True: #download_user_file(filename):
        filepath = Path(BASE_DIR, 'django_telegram_auth_example', filename)
        print(filepath)
        path = open(filepath, 'r')
        # path = open('django_telegram_auth_example\\test.txt', 'r')

        mime_type, _ = mimetypes.guess_type(filepath)
        response = HttpResponse(path, content_type=mime_type)
        response['Content-Disposition'] = "attachment; filename=%s" % filename
        return response
