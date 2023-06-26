from aiogram import Dispatcher

from loader import dp
from .group import IsGroup


if __name__ == "filters":
    dp.filters_factory.bind(IsGroup)
