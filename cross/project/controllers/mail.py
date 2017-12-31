#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import gmail
from gmail import Message


def send_mail(base_mail, to_mail, user_name, user_text):
    # try:
    b = "".join(["Thanks 2018! <", base_mail, ">"])

    gm = gmail.GMail(b, 'sonic1980')
    msg = Message('Спасибо от', to="me <{0}>".format(to_mail),
                  text="Спасибо от {0}, сообщение: {1}".format(user_name, user_text))
    gm.send(msg)
    # except Exception as ex:
    #     pass

# def send_mail_key(base_mail, base_mailpass, to_mail, akey):
#
#     b = "".join(["sharkevo <", base_mail, ">"])
#     txt = "".join(["Для завершения регистрации и начала работы ",
#                    "введите указанный код активации на сайте: ",
#                    akey])
#
#     gm = gmail.GMail(b, base_mailpass)
#     msg = Message('Завершение регистрации', to="me <{0}>".format(to_mail), text=txt)
#     gm.send(msg)
