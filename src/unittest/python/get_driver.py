# -*- coding: utf-8 -*-

__author__ = 'pf'

from selenium import webdriver


def get_driver(capa = {'platform': 'LINUX', 'browserName': 'firefox', 'version': '', 'javascriptEnabled': True}, grid = True, grid_url="http://127.0.0.1:4444/wd/hub"):
    """
    подключение к серверу selenium
    :param grid: Если True - подключаемся к указанному серверу. Если False запускается вебдрайвер Фаерфокс без selenium-server-standalone
    :return: возвращает вебдрайвер
    """
    if grid:
        driver = webdriver.Remote(desired_capabilities=capa,command_executor=grid_url)
        return driver
    else:
        return webdriver.Firefox()